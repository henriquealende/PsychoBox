import mysql.connector as con

from PySide2.QtWidgets import QGraphicsOpacityEffect
from PySide2.QtCore import QPropertyAnimation

def loginUser(self, username, password):
    database = con.connect(host="localhost", user="root",
                            password="", db="embraco")
    cursor = database.cursor()
    cursor.execute("select * from users where username= '" + username +
                    "' and password= '" + password + "'")
    result = cursor.fetchone()
    if result:
        self.ui.rightContent.setCurrentWidget(self.ui.welcomePage)
        fadeIn = QGraphicsOpacityEffect(self.ui.welcomePage)
        self.animation = QPropertyAnimation(fadeIn, b"opacity")
        self.ui.welcomePage.setGraphicsEffect(fadeIn)
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
        self.ui.filterButton.setEnabled(True)
        self.ui.calibrationButton.setEnabled(True)
        self.ui.usernameLabel.setText(username.title())
        self.ui.userButton.setEnabled(True)
        self.ui.userButton.setChecked(True)
        self.online = True
        if self.ui.leftMenu.width() > 50:
            self.ui.userButton.setText(
                self.ui.usernameLabel.text()+'\nSair')
        else:
            self.ui.userButton.setText("")
    else:
        self.ui.registerInfo.setText('Access Denied! \nUnregistered user')
    
def registerUser(self, username, password):
    database = con.connect(host="localhost", user="root",
                            password="", db="embraco")
    cursor = database.cursor()
    cursor.execute("select * from users where username= '" + username +
                    "' and password= '" + password + "'")
    result = cursor.fetchone()
    if result:
        self.ui.registerInfo.setText('User already registered')
    else:
        cursor.execute("insert into users values('" + username +
                        "','" + password + "')")
        database.commit()
        self.ui.registerInfo.setText('User successfully registered')
