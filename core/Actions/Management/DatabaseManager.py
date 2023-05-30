"""

Created by Colin Gelling on 05/05/2023
Using Pycharm Professional

"""


class DatabaseManager:
    def __init__(self):
        super().__init__()

    @staticmethod
    def initialize_connection():
        from core.Actions.Connections.Database.Connectors.SQLiteConnector import SQLiteConnector
        class_instance = SQLiteConnector()
        class_method = class_instance.initialize_connection()
        return class_method

    @staticmethod
    def use_connection():
        from core.Actions.Connections.Database.SQLite.TableCreation import TableCreation
        class_instance = TableCreation()
        class_method = class_instance.create_users()
        return class_method
