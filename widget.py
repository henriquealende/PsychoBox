# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from Resources import resourceGUI

import pygame
import Buttons.login as bt_lo
import Buttons.filter as bt_fi



from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QWidget, QGraphicsOpacityEffect, QMessageBox, QGraphicsColorizeEffect, QLabel, QVBoxLayout, QMainWindow)
from PySide2.QtCore import (Qt, QFile, QPropertyAnimation, QEasingCurve, QMargins, QTime, QPoint)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QValidator, QDoubleValidator, QColor, QIcon
from PySide2.QtSql import QSqlDatabase, QSqlQuery


path = {}

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
        pygame.init()


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
        # FILTER PAGE
        self.ui.filterButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.filterButton(self))
        self.ui.importButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.importButton(self))
        self.ui.removeButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.remove(self))
        self.ui.removeAllButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.removeAllButton(self))
        self.ui.listWidget.itemClicked.connect(lambda: bt_fi.UI_Buttons_Filter.selectItem(self))
        self.ui.playButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.playButton(self))
        self.ui.pauseButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.pauseButton(self))
        self.ui.stopButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.stopButton(self))
        self.ui.volumeSlider.valueChanged.connect(lambda: bt_fi.UI_Buttons_Filter.setVolume(self))
        self.ui.muteButton.clicked.connect(lambda: bt_fi.UI_Buttons_Filter.setMute(self))

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
