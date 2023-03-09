"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""
from PyQt6 import QtCore, QtSql
from PyQt6.QtCore import QFile
from PyQt6.QtGui import QAction
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import QMainWindow, QPushButton


class RegisterView(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super(RegisterView, self).__init__()

        self.form_data = {}

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

        self.form_data['firstname'] = self.ui.RegisterFormFirstnameLineEdit
        self.form_data['suffix'] = self.ui.RegisterFormSuffixLineEdit
        self.form_data['lastname'] = self.ui.RegisterFormLastnameLineEdit
        self.form_data['username'] = self.ui.RegisterFormUsernameLineEdit
        self.form_data['email'] = self.ui.RegisterFormEmailLineEdit
        self.form_data['password'] = self.ui.RegisterFormPasswordLineEdit_1
        self.form_data['password'].setEchoMode(self.ui.RegisterFormPasswordLineEdit_1.EchoMode.Password)

        self.form_data['confirmed_password'] = self.ui.RegisterFormPasswordLineEdit_2
        self.form_data['confirmed_password'].setEchoMode(self.ui.RegisterFormPasswordLineEdit_2.EchoMode.Password)

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

        self.ui.RegisterFormPasswordLabel_1.setText("Password")
        self.ui.RegisterFormPasswordLabel_1.adjustSize()

        self.ui.RegisterFormPasswordLabel_2.setText("Confirm password")
        self.ui.RegisterFormPasswordLabel_2.adjustSize()

        self.ui.RegisterFormSubmitBtn.setText("Register")
        self.ui.RegisterFormSubmitBtn.clicked.connect(self.check_credentials)

        self.connect_db()

    def connect_db(self):
        # https:// doc.qt.io/qtforpython/overviews/sql-driver.html
        db_name = "LearningQt.sqlite"
        if not QFile.exists(db_name):
            print('The database file doesn\'t exist yet')
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('LearningQt.sqlite')
            db.open()

            if QFile.exists(db_name):
                print('Connection active:', db.isOpen())
        else:
            print('The database file exists')
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('LearningQt.sqlite')
            db.open()
            print('Connection active:', db.isOpen())

        if db.open():
            print("Processing table..")
            conn = db

            # Creating table before adding values
            sql = '''CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    firstname VARCHAR(40) NOT NULL,
                    suffix VARCHAR(16) NOT NULL,
                    lastname VARCHAR(40) NOT NULL,
                    email VARCHAR(40) NOT NULL,
                    username VARCHAR(40) NOT NULL,
                    password VARCHAR(40) NOT NULL
                )
                '''
            conn.exec(sql)

    def check_credentials(self):
        firstname = self.form_data['firstname'].text()
        suffix = self.form_data['suffix'].text()
        lastname = self.form_data['lastname'].text()
        username = self.form_data['username'].text()
        email = self.form_data['email'].text()
        password = self.form_data['password'].text()

        db = QSqlDatabase.database("LearningQt.sqlite", open=True)

        query = QtSql.QSqlQuery(db)
        sql = '''
            INSERT INTO users(firstname, suffix, lastname, username, email, password) 
            VALUES(:firstname, :suffix, :lastname, :username, :email, :password)
        '''

        query.prepare(sql)
        query.bindValue(':firstname', firstname)
        query.bindValue(':suffix', suffix)
        query.bindValue(':lastname', lastname)
        query.bindValue(':username', username)
        query.bindValue(':email', email)
        query.bindValue(':password', password)
        query.exec()

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
