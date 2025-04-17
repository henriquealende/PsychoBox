import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCore import Qt

from SupportCodes.setWindow import SetupWindow
from Forms.ui_graph import Ui_Form
from Utils.graph_utils import CustomChartView

class Expand_Graph(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Cria um widget central
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)        
        # Configura a interface dentro do widget central
        self.gp = Ui_Form()
        self.gp.setupUi(self.central_widget)
        
        # Configurações adicionais
        self.set()

    def set(self):
        from SupportCodes.buttonSignals import ButtonSignals
        self.gp.frame_axis.hide()
        
        # Configurações de tamanho inicial e mínimo
        self.setGeometry(100, 100, 1200, 800)  # Define posição e tamanho inicial da janela
        self.setMinimumSize(962, 665)  # Define o tamanho mínimo da janela
        
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        SetupWindow.setWindowInformation(self, "secondary")
        ButtonSignals.buttonCallbackGraphWindow(self)

        # Substitua QChartView por CustomChartView
        self.chartview = CustomChartView(self.gp.chart)
        self.gp.gridLayout_2.addWidget(self.chartview, 1, 0)

        # Força o layout a se ajustar ao tamanho da janela
        self.adjustSize()

    def eventFilter(self, source, event):
        return SetupWindow.handle_event_filter(self, source, event)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   widget = Expand_Graph()
   widget.show()
   QtCore.QTimer.singleShot(0, lambda: SetupWindow.centerWindow(widget))
   sys.exit(app.exec())
