from PagesSetup.setCalibration import SetCalibration
from PagesSetup.setLogin import SetLogin
from PagesSetup.setWelcome import SetWelcome
from PagesSetup.setEditor import SetEditor
from PagesSetup.setGraph import SetGraph
from PagesSetup.setLeftMenu import SetLeftMenu

class MainSettings():
    def __init__(self):
        super(MainSettings, self).__init__()

    def closeAll(self):
        self.close()

    def minimize(self):
        self.showMinimized()

    def maximize(self, window):
        self.clique = self.clique +1

        if self.clique%2 == 1:
            if window == "expand":
                SetGraph.windowLayout(self, "maximazed")
            else:
                SetCalibration.windowLayout(self, "maximazed")
                SetLogin.windowLayout(self, "maximazed")
                SetWelcome.windowLayout(self, "maximazed")
                SetEditor.windowLayout(self, "maximazed")

                #GERAL 
                self.ui.topContent.setMinimumSize(16777215, 50)
                self.ui.frame_3.setMinimumSize(50, 70)
                self.ui.minimizeButton.setMaximumSize(24, 24)
                self.ui.closeAllButton.setMaximumSize(24, 24)
                self.ui.maximizeButton.setMaximumSize(24, 24)
                self.ui.frameButtons.setMinimumSize(150, 30)
                self.ui.frameButtons.setStyleSheet(u"QPushButton {border-radius: 12px}")
            self.showFullScreen()

        elif self.clique%2 == 0:
            if window == "expand":
                SetGraph.windowLayout(self, "minimazed")
            else:
                SetCalibration.windowLayout(self, "minimazed")
                SetLogin.windowLayout(self, "minimazed")
                SetWelcome.windowLayout(self, "minimazed")
                SetEditor.windowLayout(self, "minimazed")

                #GERAL
                self.ui.topContent.setMinimumSize(16777215, 50)
                self.ui.frame_3.setMinimumSize(50, 50)
                self.ui.minimizeButton.setMaximumSize(20, 20)
                self.ui.closeAllButton.setMaximumSize(20, 20)
                self.ui.maximizeButton.setMaximumSize(20, 20)
                self.ui.frameButtons.setMinimumSize(120, 30)
                self.ui.frameButtons.setStyleSheet(u"QPushButton {border-radius: 10px}")
            self.showNormal()


    def callFunctionsCalibration(self, parameter):
        if parameter == "typeHeadBox":
            SetCalibration.changeTypeHead(self)
        elif parameter == "typeHatsBox":
            SetCalibration.changeTypeHats(self)
        elif parameter == "domainBox":
            SetCalibration.selectDomain(self)
        elif parameter == "mainBox":
            SetCalibration.selectMetrics(self)
        elif parameter == "automaticCheckBox":
            SetCalibration.automaticCheckBox(self)

    def callFunctionsEditor(self, parameter):
        if parameter == "removeGraph":
            SetEditor.remove(self, 'graph')
        elif parameter == "removeAllGraph":
            SetEditor.removeAllButton(self, 'graph')
        elif parameter == "reset":
            SetEditor.resetButton(self)
        elif parameter == "remove":
            SetEditor.remove(self, 'filter')
        elif parameter == "removeAll":
            SetEditor.removeAllButton(self, 'filter')

        elif parameter == "selectItem":
            SetEditor.selectItemLayout(self)
        elif parameter == "play":
            SetEditor.pauseAndStopLayout(self, "play")
        elif parameter == "pause/stop":
            SetEditor.pauseAndStopLayout(self, "pause/stop")
        elif parameter == "currentVolume":
            SetEditor.VolumeButton(self, self.currentVolume)




    def callFunctionsLeftMenu(self, parameter):
        if parameter == "menu":
            SetLeftMenu.toogleMenu(self)
        elif parameter == "home":
            SetLeftMenu.homeButton(self)
        elif parameter == "user":
            SetLeftMenu.userButton(self)
        elif parameter == "calibration":
            SetLeftMenu.calibrationButton(self)














    


