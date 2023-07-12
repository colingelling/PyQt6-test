
from core.Database.Connectors.SQLiteConnector import SQLiteConnector


class CreateTable(SQLiteConnector):
    def __init__(self):
        super().__init__()
        pass

    def create_users(self):

        # open the database connection (ready to use self.connection)
        self.open_connection()
        connection = self.connection

        if connection.isValid():

            print("Connection is valid.")

            # verify an open connection
            if connection.open():
                if self.query:
                    query = self.query

                    import sqlite3
                    try:

                        if query.exec("SELECT * FROM users"):

                            print("Found 'users' table.")

                        else:

                            print("Creating table 'users'...")

                            query.exec("""
                                        CREATE TABLE users (
                                           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                                           firstname VARCHAR(40) NOT NULL,
                                           suffix VARCHAR(16) NOT NULL,
                                           lastname VARCHAR(40) NOT NULL,
                                           username VARCHAR(40) NOT NULL,
                                           email VARCHAR(40) NOT NULL,
                                           password VARCHAR(40) NOT NULL,
                                           created_at TEXT NOT NULL
                                       )
                                    """)

                    except sqlite3.Error as error:
                        print("Could not create table 'users':", error)

                else:
                    raise ValueError("Could not execute queries.")
            else:
                print("Database connection isn't open, could not continue.")
