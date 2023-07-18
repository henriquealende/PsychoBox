import pandas as pd

from expandGraph import *
from Database.database import *
from Utils.graph_utils import *
from Utils.filter_utils import *   
from Utils.general_utils import *
##############################################################################

class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()
        
    def graphButton(self):
        if self.online:
            self.ui.rightContent.setCurrentWidget(self.ui.graphPage)
            
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

    def automaticCheckBox(self, window):
        if window == "defaut":
            domain = self.ui.domainBox.currentText()
            if self.ui.automaticCheckBox.isChecked():
                self.ui.spinBox.setDisabled(True)
                self.ui.spinBox_2.setDisabled(True)
                self.ui.spinBox_3.setDisabled(True)
                self.ui.spinBox_4.setDisabled(True)
                self.ui.spinBox.setValue(0)
                self.ui.spinBox_2.setValue(99000)
                self.ui.spinBox_3.setValue(0)
                self.ui.spinBox_4.setValue(99000)
            else:                
                self.ui.spinBox.setEnabled(True)
                self.ui.spinBox_2.setEnabled(True)
                self.ui.spinBox_3.setEnabled(True)
                self.ui.spinBox_4.setEnabled(True)
                if domain == 'Time':
                    self.ui.spinBox.setValue(-1)
                    self.ui.spinBox_2.setValue(1)
                    self.ui.spinBox_3.setValue(0)
                    self.ui.spinBox_4.setValue(10)
                elif domain == "Frequency":
                    self.ui.spinBox.setValue(0)
                    self.ui.spinBox_2.setValue(80)
                    self.ui.spinBox_3.setValue(20)
                    self.ui.spinBox_4.setValue(10000)
        else:
            domain = self.gp.domainBox.currentText()
            if self.gp.automaticCheckBox.isChecked():                
                self.gp.frame_axis.hide()
            else:
                self.gp.frame_axis.show()
                if domain == 'Time':
                    self.gp.spinBox.setValue(-1)
                    self.gp.spinBox_2.setValue(1)
                    self.gp.spinBox_3.setValue(0)
                    self.gp.spinBox_4.setValue(10)
                elif domain == "Frequency":
                    self.gp.spinBox.setValue(0)
                    self.gp.spinBox_2.setValue(80)
                    self.gp.spinBox_3.setValue(20)
                    self.gp.spinBox_4.setValue(10000)

    def importButton(self):
        global path
        importAdress = QFileDialog.getOpenFileName(self,'Open file','','WAV files (*.wav)')
        importPathname = importAdress[0]
        filename = os.path.basename(str(importPathname))
        path = os.path.dirname(str(importPathname))        
        self.ui.listWidget2.addItem(filename)
        

    def selectItem(self):
        global path, pathExport   
        metrics = self.ui.mainBox.currentText()
        domain = self.ui.domainBox.currentText()
        samplingBox = self.ui.samplingBox.currentText()
#        print(metrics, domain, samplingBox)
        presetImport(self, domain)
        filename = str(self.ui.listWidget2.currentItem().text())  
        self.pathname = (path + '/' + filename)
        print(self.pathname)
        selectMulti(self, metrics, domain, samplingBox) 
        pathExport = self.pathname   

        
    def changeGraph(self, window):
        print(1)
        metrics = self.gp.mainBox.currentText()
        domain = self.gp.domainBox.currentText()
        samplingBox = self.gp.samplingBox.currentText()
        self.chartview = getGraph(self, metrics, domain, samplingBox, type ='plot', window='expand')


    def getPathname(self):
        return pathExport
    
    def expandGraph(self, type):
        dados = ['metrics', 'domain', 'samplingBox']
        dados[0] = self.ui.mainBox.currentText()
        dados[1] = self.ui.domainBox.currentText()
        dados[2] = self.ui.samplingBox.currentText()
        self.gp = Expand_Graph(dados, type)
        self.gp.show()

    def showSettings(self, x):
        if x == 'show':
            self.gp.frame_21.show()
            self.gp.pushButton2.hide()
            self.gp.pushButton2_2.show()
        else:
            self.gp.frame_21.hide()
            self.gp.pushButton2.show()
            self.gp.pushButton2_2.hide()




    def saveGraph(self, window):
        from Utils.graph_utils import chartView
        #global chartView
        x = chartView
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save Image", r"H:\Image", "Image Files (*.png *.jpg *.bmp)")
        fileName = fileName + '.png'
        image = x.grab()
        #image.scaled(1000, 1000)
        image.save(fileName)


#    def saveData(self):
#        from Utils.graph_utils import x, y
#        lista_xy = list(zip(x, y))
#        df = pd.DataFrame(lista_xy, columns=['x', 'y'])
#        name = QFileDialog.getSaveFileName(self, 'Save File', filter='*.csv')
#        df.to_csv(name[0], index = False, sep = ";")

