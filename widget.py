# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from Resources import resourceGUI

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QWidget, QGraphicsOpacityEffect, QMessageBox, QGraphicsColorizeEffect, QLabel, QVBoxLayout)
from PySide2.QtCore import (Qt, QFile, QPropertyAnimation, QEasingCurve, QMargins, QTime, QPoint)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QValidator, QDoubleValidator, QColor, QIcon


class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        loader = QUiLoader()
        file = QFile("Forms/form.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        self.oldPos = self.pos()
        self.setWindowTitle('PsychoBox | v.003')
        self.setIcon()

        def mousePressEvent(self, event):
            self.oldPos = event.globalPos()

        def mouseMoveEvent(self, event):
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def setIcon(self):
        appIcon = QIcon('Resources/img/psychobox.png')
        self.setWindowIcon(appIcon)

def center_window(widget):
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
    QtCore.QTimer.singleShot(0, lambda: center_window(widget))
    sys.exit(app.exec_())
