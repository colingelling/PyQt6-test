"""

Created by Colin Gelling on 28/3/2023
Using Pycharm Professional

"""

from PyQt6 import QtCore


class Signals:

    home_window_signal = QtCore.pyqtSignal()
    register_window_signal = QtCore.pyqtSignal()
    login_window_signal = QtCore.pyqtSignal()

    logged_signal = QtCore.pyqtSignal()

    def home_window_switch(self):
        self.home_window_signal.emit()

    def register_window_switch(self):
        self.register_window_signal.emit()

    def login_window_switch(self):
        self.login_window_signal.emit()

    def trigger_login(self):
        self.logged_signal.emit()
