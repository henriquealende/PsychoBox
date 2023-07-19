from new_project import *
from Database.database import *
##############################################################################


class UI_Buttons_GeneralFunctions():
    def __init__(self):
        super(UI_Buttons_GeneralFunctions, self).__init__()

#LOGIN PAGE
    def login(self):
        username = self.ui.loginLineEdit.text()
        password = self.ui.passwordLlineEdit.text()
        loginUser(self, username, password)


    def register(self):
        username = self.ui.loginLineEdit.text()
        password = self.ui.passwordLlineEdit.text()
        registerUser(self, username, password)


#NEW PROJECT
    def newProject(self):
        self.np = New_Project_Widget()
        self.np.show()

    def applyProject(self, main):
        global projects
        project_name = self.np.projectLineEdit.text()
        projects.append(project_name)
        self.close()


    def refresh(self):
        global projects
        self.ui.project1.setText(projects[0])
        print(len(projects))

