# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import takenote_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Dbhelper import DBUserHelper


class PasswordEdit(QLineEdit):

    def __init__(self, parent):
        self.parent = parent
        super().__init__(self.parent)
        self.visibleIcon = QIcon(":/icons/icons/eyeon.png")
        self.hiddenIcon = QIcon(":/icons/icons/eyeoff.png")

        self.setEchoMode(QLineEdit.Password)
        self.togglepasswordAction = self.addAction(
            self.visibleIcon, QLineEdit.TrailingPosition)
        self.togglepasswordAction.triggered.connect(self.toggle_mode)
        self.password_shown = False

    def toggle_mode(self):
        if not self.password_shown:
            self.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.setEchoMode(QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)


class Ui_Form(object):
    def __init__(self) -> None:
        self.dbUserHelper = DBUserHelper()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(448, 364)
        Form.setFixedSize(448, 364)
        Form.setStyleSheet("background: rgb(25, 25, 40);\n"
                           "border-radius:10px;")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 441, 381))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        self.verticalWidget_2.setStyleSheet("")
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.verticalWidget_2)
        self.logo.setEnabled(False)
        self.logo.setMinimumSize(QtCore.QSize(100, 150))
        self.logo.setMaximumSize(QtCore.QSize(150, 150))
        self.logo.setStyleSheet("image:url(:/images/icons/note_48x48.png);\n"
                                "font: 55pt \"Ubuntu\";")
        self.logo.setLineWidth(3)
        self.logo.setTextFormat(QtCore.Qt.RichText)
        self.logo.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.logo.setWordWrap(False)
        self.logo.setIndent(3)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.l_title = QtWidgets.QLabel(self.verticalWidget_2)
        self.l_title.setAutoFillBackground(False)
        self.l_title.setStyleSheet("color:rgb(186, 189, 182);\n"
                                   "font:63 italic 20pt \"URW Bookman\";")
        self.l_title.setScaledContents(False)
        self.l_title.setAlignment(QtCore.Qt.AlignCenter)
        self.l_title.setWordWrap(True)
        self.l_title.setObjectName("l_title")
        self.horizontalLayout.addWidget(self.l_title)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 6, 10, 0)
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.l_username = QtWidgets.QLabel(self.verticalWidget_2)
        self.l_username.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "image:url(:/icons/lock_32x32.png);")
        self.l_username.setObjectName("l_username")
        self.gridLayout.addWidget(self.l_username, 0, 0, 1, 1)

        self.username = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.username.setPlaceholderText("username")
        self.username.setStyleSheet("QLineEdit {\n"
                                    "                                     color: white;\n"
                                    "                                    font: 15pt \\\"Verdana\\\";\n"
                                    "                                    border: None;\n"
                                    "                                    border-bottom-color: white;\n"
                                    "                                    border-radius: 10px;\n"
                                    "                                    padding: 0 8px;\n"
                                    "                                    background: rgb(25, 25, 40);\n"
                                    "                                     selection-background-color: darkgray;\n"
                                    "}")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)

        self.line_3 = QtWidgets.QFrame(self.verticalWidget_2)
        self.line_3.setStyleSheet("border: 2px solid red;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 1, 1, 1)

        self.l_passwd = QtWidgets.QLabel(self.verticalWidget_2)
        self.l_passwd.setStyleSheet("color: rgb(231, 231, 231);\n"
                                    "font: 15pt \"Verdana\";\n"
                                    "image:url(:/icons/lock_32x32.png);")
        self.l_passwd.setObjectName("l_passwd")

        self.gridLayout.addWidget(self.l_passwd, 2, 0, 1, 1)

        self.password = PasswordEdit(self.verticalWidget_2)
        self.password.setPlaceholderText('password')
        self.password.setStyleSheet("QLineEdit {\n"
                                    "                                     color: orange;\n"
                                    "                                    font: 15pt \\\"Verdana\\\";\n"
                                    "                                    border: None;\n"
                                    "                                    border-bottom-color: white;\n"
                                    "                                    border-radius: 10px;\n"
                                    "                                    padding: 0 8px;\n"
                                    "                                    background: rgb(25, 25, 40);\n"
                                    "                                     selection-background-color: darkgray;\n"
                                    "}")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.verticalWidget_2)
        self.line_2.setStyleSheet("border: 2px solid red;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.bt_login = QtWidgets.QPushButton(self.verticalWidget_2)
        self.bt_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        # self.bt_login.clicked.connect(self.login)

        self.bt_login.setStyleSheet("color: rgb(231, 231, 231);\n"
                                    "font: 17pt \\\"Verdana\\\";\n"
                                    "border: 1px solid orange;\n"
                                    "border-radius: 9px;\n"
                                    "opacity: 200;")
        self.bt_login.setFlat(True)
        self.bt_login.setIcon(QtGui.QIcon(":/icons/icons/login.png"))
        self.bt_login.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.bt_login.setToolTip("Login")
        self.bt_login.setObjectName("bt_login")
        self.verticalLayout_2.addWidget(
            self.bt_login, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.ll_cred = QtWidgets.QLabel(self.verticalWidget_2)
        self.ll_cred.setText("")
        self.ll_cred.setObjectName("ll_cred")
        self.verticalLayout_2.addWidget(
            self.ll_cred, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.verticalWidget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logo.setToolTip(_translate(
            "Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.logo.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.l_title.setText(_translate(
            "Form", "Log in to view your private notes 😉:"))
        self.l_username.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Verdana\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/user_32x32.png\" /></p></body></html>"))
        self.l_passwd.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Verdana\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icons/lock_32x32.png\" /></p></body></html>"))
        self.bt_login.setText(_translate("Form", ""))

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
