from PyQt6.QtSql import QSqlQuery

from core.Action.Connectors.DatabaseConnector import DatabaseConnector


class RegisterModel(DatabaseConnector):
    def __init__(self):
        super(RegisterModel, self).__init__()

    def open_db(self):
        pass

    def close_db(self):
        pass

    def create_users_table(self):
        pass
