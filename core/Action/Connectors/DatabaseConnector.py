

class DatabaseConnector:
    def __init__(self):
        db_path = "src/db/"
        file_extension = ".sqlite"
        self.connection_type = "QSQLITE"
        self.db_name = "LearningQt"
        self.db_file = db_path + self.db_name + file_extension

        self.connection = None

    def create_connection(self):

        db_file = self.db_file
        # TODO: build in check for ensuring that the connection is already open or not (in case of window changes)
        # (for suppressing 'QSqlDatabasePrivate::addDatabase: duplicate connection name 'qt_sql_default_connection' -
        # warnings)

        from sqlite3 import Error
        try:
            import sqlite3
            self.connection = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return self.connection

    def check_connection(self):
        if not self.create_connection():
            status = 'closed'
        else:
            status = 'open'

        print('Database connection status:', status)

    def open_connection(self):
        return self.check_connection()
