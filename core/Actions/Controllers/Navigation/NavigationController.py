"""

Created by Colin Gelling on 20/2/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore

from core.Storage.Navigation.Mapping.ViewMapping import ViewMapping


class NavigationController(QtCore.QObject, ViewMapping):

    def __init__(self):
        super().__init__()
        self.views = {}
        self.view_session = None

    def set_view(self, view_name, authenticated="no"):  # TODO: separate session stuff?
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
        # set available instances
        from core.Actions.Creators.ViewCreator import ViewCreator
        mapping = ViewMapping()
        creator = ViewCreator()

        # check and set authentication based on the ViewMapping
        creator.set_authentication(mapping, authenticated)
        creator.validate_navigation_pattern(mapping)

        # retrieve the correct view data related on the user's preferences (window switching)
        view_data = mapping.navigation_pattern.get(view_name)
        creator.validate_view_data(view_data, view_name)

        # retrieve the class value from ViewMapping and check if it has value
        view_class = view_data.get("class")
        creator.validate_view_class(view_class, view_name)

        # use the view_class and attempt to import the view module (from ... import ...)
        view_module = creator.get_view_module(view_class, authenticated)
        view = creator.import_view(view_module, view_class, view_name)

        # set the connections (available windows to switch to)
        creator.setup_connections(view, view_data.get('connections'))

        # show
        return view
        
    def close_view(self):

        # retrieve the session
        session = self.view_session.get_session()

        # check if the session is there
        if session:
            for key, value in session.items():
                # close
                if key == 'old_view':
                    value.close()
