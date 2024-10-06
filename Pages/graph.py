import os
from PySide2.QtWidgets import QFileDialog,  QAbstractItemView
import numpy as np
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
        model_hats = self.ui.modelHatsBox_2.currentText()
        model_head = self.ui.modelHeadBox_2.currentText()
        filename = str(self.ui.listWidget2.currentItem().text())
        self.pathname = f"{self.path}/{filename}"  
        pathExport = self.pathname
        self.ui.plot.setEnabled(True)
        if model_hats not in ("", "None") or model_head not in ("", "None"):
            self.ui.convolve.setEnabled(True)
        else: 
            self.ui.convolve.setEnabled(False)

        
    def selectMulti(self):
        global pathExport
        model_head = self.ui.modelHeadBox_2.currentText()
        model_hats = self.ui.modelHatsBox_2.currentText()
        if self.ui.checkHold.isChecked():
            self.ui.listWidget2.setSelectionMode(QAbstractItemView.MultiSelection)
        else:
            self.ui.listWidget2.setSelectionMode(QAbstractItemView.SingleSelection)       
        selected_items = self.ui.listWidget2.selectedItems()
        nSelectItems = len(selected_items)
        if nSelectItems > 2:
            self.ui.listWidget2.clearSelection()
            self.ui.plot.setEnabled(False)
            self.ui.convolve.setEnabled(False)
        elif nSelectItems == 1:
            self.ui.plot.setEnabled(True)
            filename = str(self.ui.listWidget2.currentItem().text())
            self.pathname = f"{self.path}/{filename}"  
            pathExport = self.pathname
            if model_hats not in ("", "None") or model_head not in ("", "None"):
                self.ui.convolve.setEnabled(True)
            else: 
                self.ui.convolve.setEnabled(False)
        elif nSelectItems == 2:
             self.ui.plot.setEnabled(True)
             self.ui.convolve.setEnabled(False)
             pathnames = []
             for item in selected_items:
                 filename = item.text()
                 pathname = f"{self.path}/{filename}"
                 pathnames.append(pathname)
             pathExport = pathnames

    def expandGraph(self):
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
        
        if not fileName:
            return
        image = x.grab()
        image.save(fileName)          
        
    def saveData(self):
        domain = self.gp.domainBox.currentText()
        
        # Inicializa os dados para exportação
        data_to_export = []
        num_curves = len(self.x)
        print(num_curves)
        
        # Prepara os cabeçalhos incluindo os nomes dos arquivos.
        if domain == 'Time':
            headers = ['Time [s]']
        elif domain == "Frequency":
            headers = ['Frequency [Hz]']
        if num_curves > 1:
            headers.extend(f'Amplitude ({os.path.basename(path)})' for i, path in enumerate(pathExport))
        else:
            headers.extend('Amplitude')

        # Prepara os dados de cada curva para exportação
        for i in range(num_curves):
            data_to_export.extend(zip(self.x[i], self.y[i]))
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV Files (*.csv)')

        if not fileName:
            return  

        with open(fileName, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            
            # Escreve os dados no arquivo CSV linha por linha
            for row in data_to_export:
                writer.writerow(row)
        
    # def saveData(self):
    #     domain = self.gp.domainBox.currentText()
    #     if domain == 'Time':
    #         headers = ['Amplitude []', 'Time [s]']
    #     elif domain == "Frequency":
    #         headers = ['Amplitude [Pa]', 'Frequency [Hz]']
        
    #     fileName, _ = QFileDialog.getSaveFileName(
    #         self, 'Save File', '', 'CSV Files (*.csv)')

    #     if not fileName:
    #         return
        
    #     with open(fileName, mode='w', newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow(headers)
    
    #         for x_val, y_val in zip(self.x, self.y):
    #             writer.writerow([y_val, x_val])
            
 




class GetWave():
    def __init__(self):
        super(GetWave, self).__init__()

    def getAndReadWav(self, pathExports):
        from Utils.filter_utils import FilterUtils
        from Utils.graph_utils import GraphUtils
        domain = 'Time'
        samplingBox = 'Linear'
        # Garante que pathExports seja uma lista
        if not isinstance(pathExports, list):
            pathExports = [pathExports]
        timeDataList = []
        samplingRateList = []
        for pathExport in pathExports[:2]:  # Limita a processar no máximo dois arquivos
            self.pathname = pathExport
            timeData, samplingRate = FilterUtils.getAudio(self.pathname)
            normalizedTimeData = 2 * (timeData / (2**16))
            timeDataList.append(normalizedTimeData)
            samplingRateList.append(samplingRate)
        if len(timeDataList) > 0:
            self.timeData1 = timeDataList[0]
            self.samplingRate1 = samplingRateList[0]
        if len(timeDataList) > 1:
            self.timeData2 = timeDataList[1]
            self.samplingRate2 = samplingRateList[1]
        self.timeData = timeDataList
        self.samplingRate = samplingRateList
        
        self.chartview = GraphUtils.getGraph(self, domain, samplingBox)

