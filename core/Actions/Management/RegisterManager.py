"""

Created by Colin Gelling on 02/05/2023
Using Pycharm Professional

"""

from core.Models.User import User


class RegisterManager(User):
    def __init__(self):
        super().__init__()

    def submit(self):

        self.create_user()

        # TODO:
        #  1) forward to self.create_user
        #  2) forward to the next screen (depending on the existence of a particular dataset)
