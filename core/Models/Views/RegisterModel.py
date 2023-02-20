"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""


from PyQt6.QtWidgets import QMainWindow

from src.gui.ui.register.register_view import Ui_RegisterWindow


class RegisterModel(QMainWindow):

    def __init__(self):
        super(RegisterModel, self).__init__()

        self.register_ui = Ui_RegisterWindow()
        self.ui()

    def setup_ui(self):
        self.register_ui.setupUi(self)

    def ui(self):
        return self.setup_ui()