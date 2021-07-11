import re

from PyQt5.QtGui import QIcon
from UTILS import WelcomeUI, SplashScreen
import sys
from PyQt5.QtWidgets import QApplication
from Dbhelper import DBUserHelper


def main():
    # try to get the logged in user from db ...
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":images/icons/note_48x48.png"))
    dbuser = DBUserHelper()
    result = dbuser.getLoggedInUser()
    print(result)
    
    if len(result) > 0:
        
        splash = SplashScreen(userna=result[0][1])
        splash.show()
    else:
        welcome = WelcomeUI()
        welcome.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
