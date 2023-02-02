"""

Created by Colin Gelling on 30/1/2023

"""
import sys

from PyQt6.QtWidgets import QApplication

import bootstrap.bootstrapper as Bootstrapper

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Bootstrapper.Bootstrapper()
    sys.exit(app.exec())
