# Form implementation generated from reading gui file '/home/colin/Python/Projects/LearningQt/views/login.gui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(903, 678)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(LoginWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 903, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHome = QtWidgets.QMenu(self.menuBar)
        self.menuHome.setObjectName("menuHome")
        self.menuLogin = QtWidgets.QMenu(self.menuBar)
        self.menuLogin.setObjectName("menuLogin")
        LoginWindow.setMenuBar(self.menuBar)
        self.actionLogin = QtGui.QAction(LoginWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionRegister = QtGui.QAction(LoginWindow)
        self.actionRegister.setObjectName("actionRegister")
        self.menuLogin.addAction(self.actionLogin)
        self.menuLogin.addAction(self.actionRegister)
        self.menuBar.addAction(self.menuHome.menuAction())
        self.menuBar.addAction(self.menuLogin.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.menuHome.setTitle(_translate("LoginWindow", "Home"))
        self.menuLogin.setTitle(_translate("LoginWindow", "User accounts"))
        self.actionLogin.setText(_translate("LoginWindow", "Login"))
        self.actionRegister.setText(_translate("LoginWindow", "Register"))
