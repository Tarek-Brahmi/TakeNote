# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_sc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(600, 250)
        SplashScreen.setFixedSize(600, 250)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
                                           "    background: rgb(25, 25, 40);   \n"
                                           "    color: rgb(220, 220, 220);\n"
                                           "    border-radius: 10px;\n"
                                           "}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 20, 600, 52))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(114, 159, 207);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(0, 78, 600, 44))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(186, 189, 182);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(25, 128, 551, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    \n"
                                       "    background-color: rgb(98, 114, 164);\n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "    border-style: none;\n"
                                       "    border-radius: 10px;\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "    border-radius: 10px;\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.975, y1:0.5, x2:0.02, y2:0.522773, stop:0 rgba(195, 127, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                       "}")
        self.progressBar.setProperty("value", 6)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(0, 161, 600, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(243, 243, 243);")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(0, 220, 591, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_credits.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate(
            "SplashScreen", "<strong>Take Note </strong>"))
        self.label_description.setText(_translate(
            "SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Take </span><span style=\" font-weight:600; font-style:italic;\">Note</span> and save your <span style=\" font-weight:600; font-style:italic;\">Time </span><span style=\" font-size:18pt;\">ッ </span></p></body></html>"))
        self.label_loading.setText(_translate("SplashScreen", "loading..."))
        self.label_credits.setText(_translate(
            "SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">Created by</span>: <span style=\" font-style:italic;\">Brahmi Tarek </span>🙋</p></body></html>"))
