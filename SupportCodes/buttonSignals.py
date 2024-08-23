from Pages.graph import UI_Buttons_Graph
from Pages.editor import UI_Buttons_Filter
from Pages.calibration import UI_Buttons_Cali

from PagesSetup.mainSettings import MainSettings


class ButtonSignals():
    def __init__(self, ui):
        super(ButtonSignals, self).__init__()

    def buttonCallbackMainWindow(self):
        #GENERAL BUTTONS
        self.clique = 0
        self.ui.closeAllButton.clicked.connect(lambda: MainSettings.closeAll(self))
        self.ui.minimizeButton.clicked.connect(lambda: MainSettings.minimize(self))
        self.ui.maximizeButton.clicked.connect(lambda: MainSettings.maximize(self, window="defaut"))

        #LEFL MENU
        self.ui.menuButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "menu"))
        self.ui.homeButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "home"))
        self.ui.userButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "user"))
        self.ui.calibrationButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "calibration"))
        self.ui.filterButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "filter"))

        #FILTER PAGE
        self.ui.removeButton.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "remove"))
        self.ui.removeAllButton.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "removeAll"))
        self.ui.resetButton.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "reset"))        
        self.ui.importButton.clicked.connect(lambda: UI_Buttons_Filter.importButton(self))
        self.ui.listWidget.itemClicked.connect(lambda: UI_Buttons_Filter.selectItem(self))
        self.ui.playButton.clicked.connect(lambda: UI_Buttons_Filter.playButton(self))
        self.ui.pauseButton.clicked.connect(lambda: UI_Buttons_Filter.pauseButton(self))
        self.ui.stopButton.clicked.connect(lambda: UI_Buttons_Filter.stopButton(self))
        self.ui.volumeSlider.valueChanged.connect(lambda: UI_Buttons_Filter.setVolume(self))
        self.ui.muteButton.clicked.connect(lambda: UI_Buttons_Filter.setMute(self))
        self.ui.filterAudioButton.clicked.connect(lambda: UI_Buttons_Filter.filterAudioButton(self))
        self.frequencieBands = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000]
        params = {"self": self, "UI_Buttons": UI_Buttons_Filter}
        for slider in self.frequencieBands:
            eval('''self.ui.switch_{}.clicked.connect(lambda: UI_Buttons.switchSlider(self))'''.format(slider), params)
            eval('''self.ui.slider_{}.valueChanged.connect(lambda: UI_Buttons.switchSlider(self))'''.format(
                slider), params)

        #CALIBRATION PAGE FUNCTION
        self.ui.removeGraph.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "removeGraph"))
        self.ui.removeAllGraph.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "removeAllGraph"))
        self.ui.typeHeadBox_2.activated[str].connect(lambda: MainSettings.callFunctionsCalibration(self, "typeHeadBox"))
        self.ui.typeHatsBox_2.activated[str].connect(lambda: MainSettings.callFunctionsCalibration(self, "typeHatsBox"))

        self.ui.importGraph.clicked.connect(lambda: UI_Buttons_Graph.importButton(self))
        self.ui.listWidget2.itemClicked.connect(lambda: UI_Buttons_Graph.selectMulti(self))
        self.ui.modelHeadBox_2.activated[str].connect(lambda: UI_Buttons_Cali.changeModelHead(self))
        self.ui.modelHatsBox_2.activated[str].connect(lambda: UI_Buttons_Cali.changeModelHats(self))
        self.ui.plot.clicked.connect(lambda: UI_Buttons_Graph.expandGraph(self))

    def buttonCallbackGraphWindow(self):
        #Layout Callbacks
        self.clique = 0
        self.gp.closeAllButton.clicked.connect(lambda: MainSettings.closeAll(self))
        self.gp.minimizeButton.clicked.connect(lambda: MainSettings.minimize(self))
        self.gp.maximizeButton.clicked.connect(lambda: MainSettings.maximize(self, window="expand"))
        self.gp.domainBox.activated[str].connect(lambda: MainSettings.callFunctionsCalibration(self, "domainBox"))
        self.gp.mainBox.activated[str].connect(lambda: MainSettings.callFunctionsCalibration(self, "mainBox"))
        self.gp.automaticCheckBox.clicked.connect(lambda: MainSettings.callFunctionsCalibration(self, "automaticCheckBox"))

        #Functions Callbacks
        self.gp.exportFig.clicked.connect(lambda: UI_Buttons_Graph.saveGraph(self))
        self.gp.exportData.clicked.connect(lambda: UI_Buttons_Graph.saveData(self))
        self.gp.mainBox.activated[str].connect(lambda: UI_Buttons_Graph.changeGraph(self, window="expand"))
        self.gp.domainBox.activated[str].connect(lambda: UI_Buttons_Graph.changeGraph(self, window="expand"))
        self.gp.samplingBox.activated[str].connect(lambda: UI_Buttons_Graph.changeGraph(self, window="expand"))
        self.gp.refresh.clicked.connect(lambda: UI_Buttons_Graph.changeGraph(self, window="expand"))
