

class UI_Buttons_Cali():
    def __init__(self):
        super(UI_Buttons_Cali, self).__init__()

    def changeTypeHead(self):
        type = self.ui.typeHeadBox.currentText()
        if type == "Sennheiser":
            self.ui.modelHatsBox.clear()
            self.ui.modelHeadBox.addItems(['HD 600', 'HD 450X', 'HD 650'])
            self.ui.modelHeadBox.setEnabled(True)
        else:
            self.ui.modelHeadBox.clear()
            self.ui.modelHeadBox.setEnabled(False)

    def changeTypeHats(self):
        type = self.ui.typeHatsBox.currentText()
        if type == "HeadAcoustics":
            self.ui.modelHatsBox.clear()
            self.ui.modelHatsBox.addItems(['HMS III.2', 'HMS III'])
            self.ui.modelHatsBox.setEnabled(True)
        elif type == "GRASS":
            self.ui.modelHatsBox.clear()
            self.ui.modelHatsBox.addItems(['Kemar'])
            self.ui.modelHatsBox.setEnabled(True)
        else:
            self.ui.modelHatsBox.clear()
            self.ui.modelHatsBox.setEnabled(False)

