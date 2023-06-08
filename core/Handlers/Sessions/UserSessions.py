"""

Created by Colin Gelling on 03/03/2023
Using Pycharm Professional

"""

from PyQt6.QtCore import QSettings

from core.Handlers.Database.UserDatabaseHandler import UserDatabaseHandler


class UserSessions(UserDatabaseHandler):

    settings = QSettings()

    current_session = {}
    request_session = []
    new_session = {}

    def __init__(self):
        super().__init__()

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

    def open_session(self):

        # set and return session
        session_opener = self.settings.beginGroup("user_session")
        return session_opener

    def close_session(self):

        # when session is active
        if self.settings:
            for key in self.request_session:
                self.settings.remove(key)
                self.settings.sync()
                self.settings.endGroup()

        # TODO: not showing, possibly needs another approach
        if not self.settings:
            print("Session has been destroyed.")

    def check_session(self):
        # TODO:
        #   1) Get user id's
        #   2) Compare session id with a user id
        #   - Also use another approach for this?

        # retrieve user id's
        self.get_user_ids()

        collection = self.user_ids

        if not collection:
            raise ValueError("The attribute that holds the user id's has not been set properly.")

        for value in collection:
            print(f"Found id '{ value }'")

    def change_session(self):
        # only continue when there are requested values
        if self.request_session:
            # scope declaration
            requested_session = self.request_session
            current_session = self.current_session

            # iterate over values and prepare the new collection
            for key, value in current_session.items():
                if "id" in key:
                    self.new_session = {
                        'id': value
                    }

            # scope declaration (als returns user_id/session_id)
            new = self.new_session

            # assign the 'requested_session' key and put it into the new collection
            if current_session and requested_session and new:
                for requested_value in requested_session:
                    if requested_value not in new:
                        new.update({
                            requested_value: None
                        })

            # push collection values to the next one in order to finish the task
            UserDatabaseHandler.new_session.update(new)

            # function call giving a parameter for retrieving database table information
            self.retrieve_rows('users')
