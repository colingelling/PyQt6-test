"""

Created by Colin Gelling on 24/05/2023
Using Pycharm Professional

"""

from PyQt6.QtCore import QSettings


class ViewSessions:
    view_session = {}
    view_objects = {}
    counter = 0

    def __init__(self):
        super().__init__()
        self.settings = QSettings()

    @classmethod
    def generate_unique_identifier(cls):
        ViewSessions.counter += 1
        return ViewSessions.counter

    def set_session(self):
        self.settings.beginGroup("view_session")
        self.settings.clear()

        if self.view_session:
            for key, value in self.view_session.items():
                if value is not None:
                    view_identifier = self.generate_unique_identifier()
                    ViewSessions.view_objects[view_identifier] = value
                    self.settings.setValue(key, view_identifier)

        self.settings.endGroup()

    def get_session(self):

        view_objects = {}

        self.settings.beginGroup("view_session")

        keys = self.settings.allKeys()
        for key in keys:
            view_identifier = self.settings.value(key)
            if view_identifier is not None:
                view_object = ViewSessions.view_objects.get(view_identifier)
                if view_object is not None:
                    view_objects = {key: view_object}
                else:
                    print(f"{key}: View object with identifier {view_identifier} is missing.")

        self.settings.endGroup()

        if view_objects:
            return view_objects

    def destroy_session(self):
        return self.settings.clear()
