"""

Created by Colin Gelling on 30/1/2023

"""

from PyQt6 import QtWidgets
from core.Action.Controllers.HomeController import HomeController


def main():
    app = QtWidgets.QApplication(sys.argv)
    from views.home_view import Controller
    window = Controller()
    window.show_main_window()
    # controller = HomeController()
    # controller.show_window()
    sys.exit(app.exec())


# Instantiate the application
if __name__ == '__main__':
    import sys
    main()
