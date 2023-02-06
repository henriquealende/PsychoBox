from expandGraph import *

from Database.database import *
from Utils.graph_utils import *
from Utils.utils import *   

import pandas as pd

class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()


    def selectGraph(self):
        condition = self.ui.mainBox.currentText()
        if condition != 'Time-Frequency':
            self.ui.domainBox.setDisabled(True)
            self.ui.samplingBox.setDisabled(True)
            self.ui.automaticCheckBox.setDisabled(True)
            self.ui.automaticCheckBox.setChecked(True)
            self.ui.spinBox.setDisabled(True)
            self.ui.spinBox_2.setDisabled(True)
            self.ui.spinBox_3.setDisabled(True)
            self.ui.spinBox_4.setDisabled(True)
            self.ui.applyButton.setDisabled(False)
        elif condition == 'Time-Frequency':
            self.ui.domainBox.setEnabled(True)
            self.ui.domainBox.setCurrentIndex(0)
            self.ui.samplingBox.setEnabled(False)
            self.ui.samplingBox.setCurrentIndex(0)
            self.ui.automaticCheckBox.setEnabled(True)
            self.ui.automaticCheckBox.setChecked(True)
            self.ui.applyButton.setEnabled(True)

    def selectDomain(self, window):
        if window == "defaut":
            domain = self.ui.domainBox.currentText()
            if domain == "Time":
                self.ui.samplingBox.setDisabled(True)
            elif domain == "Frequency":
                self.ui.samplingBox.setEnabled(True)
        else:
            domain = self.gp.domainBox.currentText()
            if domain == "Time":
                self.gp.frame_samplingBox.hide()
            else:
                self.gp.frame_samplingBox.show()

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
        global path, pathname
        self.ui.mainBox.setCurrentIndex(0)

        metrics = self.ui.mainBox.currentText()
        domain = self.ui.domainBox.currentText()
        samplingBox = self.ui.samplingBox.currentText()

        if domain == "Time":
            self.ui.domainBox.setCurrentIndex(0)
            self.ui.domainBox.setEnabled(True)
            #self.ui.samplingBox.setCurrentIndex(0)
            self.ui.samplingBox.setEnabled(False)
            self.ui.automaticCheckBox.setEnabled(True)
            self.ui.automaticCheckBox.setChecked(True)
            self.ui.applyButton.setEnabled(True)

        filename = str(self.ui.listWidget2.currentItem().text())
        self.timeVector, self.samplingRate = read_wav(path + '/' + filename)
        self.timeVector = 2*(self.timeVector/(2**16))
        self.ui.expandGraph.setEnabled(True)

        self.chartview = getGraph(self, self.timeVector, self.samplingRate, metrics, domain, samplingBox, window = "default")
        pathname = (path + '/' + filename)
    
    def getAndReadWav(self):
        #from main import Main_Window
        #main = Main_Window()
        #pathname = main.getPath()
        global pathname
        metrics = self.gp.mainBox.currentText()
        domain = self.gp.domainBox.currentText()
        samplingBox = self.gp.samplingBox.currentText()
        self.timeVector, self.samplingRate = read_wav(pathname)
        self.timeVector = 2*(self.timeVector/(2**16))
        self.chartview = getGraph(self, self.timeVector, self.samplingRate, metrics, domain, samplingBox, window = "expand")

#    def getPathname(self):
#        global pathname
#        return pathname

#    def changeGraph(self):
#        metrics = self.ui.mainBox.currentText()
#        domain = self.ui.domainBox.currentText()
#        samplingBox = self.ui.samplingBox.currentText()
#        self.chartview = getGraph(self, self.timeVector, self.samplingRate, metrics, domain, samplingBox, window = "default")

    def expandGraph(self):
        self.gp = Expand_Graph()
        self.gp.show()

    def saveGraph(self, window):
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save Image", r"H:\Image", "Image Files (*.png *.jpg *.bmp)")
        fileName = fileName + '.png'
        image = self.chartview.grab()

        if window == "default":
            image = image.scaled(800, 800)
            image.save(fileName)

        else:
            image.save(fileName)

    def saveData(self):
        from Utils.graph_utils import x, y
        lista_xy = list(zip(x, y))
        df = pd.DataFrame(lista_xy, columns=['x', 'y'])

        name = QFileDialog.getSaveFileName(self, 'Save File', filter='*.csv')
        df.to_csv(name[0], index = False, sep = ";")

#    def changeDomainExpand(self):
 #       domain = self.gp.domainBox.currentText()
  #      self.chartview = getGraph(self, self.timeVector, self.samplingRate, domain = domain, window = "expand")
