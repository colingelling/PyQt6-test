"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow


class RegisterView(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        from src.gui.ui.register.register_view import Ui_RegisterWindow
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)

        self.content()

    def content(self):
        self.setWindowTitle('Register')

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

        self.ui.RegisterViewTitleLabel.setText("Register")
        self.ui.RegisterViewTitleLabel.adjustSize()

        self.ui.RegisterViewDescriptionLabel.setText("Create an account")
        self.ui.RegisterViewDescriptionLabel.adjustSize()

        self.ui.RegisterFormFirstnameLabel.setText("Firstname")
        self.ui.RegisterFormFirstnameLabel.adjustSize()

        self.ui.RegisterFormSuffixLabel.setText("Suffix")
        self.ui.RegisterFormSuffixLabel.adjustSize()

        self.ui.RegisterFormLastnameLabel.setText("Lastname")
        self.ui.RegisterFormLastnameLabel.adjustSize()

        self.ui.RegisterFormUsernameLabel.setText("Username")
        self.ui.RegisterFormUsernameLabel.adjustSize()

        self.ui.RegisterFormEmailLabel.setText("Email address")
        self.ui.RegisterFormEmailLabel.adjustSize()

        self.ui.RegisterFormPasswordLabel.setText("Password")
        self.ui.RegisterFormPasswordLabel.adjustSize()

        self.ui.RegisterFormSubmitBtn.setText("Register account")

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
