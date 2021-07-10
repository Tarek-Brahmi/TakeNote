import takenote_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 530)
        MainWindow.setFixedSize(820, 530)
        MainWindow.setStyleSheet("background-color: rgb(136, 138, 133);\n"
                                 "border-radius:3px;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 820, 500))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")

        self.w_forAllMyNotes = QtWidgets.QWidget(self.splitter)
        self.w_forAllMyNotes.setStyleSheet(
            "background-color: rgb(85, 87, 83);")
        self.w_forAllMyNotes.setObjectName("w_forAllMyNotes")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.w_forAllMyNotes)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.w_forAllMyNotes)
        self.label_2.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self._myListContainer = QtWidgets.QListWidget(self.w_forAllMyNotes)
        self._myListContainer.setObjectName("_myListContainer")
        self.verticalLayout_2.addWidget(self._myListContainer)

        
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.w_forContent = QtWidgets.QWidget(self.splitter)
        self.w_forContent.setStyleSheet(
            "background-color: rgb(136, 138, 133);")
        self.w_forContent.setObjectName("w_forContent")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.w_forContent)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.w_forContent)
        self.label.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self._mySelectedNoteContainer = QtWidgets.QScrollArea(self.w_forContent)
        self._mySelectedNoteContainer.setWidgetResizable(True)
        self._mySelectedNoteContainer.setObjectName("_mySelectedNoteContainer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(-21, 0, 345, 368))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.l_content = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.l_content.setWordWrap(True)
        self.l_content.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        font = QtGui.QFont()
        font.setFamily("VL Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l_content.setFont(font)
        self.l_content.setObjectName("l_content")
        self.verticalLayout_4.addWidget(
            self.l_content, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self._mySelectedNoteContainer.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self._mySelectedNoteContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "My private notes:"))
        self.label.setText(_translate("MainWindow", "Content:"))
        
