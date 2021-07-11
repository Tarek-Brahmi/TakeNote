# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addnote.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import takenote_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 360)
        MainWindow.setFixedSize(680, 360)
        MainWindow.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 680, 327))
        self.splitter.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(6, 0, 2, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_text = QtWidgets.QLabel(self.widget)
        self.l_text.setObjectName("l_text")
        self.horizontalLayout_2.addWidget(self.l_text)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_reset = QtWidgets.QPushButton(self.widget)
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.setIcon(QtGui.QIcon(":/icons/icons/reset.png"))
        self.btn_reset.setStyleSheet("background-color: rgb(32, 74, 135);")

        self.btn_reset.setToolTip('Reset Inputs')

        self.horizontalLayout.addWidget(self.btn_reset)

        self.btn_addnote = QtWidgets.QPushButton(self.widget)
        self.btn_addnote.setObjectName("btn_addnote")
        self.btn_addnote.setIcon(QtGui.QIcon(":/icons/icons/addnote.png"))
        self.btn_addnote.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.btn_addnote.setToolTip("Add Note")

        self.horizontalLayout.addWidget(self.btn_addnote)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.widget1)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("13pt Ubuntu Condensed")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(117, 80, 123);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.930577, y1:0.136136, x2:0.0248756, y2:0.988682, stop:0 rgba(42, 21, 28, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: blod 13pt \"Ubuntu Condensed\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editt_desc = QtWidgets.QLineEdit(self.frame_2)
        self.editt_desc.setPlaceholderText('describe your note !')
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editt_desc.sizePolicy().hasHeightForWidth())
        self.editt_desc.setSizePolicy(sizePolicy)
        self.editt_desc.setMinimumSize(QtCore.QSize(0, 0))
        self.editt_desc.setStyleSheet("color: orange;\n"
                                      "font: 13pt \\\"Verdana\\\";\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(25, 25, 40);\n"
                                      "selection-background-color: darkgray;")
        self.editt_desc.setObjectName("editt_desc")
        self.verticalLayout.addWidget(self.editt_desc)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("13pt Ubuntu Condensed")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(117, 80, 123);\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.930577, y1:0.136136, x2:0.0248756, y2:0.988682, stop:0 rgba(42, 21, 28, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "font: blod 13pt \"Ubuntu Condensed\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.editt_content = QtWidgets.QPlainTextEdit(self.frame_3)
        self.editt_content.setPlaceholderText('content of the note')
        self.editt_content.setStyleSheet("color: white;\n"
                                         "font: 11pt \\\"Verdana\\\";\n"
                                         "padding: 0 8px;\n"
                                         "border-radius:3px;\n"
                                         "background: rgb(25, 25, 40);\n"
                                         "selection-background-color: darkgray;")
        self.editt_content.setObjectName("editt_content")
        self.verticalLayout_2.addWidget(self.editt_content)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.ll_cred = QtWidgets.QLabel(self.splitter)
        self.ll_cred.setObjectName("ll_cred")
        self.ll_cred.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.ll_cred.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_text.setText(_translate("MainWindow", "Adding Note :"))

        self.label_2.setText(_translate("MainWindow", "  description :"))
        self.label.setText(_translate("MainWindow", "  content:"))
        self.ll_cred.setText(_translate("MainWindow", ""))

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(
            QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
