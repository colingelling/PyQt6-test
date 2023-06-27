"""

Created by Colin Gelling on 25/05/2023
Using Pycharm Professional

"""


class ViewMapping:

    navigation_pattern = {}

    def __init__(self):
        pass

    def not_authenticated(self):
        pattern = {
            "HomeView": {
                "view_class": "HomeView",
                "window_class": "HomeWindow",
                "authenticated": "no",
                "connections": [
                    ("switch_second", "RegisterView"),
                    ("switch_third", "LoginView")
                ]
            },
            "RegisterView": {
                "view_class": "RegisterView",
                "window_class": "RegisterWindow",
                "authenticated": "no",
                "connections": [
                    ("switch_first", "HomeView"),
                    ("switch_third", "LoginView")
                ]
            },
            "LoginView": {
                "view_class": "LoginView",
                "window_class": "LoginWindow",
                "authenticated": "no",
                "connections": [
                    ("switch_first", "HomeView"),
                    ("switch_second", "RegisterView")
                ]
            }
        }

        self.navigation_pattern = pattern
        return pattern

    def authenticated(self):
        # TODO: Give certain views specific parameters such as 'authenticated yes | no'. Provide the user_session while
        #  yes, do nothing when it has the value 'no'.

        pattern = {
            "UserView": {
                "view_class": "UserView",
                "window_class": "UserWindow",
                "authenticated": "yes",
            }
        }

        self.navigation_pattern = pattern
        return pattern
