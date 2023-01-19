from main import *
from Database.database import *



class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()

    def selectGraph(self):
        # print(self.ui.comboBox.currentText())
        # PENSAR EM CASE
        condition = self.ui.mainBox.currentText()
        if condition != 'Tempo-Frequência':
            self.ui.domainBox.setDisabled(True)
            self.ui.comboBox_3.setDisabled(True)
            self.ui.automaticCheckBox.setDisabled(True)
            self.ui.spinBox.setDisabled(True)
            self.ui.spinBox_2.setDisabled(True)
            self.ui.spinBox_3.setDisabled(True)
            self.ui.spinBox_4.setDisabled(True)
            self.ui.applyButton.setDisabled(True)
        elif condition == 'Tempo-Frequência':
            self.ui.domainBox.setEnabled(True)
            self.ui.comboBox_3.setEnabled(True)
            self.ui.automaticCheckBox.setEnabled(True)
            self.ui.automaticCheckBox.setChecked(True)
            self.ui.applyButton.setEnabled(True)

    def automaticCheckBox(self):
        if self.ui.automaticCheckBox.isChecked():
            self.ui.spinBox.setDisabled(True)
            self.ui.spinBox_2.setDisabled(True)
            self.ui.spinBox_3.setDisabled(True)
            self.ui.spinBox_4.setDisabled(True)
        else:
            self.ui.spinBox.setEnabled(True)
            self.ui.spinBox_2.setEnabled(True)
            self.ui.spinBox_3.setEnabled(True)
            self.ui.spinBox_4.setEnabled(True)

    def graphButton(self):
        if self.online:
            self.ui.rightContent.setCurrentWidget(self.ui.graphPage)
