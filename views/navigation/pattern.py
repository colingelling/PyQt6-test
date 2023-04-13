class Pattern:
    def __init__(self):
        pass

    # TODO: in order to get access to ui elements it will be required to look for active windows followed by a
    #  statement for example for loading in multiple UIs

    # def global_pattern(self):
    #     button_home = QAction("Home", self)
    #     button_register = QAction("Register", self)
    #     button_login = QAction("Login", self)
    #
    #     button_home.triggered.connect(self.switch_first_window)
    #     button_register.triggered.connect(self.switch_second_window)
    #     button_login.triggered.connect(self.switch_third_window)
    #
    #     menubar = ui_layout.menuBar
    #     menubar.addAction(button_home)
    #     menubar.addAction(button_register)
    #     menubar.addAction(button_login)