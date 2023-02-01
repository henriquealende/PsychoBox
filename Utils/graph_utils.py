import numpy as np
from PySide2.QtCharts import * 
from PySide2 import  QtGui
from PySide2.QtGui import  QPainter, QBrush, QColor, QPen

from Utils.utils import *

def getGraph(self, timeData, samplingRate, domain, window):
    chart = QtCharts.QChart() 
    chart.setBackgroundRoundness(12.0)
    chart.setDropShadowEnabled(True)
    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    chartView.chart().setAnimationOptions(QtCharts.QChart.AllAnimations)
    chartView.chart().setBackgroundBrush(QBrush(QColor(242, 240, 241)))
    chartView.chart().legend().hide() 
    #if domain == "Time":
    #    chart.setTitle('Time')  
    series = QtCharts.QLineSeries()
    pen = QPen(QtGui.QColor(0, 155, 74))
    pen.setWidth(1)
    series.setPen(pen)

    if domain == 'Time':
        y = timeData    
        T = len(timeData)/samplingRate
        x = np.linspace(0, T, len(y))

        for pos in np.arange(len(y)):
            series.append(x[pos], y[pos])
        chart.addSeries(series)
        #chart.createDefaultAxes()

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
        if self.ui.samplingBox.currentText() == "Linear":            
            for pos in np.arange(len(y)):
                # add point to chart
                series.append(x[pos], y[pos])

            ''' chart - add series'''
            chart.addSeries(series)
            #chart.createDefaultAxes()

            self.axis_x = QtCharts.QLogValueAxis()
            self.axis_x.setRange(20, np.max(x))
            #self.axis_x.setTickCount(5)
            self.axis_x.setLabelFormat("%.0f")
            self.axis_x.setTitleText("Frequency [Hz]")
            chart.setAxisX(self.axis_x, series)
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("SPL [dB]")
            chart.setAxisY(self.axis_y, series)
        else:
            y = getBandValue(Yplot, samplingRate)            
            x = np.array([50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250,
            1600, 2000, 2500,3150, 4000, 5000, 6300, 8000, 10000])
            y = 20*np.log10(y/2e-5)
            for pos in np.arange(len(y)):
                # add point to chart
                series.append(x[pos], y[pos])

            ''' chart - add series'''
            chart.addSeries(series)
            #chart.createDefaultAxes()

            self.axis_x = QtCharts.QLogValueAxis()
            self.axis_x.setRange(np.min(x), np.max(x))
            #self.axis_x.setTickCount(5)
            self.axis_x.setLabelFormat("%.0f")
            self.axis_x.setTitleText("Frequency [Hz]")
            chart.setAxisX(self.axis_x, series)
            self.axis_y = QtCharts.QValueAxis()
            self.axis_y.setTickCount(5)
            self.axis_y.setLabelFormat("%.2f")
            self.axis_y.setTitleText("SPL [dB]")
            chart.setAxisY(self.axis_y, series)


    if window == "default":
        self.ui.gridLayout.addWidget(chartView, 1, 0)
    elif window == "expand":
        self.gp.gridLayout.addWidget(chartView, 1, 0)
    
    
#def populate_animationbox(self):
    #animated = self.ui.animatedComboBox
    #chart_view.chart().setAnimationOptions(options_name)


    # animated.addItem("No Animations", QtCharts.QChart.NoAnimation)
    # animated.addItem("GridAxis Animations", QtCharts.QChart.GridAxisAnimations)
    # animated.addItem("Series Animations", QtCharts.QChart.SeriesAnimations)
    # animated.addItem("All Animations", QtCharts.QChart.AllAnimations)
