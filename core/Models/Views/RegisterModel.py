"""

Created by Colin Gelling on 30/1/2023

"""


from PyQt6.QtWidgets import QMainWindow

from src.gui.ui.register.register_view import Ui_RegisterWindow


class RegisterModel(QMainWindow):

    def __init__(self):
        super(RegisterModel, self).__init__()

        self.home_ui = Ui_RegisterWindow()
        self.ui()

    def setup_ui(self):
        self.home_ui.setupUi(self)

    def ui(self):
        return self.setup_ui()