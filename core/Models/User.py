from core.Action.Connectors.DatabaseConnector import DatabaseConnector


class User(DatabaseConnector):
    def __init__(self):
        super(User, self).__init__()

        self.form_data = {}  # TODO: make sure for safety purposes that this will be emptied afterwards

    def create_users_table(self):
        if self.db.open():
            print("Processing table..")
            connection = self.db

            # Creating table before adding values
            query = '''CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    firstname VARCHAR(40) NOT NULL,
                    suffix VARCHAR(16) NOT NULL,
                    lastname VARCHAR(40) NOT NULL,
                    email VARCHAR(40) NOT NULL,
                    username VARCHAR(40) NOT NULL,
                    password VARCHAR(40) NOT NULL
                )
                '''

            connection.exec(query)

    def create_user(self):
        # assign key values
        firstname = self.form_data['firstname'].text()
        suffix = self.form_data['suffix'].text()
        lastname = self.form_data['lastname'].text()
        username = self.form_data['username'].text()
        email = self.form_data['email'].text()
        password = self.form_data['password'].text()

        import bcrypt
        field_to_encrypt = password
        change_format = "{}".format(field_to_encrypt)
        encrypted_password = field_to_encrypt.encode('utf-8')
        salt_object = bcrypt.gensalt(rounds=16)
        hashed_str = bcrypt.hashpw(encrypted_password, salt_object)
        bytes = hashed_str.decode("utf-8")

        print("The encrypted text or password is: {}".format(bytes))

        if self.db.open():
            # include database query functionality and database, set a query afterwards for creating a user account
            from PyQt6 import QtSql
            pointer = QtSql.QSqlQuery(self.db)
            query = '''
                        INSERT INTO users(firstname, suffix, lastname, username, email, password) 
                        VALUES(:firstname, :suffix, :lastname, :username, :email, :password)
                    '''

            # bind query values to the key values (above) and process data into the database
            pointer.prepare(query)
            pointer.bindValue(':firstname', firstname)
            pointer.bindValue(':suffix', suffix)
            pointer.bindValue(':lastname', lastname)
            pointer.bindValue(':username', username)
            pointer.bindValue(':email', email)
            pointer.bindValue(':password', str(bytes))
            pointer.exec()
