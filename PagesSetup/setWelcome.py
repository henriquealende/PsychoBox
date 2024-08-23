class SetWelcome():
    def __init__(self):
        super(SetWelcome, self).__init__()

    def windowLayout(self, parameter):
        if parameter == "maximazed":
            self.ui.frame_17.setMinimumSize(0, 100)
            self.ui.welcomeUser.setMinimumSize(0, 140)
            self.ui.welcome.setMinimumSize(0, 60)
            self.ui.logo_2.setMinimumSize(600, 250)
            self.ui.settings.setMinimumSize(0, 400)
           

        else:
            self.ui.frame_17.setMinimumSize(0, 100)
            self.ui.welcomeUser.setMinimumSize(464, 80)
            self.ui.welcome.setMinimumSize(0, 50)
            self.ui.logo_2.setMinimumSize(300, 125)
            self.ui.settings.setMinimumSize(0, 250)           
         