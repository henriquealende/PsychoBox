import os

from PySide2.QtWidgets import (QFileDialog)
##############################################################################


class UI_Buttons_Cali():
    def __init__(self):
        super(UI_Buttons_Cali, self).__init__()

    def changeTypeHead(self):
        type = self.ui.typeHeadBox_2.currentText()
        if type == "Sennheiser":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHeadBox_2.addItems(['HD 600', 'HD 450X', 'HD 650'])
            self.ui.modelHeadBox_2.setEnabled(True)
        else:
            self.ui.modelHeadBox_2.clear()
            self.ui.modelHeadBox_2.setEnabled(False)

    def changeTypeHats(self):
        type = self.ui.typeHatsBox_2.currentText()
        if type == "HeadAcoustics":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.addItems(['HMS III.2', 'HMS III'])
            self.ui.modelHatsBox_2.setEnabled(True)
        elif type == "GRASS":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.addItems(['Kemar'])
            self.ui.modelHatsBox_2.setEnabled(True)
        else:
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.setEnabled(False)

    def changeModelHead(self):
        type = self.ui.modelHeadBox_2.currentText()
        print(type)
        if type == "HD 600":
            dados = '123'
            print(dados)

        elif type == "HD 450X":
            dados = '123'
            print(dados)

        elif type == "HD 650":
            dados = '123'
            print(dados)
        else:
            dados = '123'
            print(dados)

    def changeModelHats(self):
        pass





