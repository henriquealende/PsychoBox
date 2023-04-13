import numpy as np
from PySide2.QtCharts import *
from PySide2.QtCore import QPointF
from PySide2 import  QtGui
from PySide2.QtGui import  QPainter, QBrush, QColor, QPen
from PySide2.QtWidgets import QAbstractItemView

from Utils.filter_utils import *

global chartView


def addNewSeries(self):
 # Criar uma nova série de dados
    new_series = QtCharts.QLineSeries()
    new_series.append(0, 0)
    new_series.append(2, 2)

    # Adicionar as séries anteriores e a nova série ao gráfico
    self.chart.addSeries(self.previous_series)
    self.chart.addSeries(new_series)

    # Definir os eixos para as novas séries de dados
    self.previous_series.attachAxis(self.chart.axisX())
    self.previous_series.attachAxis(self.chart.axisY())
    new_series.attachAxis(self.chart.axisX())
    new_series.attachAxis(self.chart.axisY())

    # Salvar a nova série como a série anterior
    self.previous_series = new_series

def getGraph(self, metrics, domain, samplingBox, window):
    global chartView
    
    self.chart = QtCharts.QChart()
    self.chart.legend().hide()
    self.chart.setBackgroundRoundness(12.0)
    self.chart.setDropShadowEnabled(True)
    self.chart.setAnimationOptions(QtCharts.QChart.NoAnimation)
    self.chart.setBackgroundBrush(QBrush(QColor(242, 240, 241)))
    # Define o domínio e prepara os dados para o plot
    defineDomain(self, domain, window, samplingBox)    
    # Cor do plot
    pen = QPen(QtGui.QColor(0, 155, 74))
    pen.setWidth(1)
    self.series.setPen(pen)
    plotGraph(self, window)       

def defineDomain(self, domain, window, samplingBox):
    # Domínio do tempo
    if domain == 'Time':
        # Entrada de dados
        y = self.timeData
        T = len(self.timeData)/self.samplingRate
        x = np.linspace(0, T, len(y))        
        # Criação da série de dados
        self.series = QtCharts.QLineSeries()
        for i in range(len(y)):
            self.series.append(x[i], y[i])
        # Configuração dos eixos
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTickCount(5)
        self.axis_x.setLabelFormat("%.2f")
        self.axis_x.setTitleText("Time [s]")
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(5)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Amplitude")
        # Ajuste de Limites
        limitsAdjust(self, window, domain, T)
    # Domínio da frequência
    elif domain == 'Frequency':
        x, y, Yplot = getFFT(self.timeData, self.samplingRate)
        if samplingBox == "1/3 octave":
            y = getBandValue(Yplot, self.samplingRate)
            x = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
                            630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000,
                            5000, 6300, 8000, 10000])
            y = 20*np.log10(y/2e-5)
        # Criação da série de dados
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
        # Ajuste de Limites
        limitsAdjust(self, window, domain, np.max(x))


def limitsAdjust(self, window, domain, LIM):
    if window == "default":
        automaticCheckBox = self.ui.automaticCheckBox
        spinBox = self.ui.spinBox
        spinBox_2 = self.ui.spinBox_2
        spinBox_3 = self.ui.spinBox_3
        spinBox_4 = self.ui.spinBox_4
    elif window == "expand":
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
                
def plotGraph(self, window):    
    # Adiciona a série ao gráfico
    self.chart.addSeries(self.series)
    self.chart.setAxisX(self.axis_x, self.series)
    self.chart.setAxisY(self.axis_y, self.series)
    # Adiciona o gráfico à visualização
    chartView = QtCharts.QChartView(self.chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    if window == "default":
        self.ui.gridLayout.addWidget(chartView, 1, 0)
    elif window == "expand":
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
    return chartView

###########################################################################

def selectMulti(self, metrics, domain, samplingBox):
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
            print(self.ui.listWidget2.selectedItems());
    else:
        self.ui.listWidget2.setSelectionMode(QAbstractItemView.SingleSelection)
        # filename = str(self.ui.listWidget2.currentItem().text())
        self.timeData, self.samplingRate = getAudio(self.pathname)
        self.timeData = 2*(self.timeData/(2**16))
    
        self.chartview = getGraph(self, metrics, domain, samplingBox, window = "default")
        # pathname = (path + '/' + filename)
        # return pathname
    
def presetImport(self, domain):
    self.ui.mainBox.setCurrentIndex(0)
    self.ui.expandGraph.setEnabled(True)
    self.ui.exportFig.setEnabled(True)
    self.ui.exportData.setEnabled(True)
    if domain == "Time":
        self.ui.domainBox.setCurrentIndex(0)
        self.ui.domainBox.setEnabled(True)
        self.ui.samplingBox.setCurrentIndex(0)
        self.ui.samplingBox.setEnabled(False)
        self.ui.automaticCheckBox.setEnabled(True)
        self.ui.automaticCheckBox.setChecked(True)
        self.ui.applyButton.setEnabled(True)