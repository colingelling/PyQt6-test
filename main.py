"""

Created by Colin Gelling on 30/1/2023

"""

from PyQt6 import QtWidgets
from core.Action.Controllers.Controller import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main_window()
    sys.exit(app.exec())


# Instantiate the application
if __name__ == '__main__':
    import sys
    main()
