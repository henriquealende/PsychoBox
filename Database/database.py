from widget import *
import mysql.connector as con

def loginUser(self, username, password):
    database = con.connect(host="localhost", user="root",
                            password="", db="embraco")
    cursor = database.cursor()
    cursor.execute("select * from users where username= '" + username +
                    "' and password= '" + password + "'")
    result = cursor.fetchone()
    if result:
        pass
        # MUDAR A WIDGET AQUI
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