import numpy as np
import scipy.signal

from PySide2 import  QtGui
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import  QPainter, QBrush, QPen, QColor

from Utils.filter_utils import FilterUtils
from Psychoacoustics.mpi import MPI
from Psychoacoustics.loudness_zwk import Loudness_ZWK
from Psychoacoustics.sharnpness_din import Sharpnes_DIN

mpi = MPI()
loudness_zwk = Loudness_ZWK()
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
        self.chart.setBackgroundBrush(QBrush(QColor(242, 240, 241)))
        GraphUtils.defineDomain(self, domain, samplingBox)
        pen = QPen(QtGui.QColor(0, 155, 74))
        pen.setWidth(1)
        self.series.setPen(pen)
        GraphUtils.plotGraph(self)
        #self.previous_series = self.series


    def defineDomain(self, domain, samplingBox):
        # self.plotTimeData, self.plotSamplingRate = GraphUtils.decimateAudioSignal(self)
        if domain == 'Time':
            y = self.timeData
            T = len(self.timeData)/self.samplingRate
            x = np.linspace(0, T, len(y))

            self.series = QtCharts.QLineSeries()
            for i in range(len(y)):
                self.series.append(x[i], y[i])
            self.axis_x = QtCharts.QValueAxis()
            self.axis_x.setTickCount(5)
            self.axis_x.setLabelFormat("%.2f")
            self.axis_x.setTitleText("Time [s]")
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("Amplitude")

        elif domain == 'Frequency':
            x, y, Yplot = FilterUtils.getFFT(self.timeData, self.samplingRate)
            if samplingBox == "1/3 octave":
                y = FilterUtils.getBandValue(Yplot, self.samplingRate)
                x = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
                                630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000,
                                5000, 6300, 8000, 10000])
                y = 20*np.log10(y/2e-5)


            self.series = QtCharts.QLineSeries()
            for i in range(len(y)):
                self.series.append(x[i], y[i])

            # Configuração dos eixos
            self.axis_x = QtCharts.QLogValueAxis()
            self.axis_x.setLabelFormat("%.0f")
            self.axis_x.setTitleText("Frequency [Hz]")
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("SPL [dB]")

        elif domain == 'MPI':    
            x, MPI_values = mpi.calculateMPI(self.timeData, self.samplingRate)
            y = MPI_values[0,:]
            self.series = QtCharts.QLineSeries()
            for i in range(len(y)):
                self.series.append(x[i], y[i])
            # Configuração dos eixos
            self.axis_x = QtCharts.QValueAxis()
            self.axis_x.setLabelFormat("%.0f")
            self.axis_x.setTitleText("Frequency [Bark]")
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("MPI [-]")
            
        elif domain == 'Loudness':
            x, _, y = loudness_zwk.loudnessCalculation(self.timeData, self.samplingRate)
            self.series = QtCharts.QLineSeries()
            for i in range(len(y)):
                self.series.append(x[i], y[i])
            # Configuração dos eixos
            self.axis_x = QtCharts.QValueAxis()
            self.axis_x.setLabelFormat("%.0f")
            self.axis_x.setTitleText("Frequency [Bark]")
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("Loudness [sone/Bark]")
            
        elif domain == 'Sharpness':
            x, y = sharpness_din.specificSharpnessCalculation(self.timeData, self.samplingRate)
            self.series = QtCharts.QLineSeries()
            for i in range(len(y)):
                self.series.append(x[i], y[i])
            # Configuração dos eixos
            self.axis_x = QtCharts.QValueAxis()
            self.axis_x.setLabelFormat("%.0f")
            self.axis_x.setTitleText("Frequency [Bark]")
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("Sharpness [acum/Bark]")


    def plotGraph(self):
        global chartView
        # Adiciona a série ao gráfico
        self.chart.addSeries(self.series)
        self.chart.setAxisX(self.axis_x, self.series)
        self.chart.setAxisY(self.axis_y, self.series)
        self.chart.createDefaultAxes()  # Isso automaticamente configura os eixos X e Y baseados na série adicionada
        
        # Adiciona o gráfico à visualização
        chartView = QtCharts.QChartView(self.chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
        chartView.repaint() 
        return chartView


    # def decimateAudioSignal(self):
    #     newSamplingRate = self.samplingRate/4
    #     decimation_factor = int(self.samplingRate / newSamplingRate)
    #     cutoff = newSamplingRate / 2
    #     normalized_cutoff = cutoff / (self.samplingRate / 2)
    #     b, a = scipy.signal.butter(8, normalized_cutoff, btype='lowpass')
    #     audio_signal_filtered = scipy.signal.filtfilt(b, a, self.timeData)
    #     decimated_signal = audio_signal_filtered[::decimation_factor]
    #     return (decimated_signal, newSamplingRate)




