# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addnote.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 555)
        MainWindow.setFixedSize(600, 555)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setGeometry(QtCore.QRect(0, 0, 600, 555))
        self.formWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.930577, y1:0.136136, x2:0.0248756, y2:0.988682, stop:0 rgba(42, 21, 28, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "border-radius:3px;")
        self.formWidget.setObjectName("formWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.formWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 600, 555))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_reset = QtWidgets.QPushButton(self.frame)
        ## join the reset button to the reset function
        self.bt_reset.clicked.connect(self.resetInputs)
        self.bt_reset.setStyleSheet("background-color: rgb(245, 121, 0);\n"
                                    "font: 75 italic 13pt \"Ubuntu Condensed\";")
        self.bt_reset.setObjectName("bt_reset")
        self.horizontalLayout.addWidget(self.bt_reset)
        self.bt_addNote = QtWidgets.QPushButton(self.frame)
        self.bt_addNote.clicked.connect(self.addNote)
        self.bt_addNote.setStyleSheet("font: 75 italic 13pt \"Ubuntu Condensed\";\n"
                                      "background-color:green;")
        self.bt_addNote.setObjectName("bt_addNote")
        self.horizontalLayout.addWidget(self.bt_addNote)
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ll_descr = QtWidgets.QLabel(self.frame_2)
        self.ll_descr.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setFamily("13pt Ubuntu Condensed")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ll_descr.setFont(font)
        self.ll_descr.setStyleSheet("color: black;\n"
                                    "background-color: qlineargradient(spread:pad, x1:0.930577, y1:0.136136, x2:0.0248756, y2:0.988682, stop:0 rgba(42, 21, 28, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                    "font: blod 13pt \"Ubuntu Condensed\";")
        self.ll_descr.setObjectName("ll_descr")
        self.verticalLayout.addWidget(self.ll_descr)
        self.editt_desc = QtWidgets.QLineEdit(self.frame_2)
        self.editt_desc.setPlaceholderText('describe your note !')
        self.editt_desc.setMaxLength(100)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.editt_desc.sizePolicy().hasHeightForWidth())
        self.editt_desc.setSizePolicy(sizePolicy)
        self.editt_desc.setMinimumSize(QtCore.QSize(0, 0))
        self.editt_desc.setStyleSheet("color: orange;\n"
                                      "font: 11pt \\\"Verdana\\\";\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(25, 25, 40);\n"
                                      "selection-background-color: darkgray;")
        self.editt_desc.setObjectName("editt_desc")
        self.verticalLayout.addWidget(self.editt_desc)
        self.frame_3 = QtWidgets.QFrame(self.splitter)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ll_content = QtWidgets.QLabel(self.frame_3)
        self.ll_content.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setFamily("13pt Ubuntu Condensed")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ll_content.setFont(font)
        self.ll_content.setStyleSheet("color: black;\n"
                                      "background-color: qlineargradient(spread:pad, x1:0.930577, y1:0.136136, x2:0.0248756, y2:0.988682, stop:0 rgba(42, 21, 28, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "font: blod 13pt \"Ubuntu Condensed\";")
        self.ll_content.setObjectName("ll_content")
        self.verticalLayout_2.addWidget(self.ll_content, 0, QtCore.Qt.AlignTop)
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
        self.ll_cred = QtWidgets.QLabel(self.splitter)
        self.ll_cred.setVisible(False)
        self.ll_cred.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ll_cred.setFont(font)
        self.ll_cred.setStyleSheet("text-align:center;")
        self.ll_cred.setObjectName("ll_cred")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "   Adding note:"))
        self.bt_reset.setText(_translate("MainWindow", "Reset"))
        self.bt_addNote.setText(_translate("MainWindow", "Add note"))
        self.ll_descr.setText(_translate("MainWindow", "description:"))
        self.ll_content.setText(_translate("MainWindow", "content:"))
        self.ll_cred.setText(_translate("MainWindow", ""))

    def addNote(self, **kwargs):
        self.ll_cred.setText("")
        if(self.editt_content.toPlainText()!="" and self.editt_desc.text()!=""):
            desc=self.editt_desc.text()
            content=self.editt_content.toPlainText()
            print(desc,content)
            self.ll_cred.setText("Note added succesfuly !")
            self.ll_cred.setStyleSheet("background: green;")
            
        else:
            if self.editt_content.toPlainText()=="" and self.editt_desc.text()=="" :
                self.ll_cred.setText("Content of the note or description are required !")
                self.ll_cred.setStyleSheet("background: yellow;")
            elif self.editt_content.toPlainText()=="":
                self.ll_cred.setText("Content of the note is required !")
                self.ll_cred.setStyleSheet("background: red;")
            elif self.editt_desc.text()=="":
                self.ll_cred.setText("Description is required !")
                self.ll_cred.setStyleSheet("background: red;")
            
        self.ll_cred.setVisible(True)
    def resetInputs(self, **kwargs):
        self.ll_cred.setVisible(False)
        self.editt_desc.setText("")
        self.editt_content.setPlainText("")


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
