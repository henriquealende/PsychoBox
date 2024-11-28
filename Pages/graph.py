import os
from PySide6.QtWidgets import QFileDialog,  QAbstractItemView, QMessageBox, QProgressDialog
from PySide6.QtGui import QImage, QPainter
import numpy as np
import csv

from Psychoacoustics.loudness import Loudness
from Psychoacoustics.sharpness_din import Sharpnes_DIN
from Psychoacoustics.roughness import Roughness

from Utils.filter_utils import FilterUtils

loudness = Loudness()
sharpness_din = Sharpnes_DIN()
roughness = Roughness()
class UI_Buttons_Graph():
    def __init__(self):
        super(UI_Buttons_Graph, self).__init__()
        self.chartview = None
        self.gp = None  


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

    def changeGraph(self):
        from Utils.graph_utils import GraphUtils
        domain = self.gp.domainBox.currentText()
        samplingBox = self.gp.samplingBox.currentText()
        self.chartview = GraphUtils.getGraph(self, pathExport, domain, samplingBox)
        print(self.chartview)

    def saveGraph(self):
        if self.chartview is None:
            print("Erro: chartview não foi inicializado.")
            return

        fileName, fileExtension = QFileDialog.getSaveFileName(self, "Save Image", "", "Image Files (*.png *.jpg *.bmp)")
        if not fileName:
            return

        self.chartview.update()
        pixmap = self.chartview.grab()

        # Converter para QImage
        image = QImage(pixmap.size(), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(image)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        # Salvar a imagem e imprimir o resultado
        print(image.save(fileName, "PNG")) 


    def saveData(self):
        """
        Calcula as métricas psicoacústicas e salva os resultados em um arquivo .csv.
        """
        # Caixa de diálogo para salvar o arquivo
        fileName, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "CSV (*.csv)")
        if not fileName:
            return
        # Abre o arquivo CSV para escrita
        with open(fileName, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Define o cabeçalho
            headers = [
                "File", "Frequency (Bark)", 
                "Global Loudness Zwicker (sone)", "Specific Loudness Zwicker", 
                "Global Loudness ECMA", "Specific Loudness ECMA", "Global Roughness DW", 
                "Specific Roughness DW", "Global Roughness ECMA", "Specific Roughness ECMA", 
                "Global Sharpness", "Specific Sharpness"
            ]
            writer.writerow(headers)

            # Preenche os dados
            for i in range(len(self.timeData)):
                filename = os.path.basename(pathExport[i])
                timeData = self.timeData[i]
                samplingRate = self.samplingRate[i]
                
                # Calcula as métricas
                Bark, globalLoudnessZWK, specificLoudnessZWK = loudness.loudnessZWK(timeData, samplingRate)
                Bark, globalLoudnessECMA, specificLoudnessECMA = loudness.loudnessECMA(timeData, samplingRate)
                Bark, globalRoughnessECMA, specificRoughnessECMA = roughness.roughnessECMA(timeData, samplingRate)
                Bark, globalSharpness, specificSharpness = sharpness_din.sharpnessCalculation(timeData, samplingRate)
                Bark, globalRoughnessDW, specificRoughnessDW = roughness.roughnessDW(timeData, samplingRate)
                writer.writerow([filename,
                                Bark,
                                globalLoudnessZWK, specificLoudnessZWK,
                                globalLoudnessECMA, specificLoudnessECMA,
                                globalRoughnessDW, specificRoughnessDW,
                                globalRoughnessECMA, specificRoughnessECMA,
                                globalSharpness, specificSharpness])
            QMessageBox.information(self, "Data Saved", "Psychoacoustic metrics were saved successfully!")

       
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

        # Processa no máximo dois arquivos
        for pathExport in pathExports[:2]:
            self.pathname = pathExport
            timeData, samplingRate = FilterUtils.getAudio(self.pathname)
            
            # Normaliza os dados de áudio para o intervalo [-1, 1]
            normalizedTimeData = 2 * (timeData / (2**16))
            
            # Padroniza os dados para que sejam arrays 1D, caso não sejam
            if normalizedTimeData.ndim > 1:
                normalizedTimeData = normalizedTimeData.flatten()
            
            timeDataList.append(normalizedTimeData)
            samplingRateList.append(samplingRate)

        # Armazena os dados em atributos padronizados para uso posterior
        self.timeData = timeDataList
        self.samplingRate = samplingRateList
        
        # Caso queira também armazenar as duas primeiras séries de maneira separada
        if len(timeDataList) > 0:
            self.timeData1 = timeDataList[0]
            self.samplingRate1 = samplingRateList[0]
        if len(timeDataList) > 1:
            self.timeData2 = timeDataList[1]
            self.samplingRate2 = samplingRateList[1]
            
        self.chartview = GraphUtils.getGraph(self, pathExports, domain, samplingBox)

