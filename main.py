import sys
import pygame

from PySide2 import QtCore
from PySide2.QtCore import Qt, QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from SupportCodes.setWindow import SetupWindow
from Resources import resourceGUI


class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.initUI()
        self.set()

    def initUI(self):
        loader = QUiLoader()
        file = QFile("Forms/form.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

    def set(self):
        from SupportCodes.buttonSignals import ButtonSignals
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        SetupWindow.setWindowInformation(self, "main")
        ButtonSignals.buttonCallbackMainWindow(self)
        pygame.init()

    def eventFilter(self, source, event):
        return SetupWindow.handle_event_filter(self, source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Main_Window()
    widget.show()

    QtCore.QTimer.singleShot(0, lambda: SetupWindow.centerWindow(widget))
    sys.exit(app.exec_())
