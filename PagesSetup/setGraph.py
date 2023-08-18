class SetGraph():
    def __init__(self):
        super(SetGraph, self).__init__()

    def windowLayout(self, parameter):
        if parameter == "maximazed":
            self.gp.infoBar3.setMinimumSize(16777215, 70)
            self.gp.frame_21.setMinimumSize(400, 16777215)
            self.gp.minimizeButton.setMaximumSize(24, 24)
            self.gp.closeAllButton.setMaximumSize(24, 24)
            self.gp.maximizeButton.setMaximumSize(24, 24)
            self.gp.frameButtons.setMinimumSize(150, 30)
            self.gp.frameButtons.setStyleSheet(u"QPushButton {border-radius: 12px}")

        else:
            self.gp.infoBar3.setMinimumSize(16777215, 50)
            self.gp.frame_21.setMinimumSize(250, 16777215)
            self.gp.minimizeButton.setMaximumSize(20, 20)
            self.gp.closeAllButton.setMaximumSize(20, 20)
            self.gp.maximizeButton.setMaximumSize(20, 20)
            self.gp.frameButtons.setMinimumSize(120, 30)
            self.gp.frameButtons.setStyleSheet(u"QPushButton {border-radius: 10px}")
