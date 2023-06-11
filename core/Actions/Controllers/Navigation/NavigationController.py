"""

Created by Colin Gelling on 20/2/2023
Using Pycharm Professional

"""
import importlib

from PyQt6 import QtCore

from core.Storage.Navigation.Mapping.ViewMapping import ViewMapping


class NavigationController(QtCore.QObject, ViewMapping):

    def __init__(self):
        super().__init__()
        self.views = {}
        self.view_session = None

        self.view_subject = None
        self.view_class = None
        self.view_authentication = None
        self.view_connections = {}

    def set_view(self, view_name, authenticated="no"):
        # show the requested view (sourced from the Controller)
        if view_name not in self.views:
            view = self.create_view(view_name, authenticated)
            self.views[view_name] = view

            from core.Handlers.Sessions.ViewSessions import ViewSessions
            self.view_session = ViewSessions()

            # get both the old view and next view
            old_view = ViewSessions.view_session.get('current_view')
            current_view = self.views[view_name]

            # put them into a Dictionary
            ViewSessions.view_session = {
                'old_view': old_view,
                'current_view': current_view
            }

            # put the Dictionary into a session
            self.view_session.set_session()

            # close a view (window)
            self.close_view()

        self.views[view_name].show()

    def create_view(self, view_name, authenticated="no"):
        # instantiate and set functionality switch through options
        mapping = ViewMapping()
        if authenticated == "yes":
            mapping.authenticated()
        else:
            mapping.not_authenticated()

        if not mapping.navigation_pattern:
            raise ValueError("Navigation pattern has not been set")

        view_data = mapping.navigation_pattern.get(view_name)
        if not view_data:
            raise ValueError(f"View data not found for view: {view_name}")

        view_class = view_data.get("class")
        if not view_class:
            raise ValueError(f"View class not specified for view: {view_name}")

        view_module = None

        if authenticated == "yes":
            view_module = f"views.Auth.{view_class}"
        elif authenticated == "no":
            view_module = f"views.{view_class}"
        else:
            raise ValueError("Authentication value has not been set properly.")

        try:
            module_import = importlib.import_module(view_module)
            view_class = getattr(module_import, view_class)
            view = view_class()

            # set up any connections or additional logic specific to the view
            connections = view_data.get('connections')
            if connections:
                for connection in connections:
                    switch, connected_view = connection

                    switch_attr = getattr(view, switch, None)
                    if switch_attr is not None:
                        switch_attr[str].connect(lambda: self.set_view(connected_view))
                    else:
                        print(f"Switch attribute '{switch}' not found in the view")

            return view
        except (ImportError, AttributeError) as e:
            # Handle import errors or attribute errors
            print(f"Error creating view: {view_name}. {str(e)}")
            return None
        
    def close_view(self):

        # retrieve the session
        session = self.view_session.get_session()

        if session:
            for key, value in session.items():
                # close
                if key == 'old_view':
                    value.close()
