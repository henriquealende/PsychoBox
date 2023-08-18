from PySide2 import QtCore
from PySide2.QtGui import QIcon
from PySide2 import QtGui, QtWidgets

class SetupWindow():
    def __init__(self):
        super(SetupWindow, self).__init__()

    def handle_event_filter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.offset = event.pos()
        elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
            self.move(self.pos() - self.offset + event.pos())
            return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            self.offset = None
        return False

    def setWindowInformation(self, window):
        appIcon = QIcon('Resources/img/psychobox.png')
        self.setWindowIcon(appIcon)
        self.setWindowTitle('PsychoBox | v.003')

        if window == "main":
            self.ui.infoBar.installEventFilter(self)
        else:
            self.gp.infoBar3.installEventFilter(self)
            self.gp.frame_samplingBox.hide()

    def centerWindow(widget):
        print("arquivo setWindow")
        window = widget.window()
        window.setGeometry(
           QtWidgets.QStyle.alignedRect(
               QtCore.Qt.LeftToRight,
               QtCore.Qt.AlignCenter,
               window.size(),
               QtGui.QGuiApplication.primaryScreen().availableGeometry(),
           ),
        )








