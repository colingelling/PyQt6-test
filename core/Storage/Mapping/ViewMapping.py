"""

Created by Colin Gelling on 25/05/2023
Using Pycharm Professional

"""


class ViewMapping:

    navigation_pattern = {}
    type = None

    def __init__(self):
        pass

    def non_authenticated(self):
        from views.HomeView import HomeView
        from views.RegisterView import RegisterView
        from views.LoginView import LoginView

        self.navigation_pattern = {
            "HomeView": {
                "class": HomeView,
                "connections": [
                    ("switch_second", "RegisterView"),
                    ("switch_third", "LoginView")
                ]
            },
            "RegisterView": {
                "class": RegisterView,
                "connections": [
                    ("switch_first", "HomeView"),
                    ("switch_third", "LoginView")
                ]
            },
            "LoginView": {
                "class": LoginView,
                "connections": [
                    ("switch_first", "HomeView"),
                    ("switch_second", "RegisterView")
                ]
            }
        }

    def authenticated(self):
        from views.UserView import UserView

        self.navigation_pattern = {
            "HomeView": {
                "class": UserView,
            }
        }
