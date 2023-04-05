from core.Action.Connectors.DatabaseConnector import DatabaseConnector


class User(DatabaseConnector):
    def __init__(self):
        super(User, self).__init__()

        self.form_data = {}  # TODO: make sure for safety purposes that this will be emptied afterwards

        self.users = []

        # execute the following first because of requiring it for multiple purposes
        self.create_users_table()

    def create_users_table(self):

        self.open_connection()
        conn = self.connection

        if conn:
            print(f"Creating database table: 'users'")

            cursor = conn.cursor()

            query = """
                CREATE TABLE users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                   firstname VARCHAR(40) NOT NULL,
                   suffix VARCHAR(16) NOT NULL,
                   lastname VARCHAR(40) NOT NULL,
                   email VARCHAR(40) NOT NULL,
                   username VARCHAR(40) NOT NULL,
                   password VARCHAR(40) NOT NULL
               )
            """

            import sqlite3
            try:
                cursor.execute(query)
            except sqlite3.Error as error:
                print("The program could not create the table:", error)

            if cursor.execute("SELECT * FROM users"):
                print('Table users has been found successfully!')
                cursor.close()

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
        password_hash = hashed_str.decode("utf-8")

        print("The encrypted text or password is: {}".format(password_hash))

        self.open_connection()
        conn = self.connection

        if conn:
            print(f"Creating a user..")

            cursor = conn.cursor()

            import sqlite3
            try:

                # include database query functionality and database, set a query afterwards for creating a user account
                query_data = dict(firstname=firstname, suffix=suffix, lastname=lastname,
                                  username=username, email=email, password=password_hash)

                query = ("""
                            insert into users (
                            firstname, suffix, lastname, username, email, password)
                            values (:firstname, :suffix, :lastname, :username, :email, :password)
                            """)

                cursor.execute(query, query_data)
                conn.commit()
                conn.close()

            except sqlite3.Error as error:
                print("This program could not create the user:", error)
                conn.close()

            # if cursor.execute("SELECT * FROM users WHERE username=':username'", ':username' = username):
            #     print('The user that was created has been found!')
            #     cursor.close()

    def login_user(self):
        self.open_connection()
        conn = self.connection

        if conn:
            print(f"Logging in user..")

            collect_users = "SELECT id, email, username, password FROM users"
            cursor = conn.cursor()
            cursor.execute(collect_users)
            users = cursor.fetchall()
            conn.commit()

            # TODO: change this according to one user, not all users

            for val in users:
                self.users.append([
                    val[0],
                    val[1],
                    val[2],
                ])
