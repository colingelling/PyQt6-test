"""

Created by Colin Gelling on 30/1/2023

"""

import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication

import core.Models.Views.LoginModel as LoginModel


class LoginView(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(LoginView, self).__init__(parent)

        self.view_ui = LoginModel.LoginModel()
        self.ui()
        self.content()

        self.switch_window.connect(self.test)

    def ui(self):
        self.view_ui.setup_ui()
        self.view_ui.show()

    def content(self):
        self.view_ui.setWindowTitle('Login')
        button = self.view_ui.login_ui.pushButton
        button.setText('Go to Test screen')
        button.clicked.connect(self.test)

    def test(self):
        from router.routes import Routes as route
        ui = self.view_ui
        route.test()
        ui.close()


app = QApplication(sys.argv)
window = LoginView()
