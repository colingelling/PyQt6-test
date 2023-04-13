
# TODO: figure out how to alter the structure in order to load


class SetLoginCredentials:
    def __init__(self):
        super(SetLoginCredentials).__init__()

    @staticmethod
    def set_credentials(self):
        from views.login_view import LoginView
        view = LoginView()

        ui = view.load_login_ui()

        form_username_email = ui.LoginFormUsernameLineEdit.text()
        form_password = ui.LoginFormPasswordLineEdit.text()

        form_input = [
            form_username_email,
            form_password
        ]

    # def bind_credentials(self):
    #     m = self.login_ui()
    #     username_email = m.LoginFormUsernameLineEdit.text()
    #     password = m.LoginFormPasswordLineEdit.text()
    #     return username_email, password

    # def set_credentials(self):
    #     return print(self.bind_credentials)
        # form_input = [
        #     self.username_email,
        #     self.password
        # ]
        #
        # return form_input

    def get_credentials(self):
        return self.set_credentials
