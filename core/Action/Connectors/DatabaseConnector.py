from PyQt6.QtSql import QSqlDatabase


class DatabaseConnector:
    def __init__(self):
        self.connection_type = "QSQLITE"
        self.db_name = "LearningQt.sqlite"

    def set_connection(self):
        db = QSqlDatabase.addDatabase(self.connection_type)
        db.setDatabaseName(self.db_name)
        return db

    def get_connection(self):
        return self.set_connection()

    def open_connection(self):
        # https:// doc.qt.io/qtforpython/overviews/sql-driver.html
        from PyQt6.QtCore import QFile
        if not QFile.exists(self.db_name):
            print('The database file doesn\'t exist yet')
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('LearningQt.sqlite')
            db.open()
        else:
            print('The database file exists')
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('LearningQt.sqlite')
            db.open()
            print('Connection active:', db.isOpen())

    def check_connection(self):
        from PyQt6.QtCore import QFile
        db = QSqlDatabase.database('LearningQt.sqlite')
        if QFile.exists(self.db_name):
            print('Connection active:', db.isOpen())

    def close_database_connection(self):
        db = QSqlDatabase.database('LearningQt.sqlite')
        return db.close()

    def connect_db(self):
        # https:// doc.qt.io/qtforpython/overviews/sql-driver.html
        db_name = "LearningQt.sqlite"
        from PyQt6.QtCore import QFile
        if not QFile.exists(db_name):
            print('The database file doesn\'t exist yet')
            db = QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('LearningQt.sqlite')
            db.open()

            if QFile.exists(db_name):
                print('Connection active:', db.isOpen())
        else:
            print('The database file exists')
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName('LearningQt.sqlite')
            db.open()
            print('Connection active:', db.isOpen())

        if db.open():
            print("Processing table..")
            conn = db

            # Creating table as per requirement
            sql = '''CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    firstname VARCHAR(40) NOT NULL,
                    suffix VARCHAR(16) NOT NULL,
                    lastname VARCHAR(40) NOT NULL,
                    email VARCHAR(40) NOT NULL,
                    username VARCHAR(40) NOT NULL,
                    password VARCHAR(40) NOT NULL
                )
                '''
            conn.exec(sql)
