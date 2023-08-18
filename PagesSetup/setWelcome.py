class SetWelcome():
    def __init__(self):
        super(SetWelcome, self).__init__()

    def windowLayout(self, parameter):
        if parameter == "maximazed":
            self.ui.frame_17.setMinimumSize(0, 100)
            self.ui.welcomeUser.setMinimumSize(0, 140)
            self.ui.welcome.setMinimumSize(0, 60)
            self.ui.logo_2.setMinimumSize(150, 75)
            self.ui.newProject.setMinimumSize(0, 420)
            self.ui.settings.setMinimumSize(0, 400)
            self.ui.label_41.setMinimumSize(150, 150)
            self.ui.label_41.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_35.setMinimumSize(150, 150)
            self.ui.label_35.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_38.setMinimumSize(150, 150)
            self.ui.label_38.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")

        else:
            self.ui.frame_17.setMinimumSize(0, 100)
            self.ui.welcomeUser.setMinimumSize(464, 80)
            self.ui.welcome.setMinimumSize(0, 50)
            self.ui.logo_2.setMinimumSize(100, 50)
            self.ui.newProject.setMinimumSize(0, 120)
            self.ui.settings.setMinimumSize(0, 250)
            self.ui.label_41.setMinimumSize(100, 100)
            self.ui.label_41.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_35.setMinimumSize(100, 100)
            self.ui.label_35.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_38.setMinimumSize(100, 100)
            self.ui.label_38.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
