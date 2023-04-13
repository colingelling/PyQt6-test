"""

Created by Colin Gelling on 03/3/2023
Using Pycharm Professional

"""

from core.Models.User import User

from PyQt6.QtCore import QSettings


class UserSessionHandler(User):
    def __init__(self):
        super(UserSessionHandler).__init__()
        self.settings = QSettings()

    def set_session(self):
        # set the session

        self.settings.beginGroup("user_session")

        # TODO: get the user credentials from the User model

        # self.settings.setValue('user_id', user_id)
        # self.settings.setValue('user', username)

        self.settings.endGroup()

    def get_session(self):
        user_id = self.settings.value

    def destroy_session(self):
        return self.settings.clear()
