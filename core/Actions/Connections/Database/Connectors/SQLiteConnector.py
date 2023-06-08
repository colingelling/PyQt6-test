"""

Created by Colin Gelling on 06/03/2023
Using Pycharm Professional

"""

from core.Configurators.EnvironmentConfigurator import EnvironmentConfigurator
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from sqlite3 import Error

import os


class SQLiteConnector(EnvironmentConfigurator):

    # TODO: Build functionality for checking the connection (instead of checking whether the connection is valid or not)

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
        db_credentials = EnvironmentConfigurator.db_credentials

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

    def database_path(self):

        # set connection credentials
        self.set_env()

        # get the path to the current file
        current_file = __file__

        # get the path to the root of the project directory
        project_root = current_file
        while not os.path.exists(os.path.join(project_root, self.db_name)):
            project_root = os.path.dirname(project_root)
        project_root = os.path.join(project_root, self.db_name)

        # TODO: Maybe change self.db_name usage from above with the project_name (new env)?

        # define the name of the subdirectory and database file
        subdir = "src/db"
        db_name = self.db_name

        # construct the full path to the database file
        dir_path = os.path.join(project_root, subdir)
        full_path = os.path.join(dir_path, db_name + '.sqlite')

        if full_path:
            self.db_path = full_path

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

        if connection.isValid():

            # only do something when the file has not been created earlier
            if not os.path.exists(db_path):

                print("Database file has not been found, initializing the connection now..")

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

        else:
            raise Error("Connection could not be validated.")

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

        if connection.isValid():

            if os.path.exists(db_path):

                print("Database connection has been found, attempting to connect to it...")

                try:

                    # reach the database
                    connection.setDatabaseName(db_path)
                    connection.open()

                    # assign connection objects to class attributes for access to other functions
                    self.connection = connection
                    self.query = QSqlQuery(connection)

                    # check if the connection could be opened
                    if not connection.open():
                        print(f'Error opening database: { connection.lastError().text() }')
                    else:
                        print('Database connection successfully opened.')

                except Error as e:
                    raise Error(f"Could not set connection: {e}")
            else:
                raise Error("Database does not exist!")

        else:
            raise Error("Connection could not be validated.")

    def close_connection(self):

        """
        This piece is capable of closing the connection to the database and cleaning up afterward.
        :return:
        """

        # check whether attribute is available or not
        if self.connection:
            connection = self.connection

            # the connection only could be closed when it was opened earlier
            if connection.isOpen():

                # close the connection
                connection.close()

                # set attributes to empty
                self.connection = None
                self.query = None

                # confirm if they are empty
                if not self.connection and self.query:
                    print("Database connections closed and cleared attributes.")
                else:
                    raise Warning("Database connections could not be emptied.")

        else:
            raise ValueError("Database connection was not set correctly for available use.")
