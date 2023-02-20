"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6.QtWidgets import QMainWindow

from src.gui.ui.login.login_view import Ui_LoginWindow


class LoginModel(QMainWindow):

    def __init__(self):
        super(LoginModel, self).__init__()

        self.login_ui = Ui_LoginWindow()
        self.ui()

    def setup_ui(self):
        self.login_ui.setupUi(self)

    def ui(self):
        return self.setup_ui()
