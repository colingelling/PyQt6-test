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
