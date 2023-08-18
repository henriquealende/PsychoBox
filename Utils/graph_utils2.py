import numpy as np
import scipy.signal

from PySide2.QtCharts import QtCharts
from PySide2.QtGui import  QPainter



from Utils.filter_utils import FilterUtils


class GraphUtils(QObject):

    def __init__(self, widget, domain, samplingBox):
        super().__init__()
        self.widget = widget
        self.domain = domain
        self.samplingBox = samplingBox

    def run(self):
        self.getGraph(self.domain, self.samplingBox)

#class GraphUtils():
#    def __init__(self):
#        super(GraphUtils, self).__init__()

    def getGraph(self, domain, samplingBox):
        self.chart = QtCharts.QChart()
        GraphUtils.defineDomain(self, domain, samplingBox)
        GraphUtils.plotGraph(self)


    def defineDomain(self, domain, samplingBox):
        self.plotTimeData, self.plotSamplingRate = GraphUtils.decimateAudioSignal(self)
        if domain == 'Time':
            y = self.plotTimeData
            T = len(self.plotTimeData)/self.plotSamplingRate
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


    def plotGraph(self):
        global chartView
        # Adiciona a série ao gráfico
        self.chart.addSeries(self.series)
        self.chart.setAxisX(self.axis_x, self.series)
        self.chart.setAxisY(self.axis_y, self.series)
        # Adiciona o gráfico à visualização
        chartView = QtCharts.QChartView(self.chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
        return chartView


    def decimateAudioSignal(self):
        newSamplingRate = self.samplingRate/4
        decimation_factor = int(self.samplingRate / newSamplingRate)
        cutoff = newSamplingRate / 2
        normalized_cutoff = cutoff / (self.samplingRate / 2)
        b, a = scipy.signal.butter(8, normalized_cutoff, btype='lowpass')
        audio_signal_filtered = scipy.signal.filtfilt(b, a, self.timeData)
        decimated_signal = audio_signal_filtered[::decimation_factor]
        return (decimated_signal, newSamplingRate)






###############################################################################################################
################################## NÃO ESTÃO SENDO CHAMADAS AINDA #############################################
    def limitsAdjust(self, domain, LIM):
        automaticCheckBox = self.gp.automaticCheckBox
        spinBox = self.gp.spinBox
        spinBox_2 = self.gp.spinBox_2
        spinBox_3 = self.gp.spinBox_3
        spinBox_4 = self.gp.spinBox_4
        if domain == "Time":
            if automaticCheckBox.isChecked():
                self.axis_x.setRange(0, LIM)
                self.axis_y.setRange(-1, 1)
            else:
                xlim_inf = spinBox_3.value()
                xlim_sup = spinBox_4.value()
                ylim_inf = spinBox.value()
                ylim_sup = spinBox_2.value()
                self.axis_x.setRange(xlim_inf, xlim_sup)
                self.axis_y.setRange(ylim_inf, ylim_sup)
        elif domain == "Frequency":
            if automaticCheckBox.isChecked():
                self.axis_x.setRange(20, np.max(LIM))
            else:
                xlim_inf = spinBox_3.value()
                xlim_sup = spinBox_4.value()
                ylim_inf = spinBox.value()
                ylim_sup = spinBox_2.value()
                self.axis_x.setRange(xlim_inf, xlim_sup)
                self.axis_y.setRange(ylim_inf, ylim_sup)
        elif domain == 'MPI':
            if automaticCheckBox.isChecked():
                self.axis_x.setRange(0, LIM)
                self.axis_y.setRange(0, 10)
            else:
                xlim_inf = spinBox_3.value()
                xlim_sup = spinBox_4.value()
                ylim_inf = spinBox.value()
                ylim_sup = spinBox_2.value()
                self.axis_x.setRange(xlim_inf, xlim_sup)
                self.axis_y.setRange(ylim_inf, ylim_sup)


    def selectMulti(self, metrics, domain, samplingBox):
           global chartView
           if self.ui.holdOnCheck.isChecked():
               self.ui.listWidget2.setSelectionMode(QAbstractItemView.MultiSelection)
               nSelectItems = len(self.ui.listWidget2.selectedItems())
               if nSelectItems > 2:
                   self.ui.listWidget2.clearSelection()
                   self.ui.mainBox.setCurrentIndex(0)
                   self.ui.expandGraph.setEnabled(False)
                   self.ui.exportFig.setEnabled(False)
                   self.ui.exportData.setEnabled(False)
                   self.ui.domainBox.setCurrentIndex(0)
                   self.ui.domainBox.setEnabled(False)
                   self.ui.samplingBox.setCurrentIndex(0)
                   self.ui.samplingBox.setEnabled(False)
                   self.ui.automaticCheckBox.setEnabled(False)
                   self.ui.automaticCheckBox.setChecked(True)
                   self.ui.applyButton.setEnabled(False)
               elif nSelectItems > 1:
                   pass

           else:
               type == 'plot'
               self.ui.listWidget2.setSelectionMode(QAbstractItemView.SingleSelection)
               self.timeData, self.samplingRate = getAudio(self.pathname)
               self.timeData = 2*(self.timeData/(2**16))
               self.chartview = self.getGraph(metrics, domain, samplingBox, type, window = "default")


       def presetImport(self, domain):
           self.ui.mainBox.setCurrentIndex(0)
           if domain == "Time":
               self.ui.domainBox.setCurrentIndex(0)
               self.ui.domainBox.setEnabled(True)
               self.ui.samplingBox.setCurrentIndex(0)
               self.ui.samplingBox.setEnabled(False)
               self.ui.automaticCheckBox.setEnabled(True)
               self.ui.automaticCheckBox.setChecked(True)

