# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import takenote_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Form as loginPage


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(333, 222)
        Form.setFixedSize(333, 222)
        Form.setStyleSheet("background-color: rgb(25, 25, 40);\n"
                           "border-radius:3px;")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 333, 222))
        self.verticalWidget.setStyleSheet("background-color: rgb(25, 25, 40);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalWidget)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.logo = QtWidgets.QLabel(self.splitter)
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
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setStyleSheet("font: 75 16pt \"Ubuntu Condensed\";\n"
                                 "\n"
                                 "color: rgb(186, 189, 182);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget1 = QtWidgets.QWidget(self.verticalWidget)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.widget1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(1)
        self.splitter_2.setObjectName("splitter_2")
        self.bt_login = QtWidgets.QPushButton(self.splitter_2)

        self.bt_login.setObjectName("bt_login")
        self.bt_login.setIcon(QtGui.QIcon(":/icons/icons/login.png"))
        self.bt_login.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.bt_login.setToolTip("Login")

        self.bt_shownotes = QtWidgets.QPushButton(self.splitter_2)
        self.bt_shownotes.setObjectName("bt_shownotes")
        self.bt_shownotes.setIcon(QtGui.QIcon(":/icons/icons/notes.png"))
        self.bt_shownotes.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.bt_shownotes.setToolTip("MyNotes")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout_3.addWidget(
            self.frame, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.widget1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logo.setToolTip(_translate(
            "Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.logo.setText(_translate(
            "Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("Form", "Welcome ☺:"))
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())