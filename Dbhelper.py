from constants import *
import datetime
import mysql.connector
from mysql.connector import Error


def wrapContent(content):
    return content.replace('"', r'\"').replace("'", r"\'")


class DbNoteHelper:
    class DBException(Exception):
        pass

    def __init__(self) -> None:
        self.insertQuery = """INSERT INTO %s(id_note, athour, description,content,status,created_at,updated_at) VALUES(NULL, "%s", "%s", "%s", "%s","%s","%s");"""
        self.deleteQuery = """DELETE FROM %s WHERE id_note=%d;"""
        self.updateQuery = """UPDATE %s SET description="%s",content="%s", updated_at="%s" WHERE id_note=%d;"""
        
        self.selectAllQuery = """SELECT * FROM %s WHERE athour="%s" ORDER BY id_note DESC;"""
        self.selectstatusQuery = """SELECT * FROM %s WHERE status="%s" ORDER BY id_note DESC;"""
        
        self.selectQuery1 = """SELECT * FROM %s WHERE id_note=%d;"""

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db_name
        )
        self.cursor = self.connection.cursor(prepared=True)

    def __exit__(self):
        self.cursor.close()
        self.connection.close()

    def executeQuery(self, query, **kwargs):
        print("QUERY :", query)
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

        except Error as e:

            raise self.DBException(e)
        return result

    def executequery(self, query, **kwargs):
        print("QUERY :", query)
        try:
            self.cursor.execute(query)
            self.connection.commit()

        except Error as e:
            raise self.DBException()

    def insertNote(self, desc, athour, content,status):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return self.executequery(self.insertQuery % (note_table, str(athour), wrapContent(str(desc)), wrapContent(str(content)),status, now, now))

    def deleteNote(self, id):
        self.executequery(self.deleteQuery % (note_table, int(id)))

    def updateNote(self, id, description, content):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.executequery(self.updateQuery %
                          (note_table, wrapContent(str(description)), wrapContent(str(content)), now, int(id)))
    ### used whene user is logged in ...
    def getAllNotes(self, athour):
        return self.executeQuery(self.selectAllQuery % (note_table, str(athour)))
    ### used whene no user is logged in 
    def getAllNotstatusNotes(self, status=NO):
        return self.executeQuery(self.selectstatusQuery % (note_table,str(status)))
    
    def getNoteById(self, id):
        return self.executeQuery(self.selectQuery1 % (note_table, int(id)))


class DBUserHelper:
    class DBException(Exception):
        pass

    def __init__(self) -> None:
        self.insertQuery = """INSERT INTO %s(id_user, username ,password, created_at,updated_at,isLoggedIn) VALUES(NULL, "%s", "%s", "%s", "%s","%s");"""
        self.updateQuery = """UPDATE %s SET username="%s",password="%s", updated_at="%s",isLoggedIn='%s' WHERE id_user=%d;"""
        self.deleteQuery = """DELETE FROM %s WHERE id_user=%d;"""
        self.selectQuery = """SELECT id_user, username , created_at,isLoggedIn FROM %s WHERE username="%s" and password="%s";"""

        self.selectQuery1 = """SELECT id_user, username , created_at,isLoggedIn FROM %s ;"""

        self.selectQueryGetNotes = """SELECT %s.id_note,%s.description,%s.content,%s.created_at FROM %s,%s WHERE %s.username="%s" and %s.athour="%s" and %s.status="%s" ORDER BY NOTES.updated_at DESC;"""

        self.loginQuery = """UPDATE %s SET isLoggedIn='%s' WHERE id_user=%d;"""
        self.logoutQuery = """UPDATE %s SET isLoggedIn='%s' WHERE username="%s";"""

        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            database=db_name
        )
        self.cursor = self.connection.cursor(prepared=True)

    def executequery(self, query):
        print("QUERY :", query)
        try:
            self.cursor.execute(query)
            self.connection.commit()

        except Error as e:
            raise self.DBException()

    def executeQuery(self, query, **kwargs):
        print("QUERY :", query)
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()

        except Error as e:
            raise self.DBException(e)
        return result

    def insertUser(self, **kwargs):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.executequery(self.insertQuery % (user_table, str(kwargs["username"]), str(kwargs["password"]), now, now, NO))

    def updateUser(self, **kwargs):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.executequery(self.updateQuery % (user_table, str(kwargs["new_username"]), str(kwargs["new_password"]), now, str(kwargs['isLoggedIn']), int(kwargs["id"])))

    def deleteUser(self, **kwargs):
        return self.executequery(self.deleteQuery % (user_table, int(kwargs["id"])))

    def loginUser(self, **kwargs):
        user = self.executeQuery(self.selectQuery % (
            user_table, str(kwargs["username"]), str(kwargs["password"])))
        if user:
            self.executequery(self.loginQuery %
                              (user_table, YES, int(user[0][0])))
        return self.executeQuery(self.selectQuery % (user_table, str(kwargs["username"]), str(kwargs["password"])))

    def logoutUser(self, **kwargs):
        return self.executequery(self.logoutQuery % (user_table, NO, str(kwargs['username'])))

    def selectAllUsers(self, **kwargs):
        return self.executeQuery(self.selectQuery1 % (user_table))

    def getNotes(self, **kwargs):
        return self.executeQuery(self.selectQueryGetNotes % (note_table, note_table, note_table, note_table, note_table, user_table, user_table, str(kwargs['username']), note_table, str(kwargs['username']),note_table,str(kwargs['status'])))
