"""

Created by Colin Gelling on 30/1/2023

"""

import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QPushButton

import core.Models.Views.HomeModel as HomeModel


class HomeView(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)

        self.switch_window.connect(self.refer_login_route)

        self.view_ui = HomeModel.HomeModel()
        self.ui()
        self.content()

    def ui(self):
        self.view_ui.setup_ui()
        self.view_ui.show()

    def content(self):

        self.view_ui.setWindowTitle("Home: My first PyQt6 program!")

        # Navigation

        menubar = self.view_ui.home_ui.menuBar

        button_home = QAction("Home", self)
        button_home.triggered.connect(self.refer_home_route) # TODO: fix error -> AttributeError: module 'core.Action.Controllers.HomeController' has no attribute 'HomeController'

        button_login = QAction("Login", self)
        button_login.triggered.connect(self.refer_login_route)

        button_register = QAction("Register", self)
        button_register.triggered.connect(self.refer_register_route)

        # button_register.triggered.signal(lambda: self.close())

        menubar.addAction(button_home)
        menubar.addAction(button_login)
        menubar.addAction(button_register)

        # menubar.addAction(trigger_login)

        # Navigation end

        # Set text for the first label (first tab)
        self.view_ui.home_ui.homeIntroLabelTabTitle_1.setText("Welcome")

        # Make sure that the label is not going to be cut in relation to the text size
        self.view_ui.home_ui.homeIntroLabelTabTitle_1.adjustSize()

        # Same thing for this, prevent cutting the label/add dynamic length according to text
        self.view_ui.home_ui.homeIntroTitleFrameTab_1.adjustSize()

        # Divide the text over multiple lines instead of one limited by an x amount of characters
        self.view_ui.home_ui.homeIntroLongTextTab_1.setWordWrap(1)
        self.view_ui.home_ui.homeIntroLongTextTab_1.setText(
            "This application is a practice program in order to learn the Python language including OOP terms and most of all knowing what to do with PyQt6"
        )

        '''
        The following block has the same rules as the code described above this text
        '''

        self.view_ui.home_ui.homeIntroLabelTabTitle_2.setText("Application language information")
        self.view_ui.home_ui.homeIntroLabelTabTitle_2.adjustSize()
        self.view_ui.home_ui.homeIntroTitleFrameTab_2.adjustSize()
        self.view_ui.home_ui.homeIntroLongTextTab_2.setWordWrap(1)
        self.view_ui.home_ui.homeIntroLongTextTab_2.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        )

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


window = HomeView()
