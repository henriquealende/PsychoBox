
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt

from SupportCodes.setWindow import SetupWindow
from Forms.ui_expand import Ui_MainWindow

class Expand_Graph(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gp = Ui_MainWindow()
        self.gp.setupUi(self)
        self.set()

    def set(self):
        from SupportCodes.buttonSignals import ButtonSignals
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        SetupWindow.setWindowInformation(self, "secondary")
        ButtonSignals.buttonCallbackGraphWindow(self)

    def eventFilter(self, source, event):
        return SetupWindow.handle_event_filter(self, source, event)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   widget = Expand_Graph()
   widget.show()
   QtCore.QTimer.singleShot(0, lambda: SetupWindow.centerWindow(widget))
   sys.exit(app.exec_())
    