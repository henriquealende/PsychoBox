import numpy as np
from PySide2.QtCharts import *
from PySide2.QtCore import QPointF
from PySide2 import  QtGui
from PySide2.QtGui import  QPainter, QBrush, QColor, QPen
from PySide2.QtWidgets import QAbstractItemView

from Utils.utils import *

global chartView

def getGraph(self, timeData, samplingRate, metrics, domain, samplingBox, window):
    global chartView
    
    chart = QtCharts.QChart()
    chart.legend().hide()
    chart.setBackgroundRoundness(12.0)
    chart.setDropShadowEnabled(True)
    chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
    chart.setBackgroundBrush(QBrush(QColor(242, 240, 241)))
    series = QtCharts.QLineSeries()

    if domain == 'Time':
        y = timeData
        T = len(timeData)/samplingRate
        x = np.linspace(0, T, len(y))        
        self.data_table = prepareData(x, y)       
        name = "Series "
        for i, lst in enumerate(self.data_table):
            series = QtCharts.QLineSeries(chart)
            for data in lst:
                series.append(data[0])
            series.setName(f"{name}{i}") 
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTickCount(5)
        self.axis_x.setLabelFormat("%.2f")
        self.axis_x.setTitleText("Time [s]")
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(5)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Amplitude")
        limitsAdjust(self, window, domain, T)

    elif domain == 'Frequency':
        x, y, Yplot = getFFT(timeData, samplingRate)
        if samplingBox == "1/3 octave":
            y = getBandValue(Yplot, samplingRate)
            x = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500,
                            630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000,
                            5000, 6300, 8000, 10000])
            y = 20*np.log10(y/2e-5)
        self.data_table = prepareData(x, y)       
        name = "Series "
        for i, lst in enumerate(self.data_table):
            series = QtCharts.QLineSeries(chart)
            for data in lst:
                series.append(data[0])
            series.setName(f"{name}{i}")           

        self.axis_x = QtCharts.QLogValueAxis()
        self.axis_x.setLabelFormat("%.0f")
        self.axis_x.setTitleText("Frequency [Hz]")
        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(5)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("SPL [dB]")
        limitsAdjust(self, window, domain, np.max(x))
    
    pen = QPen(QtGui.QColor(0, 155, 74))
    pen.setWidth(1)
    series.setPen(pen)
    plotGraph(self, series, chart, window)
    

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


def selectMulti(self):
    if self.ui.holdOnCheck.isChecked():
        self.ui.listWidget2.setSelectionMode(QAbstractItemView.MultiSelection)
    else:
        self.ui.listWidget2.setSelectionMode(QAbstractItemView.SingleSelection)
    
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

def prepareData(x, y, list_count = 1):
    data_table = []
    N = len(x)
    for i in range(list_count):
        data_list = []
        for j in range(N):
            value = QPointF(x[j], y[j])
            label = f"Slice {i}: {j}"
            data_list.append((value, label))
        data_table.append(data_list)
    return data_table
                
def plotGraph(self, series, chart, window):    
    chart.addSeries(series)
    chart.setAxisX(self.axis_x, series)
    chart.setAxisY(self.axis_y, series)
    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    if window == "default":
        self.ui.gridLayout.addWidget(chartView, 1, 0)
    elif window == "expand":
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
    return chartView

 #   items = self.ui.listWidget2.selectedItems()
 #   if len(items) >= 3:
 #       print(len(items))


