from PySide6 import QtCharts
from PySide6.QtGui import QPainter, QColor, QBrush, QPen
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, QRectF, QPointF

from Utils.filter_utils import FilterUtils
import numpy as np
from tqdm import tqdm
import os

from Psychoacoustics.loudness import Loudness
from Psychoacoustics.sharpness_din import Sharpnes_DIN
from Psychoacoustics.roughness import Roughness

loudness = Loudness()
sharpness_din = Sharpnes_DIN()
roughness = Roughness()

class CustomChartView(QtCharts.QChartView):
    def __init__(self, chart, parent=None, gp=None):
        super().__init__(chart, parent)
        self.setMouseTracking(True)
        self.start_pos = None
        self.end_pos = None
        self.selection_rect = None  # Retângulo gráfico para a seleção
        self.gp = gp  # Referência à interface gráfica (Ui_Form)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Verifica se o botão "select_area" está checado
            if self.gp and not self.gp.select_area.isChecked():
                return  # Não faz nada se o botão não estiver checado

            # Captura a posição inicial do clique
            self.start_pos = self.chart().mapToValue(event.scenePosition())
            self.selection_rect = QRectF()  # Inicializa o retângulo de seleção

    def mouseMoveEvent(self, event):
        if self.start_pos:
            self.end_pos = self.chart().mapToValue(event.scenePosition())

            # Calcula as coordenadas do retângulo no plotArea
            x1, x2 = sorted([self.start_pos.x(), self.end_pos.x()])
            plot_area = self.chart().plotArea()
            y1 = plot_area.top()
            y2 = plot_area.bottom()

            # Atualiza o retângulo de seleção
            self.selection_rect = QRectF(
                self.chart().mapToPosition(QPointF(x1, 0)).x(),
                y1,
                self.chart().mapToPosition(QPointF(x2, 0)).x() - self.chart().mapToPosition(QPointF(x1, 0)).x(),
                y2 - y1
            )
            self.viewport().update()  # Atualiza a exibição para desenhar o retângulo

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.start_pos:
            self.end_pos = self.chart().mapToValue(event.scenePosition())
            x1, x2 = sorted([self.start_pos.x(), self.end_pos.x()])

            # Save x1 and x2 to self for later use
            self.selected_x1 = x1
            self.selected_x2 = x2

            # Enable or disable the windowButton based on the selection
            if self.gp and hasattr(self.gp, 'windowButton'):
                if self.selected_x1 == self.selected_x2:
                    self.gp.windowButton.setEnabled(False)  # Disable if no region is selected
                else:
                    self.gp.windowButton.setEnabled(True)  # Enable if a region is selected

            # Reset selection
            self.start_pos = None
            self.end_pos = None
            self.viewport().update()  # Update the viewport to remove the rectangle

    def paintEvent(self, event):
        super().paintEvent(event)

        # Draw the selection rectangle, if it exists
        if self.selection_rect and not self.selection_rect.isNull():
            painter = QPainter(self.viewport())
            painter.setPen(QPen(QColor("#f16637"), 2))  # Border color: #f16637
            painter.setBrush(QBrush(QColor(241, 102, 55, 50)))  # Fill color: #f16637 with transparency
            painter.drawRect(self.selection_rect)


