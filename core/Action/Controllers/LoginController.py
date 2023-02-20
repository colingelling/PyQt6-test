"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""


import views.login_view as LoginView


class LoginController:
    def __init__(self):
        self.pointer()

    @staticmethod
    def pointer():
        return LoginView.LoginView()
