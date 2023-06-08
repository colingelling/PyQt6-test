"""

Created by Colin Gelling on 20/2/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore


class NavigationController(QtCore.QObject):

    def __init__(self):
        super().__init__()

        # TODO: Think about separating this Class since its about deeper level functionality

        """

            self.views should contain the available views of the application as the functionality expands; 
            The keys are names of the views and the values are actual view objects

        """

        self.views = {}
        self.view_session = None

    def set_view(self, view_name):
        # show the requested view (sourced from the Controller)
        if view_name not in self.views:
            view = self.create_view(view_name)
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

    def create_view(self, view_name):
        # no authentication
        if view_name == "HomeView":
            from views.HomeView import HomeView
            view = HomeView()
            view.switch_second[str].connect(lambda: self.set_view("RegisterView"))
            view.switch_third[str].connect(lambda: self.set_view("LoginView"))
            return view
        elif view_name == "RegisterView":
            from views.RegisterView import RegisterView
            view = RegisterView()
            view.switch_first[str].connect(lambda: self.set_view("HomeView"))
            view.switch_third[str].connect(lambda: self.set_view("LoginView"))
            return view
        elif view_name == "LoginView":
            from views.LoginView import LoginView
            view = LoginView()
            view.switch_first[str].connect(lambda: self.set_view("HomeView"))
            view.switch_second[str].connect(lambda: self.set_view("RegisterView"))
            return view
        elif view_name == "UserView":
            from views.Authenticated.UserView import UserView
            view = UserView()
            return view
        
    def close_view(self):

        # retrieve the session
        session = self.view_session.get_session()

        # check if there are values
        if session:
            # unpack
            for key, value in session.items():
                # only the old_view needs to be closed after another window has been opened
                if key == 'old_view':
                    value.close()
