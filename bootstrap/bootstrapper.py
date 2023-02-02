"""

Created by Colin Gelling on 30/1/2023

"""

from router.routes import Routes as route


class Bootstrapper:
    def __init__(self):
        self.load()

    @staticmethod
    def load():
        return route.home()
