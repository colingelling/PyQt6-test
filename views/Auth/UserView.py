"""

Created by Colin Gelling on 01/01/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from core.Controllers.ViewController import ViewController
from core.Environment.CollectEnvironmentalValues import CollectEnvironmentalValues
from core.Layout.ManageUi import ManageUi


class UserView(QMainWindow, CollectEnvironmentalValues, ViewController, ManageUi):

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # set layout
        self.ui = self.load_user_ui()

        # open session since this is a protected view
        import views.Auth.Sessions.requests as SessionRequests
        SessionRequests.load_user_session()

        for key, value in CollectEnvironmentalValues.app_credentials.items():
            if 'NAME' in key:
                self.setWindowTitle(f"Welcome | {value}")

        # set accessible class
        from core.Sessions.ManageUserSession import ManageUserSession
        self.user_sessions = ManageUserSession()

        # set navigation
        self.setup_navigation()

        # show view content
        self.content()

        # session can be closed
        self.user_sessions.close_session()

        # TODO: logout means returning back to view and clearing session

    def setup_navigation(self):

        # set ui within scope
        ui = self.ui

        user_logout = QAction("Logout", self)

        menubar = ui.menuBar
        menubar.addMenu("Settings")
        menubar.addAction(user_logout)  # TODO: Trigger logout function, return back to the HomeView

    def content(self):
        # set ui within scope
        ui = self.ui

        # declare session
        session = self.user_sessions.settings

        ui.welcomeUser.setText(f"Welcome, { session.value('firstname') }!")

        ui.userIntroductionLabel.setText("You're successfully logged in now, this area is all about showing you "
                                         "some data coming from the database behind this app.")

        ui.userDataTitleLabel.setText("Displayed user information")

        ui.userDataNameTitleLabel.setText("Name:")  # TODO: firstname, suffix + lastname
        ui.userDataCreatedLabel.setText("Account created on:")  # TODO: created_at

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()
