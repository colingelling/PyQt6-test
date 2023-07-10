"""

Created by Colin Gelling on 26/4/2023
Using Pycharm Professional

"""

from core.Controllers.Navigation.NavigationController import NavigationController


class ViewController(NavigationController):
    def __init__(self):
        super().__init__()

    def show_home(self):
        view = "HomeView"
        self.set_view(view, authenticated="no")

    def show_register(self):
        view = "RegisterView"
        self.set_view(view, authenticated="no")

    def show_login(self):
        view = "LoginView"
        self.set_view(view, authenticated="no")

    def show_user(self):
        view = "UserView"
        self.set_view(view, authenticated="yes")
