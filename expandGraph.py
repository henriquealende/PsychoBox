from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Qt, QFile
from PySide2.QtUiTools import QUiLoader

from SupportCodes.setWindow import SetupWindow

class Expand_Graph(QMainWindow):
    def __init__(self):
        super(Expand_Graph, self).__init__()
        self.initUI()
        self.set()
#        self.set2()

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

#    def set2(self):
#        # Set up the matplotlib widget
#        self.matplotlib_widget = QWidget(self.gp.frame)
#        self.fig = plt.figure(figsize=(6, 4), dpi=100)
#        self.ax = self.fig.add_subplot(111)
#        self.canvas = FigureCanvas(self.fig)
#        layout = QVBoxLayout(self.matplotlib_widget)
#        layout.addWidget(self.canvas)

#        layout = QVBoxLayout(self.gp.frame)
#        layout.addWidget(self.matplotlib_widget)

#        # Show the UI
#        self.setCentralWidget(self.gp)
#        self.show()

#        # Draw the initial graph
#        QTimer.singleShot(0, lambda: self.canvas.draw())
#        #QTimer.singleShot(0, lambda: TESTE.plot_quadratic(self))

    def eventFilter(self, source, event):
        return SetupWindow.handle_event_filter(self, source, event)



#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    widget = Expand_Graph()
#    #QtCore.QTimer.singleShot(0, lambda: SetupWindow.centerWindow(widget))
#    sys.exit(app.exec_())

