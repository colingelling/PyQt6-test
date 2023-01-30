"""

Created by Colin Gelling on 30/1/2023

"""


from PyQt6.QtWidgets import QMainWindow

from src.gui.ui.home.home_view import Ui_HomeWindow


class HomeModel(QMainWindow):

    def __init__(self):
        super(HomeModel, self).__init__()

        self.home_ui = Ui_HomeWindow()
        self.ui()

    def setup_ui(self):
        self.home_ui.setupUi(self)

    def ui(self):
        return self.setup_ui()