"""

    Created by Colin Gelling on 20/02/2023
    Using Pycharm Professional

"""

from PyQt6 import QtCore

from core.Navigation.Mapping.ViewMapping import ViewMapping


class ViewManager(QtCore.QObject, ViewMapping):

    def __init__(self):
        super().__init__()
        self.views = {}
        self.view_session = None
        self.view_data = {}

    def set_view(self, view_name, authenticated="no"):

        """
            Set and show the requested view from the ViewController
            Handle the switching part between windows
            Use sessions (Qt) in order to close old windows
        """

        if view_name not in self.views:
            view = self.create_view(view_name, authenticated)
            self.views[view_name] = view

            from core.Sessions.ManageViewSession import ManageViewSession
            self.view_session = ManageViewSession()

            # get both the old view and next view
            old_view = ManageViewSession.view_session.get('current_view')
            current_view = self.views[view_name]

            # put them into a Dictionary
            ManageViewSession.view_session = {
                'old_view': old_view,
                'current_view': current_view
            }

            # put the Dictionary into a session
            self.view_session.set_session()

            # close a view (window)
            self.close_view()

        self.views[view_name].show()

    @staticmethod
    def create_view(view_name, authenticated="no"):

        """
            Collect view/window data and provide the view to the set functionality
        """

        # set available instances
        from core.Navigation.ViewCreator import ViewCreator
        mapping = ViewMapping()
        creator = ViewCreator()

        # check and set authentication based on the ViewMapping
        creator.set_authentication(mapping, authenticated)
        creator.validate_navigation_pattern(mapping)

        # retrieve the correct view data related on the user's preferences (window switching)
        window_data = mapping.navigation_pattern.get(view_name)
        creator.validate_view_data(window_data, view_name)

        # retrieve the class value from ViewMapping and check if it has value
        view_class = window_data.get("view_class")
        creator.validate_view_class(view_class, view_name)

        # use the view_class and attempt to import the view module (from ... import ...)
        view_module = creator.get_view_module(view_class, authenticated)
        view = creator.import_view(view_module, view_class, view_name)

        # set the connections (available windows to switch to)
        creator.setup_connections(view, window_data.get('connections'))

        # show
        return view
        
    def close_view(self):

        """
            Attempt to close the old view using Qt 's session manager
        """

        # retrieve the session
        session = self.view_session.get_session()

        # verify that the session is there
        if not session:
            raise ValueError("Error: View session returned empty!")

        for key, value in session.items():
            if key == 'old_view':
                value.close()
