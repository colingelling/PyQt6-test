"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""
from PyQt6 import QtCore, QtSql
from PyQt6.QtCore import QFile
from PyQt6.QtGui import QAction
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QMainWindow, QPushButton

from core.Models.RegisterModel import RegisterModel


class RegisterView(QMainWindow, RegisterModel):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super(RegisterView, self).__init__()

        self.initialize_layout()
        self.load_css()
        self.show_content()

    def initialize_layout(self):
        # load the layout
        from src.gui.ui.register.register_view import Ui_RegisterWindow
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)

    def load_css(self):
        # import CSS file
        css_file = "src/gui/css/register.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def show_content(self):
        window_title = 'Register'

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

        self.ui.RegisterViewTitleLabel.setText("Register")
        self.ui.RegisterViewTitleLabel.adjustSize()

        self.ui.RegisterViewDescriptionLabel.setText("Create an account")
        self.ui.RegisterViewDescriptionLabel.adjustSize()

        # bind form field -data to key values for preparation purposes
        self.form_data['firstname'] = self.ui.RegisterFormFirstnameLineEdit
        self.form_data['suffix'] = self.ui.RegisterFormSuffixLineEdit
        self.form_data['lastname'] = self.ui.RegisterFormLastnameLineEdit
        self.form_data['username'] = self.ui.RegisterFormUsernameLineEdit
        self.form_data['email'] = self.ui.RegisterFormEmailLineEdit
        self.form_data['password'] = self.ui.RegisterFormPasswordLineEdit_1
        self.form_data['password'].setEchoMode(self.ui.RegisterFormPasswordLineEdit_1.EchoMode.Password)
        self.form_data['confirmed_password'] = self.ui.RegisterFormPasswordLineEdit_2
        self.form_data['confirmed_password'].setEchoMode(self.ui.RegisterFormPasswordLineEdit_2.EchoMode.Password)

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

        self.ui.RegisterFormPasswordLabel_1.setText("Password")
        self.ui.RegisterFormPasswordLabel_1.adjustSize()

        self.ui.RegisterFormPasswordLabel_2.setText("Confirm password")
        self.ui.RegisterFormPasswordLabel_2.adjustSize()

        # open the database connection
        self.open_connection()

        # create the users table (when doesn't exist)
        self.create_users_table()

        self.ui.RegisterFormSubmitBtn.setText("Register")
        self.ui.RegisterFormSubmitBtn.clicked.connect(self.create_user)

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
