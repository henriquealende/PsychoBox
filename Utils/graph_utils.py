
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import  QPainter, QColor
from PySide2.QtCore import Qt

from Utils.filter_utils import FilterUtils
import numpy as np

from Psychoacoustics.mpi import IPM
from Psychoacoustics.loudness import Loudness
from Psychoacoustics.sharpness_din import Sharpnes_DIN

mpi = IPM()
loudness = Loudness()
sharpness_din = Sharpnes_DIN()

class GraphUtils():
    def __init__(self):
        super(GraphUtils, self).__init__()
        
    def getGraph(self, domain, samplingBox):
        self.chart = QtCharts.QChart()
        self.chart.removeAllSeries()
        self.chart.legend().hide()
        self.chart.setBackgroundRoundness(12.0)
        self.chart.setDropShadowEnabled(True)
        self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)
        self.chart.setBackgroundBrush(QColor(242, 240, 241))        
        self.x, self.y = GraphUtils.defineDomain(self, domain, samplingBox)      
        GraphUtils.plotGraph(self)
        
        

    def defineDomain(self, domain, samplingBox):
        x_list = []
        y_list =[]
        colors = [QColor("#009b4a"), QColor(241, 102, 55)] # Lista de cores para as séries
        for timeData, samplingRate, color in zip(self.timeData, self.samplingRate, colors):
            if domain == 'Time':
                y = timeData
                T = len(timeData) / samplingRate
                x = np.linspace(0, T, len(y))
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  # Usa zip para garantir que xi e yi sejam escalares
                    self.series.append(float(xi), float(yi))  # Converte xi e yi em float para garantir compatibilidade
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
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Hz]", "SPL [dB]")
                
            elif domain == 'IPM':    
                x, MPI_values = mpi.calculateMPI(timeData, samplingRate)
                y = MPI_values[0,:]
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark]", "IPM [dB/Bark]")
                
            elif domain == 'Loudness Zwicker':
                x, _, y = loudness.loudnessZWK(timeData, samplingRate)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark]", "Loudness [sone/Bark]")
                
            elif domain == 'Loudness ECMA':
                x, _, y = loudness.loudnessECMA(timeData, samplingRate)
                y = np.mean(y, axis=1)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark HMS]", "Loudness [sone/Bark HMS]")
            
            elif domain == 'Sharpness':
                x, y = sharpness_din.specificSharpnessCalculation(timeData, samplingRate)
                self.series = QtCharts.QLineSeries()
                for xi, yi in zip(x, y):  
                    self.series.append(float(xi), float(yi)) 
                self.series.setColor(color)
                self.chart.addSeries(self.series)
                GraphUtils.configureAxes(self, "Frequency [Bark]", "Sharpness [acum/Bark]")
            x_list.append(x)
            y_list.append(y)  
        return(x_list, y_list)   
          
    def configureAxes(self, x_title, y_title):
        # Configuração unificada dos eixos
        axis_x = QtCharts.QValueAxis()
        axis_x.setTickCount(5)
        axis_x.setLabelFormat("%.2f")
        axis_x.setTitleText(x_title) 
        axis_y = QtCharts.QValueAxis()
        axis_y.setTitleText(y_title) 
        axis_y.setTickCount(5)
        axis_y.setLabelFormat("%.2f")
       
        
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self.chart.addAxis(axis_y, Qt.AlignLeft)
       
        for series in self.chart.series():
            series.attachAxis(axis_x)
            series.attachAxis(axis_y)

    def plotGraph(self):
        #self.chart.createDefaultAxes()  # Configura os eixos X e Y baseados nas séries adicionadas
        chartView = QtCharts.QChartView(self.chart)
        chartView.setRenderHint(QPainter.Antialiasing)  # Habilita o antialiasing para melhor qualidade visual
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
        chartView.repaint()  # Força a repintura para atualizar o gráfico
        return chartView
    