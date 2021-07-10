from Dbhelper import DBUserHelper
import sys

db=DBUserHelper()
db.insertUser(username=sys.argv[1],password=sys.argv[2])
