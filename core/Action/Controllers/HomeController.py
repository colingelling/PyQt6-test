"""

Created by Colin Gelling on 30/1/2023

"""

from PyQt6 import QtCore

from views.home_view import HomeView


class HomeController:

    def __init__(self):
        pass

    def show_window(self):
        self.main_window = HomeView()

        from core.Action.Controllers.RegisterController import RegisterController
        register_controller = RegisterController()
        self.main_window.switch_second.connect(register_controller.show_window)

        self.main_window.show()
