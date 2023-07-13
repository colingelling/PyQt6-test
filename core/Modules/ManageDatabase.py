"""

    Created by Colin Gelling on 05/05/2023
    Using Pycharm Professional

"""


class ManageDatabase:
    def __init__(self):
        super().__init__()

    @staticmethod
    def initialize_connection():
        from core.Database.Connectors.SQLiteConnector import SQLiteConnector
        class_instance = SQLiteConnector()
        class_method = class_instance.initialize_connection()
        return class_method

    @staticmethod
    def use_connection():
        from core.Database.Tasks.CreateTable import CreateTable
        class_instance = CreateTable()
        class_method = class_instance.create_users()
        return class_method
