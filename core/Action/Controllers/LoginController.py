"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""


class LoginController:

    def __init__(self):
        from views.login_view import LoginView
        self.window = LoginView()

    def show_window(self):
        from core.Action.Controllers import HomeController
        from core.Action.Controllers import RegisterController

        home_controller = HomeController.HomeController()
        login_controller = RegisterController.RegisterController()

        self.window.switch_first.connect(home_controller.show_window)
        self.window.switch_third.connect(login_controller.show_window)
        self.window.show()

        # TODO: The code below should have a different approach because of the fact that the LoginView will initialize
        # TODO: -- both views (and) background sources such as Models

        # from views.login_view import LoginView
        # main_window = LoginView()
        # if main_window.isVisible():
        #     main_window.hide()
        #
        # from views.register_view import RegisterView
        # second_window = RegisterView()
        # if second_window.isVisible():
        #     second_window.hide()
