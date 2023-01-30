"""

Created by Colin Gelling on 30/1/2023

"""


class Routes:

    @staticmethod
    def home():
        import core.Action.Controllers.HomeController as HomeController
        HomeController.HomeController()

    @staticmethod
    def login():
        import core.Action.Controllers.LoginController as LoginController
        LoginController.LoginController()

    @staticmethod
    def test():
        import core.Action.Controllers.TestController as TestController
        TestController.TestController()
