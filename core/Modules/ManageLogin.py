"""

Created by Colin Gelling on 05/05/2023
Using Pycharm Professional

"""

from core.Sessions.ManageUserSession import ManageUserSession


class ManageLogin(ManageUserSession):

    """
        This class handles the login process for the user
    """

    def __init__(self):
        super().__init__()

    def submit(self):

        # verify the login state and bind the logged user to a session (QtSettings session manager)
        self.login_user()
        self.set_session()

        from core.Controllers.ViewController import ViewController
        controller = ViewController()

        # forward to the view after login
        controller.show_user()
