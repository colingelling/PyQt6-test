"""

Created by Colin Gelling on 20/2/2023
Using Pycharm Professional

"""


class Controller:

    def __init__(self):
        pass

    # Instantiate the window Classes per method from now on, bind the windows to individual signals and show the window

    def show_main_window(self):
        from views.home_view import HomeView
        self.main_window = HomeView()
        self.main_window.switch_second.connect(self.show_second_window)
        self.main_window.switch_third.connect(self.show_third_window)
        self.main_window.show()

        # TODO: The code below should have a different approach because of the fact that the LoginView will initialize
        # TODO: -- both views (and) background sources such as Models

        # from views.register_view import RegisterView
        # self.second_window = RegisterView()
        # if self.second_window.isVisible():
        #     self.second_window.hide()
        #
        # from views.login_view import LoginView
        # self.third_window = LoginView()
        # if self.third_window.isVisible():
        #     self.third_window.hide()

    def show_second_window(self):
        from views.register_view import RegisterView
        self.second_window = RegisterView()
        self.second_window.switch_first.connect(self.show_main_window)
        self.second_window.switch_third.connect(self.show_third_window)
        self.second_window.show()

        # TODO: The code below should have a different approach because of the fact that the LoginView will initialize
        # TODO: -- both views (and) background sources such as Models

        # from views.home_view import HomeView
        # self.main_window = HomeView()
        # if self.main_window.isVisible():
        #     self.main_window.hide()
        #
        # from views.login_view import LoginView
        # self.third_window = LoginView()
        # if self.third_window.isVisible():
        #     self.third_window.hide()

    def show_third_window(self):
        from views.login_view import LoginView
        self.third_window = LoginView()
        self.third_window.switch_first.connect(self.show_main_window)
        self.third_window.switch_second.connect(self.show_second_window)
        self.third_window.show()

        # TODO: The code below should have a different approach because of the fact that the LoginView will initialize
        # TODO: -- both views (and) background sources such as Models

        # from views.home_view import HomeView
        # self.main_window = HomeView()
        # if self.main_window.isVisible():
        #     self.main_window.hide()
        #
        # from views.register_view import RegisterView
        # self.second_window = RegisterView()
        # if self.second_window.isVisible():
        #     self.second_window.hide()
