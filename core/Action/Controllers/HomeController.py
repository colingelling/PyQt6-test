"""

Created by Colin Gelling on 30/1/2023

"""


import views.home_view as HomeView


class HomeController:
    def __init__(self):
        super(HomeController, self).__init__()
        self.pointer()

    @staticmethod
    def pointer():
        return HomeView.HomeView()
