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
                "class": "HomeView",
                "authenticated": "no",
                "connections": [
                    ("switch_second", "RegisterView"),
                    ("switch_third", "LoginView")
                ]
            },
            "RegisterView": {
                "class": "RegisterView",
                "authenticated": "no",
                "connections": [
                    ("switch_first", "HomeView"),
                    ("switch_third", "LoginView")
                ]
            },
            "LoginView": {
                "class": "LoginView",
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
                "class": "UserView",
                "authenticated": "yes",
            }
        }

        self.navigation_pattern = pattern
        return pattern
