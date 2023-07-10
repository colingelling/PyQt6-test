"""

Created by Colin Gelling on 30/01/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.Navigation.ViewController import ViewController
from core.Layout.SetUi import SetUi
from core.Modules.Manage.ManageRegister import RegisterManager


class RegisterView(QMainWindow, ViewController, SetUi, RegisterManager):

    switch_first = QtCore.pyqtSignal(str)
    switch_second = QtCore.pyqtSignal(str)
    switch_third = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # set Ui (must happen before doing anything else because any alterations to the window won't work)
        self.ui = self.load_register_ui()

        for key, value in self.app_credentials.items():
            if 'NAME' in key:
                self.window_title = 'Register'
                self.setWindowTitle(f"{self.window_title}: { value }")

        self.home_nav = None
        self.register_nav = None
        self.login_nav = None

        self.setup_navigation()

        self.form_data = {}

        # show the ui elements
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

        ui = self.ui

        # Navigation

        button_home = QAction("Home", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        button_home.triggered.connect(self.switch_home_window)
        button_register.triggered.connect(self.switch_register_window)
        button_login.triggered.connect(self.switch_login_window)

        menubar = ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

        ui.RegisterViewTitleLabel.setText("Register")
        ui.RegisterViewTitleLabel.adjustSize()

        ui.RegisterViewDescriptionLabel.setText("Create an account")
        ui.RegisterViewDescriptionLabel.adjustSize()

        from PyQt6.QtCore import Qt

        # TODO 's:
        #  Check whether form fields are empty or not within the view side instead of here

        ui.RegisterFormFirstnameLabel.setText("Firstname")
        ui.RegisterFormFirstnameLabel.adjustSize()
        ui.RegisterFormFirstnameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormFirstnameLineEdit.setFocus()

        ui.RegisterFormSuffixLabel.setText("Suffix")
        ui.RegisterFormSuffixLabel.adjustSize()
        ui.RegisterFormSuffixLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormLastnameLabel.setText("Lastname")
        ui.RegisterFormLastnameLabel.adjustSize()
        ui.RegisterFormLastnameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormUsernameLabel.setText("Username")
        ui.RegisterFormUsernameLabel.adjustSize()
        ui.RegisterFormUsernameLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormEmailLabel.setText("Email address")
        ui.RegisterFormEmailLabel.adjustSize()
        ui.RegisterFormEmailLineEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        ui.RegisterFormPasswordLabel_1.setText("Password")
        ui.RegisterFormPasswordLabel_1.adjustSize()
        ui.RegisterFormPasswordLineEdit_1.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormPasswordLineEdit_1.setEchoMode(ui.RegisterFormPasswordLineEdit_1.EchoMode.Password)

        ui.RegisterFormPasswordLabel_2.setText("Confirm password")
        ui.RegisterFormPasswordLabel_2.adjustSize()
        ui.RegisterFormPasswordLineEdit_2.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormPasswordLineEdit_2.setEchoMode(ui.RegisterFormPasswordLineEdit_2.EchoMode.Password)

        # Set the tab order among line edits
        self.setTabOrder(ui.RegisterFormFirstnameLineEdit, ui.RegisterFormSuffixLineEdit)
        self.setTabOrder(ui.RegisterFormSuffixLineEdit, ui.RegisterFormLastnameLineEdit)
        self.setTabOrder(ui.RegisterFormLastnameLineEdit, ui.RegisterFormUsernameLineEdit)
        self.setTabOrder(ui.RegisterFormUsernameLineEdit, ui.RegisterFormEmailLineEdit)
        self.setTabOrder(ui.RegisterFormEmailLineEdit, ui.RegisterFormPasswordLineEdit_1)
        self.setTabOrder(ui.RegisterFormPasswordLineEdit_1, ui.RegisterFormPasswordLineEdit_2)

        ui.RegisterFormSubmitBtn.setText("Register")
        ui.RegisterFormSubmitBtn.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        ui.RegisterFormSubmitBtn.clicked.connect(self.pre_submit)

    def pre_submit(self):

        """
            Prepare the submit process. Creating a Dictionary and filling it with the form field data before forwarding.
            :return:
        """

        ui = self.ui

        firstname = ui.RegisterFormFirstnameLineEdit.text()
        suffix = ui.RegisterFormSuffixLineEdit.text()
        lastname = ui.RegisterFormLastnameLineEdit.text()
        username = ui.RegisterFormUsernameLineEdit.text()
        email = ui.RegisterFormEmailLineEdit.text()
        password = ui.RegisterFormPasswordLineEdit_1.text()
        confirmed_password = ui.RegisterFormPasswordLineEdit_2.text()

        self.form_data = {
            'firstname': firstname,
            'suffix': suffix,
            'lastname': lastname,
            'username': username,
            'email': email,
            'password': password,
            'confirmed_password': confirmed_password
        }

        # forward to the actual submit process
        self.submit()

    def switch_home_window(self):
        self.show_home()

    def switch_register_window(self):
        self.show_register()

    def switch_login_window(self):
        self.show_login()
