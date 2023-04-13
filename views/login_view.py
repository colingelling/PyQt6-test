"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Configurators.LayoutConfigurator import LayoutConfigurator
from core.Management.ManageLogin import ManageLogin


class LoginView(QMainWindow, LayoutConfigurator, ManageLogin):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    loggedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginView, self).__init__()
        ManageLogin.__init__(self)

        self.ui = self.load_login_ui()

        window_title = 'Login'  # TODO: use another specific subjected file for these type of things
        self.setWindowTitle(f"{window_title}: My first PyQt6 program!")

        self.show_content()

    def show_content(self):

        ui = self.ui

        # Navigation

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        button_home.triggered.connect(self.switch_first_window)
        button_register.triggered.connect(self.switch_second_window)
        button_login.triggered.connect(self.switch_third_window)

        menubar = ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

        ui.LoginViewTitleLabel.setText("Login")
        ui.LoginViewTitleLabel.adjustSize()

        ui.LoginViewDescriptionLabel.setText("Sign in to your account")
        ui.LoginViewDescriptionLabel.adjustSize()

        # bind form field -data to key values for preparation purposes - TODO: could possibly be removed
        # self.form_data['username'] = ui.LoginFormUsernameLineEdit
        # self.form_data['password'] = ui.LoginFormPasswordLineEdit
        # self.form_data['password'].setEchoMode(ui.LoginFormPasswordLineEdit.EchoMode.Password)

        ui.LoginFormUsernameLabel.setText("Username or email address")
        ui.LoginFormUsernameLabel.adjustSize()

        ui.LoginFormPasswordLabel.setText("Password")
        ui.LoginFormPasswordLabel.adjustSize()
        ui.LoginFormPasswordLineEdit.setEchoMode(ui.LoginFormPasswordLineEdit.EchoMode.Password)

        ui.LoginFormSubmitBtn.setText("Sign in")

        ui.LoginFormSubmitBtn.clicked.connect(self.check_credentials)

    # TODO: move to the navigation subject folder
    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
    # end TODO

    # def trigger_login(self):
    #     self.loggedSignal.emit()
