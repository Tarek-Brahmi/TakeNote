# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import takenote_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 465)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 661, 451))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.horizontalLayoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(1)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.verticalLayoutWidget_2)
        self.splitter.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.SpanningRole, self.label_10)
        
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setObjectName("widget")
        
        self.vl_mynoteDescContent = QtWidgets.QVBoxLayout(self.widget)
        self.vl_mynoteDescContent.setSpacing(1)
        self.vl_mynoteDescContent.setObjectName("vl_mynoteDescContent")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.note_content_2 = QtWidgets.QLabel(self.widget)
        self.note_content_2.setObjectName("note_content_2")
        self.horizontalLayout_2.addWidget(self.note_content_2)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.update_note = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.update_note.setFont(font)
        self.update_note.setStyleSheet("image: url(:/icons/icons/update.png);\n"
                                       "")
        self.update_note.setText("")
        self.update_note.setObjectName("update_note")
        self.horizontalLayout_2.addWidget(self.update_note)
        self.note_delete = QtWidgets.QLabel(self.widget)
        self.note_delete.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.note_delete.setFont(font)
        self.note_delete.setStyleSheet("image: url(:/icons/icons/delete.png);")
        self.note_delete.setFrameShadow(QtWidgets.QFrame.Raised)
        self.note_delete.setText("")
        self.note_delete.setObjectName("note_delete")
        self.horizontalLayout_2.addWidget(self.note_delete)
        self.vl_mynoteDescContent.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("image: url(:/icons/icons/update.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("image: url(:/icons/icons/delete.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.vl_mynoteDescContent.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("image: url(:/icons/icons/update.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setStyleSheet("image: url(:/icons/icons/delete.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.vl_mynoteDescContent.addLayout(self.horizontalLayout_4)
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.widget)
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.note_content = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.note_content.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                        "border-radius:3px;")
        self.note_content.setWidgetResizable(True)
        self.note_content.setObjectName("note_content")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 136, 427))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.note_content.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.note_content)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "My notes :"))
        self.note_content_2.setText(_translate(
            "MainWindow", "TextLabelsdqsdqsdqdssdqd"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "My note:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
