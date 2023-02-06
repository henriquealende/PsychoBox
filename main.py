# This Python file uses the following encoding: utf-8

import os
from pathlib import Path
import sys
from Resources import resourceGUI

import pygame
import Buttons.login as bt_lo
import Buttons.filter as bt_fi
import Buttons.graph as bt_gh



from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QWidget, QGraphicsOpacityEffect, QMessageBox, QGraphicsColorizeEffect, QLabel, QVBoxLayout, QMainWindow)
from PySide2.QtCore import (Qt, QFile, QPropertyAnimation, QEasingCurve, QMargins, QTime, QPoint)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QValidator, QDoubleValidator, QColor, QIcon

pathname = {}
path = {}
projects = []



class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()

        self.initUI()
        self.buttonCallback()

    def initUI(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        loader = QUiLoader()
        file = QFile("Forms/form.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        self.setWindowTitle('PsychoBox | v.003')
        self.setIcon()
        self.ui.infoBar.installEventFilter(self)
        self.ui.mainBox.addItems(['Time-Frequency', 'Metrics'])
        self.ui.domainBox.addItems(['Time', 'Frequency'])
        self.ui.samplingBox.addItems(['Linear', '3º octave'])
        pygame.init()
        
    def getPath(self):
        pathname = bt_gh.UI_Buttons_Graph.getPathname(self)
        return pathname
    
    def eventFilter(self, source, event):
        if source == self.ui.infoBar:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                self.move(self.pos() - self.offset + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        return super().eventFilter(source, event)

    def setIcon(self):
        appIcon = QIcon('Resources/img/psychobox.png')
        self.setWindowIcon(appIcon)

    def buttonCallback(self):
        self.ui.closeAllButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.closeAll(self))
        self.ui.minimizeButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.minimize(self))
        self.ui.connectButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.login(self))
        self.ui.registerButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.register(self))
        self.ui.menuButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.toogleMenu(self))
        self.ui.userButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.userButton(self))
        self.ui.homeButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.homeButton(self))
        self.ui.newProjectButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.newProject(self))
        #self.ui.refreshButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.refresh(self))

        # FILTER PAGE

        self.ui.filterButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.filterButton(self))
        self.ui.importButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.importButton(self))
        self.ui.removeButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.remove(self, 'filter'))
        self.ui.removeAllButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.removeAllButton(self, 'filter'))
        self.ui.listWidget.itemClicked.connect(lambda: bt_fi.UI_Buttons_Filter.selectItem(self))
        self.ui.playButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.playButton(self))
        self.ui.pauseButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.pauseButton(self))
        self.ui.stopButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.stopButton(self))
        self.ui.volumeSlider.valueChanged.connect(lambda: bt_fi.UI_Buttons_Filter.setVolume(self))
        self.ui.muteButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.setMute(self))
        self.frequencieBands = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400,
                                500, 630, 800, 1000, 1250, 1600, 2000, 2500,
                                3150, 4000, 5000, 6300, 8000, 10000]
        params = {"self": self, "UI_Buttons": bt_fi.UI_Buttons_Filter}
        for slider in self.frequencieBands:
            eval('''self.ui.switch_{}.clicked.connect(lambda: UI_Buttons.switchSlider(self))'''.format(slider), params)
            eval('''self.ui.slider_{}.valueChanged.connect(lambda: UI_Buttons.switchSlider(self))'''.format(
                slider), params)
        self.ui.resetButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.resetButton(self))
        self.ui.filterAudioButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.filterAudioButton(self))

        # GRAPH PAGE

        self.ui.mainBox.activated[str].connect(lambda: bt_gh.UI_Buttons_Graph.selectGraph(self))
        self.ui.domainBox.activated[str].connect(lambda: bt_gh.UI_Buttons_Graph.selectDomain(self, window="defaut"))
        self.ui.automaticCheckBox.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.automaticCheckBox(self))
        self.ui.graphButton.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.graphButton(self))
        self.ui.importGraph.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.importButton(self))
        self.ui.removeGraph.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.remove(self, 'graph'))
        self.ui.removeAllGraph.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.removeAllButton(self, 'graph'))
        self.ui.listWidget2.itemClicked.connect(lambda: bt_gh.UI_Buttons_Graph.selectItem(self))
        self.ui.applyButton.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.selectItem(self))
        self.ui.expandGraph.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.expandGraph(self))
        self.ui.exportFig.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.saveGraph(self, window = "default"))
        self.ui.exportButton.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.saveData(self))

def centerWindow(widget):
    window = widget.window()
    window.setGeometry(
       QtWidgets.QStyle.alignedRect(
           QtCore.Qt.LeftToRight,
           QtCore.Qt.AlignCenter,
           window.size(),
           QtGui.QGuiApplication.primaryScreen().availableGeometry(),
       ),
    )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main_Window()
    widget.resize(962,665)
    widget.show()
    QtCore.QTimer.singleShot(0, lambda: centerWindow(widget))
    sys.exit(app.exec_())
