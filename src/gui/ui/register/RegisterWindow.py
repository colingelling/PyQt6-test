# Form implementation generated from reading ui file '/home/colin/Python/Projects/Pycharm/Development/Learning_PyQt/LearningQt/src/gui/ui/register/RegisterWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(634, 714)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegisterWindow.sizePolicy().hasHeightForWidth())
        RegisterWindow.setSizePolicy(sizePolicy)
        RegisterWindow.setMinimumSize(QtCore.QSize(634, 714))
        RegisterWindow.setMaximumSize(QtCore.QSize(634, 714))
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 17, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem1, 15, 19, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 17, 19, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem3, 4, 19, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.RegisterFormFirstnameLabel = QtWidgets.QLabel(self.widget_2)
        self.RegisterFormFirstnameLabel.setObjectName("RegisterFormFirstnameLabel")
        self.gridLayout_3.addWidget(self.RegisterFormFirstnameLabel, 0, 0, 1, 1)
        self.RegisterFormFirstnameLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.RegisterFormFirstnameLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.RegisterFormFirstnameLineEdit.setObjectName("RegisterFormFirstnameLineEdit")
        self.gridLayout_3.addWidget(self.RegisterFormFirstnameLineEdit, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 3, 2, 2, 7)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.RegisterFormSuffixLabel = QtWidgets.QLabel(self.widget_3)
        self.RegisterFormSuffixLabel.setObjectName("RegisterFormSuffixLabel")
        self.gridLayout_4.addWidget(self.RegisterFormSuffixLabel, 0, 0, 1, 1)
        self.RegisterFormSuffixLineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.RegisterFormSuffixLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormSuffixLineEdit.setObjectName("RegisterFormSuffixLineEdit")
        self.gridLayout_4.addWidget(self.RegisterFormSuffixLineEdit, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_3, 3, 9, 2, 4)
        spacerItem4 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem4, 8, 19, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 17, 17, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem6, 13, 19, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.RegisterFormUsernameLabel = QtWidgets.QLabel(self.widget_5)
        self.RegisterFormUsernameLabel.setObjectName("RegisterFormUsernameLabel")
        self.gridLayout_6.addWidget(self.RegisterFormUsernameLabel, 0, 0, 1, 1)
        self.RegisterFormUsernameLineEdit = QtWidgets.QLineEdit(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterFormUsernameLineEdit.sizePolicy().hasHeightForWidth())
        self.RegisterFormUsernameLineEdit.setSizePolicy(sizePolicy)
        self.RegisterFormUsernameLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormUsernameLineEdit.setObjectName("RegisterFormUsernameLineEdit")
        self.gridLayout_6.addWidget(self.RegisterFormUsernameLineEdit, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_5, 5, 2, 2, 17)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem7, 17, 6, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem8, 2, 19, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem9, 17, 13, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem10, 17, 5, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.RegisterFormPasswordLabel_1 = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterFormPasswordLabel_1.sizePolicy().hasHeightForWidth())
        self.RegisterFormPasswordLabel_1.setSizePolicy(sizePolicy)
        self.RegisterFormPasswordLabel_1.setObjectName("RegisterFormPasswordLabel_1")
        self.gridLayout_8.addWidget(self.RegisterFormPasswordLabel_1, 0, 0, 1, 1)
        self.RegisterFormPasswordLineEdit_1 = QtWidgets.QLineEdit(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterFormPasswordLineEdit_1.sizePolicy().hasHeightForWidth())
        self.RegisterFormPasswordLineEdit_1.setSizePolicy(sizePolicy)
        self.RegisterFormPasswordLineEdit_1.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormPasswordLineEdit_1.setObjectName("RegisterFormPasswordLineEdit_1")
        self.gridLayout_8.addWidget(self.RegisterFormPasswordLineEdit_1, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_7, 9, 2, 2, 17)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem11, 17, 8, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem12, 11, 19, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem13, 17, 14, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem14, 6, 19, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem15, 17, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem16, 17, 15, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RegisterFormLastnameLineEdit = QtWidgets.QLineEdit(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterFormLastnameLineEdit.sizePolicy().hasHeightForWidth())
        self.RegisterFormLastnameLineEdit.setSizePolicy(sizePolicy)
        self.RegisterFormLastnameLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormLastnameLineEdit.setObjectName("RegisterFormLastnameLineEdit")
        self.gridLayout_5.addWidget(self.RegisterFormLastnameLineEdit, 1, 0, 1, 1)
        self.RegisterFormLastnameLabel = QtWidgets.QLabel(self.widget_4)
        self.RegisterFormLastnameLabel.setObjectName("RegisterFormLastnameLabel")
        self.gridLayout_5.addWidget(self.RegisterFormLastnameLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_4, 3, 13, 2, 6)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem17, 17, 16, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem18, 0, 19, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem19, 17, 10, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.RegisterFormEmailLabel = QtWidgets.QLabel(self.widget_6)
        self.RegisterFormEmailLabel.setObjectName("RegisterFormEmailLabel")
        self.gridLayout_7.addWidget(self.RegisterFormEmailLabel, 0, 0, 1, 1)
        self.RegisterFormEmailLineEdit = QtWidgets.QLineEdit(self.widget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterFormEmailLineEdit.sizePolicy().hasHeightForWidth())
        self.RegisterFormEmailLineEdit.setSizePolicy(sizePolicy)
        self.RegisterFormEmailLineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormEmailLineEdit.setObjectName("RegisterFormEmailLineEdit")
        self.gridLayout_7.addWidget(self.RegisterFormEmailLineEdit, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_6, 7, 2, 2, 17)
        spacerItem20 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem20, 3, 19, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem21, 1, 19, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem22, 17, 4, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem23, 17, 9, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem24, 5, 19, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem25, 16, 19, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem26, 10, 19, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem27, 9, 19, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem28, 17, 12, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem29, 12, 19, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(3, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.gridLayout.addItem(spacerItem30, 7, 19, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem31, 14, 19, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setObjectName("widget_9")
        self.RegisterFormSubmitBtn = QtWidgets.QPushButton(self.widget_9)
        self.RegisterFormSubmitBtn.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.RegisterFormSubmitBtn.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormSubmitBtn.setObjectName("RegisterFormSubmitBtn")
        self.gridLayout.addWidget(self.widget_9, 14, 9, 2, 4)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem32, 17, 11, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.RegisterViewTitleLabel = QtWidgets.QLabel(self.widget)
        self.RegisterViewTitleLabel.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.RegisterViewTitleLabel.setFont(font)
        self.RegisterViewTitleLabel.setObjectName("RegisterViewTitleLabel")
        self.RegisterViewDescriptionLabel = QtWidgets.QLabel(self.widget)
        self.RegisterViewDescriptionLabel.setGeometry(QtCore.QRect(10, 40, 67, 17))
        self.RegisterViewDescriptionLabel.setObjectName("RegisterViewDescriptionLabel")
        self.gridLayout.addWidget(self.widget, 0, 2, 3, 7)
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.RegisterFormPasswordLabel_2 = QtWidgets.QLabel(self.widget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterFormPasswordLabel_2.sizePolicy().hasHeightForWidth())
        self.RegisterFormPasswordLabel_2.setSizePolicy(sizePolicy)
        self.RegisterFormPasswordLabel_2.setObjectName("RegisterFormPasswordLabel_2")
        self.gridLayout_9.addWidget(self.RegisterFormPasswordLabel_2, 0, 0, 1, 1)
        self.RegisterFormPasswordLineEdit_2 = QtWidgets.QLineEdit(self.widget_8)
        self.RegisterFormPasswordLineEdit_2.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.RegisterFormPasswordLineEdit_2.setObjectName("RegisterFormPasswordLineEdit_2")
        self.gridLayout_9.addWidget(self.RegisterFormPasswordLineEdit_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_8, 11, 2, 2, 17)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem33, 1, 2, 1, 1)
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(RegisterWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 634, 22))
        self.menuBar.setObjectName("menuBar")
        RegisterWindow.setMenuBar(self.menuBar)
        self.actionLogin = QtGui.QAction(RegisterWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionRegister = QtGui.QAction(RegisterWindow)
        self.actionRegister.setObjectName("actionRegister")

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.RegisterFormFirstnameLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormSuffixLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormUsernameLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormPasswordLabel_1.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormLastnameLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormEmailLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormSubmitBtn.setText(_translate("RegisterWindow", "PushButton"))
        self.RegisterViewTitleLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterViewDescriptionLabel.setText(_translate("RegisterWindow", "TextLabel"))
        self.RegisterFormPasswordLabel_2.setText(_translate("RegisterWindow", "TextLabel"))
        self.actionLogin.setText(_translate("RegisterWindow", "Login"))
        self.actionRegister.setText(_translate("RegisterWindow", "Register"))
