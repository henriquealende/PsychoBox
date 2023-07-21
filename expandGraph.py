import sys
import Pages.general as bt_lo
import Pages.graph as bt_gh
import Pages.settingsPages as bt_lp

from Utils.graph_utils import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCore import (Qt, QFile)
from PySide2.QtUiTools import QUiLoader
from Resources import resourceGUI
##############################################################################


class Expand_Graph(QMainWindow):
    def __init__(self, dados, pathExport, type):
        super(Expand_Graph, self).__init__()
        self.initUI()
        self.buttonCallback()
        self.getAndReadWav(dados, pathExport, type)


    def initUI(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        loader = QUiLoader()
        file = QFile("Forms/graph.ui")
        file.open(QFile.ReadOnly)
        self.gp = loader.load(file, self)
        file.close()
        self.gp.infoBar3.installEventFilter(self)
        self.gp.mainBox.addItems(['Time-Frequency', 'Metrics'])
        self.gp.samplingBox.addItems(['Linear', '1/3 octave'])
        self.gp.domainBox.addItems(['Time', 'Frequency'])
        self.gp.frame_samplingBox.hide()


    def eventFilter(self, source, event):
        if source == self.gp.infoBar3:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                self.move(self.pos() - self.offset + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        return super().eventFilter(source, event)


    def buttonCallback(self):
        self.clique = 0
        self.gp.closeAllButton.clicked.connect(lambda: bt_lp.UI_Buttons_Layout.closeAll(self))
        self.gp.minimizeButton.clicked.connect(lambda: bt_lp.UI_Buttons_Layout.minimize(self))
        self.gp.maximizeButton.clicked.connect(lambda: bt_lp.UI_Buttons_Layout.maximize(self, window="expand"))
        self.gp.exportFig.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.saveGraph(self))
        self.gp.exportData.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.saveData(self))
        self.gp.domainBox.activated[str].connect(lambda: bt_gh.UI_Buttons_Graph.changeGraph(self))
        self.gp.samplingBox.activated[str].connect(lambda: bt_gh.UI_Buttons_Graph.changeGraph(self))
        self.gp.domainBox.activated[str].connect(lambda: bt_lp.UI_Buttons_Layout.selectDomain(self))
        self.gp.mainBox.activated[str].connect(lambda: bt_lp.UI_Buttons_Layout.selectMetrics(self))
        self.gp.automaticCheckBox.clicked.connect(lambda: bt_lp.UI_Buttons_Layout.automaticCheckBox(self))
        self.gp.refresh.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.changeGraph(self))


    def getAndReadWav(self, dados, pathExport, type):
        self.pathname = pathExport
        metrics = dados[0]
        domain = dados[1]
        samplingBox = dados[2]

        if domain == 'Frequency':
            self.gp.domainBox.setCurrentIndex(1)
            self.gp.frame_samplingBox.show()

            if samplingBox == '1/3 octave':
                self.gp.samplingBox.setCurrentIndex(1)

        self.timeData, self.samplingRate = getAudio(self.pathname)
        self.timeData = 2*(self.timeData/(2**16))
        self.chartview = getGraph(self, domain, samplingBox)


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
    widget = Expand_Graph()
    #widget.resize(1046,665)
    widget.show()
    QtCore.QTimer.singleShot(0, lambda: centerWindow(widget))
    sys.exit(app.exec_())

