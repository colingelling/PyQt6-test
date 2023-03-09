"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction


class HomeView(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # load the layout
        from src.gui.ui.home.home_view import Ui_HomeWindow
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)

        # import CSS file
        css_file = "src/gui/css/home.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

        self.content()

    def content(self):

        window_title = 'Home'

        self.setWindowTitle(f"{window_title}: My first PyQt6 program!")

        # Navigation

        button_home = QAction(f"{window_title}", self)
        button_register = QAction("Register", self)
        button_login = QAction("Login", self)

        button_home.triggered.connect(self.switch_first_window)
        button_register.triggered.connect(self.switch_second_window)
        button_login.triggered.connect(self.switch_third_window)

        menubar = self.ui.menuBar
        menubar.addAction(button_home)
        menubar.addAction(button_register)
        menubar.addAction(button_login)

        # Navigation end

        # Begin: tab widget (tab 1)

        first_tab_headline = 'Welcome'

        self.ui.tabWidget.setTabText(0, first_tab_headline)

        # Same thing for this, prevent cutting the label/add dynamic length according to text
        self.ui.homeIntroTitleFrameTab_1.adjustSize()

        # Divide the text over multiple lines instead of one limited by an x amount of characters
        self.ui.homeIntroLongTextTab_1.setMinimumWidth(600)
        self.ui.homeIntroLongTextTab_1.setWordWrap(1)
        self.ui.homeIntroLongTextTab_1.setText(
            "This application is a practice program in order to learn the Python language including OOP terms and most "
            "of all knowing what to do with PyQt6."
            "This application serves the ability to register an account whether you can sign in afterwards."
        )

        self.ui.homeIntroLongTextTab_1.adjustSize()

        # End: tab widget (tab 1)

        # Begin: tab widget (tab 2)
        # Also the following block has the same rules as the code described above this text

        second_tab_headline = 'Application language information'
        self.ui.tabWidget.setTabText(1, second_tab_headline)

        self.ui.homeIntroTitleFrameTab_2.adjustSize()

        self.ui.homeIntroLongTextTab_2.setMinimumWidth(600)
        self.ui.homeIntroLongTextTab_2.setWordWrap(1)
        self.ui.homeIntroLongTextTab_2.setText(
            "This program is made with Python and the PyQt(6) library. The elements are put in by using Qt Designer,"
            "which is a UI element addition application itself. This stores .ui files per window, and these are "
            "converted in the background as .py files because of the fact that it is easier to work with."
        )

        self.ui.homeIntroLongTextTab_2.adjustSize()

        # End: tab widget (tab 2)

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
