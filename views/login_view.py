"""

Created by Colin Gelling on 30/1/2023

"""

import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication

import core.Models.Views.LoginModel as LoginModel


class LoginView(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(LoginView, self).__init__(parent)

        self.view_ui = LoginModel.LoginModel()
        self.ui()
        self.content()

        self.switch_window.connect(self.submit)

    def ui(self):
        self.view_ui.setup_ui()
        self.view_ui.show()

    def content(self):
        self.view_ui.setWindowTitle('Login')

        menubar = self.view_ui.login_ui.menuBar

        button_home = QAction("Home", self)
        button_home.triggered.connect(self.refer_home_route)

        """
        TODO: 

        1. Fix error -> AttributeError: module 'core.Action.Controllers.HomeController' has no attribute 'HomeController'
        2. As of feb/1, this description has been returned without any error

        What changed? Reference (https://github.com/colingelling/PyQt6-test/blob/main/views/home_view.py)
        - Compare the main.py from this version to the main.py from https://github.com/colingelling/PyQt6-test and check 
        the bottom of the reference mentioned above this line
        
        Also, navigating between windows doesn't work properly as of now; 
        - Going from Home (launching state) to Login, to Register back to Login or either, closes the application 
        instead of keeping the event loop going
        - When clicking on the Home tab the application almost always closes instead of:
        1. Staying within the Home Window when triggered from the same window
        2. Returning to the Home window when triggered from another window
        
        Frank and Leon advised me to look into Event Handling more, maybe the first started Event 
        (According to Home route starting within Bootstrapper.py) must be closed before returning to it later.
        
        Also Leon mentioned that the application has been started within the main, maybe that each window is going to be 
        setup the same way as it did for the first launch. 

        """

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


window = LoginView()