class GraphUtils():
    def __init__(self):
        super(GraphUtils, self).__init__()
               
    def getGraph(self, pathExports, domain, samplingBox):
        
        self.chart = QtCharts.QChart()
        self.chart.removeAllSeries()
        self.chart.legend().show()
        self.chart.setBackgroundRoundness(12.0)
        self.chart.setDropShadowEnabled(True)
        self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)
        self.chart.setBackgroundBrush(QColor(242, 240, 241)) 
        self.x, self.y = GraphUtils.defineDomain(self, pathExports, domain, samplingBox)      
        chartView = GraphUtils.plotGraph(self) 
        return chartView 

    def defineDomain(self, pathExports, domain, samplingBox):
        x_list = []
        y_list =[]
        colors = [QColor("#50b89e"), QColor(241, 102, 55)] # Lista de cores para as séries
        for timeData, samplingRate, color, pathExport in tqdm(zip(self.timeData, self.samplingRate, colors, pathExports), total=len(self.timeData), desc="Processing data"):
            if domain == 'Time':
                y = timeData
                T = len(timeData) / samplingRate
                x = np.linspace(0, T, len(y))
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  # Usa zip para garantir que xi e yi sejam escalares
                    self.series.append(float(xi), float(yi))  # Converte xi e yi em float para garantir compatibilidade
                filename = os.path.basename(pathExport)
                self.series.setName(filename)  
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Time [s]", "Amplitude")
                
            elif domain == 'Frequency':
                x, y, Yplot = FilterUtils.getFFT(timeData, samplingRate)
                if samplingBox == "1/3 octave":
                    y = FilterUtils.getBandValue(Yplot, samplingRate)
                    x = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
                                630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000,
                                5000, 6300, 8000, 10000])
                    y = 20*np.log10(y/2e-5)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  # Usa zip para garantir que xi e yi sejam escalares
                    self.series.append(float(xi), float(yi))  # Converte xi e yi em float para garantir compatibilidade
                filename = os.path.basename(pathExport)
                self.series.setName(filename)  
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Hz]", "SPL [dB]")
                
            # elif domain == 'IPM':    
            #     x, MPI_values = mpi.calculateMPI(timeData, samplingRate)
            #     y = MPI_values[0,:]
            #     self.series = QtCharts.QLineSeries()
            #     for xi, yi in zip(x, y):  
            #         self.series.append(float(xi), float(yi)) 
            #     self.series.setColor(color)
            #     self.chart.addSeries(self.series)
            #     GraphUtils.configureAxes(self, "Frequency [Bark]", "IPM [dB/Bark]")
                
            elif domain == 'Loudness Zwicker':
                x, _, y = loudness.loudnessZWK(timeData, samplingRate)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                filename = os.path.basename(pathExport)
                self.series.setName(filename)      
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark]", "Loudness [sone/Bark]")
                
            elif domain == 'Loudness ECMA':
                x, _, y = loudness.loudnessECMA(timeData, samplingRate)
                y = np.mean(y, axis=1)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                filename = os.path.basename(pathExport)
                self.series.setName(filename) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark HMS]", "Loudness [sone/Bark HMS]")
            
            elif domain == 'Sharpness DIN':
                x, _, y = sharpness_din.sharpnessCalculation(timeData, samplingRate)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                filename = os.path.basename(pathExport)
                self.series.setName(filename) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark]", "Sharpness [acum/Bark]")
    
            elif domain == 'Roughness DW':
                x, _, y = roughness.roughnessDW(timeData, samplingRate)
                y = np.mean(y, axis=1)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                filename = os.path.basename(pathExport)
                self.series.setName(filename) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark]", "Roughness [vacil/Bark]")            
                
            elif domain == 'Roughness ECMA':
                x, _, y = roughness.roughnessECMA(timeData, samplingRate)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                filename = os.path.basename(pathExport)
                self.series.setName(filename)     
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark HMS]", "Roughness [vacil/Bark HMS]")            
            
            x_list.append(x)
            y_list.append(y)  
        return(x_list, y_list)   
          
    def configureAxes(self, x_title, y_title):
        # Remove eixos antigos para evitar sobreposição
        for axis in self.chart.axes(Qt.Horizontal):
            self.chart.removeAxis(axis)
        for axis in self.chart.axes(Qt.Vertical):
            self.chart.removeAxis(axis)

        # Configuração unificada dos eixos
        axis_x = QtCharts.QValueAxis()
        axis_x.setTickCount(5)
        axis_x.setLabelFormat("%.1f")
        axis_x.setTitleText(x_title)            
        axis_y = QtCharts.QValueAxis()
        axis_y.setTitleText(y_title) 
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.1f")       
        
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        
        for series in self.chart.series():
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)

    def plotGraph(self):
        # self.chart.createDefaultAxes()  # Configura os eixos X e Y baseados nas séries adicionadas
        if not self.gp.automaticCheckBox.isChecked():
            try:
                x_min = float(self.gp.x_min.text())
                x_max = float(self.gp.x_max.text())
                y_min = float(self.gp.y_min.text())
                y_max = float(self.gp.y_max.text())

                # Remova eixos antigos para evitar conflitos
                for axis in self.chart.axes():
                    self.chart.removeAxis(axis)

                # Crie novos eixos
                axis_x = QtCharts.QValueAxis()
                axis_x.setRange(x_min, x_max)
                axis_x.setTitleText("X-Axis")  # Substitua pelo título desejado
                self.chart.addAxis(axis_x, Qt.AlignBottom)

                axis_y = QtCharts.QValueAxis()
                axis_y.setRange(y_min, y_max)
                axis_y.setTitleText("Y-Axis")  # Substitua pelo título desejado
                self.chart.addAxis(axis_y, Qt.AlignLeft)

                # Associe os eixos às séries existentes
                for series in self.chart.series():
                    series.attachAxis(axis_x)
                    series.attachAxis(axis_y)

            except ValueError:
                # Exibe uma mensagem de erro se os valores não forem válidos
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Invalid Input")
                msg.setText("Please enter valid numeric values for the axis limits.")
                msg.exec()
                return  # Sai da função para evitar erros adicionais

        # Substitua QChartView por CustomChartView
        chartView = CustomChartView(self.chart, gp=self.gp)
        chartView.setRenderHint(QPainter.Antialiasing)  # Habilita o antialiasing para melhor qualidade visual
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
        chartView.repaint()  # Força a repintura para atualizar o gráfico
        return chartView

