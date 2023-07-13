"""

    Created by Colin Gelling on 24/05/2023
    Using Pycharm Professional

"""

from PyQt6.QtCore import QSettings


class ManageViewSession:

    view_session = {}
    view_objects = {}
    counter = 0

    def __init__(self):
        super().__init__()
        self.settings = QSettings()

    @classmethod
    def generate_unique_identifier(cls):
        ManageViewSession.counter += 1
        return ManageViewSession.counter

    def set_session(self):
        # activate a session instance
        self.settings.beginGroup("view_session")
        self.settings.clear()  # make sure that the session does not contain any 'view' values

        if not self.view_session:
            raise ValueError("View session attribute has returned empty")

        for key, value in self.view_session.items():
            if value is not None:
                view_identifier = self.generate_unique_identifier()
                ManageViewSession.view_objects[view_identifier] = value
                self.settings.setValue(key, view_identifier)

        # close session
        self.settings.endGroup()

    def get_session(self):

        view_objects = {}

        self.settings.beginGroup("view_session")

        keys = self.settings.allKeys()
        for key in keys:
            view_identifier = self.settings.value(key)
            if view_identifier is not None:
                view_object = ManageViewSession.view_objects.get(view_identifier)
                if view_object is not None:
                    view_objects = {key: view_object}
                else:
                    print(f"{key}: View object with identifier {view_identifier} is missing.")

        self.settings.endGroup()

        if view_objects:
            return view_objects

    def destroy_session(self):
        return self.settings.clear()
