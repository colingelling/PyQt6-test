"""

    Created by Colin Gelling on 02/05/2023
    Using Pycharm Professional

"""

from core.Models.User import User


class ManageRegister(User):

    """
        This class handles the user creation process
    """

    def __init__(self):
        super().__init__()

    def submit(self):
        self.create_user()
