"""

Created by Colin Gelling on 01/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

from core.Actions.Controllers.Navigation.ViewController import ViewController
from core.Configurators.EnvironmentConfigurator import EnvironmentConfigurator
from core.Configurators.LayoutConfigurator import LayoutConfigurator


class UserView(QMainWindow, EnvironmentConfigurator, ViewController, LayoutConfigurator):

    # TODO: find a solution for multiple inheritance, can be messy like the way that it is now

    switch_first = QtCore.pyqtSignal()
    switch_second = QtCore.pyqtSignal()
    switch_third = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # set layout
        self.ui = self.load_user_ui()

        for key, value in EnvironmentConfigurator.app_credentials.items():
            if 'NAME' in key:
                self.setWindowTitle(f"Welcome user: {value}")

        self.content()

    def setup_navigation(self):
        pass

    def content(self):

        # set ui
        ui = self.ui

        from core.Handlers.Sessions.UserSessions import UserSessions
        user_sessions = UserSessions()

        # Navigation

        settings = user_sessions.settings
        settings.beginGroup("user_session")

        # TODO: session verification check and retrieve firstname in relation to the id

        print(settings.value('id'))

        menubar = ui.menuBar
        menu = menubar.addMenu(f'{ settings.value("user") }')
        # menu = menubar.addMenu(f'welcome user!')

        edit = menu.addMenu("Settings")
        edit.addAction("copy")
        edit.addAction("paste")

        menu.addAction("Logout")
        menu.triggered[QAction].connect(self.processtrigger)

        settings.endGroup()

        # Navigation end

        ui.welcomeUser.setText("Welcome, user_name!")

        ui.userIntroductionLabel.setText("You're successfully logged in now, this area is all about showing you "
                                              "data coming from the database behind this program.")

    def switch_first_window(self):
        self.switch_first.emit()

    def switch_second_window(self):
        self.switch_second.emit()

    def switch_third_window(self):
        self.switch_third.emit()

    def processtrigger(self):
        from PyQt6.QtCore import QSettings
        settings = QSettings("PyQt-test", "LoggedUser")
        settings.beginGroup("user_session")
        settings.remove("user_session")
        settings.endGroup()

        # if settings.allKeys():
        #     print("Session not empty")

        print(settings.allKeys())
