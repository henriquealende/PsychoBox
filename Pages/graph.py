import os
from PySide2.QtWidgets import QFileDialog
import csv

class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()


    def importButton(self):
        importAdress = QFileDialog.getOpenFileName(self,'Open file','','WAV files (*.wav)')
        importPathname = importAdress[0]
        filename = os.path.basename(str(importPathname))
        self.path = os.path.dirname(str(importPathname))
        self.ui.listWidget2.addItem(filename)

    def selectItem(self):
        global pathExport
        filename = str(self.ui.listWidget2.currentItem().text())
        self.pathname = (self.path + '/' + filename)
        pathExport = self.pathname
        self.ui.plot.setEnabled(True)

    def expandGraph(self, type):
        from expandGraph import Expand_Graph
        self.gp = Expand_Graph()
        GetWave.getAndReadWav(self.gp, pathExport)
        self.gp.show()

    def changeGraph(self, window):
        from Utils.graph_utils import GraphUtils
        domain = self.gp.domainBox.currentText()
        samplingBox = self.gp.samplingBox.currentText()
        self.chartview = GraphUtils.getGraph(self, domain, samplingBox)

    def saveGraph(self):
        from Utils.graph_utils import chartView
        x = chartView
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Image", r"H:\Image", "Image Files (*.png *.jpg *.bmp)")
        fileName = fileName + '.png'
        image = x.grab()
        image.save(fileName)
        
    def saveData(self):
        domain = self.gp.domainBox.currentText()
        if domain == 'Time':
            headers = ['Amplitude []', 'Time [s]']
        elif domain == "Frequency":
            headers = ['Amplitude [Pa]', 'Frequency [Hz]']
        
        file_name, _ = QFileDialog.getSaveFileName(
            self, 'Salvar Arquivo', '', 'CSV Files (*.csv)')

        if not file_name:
            return
        
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    
            for x_val, y_val in zip(self.x, self.y):
                writer.writerow([y_val, x_val])
            
 




class GetWave():
    def __init__(self):
        super(GetWave, self).__init__()


    def getAndReadWav(self, pathExport):
        from Utils.filter_utils import FilterUtils
        from Utils.graph_utils import GraphUtils
        self.pathname = pathExport
        domain = 'Time'
        samplingBox = 'Linear'
        self.timeData, self.samplingRate = FilterUtils.getAudio(self.pathname)
        self.timeData = 2*(self.timeData/(2**16))
        self.chartview = GraphUtils.getGraph(self, domain, samplingBox)

