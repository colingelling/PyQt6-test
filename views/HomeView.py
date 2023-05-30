"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

from core.Actions.Controllers.Navigation.ViewController import ViewController
from core.Configurators.EnvironmentConfigurator import EnvironmentConfigurator
from core.Configurators.LayoutConfigurator import LayoutConfigurator


class HomeView(QMainWindow, EnvironmentConfigurator, ViewController, LayoutConfigurator):

    switch_first = QtCore.pyqtSignal(str)
    switch_second = QtCore.pyqtSignal(str)
    switch_third = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.ui = self.load_home_ui()

        for key, value in EnvironmentConfigurator.app_credentials.items():
            if 'NAME' in key:
                self.window_title = 'Home'
                self.setWindowTitle(f"{self.window_title}: { value }")

        self.home_nav = None
        self.register_nav = None
        self.login_nav = None

        self.setup_navigation()
        self.content()

    def setup_navigation(self):

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        button_home.triggered.connect(self.switch_home_window)
        button_register.triggered.connect(self.switch_register_window)
        button_login.triggered.connect(self.switch_login_window)

        self.home_nav = button_home
        self.register_nav = button_register
        self.login_nav = button_login

    def content(self):

        # set ui
        ui = self.ui

        # navigation
        menubar = ui.menuBar
        menubar.addAction(self.home_nav)
        menubar.addAction(self.register_nav)
        menubar.addAction(self.login_nav)

        # Begin: tab widget (tab 1)

        first_tab_headline = 'Welcome'

        ui.tabWidget.setTabText(0, first_tab_headline)

        # Same thing for this, prevent cutting the label/add dynamic length according to text
        ui.homeIntroTitleFrameTab_1.adjustSize()

        # Divide the text over multiple lines instead of one limited by an x amount of characters
        ui.homeIntroLongTextTab_1.setMinimumWidth(600)
        ui.homeIntroLongTextTab_1.setWordWrap(1)
        ui.homeIntroLongTextTab_1.setText(
            "This application is a practice program in order to learn the Python language including OOP terms and most "
            "of all knowing what to do with PyQt6."
            "This application serves the ability to register an account whether you can sign in afterwards."
        )

        ui.homeIntroLongTextTab_1.adjustSize()

        # End: tab widget (tab 1)

        # Begin: tab widget (tab 2)
        # Also the following block has the same rules as the code described above this text

        second_tab_headline = 'Application language information'
        ui.tabWidget.setTabText(1, second_tab_headline)

        ui.homeIntroTitleFrameTab_2.adjustSize()

        ui.homeIntroLongTextTab_2.setMinimumWidth(600)
        ui.homeIntroLongTextTab_2.setWordWrap(1)
        ui.homeIntroLongTextTab_2.setText(
            "This program is made with Python and the PyQt(6) library. The elements are put in by using Qt Designer,"
            "which is a UI element addition application itself. This stores .ui files per window, and these are "
            "converted in the background as .py files because of the fact that it is easier to work with."
        )

        ui.homeIntroLongTextTab_2.adjustSize()

        # End: tab widget (tab 2)

    def switch_home_window(self):
        self.show_home()

    def switch_register_window(self):
        self.show_register()

    def switch_login_window(self):
        self.show_login()
