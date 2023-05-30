"""

Created by Colin Gelling on 6/4/2023
Using Pycharm Professional

"""


class LayoutConfigurator:
    def __init__(self):
        super().__init__()

    def load_home_ui(self):
        from src.gui.ui.home.home_view import Ui_HomeWindow
        ui = Ui_HomeWindow()
        ui.setupUi(self)
        return ui

    def load_home_style(self):
        # import CSS file
        css_file = "src/gui/css/home.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def load_register_ui(self):
        from src.gui.ui.register.register_view import Ui_RegisterWindow
        ui = Ui_RegisterWindow()
        ui.setupUi(self)
        return ui

    def load_register_style(self):
        # import CSS file
        css_file = "src/gui/css/register.css"
        with open(css_file, "r") as fh:
            self.setStyleSheet(fh.read())

    def load_login_ui(self):
        from src.gui.ui.login.login_view import Ui_LoginWindow
        ui = Ui_LoginWindow()
        ui.setupUi(self)
        return ui

    def load_login_style(self):
        css_file = "src/gui/css/login.css"

        with open(css_file, "r") as fh:
            method = self.load_login_ui()
            method.setupUi(self)
            method.setStyleSheet(fh.read())

    def load_user_ui(self):
        from src.gui.ui.user.welcome_view import Ui_WelcomeUserWindow
        ui = Ui_WelcomeUserWindow()
        ui.setupUi(self)
        return ui

    def load_user_style(self):
        css_file = "src/gui/css/user.css"

        with open(css_file, "r") as fh:
            method = self.load_login_ui()
            method.setupUi(self)
            method.setStyleSheet(fh.read())
