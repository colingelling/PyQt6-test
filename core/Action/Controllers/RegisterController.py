"""

Created by Colin Gelling on 31/1/2023

"""


import views.register_view as RegisterView


class RegisterController:
    def __init__(self):
        self.pointer()

    @staticmethod
    def pointer():
        return RegisterView.RegisterView()
