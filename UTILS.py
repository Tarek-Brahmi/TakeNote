from constants import NO, YES
import random
import re
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from mysql.connector.constants import ServerFlag
from login import Ui_Form as loginForm
from welcome import Ui_Form as welcomeUI
from addnote import Ui_MainWindow as addNote
from myContainer import Ui_MainWindow as showNotes
from splashScreen import Ui_SplashScreen as splashScrenn
from Dbhelper import DbNoteHelper
from Models import Note

from Dbhelper import DBUserHelper


dbuser = DBUserHelper()
username = ""
myNotes = None
myNotesNumber = 0
counter = 0
myDBNOTEhelper = DbNoteHelper()


class AllNotes(object):

    def __init__(self) -> None:
        self.dbNoteHelper = myDBNOTEhelper

    def getAllMyNotes(self, **kwargs):
        global myNotes, myNotesNumber
        myNotes = []
        _mynotes = self.dbNoteHelper.getAllNotes(kwargs["username"])
        if len(_mynotes) > 0:
            for note in _mynotes:
                id_note, athour, description, content, status, createdAt, updatedAt = note
                new_note = Note(id_note=id_note, athour=athour, description=description,
                                content=content, status=status, createdAt=createdAt, updatedAt=updatedAt)
                myNotes.append(new_note)


