"""

Created by Colin Gelling on 30/1/2023

"""


import views.login_view as LoginView


class LoginController:
    def __init__(self):
        super(LoginController, self).__init__()
        self.pointer()

    @staticmethod
    def pointer():
        return LoginView.LoginView()
