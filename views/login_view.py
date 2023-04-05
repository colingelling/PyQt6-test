"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""
from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Models.User import User


class LoginView(QMainWindow, User):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    loggedSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(LoginView, self).__init__()

        self.initialize_layout()
        self.load_css()
        self.show_content()

    def initialize_layout(self):
        # load the layout
        from src.gui.ui.login.login_view import Ui_LoginWindow
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

    def load_css(self):
        # import CSS file
        css_file = "src/gui/css/login.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def show_content(self):
        window_title = 'Login'

        self.setWindowTitle(f"{window_title}: My first PyQt6 program!")

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

        self.ui.LoginViewTitleLabel.setText("Login")
        self.ui.LoginViewTitleLabel.adjustSize()

        self.ui.LoginViewDescriptionLabel.setText("Sign in to your account")
        self.ui.LoginViewDescriptionLabel.adjustSize()

        # bind form field -data to key values for preparation purposes
        self.form_data['username'] = self.ui.LoginFormUsernameLineEdit
        self.form_data['password'] = self.ui.LoginFormPasswordLineEdit
        self.form_data['password'].setEchoMode(self.ui.LoginFormPasswordLineEdit.EchoMode.Password)

        self.ui.LoginFormUsernameLabel.setText("Username or email address")
        self.ui.LoginFormUsernameLabel.adjustSize()

        self.ui.LoginFormPasswordLabel.setText("Password")
        self.ui.LoginFormPasswordLabel.adjustSize()

        self.ui.LoginFormSubmitBtn.setText("Sign in")

        self.ui.LoginFormSubmitBtn.clicked.connect(self.check_credentials)

    def check_credentials(self):

        self.open_connection()
        conn = self.connection

        if conn:
            print(f"Logging in user..")

            form_username_email = self.ui.LoginFormUsernameLineEdit.text()
            form_password = self.ui.LoginFormPasswordLineEdit.text()

            import bcrypt

            query = f"SELECT id, email, username, password FROM users WHERE email = '{ form_username_email }' "\
                    f"OR username = '{ form_username_email }'"
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.commit()

            users = []

            for value in rows:
                users.append([
                    value[0],
                    value[1],
                    value[2],
                    value[3]
                ])

            if users:
                for user_id, email, username, password in users:

                    if bcrypt.checkpw(form_password.encode('utf-8'), password.encode('utf-8')):
                        # set the session
                        from PyQt6.QtCore import QSettings
                        settings = QSettings("PyQt-test", "LoggedUser")
                        settings.beginGroup("user_session")
                        settings.setValue('id', user_id)
                        settings.setValue('user', username)
                        settings.endGroup()

                    # use background functionality for submitting into the next window
                    self.trigger_login()

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()

    def trigger_login(self):
        self.loggedSignal.emit()
