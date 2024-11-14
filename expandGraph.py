
from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Qt, QFile
from PySide2.QtUiTools import QUiLoader

from SupportCodes.setWindow import SetupWindow

class Expand_Graph(QMainWindow):
    def __init__(self):
        super(Expand_Graph, self).__init__()
        self.initUI()
        self.set()
        self.gp.frame_axis.hide()

    def initUI(self):
        loader = QUiLoader()
        file = QFile("Forms/graph.ui")
        file.open(QFile.ReadOnly)
        self.gp = loader.load(file, self)
        file.close()

    def set(self):
        from SupportCodes.buttonSignals import ButtonSignals
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        SetupWindow.setWindowInformation(self, "secondary")
        ButtonSignals.buttonCallbackGraphWindow(self)

    def eventFilter(self, source, event):
        return SetupWindow.handle_event_filter(self, source, event)



# if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    widget = Expand_Graph()
#    QtCore.QTimer.singleShot(0, lambda: SetupWindow.centerWindow(widget))
#    sys.exit(app.exec_())

