from main import *

import Buttons.login as bt_lo

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import (QApplication, QWidget, QGraphicsOpacityEffect, QMessageBox, QGraphicsColorizeEffect, QLabel, QVBoxLayout, QMainWindow, QGraphicsDropShadowEffect)
from PySide2.QtCore import (Qt, QFile, QPropertyAnimation, QEasingCurve, QMargins, QTime, QPoint)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QValidator, QDoubleValidator, QColor, QIcon
from PySide2.QtSql import QSqlDatabase, QSqlQuery

from Resources import resourceGUI

import sys

class New_Project_Widget(QMainWindow):
    def __init__(self):
        super(New_Project_Widget, self).__init__()
        self.main_window = Main_Window()
        
        self.initUI()
        self.buttonCallback()

    def initUI(self):
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        loader = QUiLoader()
        file = QFile("Forms/newProject.ui")
        file.open(QFile.ReadOnly)
        self.np = loader.load(file, self)
        file.close()
        self.np.infoBar2.installEventFilter(self)
         # DROP SHADOW EFFECT
#        shadow = QGraphicsDropShadowEffect(self)
#        shadow.setBlurRadius(8)
#        shadow.setColor(QtGui.QColor(76, 35, 45).lighter())
#        shadow.setOffset(4)
#        self.ui.setGraphicsEffect(shadow)

    def eventFilter(self, source, event):
        if source == self.np.infoBar2:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                self.move(self.pos() - self.offset + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        return super().eventFilter(source, event)

    def buttonCallback(self):
        self.np.closeAllButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.closeAll(self))
        self.np.minimizeButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.minimize(self))
        self.np.applyButton.clicked.connect(lambda: bt_lo.UI_Buttons_Login.applyProject(self, self.main_window))
        
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
    widget = New_Project_Widget()
    widget.resize(400,400)
    widget.show()
    QtCore.QTimer.singleShot(0, lambda: centerWindow(widget))
    sys.exit(app.exec_())


 
