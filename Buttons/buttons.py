from widget import *
from Database.database import *

class UI_Buttons():
    def __init__(self):
        super(UI_Buttons, self).__init__()

    # GLOBAL BUTTONS
    def closeAll(self):
        self.close()

    def login(self):
        username = self.ui.loginLineEdit.text()
        password = self.ui.passwordLlineEdit.text()
        loginUser(self, username, password)


    def register(self):
        username = self.ui.loginLineEdit.text()
        password = self.ui.passwordLlineEdit.text()
        registerUser(self, username, password)
        







