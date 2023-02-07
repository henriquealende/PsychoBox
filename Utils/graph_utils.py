import numpy as np
from PySide2.QtCharts import *
from PySide2 import  QtGui
from PySide2.QtGui import  QPainter, QBrush, QColor, QPen

from Utils.utils import *

global x, y
x = [0]
y = [0]

def getGraph(self, timeData, samplingRate, metrics, domain, samplingBox, window):
    chart = QtCharts.QChart()
    chart.legend().hide()
    chart.setBackgroundRoundness(12.0)
    chart.setDropShadowEnabled(True)
    chart.setBackgroundBrush(QBrush(QColor(242, 240, 241)))
    chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

    series = QtCharts.QLineSeries()
    pen = QPen(QtGui.QColor(0, 155, 74))
    pen.setWidth(1)
    series.setPen(pen)

    #if metrics == 'Time-Frequency':
    #    Time_Frequency(self, timeData, samplingRate, metrics, domain, samplingBox, window, series, chart)
    #else:
    #    Metrics(self)


#def Time_Frequency(self, timeData, samplingRate, metrics, domain, samplingBox, window, series, chart):
    global x, y
    if domain == 'Time':
        y = timeData
        T = len(timeData)/samplingRate
        x = np.linspace(0, T, len(y))

        for pos in np.arange(len(y)):
            series.append(x[pos], y[pos])
        chart.addSeries(series)

        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setRange(0, T)
        self.axis_x.setTickCount(5)
        self.axis_x.setLabelFormat("%.2f")
        self.axis_x.setTitleText("Time [s]")
        chart.setAxisX(self.axis_x, series)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setRange(-1, 1)
        self.axis_y.setTickCount(5)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Amplitude")
        chart.setAxisY(self.axis_y, series)

    elif domain == 'Frequency':
        x, y, Yplot = getFFT(timeData, samplingRate)

        if samplingBox == "3º octave":
            y = getBandValue(Yplot, samplingRate)
            x = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
            y = 20*np.log10(y/2e-5)

        for pos in np.arange(len(y)):
            series.append(x[pos], y[pos])     # add point to chart
        chart.addSeries(series)

        self.axis_x = QtCharts.QLogValueAxis()
        self.axis_x.setRange(20, np.max(x))
        self.axis_x.setLabelFormat("%.0f")
        self.axis_x.setTitleText("Frequency [Hz]")
        chart.setAxisX(self.axis_x, series)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(5)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("SPL [dB]")
        chart.setAxisY(self.axis_y, series)

    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

#    plot(self, chartView, window)


#def Metrics(self):
#    pass
    #plot(self, chartView, window)

#def plot(self, chartView, window):
    if window == "default":
        self.ui.gridLayout.addWidget(chartView, 1, 0)
    elif window == "expand":
        self.gp.gridLayout_2.addWidget(chartView, 1, 0)
    return chartView

