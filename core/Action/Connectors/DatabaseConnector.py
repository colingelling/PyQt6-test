from PyQt6.QtSql import QSqlDatabase


class DatabaseConnector:
    def __init__(self):
        db_path = "src/db/"
        file_extension = ".sqlite"
        self.connection_type = "QSQLITE"
        self.db_name = "LearningQt"
        self.db_file = db_path + self.db_name + file_extension

        self.db = QSqlDatabase.addDatabase('QSQLITE')

    def open_connection(self):
        # TODO: build in check for ensuring that the connection is already open or not (in case of window changes)
        # (for suppressing 'QSqlDatabasePrivate::addDatabase: duplicate connection name 'qt_sql_default_connection' -
        # warnings)

        db = self.db
        db.setDatabaseName(self.db_file)

        if not db.isOpen():
            db.open()

            if db.isOpen() == "False":
                status = 'closed'
            else:
                status = 'open'

            print('Database connection status:', status)

    def close_connection(self):
        if self.db.isOpen():
            print('Closing database connection..')
            return self.db.close()
