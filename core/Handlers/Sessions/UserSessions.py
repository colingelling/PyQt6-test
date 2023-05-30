"""

Created by Colin Gelling on 03/03/2023
Using Pycharm Professional

"""

from PyQt6.QtCore import QSettings

from core.Models.User import User


class UserSessions(User):
    def __init__(self):
        super().__init__()
        self.settings = QSettings()

    def set_session(self):

        # set and name the session group
        self.settings.beginGroup("user_session")

        # make sure that the session is empty when starting as a process
        self.settings.clear()

        user_data = self.user_data

        # put the values from a successful login into a session
        if user_data is not None:
            for key, value in user_data.items():
                self.settings.setValue(key, value)

        # close session
        self.settings.endGroup()

    def get_session(self):

        # set and name the session group
        self.settings.beginGroup("user_session")

        keys = self.settings.allKeys()
        for key in keys:
            print(key, self.settings.value(key))

        # TODO: need to figure out what to do with this function

        # close session
        self.settings.endGroup()

    def handle_window(self):
        # TODO:
        #  - Trigger Controller method
        #  - Extend view functionality,
        pass

    def check_session(self):
        # TODO:
        #   1) Get user id's
        #   2) Compare session id with a user id

        # retrieve user id's
        self.get_user_ids()

        collection = self.user_ids

        if not collection:
            raise ValueError("The attribute that holds the user id's has not been set properly.")

        for value in collection:
            print(f"Found id '{ value }'")

    def destroy_session(self):
        return self.settings.clear()
