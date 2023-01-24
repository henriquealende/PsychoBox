from main import *
from Database.database import *
from Utils.graph_utils import *
from Utils.utils import *   
class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()

    def selectGraph(self):
        condition = self.ui.mainBox.currentText()
        if condition != 'Time-Frequency':
            self.ui.domainBox.setDisabled(True)
            self.ui.samplingBox.setDisabled(True)
            self.ui.automaticCheckBox.setDisabled(True)
            self.ui.spinBox.setDisabled(True)
            self.ui.spinBox_2.setDisabled(True)
            self.ui.spinBox_3.setDisabled(True)
            self.ui.spinBox_4.setDisabled(True)
            self.ui.applyButton.setDisabled(True)
        elif condition == 'Time-Frequency':
            self.ui.domainBox.setEnabled(True)
            self.ui.samplingBox.setEnabled(True)
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
            
    def importButton(self):
        global path
        importAdress = QFileDialog.getOpenFileName(self,'Open file','','WAV files (*.wav)')
        importPathname = importAdress[0]
        filename = os.path.basename(str(importPathname))
        path = os.path.dirname(str(importPathname))
        self.ui.listWidget2.addItem(filename)

    def selectItem(self):
        global path
        self.ui.mainBox.setCurrentIndex(0)
        self.ui.domainBox.setCurrentIndex(0)
        self.ui.domainBox.setEnabled(True)
        self.ui.samplingBox.setCurrentIndex(0)
        self.ui.samplingBox.setEnabled(True)
        self.ui.automaticCheckBox.setEnabled(True)
        self.ui.automaticCheckBox.setChecked(True)
        self.ui.applyButton.setEnabled(True)

        filename = str(self.ui.listWidget2.currentItem().text())
        print(path + '/' + filename)
        self.timeVector, self.samplingRate = read_wav(path + '/' + filename)
        domain = self.ui.domainBox.currentText()
        getGraph(self, self.timeVector, self.samplingRate, domain) 

    def exportData(self):
        pass
