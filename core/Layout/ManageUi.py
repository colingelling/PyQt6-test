"""

Created by Colin Gelling on 06/04/2023
Using Pycharm Professional

"""


class ManageUi:

    def __init__(self):
        super().__init__()

    def load_home_ui(self):
        from src.gui.ui.home.HomeWindow import Ui_HomeWindow
        ui = Ui_HomeWindow()
        ui.setupUi(self)
        return ui

    def load_login_ui(self):
        from src.gui.ui.login.LoginWindow import Ui_LoginWindow
        ui = Ui_LoginWindow()
        ui.setupUi(self)
        return ui

    def load_register_ui(self):
        from src.gui.ui.register.RegisterWindow import Ui_RegisterWindow
        ui = Ui_RegisterWindow()
        ui.setupUi(self)
        return ui

    def load_user_ui(self):
        from src.gui.ui.user.UserWindow import Ui_UserWindow
        ui = Ui_UserWindow()
        ui.setupUi(self)
        return ui