class SplashScreen(QMainWindow, splashScrenn):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.MyNotesPage = ShowPrivateNotes(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.MyNotesPage.createFromDbNotes(username=str(username))

        self.timer.start(35)
        x = 1000-(len(myNotes)-(len(myNotes)//1000)*1000)
        QtCore.QTimer.singleShot(x, lambda: self.label_description.setText(
            "➭ <strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000-x, lambda: self.label_description.setText(
            "➭ <strong>LOADING</strong> USER INTERFACE"))
        self.show()

    def Loadingmsg(self):
        return "".join(["Loading"]+["."]*random.choice(list(range(1, 4))))

    def progress(self):
        global counter
        self.progressBar.setValue(counter)
        if counter > 100 and username != "":
            self.timer.stop()
            self.MyNotesPage.show()
            self.hide()
        else:
            QtCore.QTimer.singleShot(
                300, lambda: self.label_loading.setText(self.Loadingmsg()))
        counter += 1


class LoginForm(QMainWindow, loginForm):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle('Login | Take Note')
        self.bt_login.clicked.connect(self.handleSubmit)

    def handleSubmit(self):
        global username
        self.ll_cred.setText("")
        if(self.password.text() != "" and self.username.text() != ""):
            user = self.dbUserHelper.loginUser(username=str(
                self.username.text()), password=str(self.password.text()))
            if len(user) > 0:
                self.ll_cred.setText('logged in successfuly!')
                self.ll_cred.setStyleSheet('color:green;')
                # adding the splash screen
                username = user[0][1]
                SplashScreen(self).show()
                self.hide()
            else:
                self.ll_cred.setText('username or password are incorrect !')
                self.ll_cred.setStyleSheet('color:red;')
        elif self.password.text() == "" and self.username.text() == "":
            self.ll_cred.setText('username and password are required !')
            self.ll_cred.setStyleSheet('color:yellow;')
        elif self.password.text() == "":
            self.ll_cred.setText('password is required !')
            self.ll_cred.setStyleSheet('color:red;')
        elif self.username.text() == "":
            self.ll_cred.setText('username is required !')
            self.ll_cred.setStyleSheet('color:red;')


class UpdateNote(QMainWindow, addNote):
    def __init__(self, parent=None, selectedNote=None) -> None:
        super().__init__(parent=parent)
        self.selectedNote = selectedNote
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle('Update note | Take Note')
        self.l_text.setText('Udating Note :')
        self.btn_addnote.setObjectName("btn_addnote")
        self.btn_addnote.setIcon(QtGui.QIcon(":/icons/icons/update.png"))
        self.btn_addnote.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.btn_addnote.clicked.connect(self.UpdateNote)
        self.btn_reset.clicked.connect(self.resetInputs)

        self.btn_shownote = QtWidgets.QToolButton(self)
        self.btn_shownote.setIcon(QtGui.QIcon(':icons/icons/notes.png'))
        self.btn_shownote.setCheckable(True)
        self.btn_shownote.clicked.connect(self.myNotes)
        self.btn_shownote.setToolTip('add note')
        self.toolBar.addWidget(self.btn_shownote)

        self.editt_content.insertPlainText(self.selectedNote.getContent())

        self.editt_desc.insert(self.selectedNote.getDescription())

    def UpdateNote(self, **kwargs):
        global myDBNOTEhelper, username, myNotesNumber
        self.ll_cred.setText("")
        if(self.editt_content.toPlainText() != "" and self.editt_desc.text() != ""):
            new_desc = self.editt_desc.text()
            new_content = self.editt_content.toPlainText()

            # TODO need more testing

            myDBNOTEhelper.updateNote(
                int(self.selectedNote.getIdNote()), new_desc, new_content)

            self.ll_cred.setText("Note updated succesfuly !")
            self.ll_cred.setStyleSheet("color: green;")

            self.ll_cred.setVisible(False)
            self.editt_desc.setText("")
            self.editt_content.setPlainText("")

            # refresh the listWidget
            myNotes.clear()
            self.parent._myListContainer.clear()
            self.parent.createFromDbNotes(username=username)
            self.hide()

        else:
            if self.editt_content.toPlainText() == "" and self.editt_desc.text() == "":
                self.ll_cred.setText(
                    "Content of the note or description are required !")
                self.ll_cred.setStyleSheet("color: yellow;")
            elif self.editt_content.toPlainText() == "":
                self.ll_cred.setText("Content of the note is required !")
                self.ll_cred.setStyleSheet("color: red;")
            elif self.editt_desc.text() == "":
                self.ll_cred.setText("Description is required !")
                self.ll_cred.setStyleSheet("color: red;")

        self.ll_cred.setVisible(True)

    def resetInputs(self, **kwargs):
        self.ll_cred.setVisible(False)
        self.editt_desc.setText("")
        self.editt_content.setPlainText("")

    def myNotes(self):
        self.hide()


class AddPrivateNote(QMainWindow, addNote):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle('Adding note | Take Note')

        self.ll_cred.setVisible(False)
        self.btn_shownote = QtWidgets.QToolButton(self)
        self.btn_shownote.setIcon(QtGui.QIcon(':icons/icons/notes.png'))
        self.btn_shownote.setCheckable(True)
        self.btn_shownote.clicked.connect(self.myNotes)
        self.btn_shownote.setToolTip('add note')
        self.toolBar.addWidget(self.btn_shownote)
        self.btn_reset.clicked.connect(self.resetInputs)
        self.btn_addnote.clicked.connect(self.addNote)

    def resetInputs(self, **kwargs):
        self.ll_cred.setVisible(False)
        self.editt_desc.setText("")
        self.editt_content.setPlainText("")

    def addNote(self, **kwargs):
        global myDBNOTEhelper, username, myNotesNumber
        self.ll_cred.setText("")
        if(self.editt_content.toPlainText() != "" and self.editt_desc.text() != ""):
            desc = self.editt_desc.text()
            content = self.editt_content.toPlainText()

            # TODO need more testing
            # by default w create a private Note..
            myDBNOTEhelper.insertNote(
                desc=desc, athour=username, content=content, status=YES)
            self.ll_cred.setText("Note added succesfuly !")
            self.ll_cred.setStyleSheet("color: green;")

            self.ll_cred.setVisible(False)
            self.ll_cred.setText('')
            self.editt_desc.setText("")
            self.editt_content.setPlainText("")

            # refresh the listWidget
            myNotes.clear()
            self.parent._myListContainer.clear()
            self.parent.createFromDbNotes(username=username)
            self.hide()

        else:
            if self.editt_content.toPlainText() == "" and self.editt_desc.text() == "":
                self.ll_cred.setText(
                    "Content of the note or description are required !")
                self.ll_cred.setStyleSheet("color: yellow;")
            elif self.editt_content.toPlainText() == "":
                self.ll_cred.setText("Content of the note is required !")
                self.ll_cred.setStyleSheet("color: red;")
            elif self.editt_desc.text() == "":
                self.ll_cred.setText("Description is required !")
                self.ll_cred.setStyleSheet("color: red;")

        self.ll_cred.setVisible(True)

    def myNotes(self):

        self.hide()


class ShowPrivateNotes(QMainWindow, showNotes):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

        self.pattren = r"(?P<index>\d+)"
        self.deleteORUpdatePattren = r"(?P<delete>delete)|(?P<update>update)"
        self.setupUi(self)
        self.setWindowTitle('My Notes | Take Note')
        # self.parent.setFixedSize(720, 500)
        self.addingNoteForm = AddPrivateNote(self)
        self.allMynotes = None
        # the tool bar
        self.btn_logout = QtWidgets.QToolButton(self)
        self.btn_logout.setIcon(QtGui.QIcon(':icons/icons/logout.png'))
        self.btn_logout.setCheckable(True)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_logout.setToolTip('logout')
        self.toolBar.addWidget(self.btn_logout)

        self.btn_addnote = QtWidgets.QToolButton(self)
        self.btn_addnote.setIcon(QtGui.QIcon(':icons/icons/addnote.png'))
        self.btn_addnote.setCheckable(True)
        self.btn_addnote.clicked.connect(self.addNote)
        self.btn_addnote.setToolTip('add note')
        self.toolBar.addWidget(self.btn_addnote)

        self._myListContainer.itemSelectionChanged.connect(
            self.showContentOfNote)

    def __del__(self):
        dbuser.logoutUser(username=username)

    def logout(self):
        global username, dbuser, myNotes
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Are you sure to logout ?")
        msgBox.setStyleSheet("background-color: white;")
        msgBox.setWindowTitle("Log out ✌")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:

            self.close()
            del self

    def addNote(self):
        self.addingNoteForm.show()
        # self.hide()

    def getTheSelectedItem(self):
        sending_button = self.sender()

        index = int(
            re.search(self.pattren, sending_button.objectName()).group('index'))

        s = self._myListContainer.item(index)
        self._myListContainer.setCurrentItem(s)
        deleteOrUpdate = [i for i in list(re.search(
            self.deleteORUpdatePattren, sending_button.objectName()).groupdict().values()) if i != None][-1]
        if deleteOrUpdate == "delete":
            self.deleteNote(myNotes[index])
        else:
            self.updateNote(myNotes[index])

    def deleteNote(self, selectedNote):
        global myNotesNumber
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("deleting item")
        msgBox.setStyleSheet("background-color: white;")
        msgBox.setWindowTitle("Detete Note")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            myDBNOTEhelper.deleteNote(id=int(selectedNote.getIdNote()))

            # refresh the listWidget
            myNotes.clear()
            self._myListContainer.clear()
            self.createFromDbNotes(username=username)

    def updateNote(self, selectedNote):
        print("update", selectedNote)
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("updating item")
        msgBox.setStyleSheet("background-color: white;")
        msgBox.setWindowTitle("Update Note")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            UpdateNote(self, selectedNote).show()

    def showContentOfNote(self):

        self.label.setText("Content of note %d:" % (
                           self._myListContainer.currentIndex().row()+1))
        self.l_content.setText(self._myListContainer.currentItem().data(1))

    def genereateNoteItem(self, index, **kwargs):

        widget_3 = QtWidgets.QWidget(self._myListContainer)

        widget_3.setObjectName("widget_3%d" % index)
        note_tools = QtWidgets.QHBoxLayout(widget_3)
        note_tools.setContentsMargins(0, 0, 0, 0)
        note_tools.setSpacing(0)
        note_tools.setObjectName("note_tools%d" % index)
        note_desc = QtWidgets.QLabel(widget_3)
        note_desc.setObjectName("note_desc%d" % index)
        note_desc.setText(kwargs["note_desc"])
        # create an icon for showing the status of
        status = kwargs['status']
        note_desc.setToolTip("description of note %d" % (index+1))
        note_tools.addWidget(note_desc)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        note_tools.addItem(spacerItem)
        bouttons = QtWidgets.QHBoxLayout()
        bouttons.setSpacing(0)
        bouttons.setObjectName("bouttons%d" % index)

        btn_publicorPrivate = QtWidgets.QPushButton(widget_3)
        if status == YES:
            # Private note
            btn_publicorPrivate.setToolTip("Private note")
            btn_publicorPrivate.setIcon(
                QtGui.QIcon(":/icons/icons/private.png"))
            btn_publicorPrivate.setStyleSheet("background-color: yellow;")
            btn_publicorPrivate.setObjectName("btn_publicorPrivate%d" % index)
        else:
            # Public note
            btn_publicorPrivate.setToolTip("Public note")
            btn_publicorPrivate.setIcon(
                QtGui.QIcon(":/icons/icons/public.png"))
            btn_publicorPrivate.setStyleSheet("background-color: yellow;")
            btn_publicorPrivate.setObjectName("btn_publicorPrivate%d" % index)
        bouttons.addWidget(btn_publicorPrivate)

        btn_update = QtWidgets.QPushButton(widget_3)
        btn_update.setToolTip("update note")
        btn_update.setIcon(QtGui.QIcon(":/icons/icons/update.png"))
        btn_update.setStyleSheet("background-color: green;")
        btn_update.setObjectName("btn_update%d" % index)
        btn_update.clicked.connect(self.getTheSelectedItem)

        bouttons.addWidget(btn_update)
        btn_delete = QtWidgets.QPushButton(widget_3)
        btn_delete.setToolTip("delete note")
        btn_delete.setIcon(QtGui.QIcon(":/icons/icons/delete.png"))
        btn_delete.setStyleSheet("background-color: red;")
        btn_delete.setObjectName("btn_delete%d" % index)
        btn_delete.clicked.connect(self.getTheSelectedItem)
        bouttons.addWidget(btn_delete)
        note_tools.addLayout(bouttons)
        return widget_3

    def createFromDbNotes(self, **kwargs):
        global myNotes, myNotesNumber
        self.allMynotes = AllNotes()
        self.allMynotes.getAllMyNotes(username=kwargs["username"])
        nodes_with_desc = myNotes
        myNotesNumber = len(myNotes)
        many_note_tools = [self.genereateNoteItem(
            i, note_desc=nodes_with_desc[i].getDescription(), status=nodes_with_desc[i].getStatus()) for i in range(len(nodes_with_desc))]
        for k in range(len(many_note_tools)):
            item = QtWidgets.QListWidgetItem()
            item.setData(1, nodes_with_desc[k].getContent())
            self._myListContainer.addItem(item)
            self._myListContainer.setItemWidget(item, many_note_tools[k])


class WelcomeUI(QMainWindow, welcomeUI):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle('Welcome | Take Note')
        self.bt_login.clicked.connect(self.showLoginForm)
        self.loginPage = LoginForm(self)

    def showLoginForm(self):
        self.loginPage.show()
        self.hide()
