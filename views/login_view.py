"""

Created by Colin Gelling on 30/1/2023

"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow


class LoginView(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        from src.gui.ui.login.login_view import Ui_LoginWindow
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.content()

    def content(self):
        self.setWindowTitle('Login')

        # Navigation

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        button_home.triggered.connect(self.switch_first_window)
        button_register.triggered.connect(self.switch_second_window)
        button_login.triggered.connect(self.switch_third_window)

        menubar = self.ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

    def submit(self):
        pass

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()


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

        from views.register_view import RegisterView
        self.second_window = RegisterView()
        if self.second_window.isVisible():
            self.second_window.hide()

        self.third_window = LoginView()
        if self.third_window.isVisible():
            self.third_window.hide()

    def show_second_window(self):
        from views.register_view import RegisterView
        self.second_window = RegisterView()
        self.second_window.switch_first.connect(self.show_main_window)
        self.second_window.switch_third.connect(self.show_third_window)
        self.second_window.show()

        from views.home_view import HomeView
        self.main_window = HomeView()
        if self.main_window.isVisible():
            self.main_window.hide()

        self.third_window = LoginView()
        if self.third_window.isVisible():
            self.third_window.hide()

    def show_third_window(self):
        self.third_window = LoginView()
        self.third_window.switch_first.connect(self.show_main_window)
        self.third_window.switch_second.connect(self.show_second_window)
        self.third_window.show()

        from views.home_view import HomeView
        self.main_window = HomeView()
        if self.main_window.isVisible():
            self.main_window.hide()

        from views.register_view import RegisterView
        self.third_window = RegisterView()
        if self.third_window.isVisible():
            self.third_window.hide()
