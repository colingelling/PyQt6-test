"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow


class HomeView(QMainWindow):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        from src.gui.ui.home.home_view import Ui_HomeWindow
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)

        self.content()

    def content(self):

        self.setWindowTitle("Home: My first PyQt6 program!")

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

        # Navigation end

        first_tab_headline = 'Welcome'

        self.ui.tabWidget.setTabText(0, first_tab_headline)

        # Set text for the first label (first tab)
        self.ui.homeIntroLabelTabTitle_1.setText(first_tab_headline)

        # Make sure that the label is not going to be cut in relation to the text size
        self.ui.homeIntroLabelTabTitle_1.adjustSize()

        # Same thing for this, prevent cutting the label/add dynamic length according to text
        self.ui.homeIntroTitleFrameTab_1.adjustSize()

        # Divide the text over multiple lines instead of one limited by an x amount of characters
        self.ui.homeIntroLongTextTab_1.setWordWrap(1)
        self.ui.homeIntroLongTextTab_1.setText(
            "This application is a practice program in order to learn the Python language including OOP terms and most "
            "of all knowing what to do with PyQt6."
            "This application serves the ability to register an account whether you can sign in afterwards."
        )  # TODO: Fix height

        # The following block has the same rules as the code described above this text

        second_tab_headline = 'Application language information'
        self.ui.tabWidget.setTabText(1, second_tab_headline)
        self.ui.homeIntroLabelTabTitle_2.setText(second_tab_headline)
        self.ui.homeIntroLabelTabTitle_2.adjustSize()
        self.ui.homeIntroTitleFrameTab_2.adjustSize()
        self.ui.homeIntroLongTextTab_2.setWordWrap(1)
        self.ui.homeIntroLongTextTab_2.setText(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        )

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
