"""

Created by Colin Gelling on 06/3/2023
Using Pycharm Professional

"""


class DatabaseConnector:
    def __init__(self):
        db_path = "src/db/"
        file_extension = ".sqlite"
        self.connection_type = "QSQLITE"
        db_name = "LearningQt"
        self.db_file = db_path + db_name + file_extension

        self.connection = None

    def create_connection(self):

        print(f'self: { self }')

        db_file = self.db_file

        if self.db_file:
            from sqlite3 import Error
            try:
                import sqlite3
                self.connection = sqlite3.connect(db_file)
            except Error as e:
                print(e)

            return self.connection
        else:
            print('It seems that the variable has not been assigned to a value!')

    def check_connection(self):
        if not self.create_connection():
            status = 'closed'
        else:
            status = 'open'

        print('Database connection status:', status)

    def open_connection(self):
        return self.check_connection()
