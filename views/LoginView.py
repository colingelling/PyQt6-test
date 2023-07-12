"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.ViewController import ViewController
from core.Modules.ManageLogin import ManageLogin
from core.Layout.ManageUi import ManageUi


class LoginView(QMainWindow, ViewController, ManageUi, ManageLogin):

    switch_first = QtCore.pyqtSignal(str)
    switch_second = QtCore.pyqtSignal(str)
    switch_third = QtCore.pyqtSignal(str)

    def __init__(self):
        super(LoginView, self).__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_login_ui()

        for key, value in self.app_credentials.items():
            if 'NAME' in key:
                self.window_title = 'Login'
                self.setWindowTitle(f"{self.window_title}: {value}")

        self.home_nav = None
        self.register_nav = None
        self.login_nav = None

        self.setup_navigation()
        self.show_content()

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

    def show_content(self):
        # set ui
        ui = self.ui

        # navigation
        menubar = ui.menuBar
        menubar.addAction(self.home_nav)
        menubar.addAction(self.register_nav)
        menubar.addAction(self.login_nav)

        ui.LoginViewTitleLabel.setText("Login")
        ui.LoginViewTitleLabel.adjustSize()

        ui.LoginViewDescriptionLabel.setText("Sign in to your account")
        ui.LoginViewDescriptionLabel.adjustSize()

        ui.LoginFormUsernameLabel.setText("Username or email address")
        ui.LoginFormUsernameLabel.adjustSize()

        ui.LoginFormPasswordLabel.setText("Password")
        ui.LoginFormPasswordLabel.adjustSize()
        ui.LoginFormPasswordLineEdit.setEchoMode(ui.LoginFormPasswordLineEdit.EchoMode.Password)

        self.setTabOrder(ui.LoginFormUsernameLineEdit, ui.LoginFormPasswordLineEdit)
        ui.LoginFormUsernameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.LoginFormPasswordLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.LoginFormSubmitBtn.setText("Sign in")
        ui.LoginFormSubmitBtn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.LoginFormSubmitBtn.clicked.connect(self.pre_submit)

    def pre_submit(self):

        """
            Prepare the submit process. Creating a Dictionary and filling it with the form field data before forwarding.
            :return:
        """

        ui = self.ui

        user = ui.LoginFormUsernameLineEdit.text()
        password = ui.LoginFormPasswordLineEdit.text()

        self.form_data = {
            'user': user,
            'password': password,
        }

        # forward to the submit process
        self.submit()

    def switch_home_window(self):
        self.show_home()

    def switch_register_window(self):
        self.show_register()

    def switch_login_window(self):
        self.show_login()
