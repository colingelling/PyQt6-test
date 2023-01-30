"""

Created by Colin Gelling on 30/1/2023

"""

from router.routes import Routes as route


def bootstrap():
    return route.home()
