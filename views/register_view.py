"""

Created by Colin Gelling on 30/1/2023

"""

import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication

import core.Models.Views.RegisterModel as RegisterModel


class RegisterView(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(RegisterView, self).__init__(parent)

        self.view_ui = RegisterModel.RegisterModel()
        self.ui()
        self.content()

        self.switch_window.connect(self.submit)

    def ui(self):
        self.view_ui.setup_ui()
        self.view_ui.show()

    def content(self):
        self.view_ui.setWindowTitle('Register')

        menubar = self.view_ui.register_ui.menuBar

        button_home = QAction("Home", self)
        button_home.triggered.connect(self.refer_home_route)  # TODO: fix error -> AttributeError: module 'core.Action.Controllers.HomeController' has no attribute 'HomeController'

        button_login = QAction("Login", self)
        button_login.triggered.connect(self.refer_login_route)

        button_register = QAction("Register", self)
        button_register.triggered.connect(self.refer_register_route)

        menubar.addAction(button_home)
        menubar.addAction(button_login)
        menubar.addAction(button_register)

    def submit(self):
        pass

    def close_window(self):
        ui = self.view_ui
        ui.close()
        self.close()

    def refer_home_route(self):
        from router.routes import Routes as route
        route.home()
        self.close_window()

    def refer_login_route(self):
        from router.routes import Routes as route
        route.login()
        self.close_window()

    def refer_register_route(self):
        from router.routes import Routes as route
        route.register()
        self.close_window()


window = RegisterView()
