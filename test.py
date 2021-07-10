from Dbhelper import DbNoteHelper, DBUserHelper
from constants import *
import mysql.connector
from mysql.connector import Error


# used one time here
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def create_connection(host_name, user_name, user_password, name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "password",db_name)


#####  for note table ########
# create_database(connection,crate_db_note)
# create_database(connection,create_note_table)

myDbNotehelper = DbNoteHelper()
# # print(myDbNotehelper.selectQuery)
notes=["fNsFVpO8JtesQsxE0ccH",
 "p5EOr9hGJdUwDTSSdiL",
 "lNsjTHagbyliisvfRJ",
 "IoiT6BXPMB9SoftS5",
 "8w3tkeyvk25SIFYg",
 "uKFZnx47Od8hDpN",
 "qZ7cdVOKbhfo5I",
 "ZVr1Fx5aiKT5E",
 "rjuwvhdQoXwp",
 "13w6MTjAMvZ"]
for note in list(range(1000)):
    myDbNotehelper.insertNote(note,"tarek",note)
# # myDbNotehelper.insertNote("this is a note from salim","salim")
# myDbNotehelper.insertNote("adding","karim",open('./myContainer.py',"r").read())
# print(myDbNotehelper.getAllNotes("tarek"))
# myDbNotehelper.deleteNote(1)
# myDbNotehelper.updateNote(2,"hello from...................","comme one !")
# print(myDbNotehelper.getAllNotes("karim"))
# print(myDbNotehelper.getNoteById(2))

#####  for users table ########

# myDbUserhelper = DBUserHelper()
# # myDbUserhelper.insertUser(username="karim", password="password")
# # myDbUserhelper.insertUser(username="tarek", password="password")
# # myDbUserhelper.updateUser(new_username="salim",new_password="password",id=1,isLoggedIn=0)
# # myDbUserhelper.deleteUser(id=2)

# # print(myDbUserhelper.selectAllUsers())
# # for note in myDbUserhelper.getNotes(username="karim"):
# #     print(note)
    
    
# print(myDbUserhelper.loginUser(username="karim",password="password"))
# print(myDbUserhelper.loginUser(username="tarek",password="password"))
# print(myDbUserhelper.logoutUser(username="karim"))
# print(myDbUserhelper.selectAllUsers())