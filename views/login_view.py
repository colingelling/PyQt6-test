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
        # self.form_data['email'] = self.ui.RegisterFormEmailLineEdit  # TODO: later, make sure that it does work with the username
        self.form_data['password'] = self.ui.LoginFormPasswordLineEdit
        self.form_data['password'].setEchoMode(self.ui.LoginFormPasswordLineEdit.EchoMode.Password)

        self.ui.LoginFormUsernameLabel.setText("Username or email address")
        self.ui.LoginFormUsernameLabel.adjustSize()

        self.ui.LoginFormPasswordLabel.setText("Password")
        self.ui.LoginFormPasswordLabel.adjustSize()

        self.ui.LoginFormSubmitBtn.setText("Sign in")

        # open the database connection
        self.open_connection()

        self.ui.LoginFormSubmitBtn.clicked.connect(self.check_credentials)

    def check_credentials(self):

        username = self.ui.LoginFormUsernameLineEdit.text()
        password = self.ui.LoginFormPasswordLineEdit.text()

        # print(f"Username: { username1 }, password: { password1 }")

        # from PyQt6 import QtSql
        # pointer = QtSql.QSqlQuery(self.db)
        # pointer.exec("SELECT * FROM users WHERE username = '%s' AND password = '%s';" %(username1, password1))
        # pointer.first()

        # query = '''
        #             # SELECT id, email, username, password from users WHERE email = '%s' AND username = '%s' AND password = '%s'; %(username, password)
        #         '''
        #
        # from PyQt6 import QtSql
        # pointer = QtSql.QSqlQuery(self.db)
        # pointer.exec(query)
        # pointer.first()

        # find_user_query = "SELECT username, password FROM users WHERE username = '%s' and password = '%s';" %(username, password)
        from PyQt6 import QtSql
        pointer = QtSql.QSqlQuery(self.db)
        # pointer.exec(find_user_query)
        # pointer.first()

        # print(f"username: { pointer.value('username') } and password: { pointer.value('password') }")

        # TODO: decode pointer.value('password')
        # TODO: retrieve user password and decode it

        find_user = "SELECT username, password FROM users;"
        pointer.exec(find_user)
        pointer.first()

        print(f"Hashed password from the database: {pointer.value('password')}")

        field_to_encrypt = password
        change_format = "{}".format(field_to_encrypt)
        encrypted_password = field_to_encrypt.encode('utf-8')

        db_pass = pointer.value('password')

        import bcrypt
        if bcrypt.checkpw(password.encode('utf-8'), db_pass.encode('utf-8')):
            print('Password match!')
        else:
            print('There is some more work left to do..')

        # if username == pointer.value('username'):
        #     print('username matched!')
        #     if bcrypt.checkpw(hashed_pw, pointer.value('password')):
        #         print('Password match!')
        #     else:
        #         print('There is some more work left to do..')

        # if str(username) == pointer.value("username") and str(password) == pointer.value("password"):
        #     print('Found!')

        # print(pointer.value("username"))

        # if self.ui.LoginFormUsernameLineEdit.text() == username1 and self.ui.LoginFormPasswordLineEdit.text() == password1:
        #     print("hello")
        # else:
        #     print("nothing match")
        #
        # print(f"Encrypted password: { pointer.value('password') }")

        # change_format = "{}".format(pointer.value('password'))
        # encrypted_password = password1.encode('utf-8')
        # salt_object = bcrypt.gensalt(rounds=16)
        # hashed_str = bcrypt.hashpw(encrypted_password, salt_object)
        #
        # print("The encrypted text or password is: {}".format(hashed_str))

        # import bcrypt
        # field_to_encrypt = password1
        # change_format = "{}".format(field_to_encrypt)
        # encrypted_password = field_to_encrypt.encode('utf-8')
        # salt_object = bcrypt.gensalt(rounds=16)
        # hashed_str = bcrypt.hashpw(encrypted_password, salt_object)

        # if pointer.value('username') != None and pointer.value('password') != None:
        #     print("Login successful!")
        # else:
        #     print("Login failed!")

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
