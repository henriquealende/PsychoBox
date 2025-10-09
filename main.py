import sys
import pygame

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar

from SupportCodes.setWindow import SetupWindow
from Pages.recording import UI_Buttons_Recorder as ubr

from Forms.ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set()

    def set(self):
        from SupportCodes.buttonSignals import ButtonSignals
        # Remove a flag Qt.WindowStaysOnTopHint para permitir que a janela minimize.
        # Mantém Qt.FramelessWindowHint para remover a barra de título padrão.
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Configurações de tamanho inicial e mínimo
        self.setGeometry(100, 100, 1200, 800)  # Define posição e tamanho inicial da janela
        self.setMinimumSize(1200, 800)  # Define o tamanho mínimo da janela
        
        SetupWindow.setWindowInformation(self, "main")
        ButtonSignals.buttonCallbackMainWindow(self)
        pygame.init()
        ubr.initialParameters(self)

    def eventFilter(self, source, event):
        return SetupWindow.handle_event_filter(self, source, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    QtCore.QTimer.singleShot(0, lambda: SetupWindow.centerWindow(widget))
    sys.exit(app.exec())