"""

    Created by Colin Gelling on 06/03/2023
    Using Pycharm Professional

"""

from core.Environment.CollectEnvironmentalValues import CollectEnvironmentalValues
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from sqlite3 import Error

import os


class SQLiteConnector(CollectEnvironmentalValues):

    cwd = os.getcwd()

    def __init__(self):
        super(SQLiteConnector, self).__init__()

        # set credential attributes
        self.db_type = None
        self.db_name = None
        self.db_user = None
        self.db_pass = None

        self.db_path = None

        # set connection attributes
        self.connection = None
        self.query = None

    def set_env(self):
        # define Dictionary for receiving environmental values
        db_credentials = CollectEnvironmentalValues.db_credentials

        # set class attributes
        for key, value in db_credentials.items():
            if 'DB_TYPE' in key:
                self.db_type = value
            if 'DB_NAME' in key:
                self.db_name = value
            if 'DB_USER' in key:
                self.db_user = value
            if 'DB_PASS' in key:
                self.db_pass = value

    @staticmethod
    def project_root():

        # TODO: Move this function

        current_file = __file__

        # Get the absolute path of the current file
        current_file_path = os.path.abspath(current_file)

        # Split the path into directory components
        components = current_file_path.split(os.path.sep)

        db_name = None

        from core.Environment.CollectEnvironmentalValues import CollectEnvironmentalValues
        for key, value in CollectEnvironmentalValues.app_credentials.items():
            if 'NAME' in key:
                db_name = value

        # Find the index of the directory you want to consider as the project root
        index = components.index(db_name)

        # Join the directory components up to the project root index
        project_root = os.path.sep.join(components[:index + 1])

        return project_root

    def database_path(self):

        # set connection credentials
        self.set_env()

        project_root = self.project_root()
        source_directory = "src"
        db_directory = "db"
        db_name = self.db_name

        if db_name is None:
            ValueError("db_name has not been set.")

        # Verify if project_root and db_directory exist
        if not os.path.exists(project_root):
            raise Error(f"There's something wrong as '{project_root}' does not exist!")

        src_path = os.path.join(project_root, source_directory)
        db_directory_path = src_path + "/" + db_directory

        if os.path.exists(src_path) and not os.path.exists(db_directory_path):
            os.makedirs(db_directory_path, exist_ok=True)

        if not os.path.exists(db_directory_path):
            print("Database directory path has not been found!")

        db_path = db_directory_path + "/" + self.db_name + ".sqlite"

        if os.path.exists(db_directory_path):
            self.db_path = db_path
        else:
            print("Database directory does not exist:", db_directory_path)

    def initialize_connection(self):

        """
            Create database functionality (initialization process, one task only)
            :return:
        """

        # set connection credentials
        self.set_env()

        # set database path
        self.database_path()

        # set credentials to this scope for easy usage
        db_type = self.db_type
        db_path = self.db_path

        # set database connection (driver)
        connection = QSqlDatabase.addDatabase(db_type, db_path)

        if not connection.isValid():
            raise Error("Connection could not be validated.")

        # only do something when the file has not been created earlier
        if not os.path.exists(db_path):

            print("Database file has not been found, initializing now.")

            try:

                # set the connection (create)
                connection.setDatabaseName(db_path)
                connection.open()

                # final check if the execution was successful
                if os.path.exists(db_path):
                    print("Database connection has been created successfully!")
                    connection.close()

            except Error as e:
                raise Error(f"Could not create database: {e}")

    def open_connection(self):

        """
        This functionality is capable of opening the existing connection to the database.
        When the connection can be opened successfully, attributes are set in order for multiple usage possibilities in
        other functions.
        :return:
        """

        # set connection credentials
        self.set_env()

        # set database path
        self.database_path()

        # set credentials to this scope for easy usage
        db_type = self.db_type
        db_path = self.db_path

        # load driver by declaring path
        connection = QSqlDatabase.database(db_path, open=False)

        if not connection.isValid():
            raise Error("Connection could not be validated.")

        if not os.path.exists(db_path):
            raise Error("Database does not exist!")

        try:

            # reach the database
            connection.setDatabaseName(db_path)
            connection.open()

            # assign connection objects to class attributes for access to other functions
            self.connection = connection
            self.query = QSqlQuery(connection)

            # check if the connection could be opened
            if not connection.open():
                print(f'Error opening database: {connection.lastError().text()}')

        except Error as e:
            raise Error(f"Could not set connection: {e}")

    def close_connection(self):

        """
        This piece is capable of closing the connection to the database and cleaning up afterward.
        :return:
        """

        connection = self.connection
        if not connection.isValid():
            raise ValueError("Database connection is not available at this point.")

        # the connection should be closed, only when it was opened earlier
        if connection.isOpen():

            # close the connection
            connection.close()

            # set attributes to empty
            self.connection = None
            self.query = None

            # confirm if they are empty
            if self.connection and self.query:
                raise Warning("Database connections could not be emptied.")
