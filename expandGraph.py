from Utils.utils import *
from Utils.graph_utils import *

import Buttons.login as bt_lo
import Buttons.graph as bt_gh

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QWidget, QGraphicsOpacityEffect, QMessageBox, QGraphicsColorizeEffect, QLabel, QVBoxLayout, QMainWindow, QGraphicsDropShadowEffect)
from PySide2.QtCore import (Qt, QFile, QPropertyAnimation, QEasingCurve, QMargins, QTime, QPoint)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QValidator, QDoubleValidator, QColor, QIcon, QPixmap
from PySide2.QtSql import QSqlDatabase, QSqlQuery

from PIL import ImageQt

from Resources import resourceGUI

import sys

class Expand_Graph(QMainWindow):
    def __init__(self):
        super(Expand_Graph, self).__init__()
        self.initUI()
        self.getAndReadWav()
        self.buttonCallback()

    def initUI(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        loader = QUiLoader()
        file = QFile("Forms/graph.ui")
        file.open(QFile.ReadOnly)
        self.gp = loader.load(file, self)
        file.close()
        self.gp.infoBar3.installEventFilter(self)
        self.gp.domainBox.addItems(['Time', 'Frequency'])

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
        self.gp.closeAllButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.closeAll(self))
        self.gp.minimizeButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.minimize(self))
        self.gp.exportFig.clicked.connect(lambda: bt_gh.UI_Buttons_Graph.saveGraph(self))
        self.gp.domainBox.activated[str].connect(lambda: bt_gh.UI_Buttons_Graph.changeDomainExpand(self))

    def getAndReadWav(self):
        from main import Main_Window
        main = Main_Window()
        pathname = main.getPath()
        type = self.gp.domainBox.currentText()
        self.timeVector, self.samplingRate = read_wav(pathname)
        self.timeVector = 2*(self.timeVector/(2**16))
        if type == "Time":
            self.chartview = getGraph(self, self.timeVector, self.samplingRate, domain = 'Time', window = "expand")
        elif type == "Frequency":
            self.chartview = getGraph(self, self.timeVector, self.samplingRate, domain = 'Frequency', window = "expand")


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
    widget.resize(1046,665)
    widget.show()
    QtCore.QTimer.singleShot(0, lambda: centerWindow(widget))
    sys.exit(app.exec_())

