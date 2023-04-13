"""

Created by Colin Gelling on 13/4/2023
Using Pycharm Professional

"""

from core.Models.User import User

from core.Management.Attributes.getters.Credentials.GetLoginCredentials import GetRegisterCredentials


class ManageRegister(User, GetRegisterCredentials):

    form_data = {}

    def __init__(self):
        super(ManageRegister).__init__()

    def check_credentials(self):
        # TODO: initialize this method by executing the following

        # attempt to match the form credentials according to what is in the database
        self.login_user()

        # use background functionality for submitting into the next window
        # self.trigger_login()

        # TODO: use User model functionality to try and login

        # if conn:

            # TODO: fix an issue where users are in session even when the credentials are wrong

            # bind form fields  TODO: pass these into a variable - moved to core.setters.LoginForm
            # form_username_email = ui.LoginFormUsernameLineEdit.text()
            # form_password = ui.LoginFormPasswordLineEdit.text()

            # form_input = [  # TODO: also moved to core.setters.LoginForm
            #     form_username_email,
            #     form_password
            # ]

            # TODO: moved the next block of code to core.Models.User
            # import sqlite3
            #
            # users = []
            #
            # # try to find the user with the credentials filled in the form on the login window
            # try:
            #     query = f"SELECT id, email, username, password FROM users WHERE email = '{form_username_email}' " \
            #             f"OR username = '{form_username_email}'"
            #     cursor = conn.cursor()
            #     cursor.execute(query)
            #     rows = cursor.fetchall()
            #     conn.commit()
            #
            #     for value in rows:
            #         users.append([
            #             value[0],
            #             value[1],
            #             value[2],
            #             value[3]
            #         ])
            #
            # except sqlite3.Error as error:
            #     from PyQt6.QtWidgets import QMessageBox
            #     msg = QMessageBox()
            #     msg.setWindowTitle("Credential check")
            #     msg.setText(error)
            #     msg.exec()
            # TODO: end

            # TODO: set the following block of code as external functionality
            # import bcrypt
            #
            # if users:
            #     for user_id, email, username, password in users:
            #
            #         if bcrypt.checkpw(form_password.encode('utf-8'), password.encode('utf-8')):
            #             # set the session
            #             from PyQt6.QtCore import QSettings
            #             settings = QSettings("PyQt-test", "LoggedUser")
            #             settings.beginGroup("user_session")
            #             settings.setValue('id', user_id)
            #             settings.setValue('user', username)
            #             settings.endGroup()

            # TODO: end
