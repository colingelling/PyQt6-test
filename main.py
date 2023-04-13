"""

Created by Colin Gelling on 30/1/2023
Using Pycharm Professional

"""

from PyQt6 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)

    from core.Actions.Controllers.Controller import Controller
    controller = Controller()
    controller.show_main_window()

    sys.exit(app.exec())


# Instantiate the application
if __name__ == '__main__':
    import sys
    main()
