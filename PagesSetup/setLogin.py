class SetLogin():
    def __init__(self):
        super(SetLogin, self).__init__()

    def windowLayout(self, parameter):
        if parameter == "maximazed":
            self.ui.settingLogin.setMinimumSize(0, 400)
            self.ui.loginFrame.setMinimumSize(350, 200)
            self.ui.frame_8.setMinimumSize(16777215, 20)
            self.ui.label_50.setMinimumSize(150, 150)
            self.ui.label_50.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_47.setMinimumSize(150, 150)
            self.ui.label_47.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_32.setMinimumSize(150, 150)
            self.ui.label_32.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")

        else:
            self.ui.settingLogin.setMinimumSize(0, 250)
            self.ui.frame_8.setMinimumSize(0, 0)
            self.ui.loginFrame.setMinimumSize(350, 150)
            self.ui.label_50.setMinimumSize(100, 100)
            self.ui.label_50.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_47.setMinimumSize(100, 100)
            self.ui.label_47.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
            self.ui.label_32.setMinimumSize(100, 100)
            self.ui.label_32.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                            "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
