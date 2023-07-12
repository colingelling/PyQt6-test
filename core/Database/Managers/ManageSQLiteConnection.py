"""

Created by Colin Gelling on 30/05/2023
Using Pycharm Professional

"""

from core.Models.User import User


class ManageSQLiteConnection(User):

    requested_session = []
    new_session = {}
    session_id = None

    def __init__(self):
        super().__init__()

    # TODO: Maybe move the initialization of user_id for sessions into this class?

    def retrieve_rows(self, table):

        # open the database connection
        self.open_connection()

        # check whether the connection is usable or not
        connection = self.connection
        if not connection.isValid():
            from sqlite3 import Error
            raise Error("No valid connection")

        # retrieve rows and update new_session
        new_session = self.retrieve_rows_from_database(table)
        updated_session = self.update_new_session(new_session)

        self.new_session = updated_session
        return self.new_session

    def retrieve_rows_from_database(self, table):
        new_session = self.new_session
        if new_session:
            for key, value in new_session.items():
                session_id = None
                if "id" in key:
                    self.session_id = value

                # when value has been found empty
                if not value:
                    session_id = self.session_id
                    query_string = f"SELECT {key} FROM {table} WHERE id = '{session_id}'"

                    # prepare the query
                    query = self.query
                    query.prepare(query_string)

                    # execute the query
                    if query.exec():
                        # iterate over the query results
                        while query.next():
                            for i in range(query.record().count()):
                                column_name = query.record().fieldName(i)
                                column_value = query.value(i)
                                if key == column_name and column_value is not value:
                                    new_session[key] = column_value  # update the value(s) in new_session dictionary

                    else:
                        # handle query execution error
                        error = query.lastError().text()
                        print("Query execution error:", error)

        return new_session

    def update_new_session(self, new_session):
        # Update the new_session dictionary
        updated_session = {}
        for key, value in new_session.items():
            # Perform any additional updates or transformations if needed
            updated_value = value  # Placeholder for further updates
            updated_session[key] = updated_value

        return updated_session
