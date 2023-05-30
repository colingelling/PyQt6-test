"""

Created by Colin Gelling on 05/05/2023
Using Pycharm Professional

"""

from core.Handlers.Sessions.UserSessions import UserSessions


class LoginManager(UserSessions):
    def __init__(self):
        super().__init__()

    def submit(self):

        """

        This method is responsible for handling a collection of required functionality
        :return:
        1) login process, communication with the database
        2) create a 'session' with PyQt6 and store the user_id
        3) retrieve the session
        4) forward to the next window -> when logged in

        """

        self.login_user()
        self.set_session()

        from core.Actions.Controllers.Navigation.ViewController import ViewController
        controller = ViewController()

        # forward to the view after login
        controller.show_user()
