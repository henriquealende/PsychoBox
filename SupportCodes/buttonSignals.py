from Pages.graph import UI_Buttons_Graph
from Pages.editor import UI_Buttons_Filter
from Pages.recording import UI_Buttons_Recorder

from PagesSetup.mainSettings import MainSettings
from PagesSetup.setCalibration import SetCalibration


class ButtonSignals():
    def __init__(self, ui):
        super(ButtonSignals, self).__init__()

    def buttonCallbackMainWindow(self):
        # GENERAL BUTTONS
        self.clique = 0
        self.ui.closeAllButton.setToolTip("Close all open windows.")
        self.ui.closeAllButton.clicked.connect(lambda: MainSettings.closeAll(self))
        self.ui.minimizeButton.setToolTip("Minimize the current window.")
        self.ui.minimizeButton.clicked.connect(lambda: MainSettings.minimize(self))
        self.ui.maximizeButton.setToolTip("Maximize or restore the current window.")
        self.ui.maximizeButton.clicked.connect(lambda: MainSettings.maximize(self, window="defaut"))

        # LEFT MENU
        self.ui.menuButton.setToolTip("Toggle the left menu.")
        self.ui.menuButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "menu"))
        self.ui.homeButton.setToolTip("Navigate to the home page.")
        self.ui.homeButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "home"))
        self.ui.recordingButton.setToolTip("Navigate to the recording page.")
        self.ui.recordingButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "recording"))
        self.ui.userButton.setToolTip("Navigate to the user settings page.")
        self.ui.userButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "user"))
        self.ui.calibrationButton.setToolTip("Navigate to the calibration page.")
        self.ui.calibrationButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "calibration"))
        self.ui.filterButton.setToolTip("Navigate to the audio filter page.")
        self.ui.filterButton.clicked.connect(lambda: MainSettings.callFunctionsLeftMenu(self, "filter"))

        # FILTER PAGE
        self.ui.removeButton.setToolTip("Remove the selected item.")
        self.ui.removeButton.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "remove"))
        self.ui.removeAllButton.setToolTip("Remove all items.")
        self.ui.removeAllButton.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "removeAll"))
        self.ui.resetButton.setToolTip("Reset settings to default values.")
        self.ui.resetButton.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "reset"))
        self.ui.importButton.setToolTip("Import audio files.")
        self.ui.importButton.clicked.connect(lambda: UI_Buttons_Filter.importButton(self))
        self.ui.listWidget.setToolTip("List of available items.")
        self.ui.listWidget.itemClicked.connect(lambda: UI_Buttons_Filter.selectItem(self))
        self.ui.playButton.setToolTip("Play the selected audio.")
        self.ui.playButton.clicked.connect(lambda: UI_Buttons_Filter.playButton(self))
        self.ui.pauseButton.setToolTip("Pause the audio playback.")
        self.ui.pauseButton.clicked.connect(lambda: UI_Buttons_Filter.pauseButton(self))
        self.ui.stopButton.setToolTip("Stop the audio playback.")
        self.ui.stopButton.clicked.connect(lambda: UI_Buttons_Filter.stopButton(self))
        self.ui.volumeSlider.setToolTip("Adjust the audio volume.")
        self.ui.volumeSlider.valueChanged.connect(lambda: UI_Buttons_Filter.setVolume(self))
        self.ui.muteButton.setToolTip("Mute or unmute the audio.")
        self.ui.muteButton.clicked.connect(lambda: UI_Buttons_Filter.setMute(self))
        self.ui.filterAudioButton.setToolTip("Apply filters to the audio.")
        self.ui.filterAudioButton.clicked.connect(lambda: UI_Buttons_Filter.filterAudioButton(self))
        self.frequencieBands = [50, 63, 80, 100, 125, 160, 200, 250, 315, 400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000, 5000, 6300, 8000, 10000]
        params = {"self": self, "UI_Buttons": UI_Buttons_Filter}
        for slider in self.frequencieBands:
            eval('''self.ui.switch_{}.setToolTip("Enable or disable the {} Hz frequency band.")'''.format(slider, slider), params)
            eval('''self.ui.slider_{}.setToolTip("Adjust the gain for the {} Hz frequency band.")'''.format(slider, slider), params)
            eval('''self.ui.switch_{}.clicked.connect(lambda: UI_Buttons.switchSlider(self))'''.format(slider), params)
            eval('''self.ui.slider_{}.valueChanged.connect(lambda: UI_Buttons.switchSlider(self))'''.format(slider), params)

        # CALIBRATION PAGE FUNCTIONS
        self.ui.removeGraph.setToolTip("Remove the selected graph.")
        self.ui.removeGraph.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "removeGraph"))
        self.ui.removeAllGraph.setToolTip("Remove all graphs.")
        self.ui.removeAllGraph.clicked.connect(lambda: MainSettings.callFunctionsEditor(self, "removeAllGraph"))
        self.ui.importGraph.setToolTip("Import data for the graph.")
        self.ui.importGraph.clicked.connect(lambda: UI_Buttons_Graph.importButton(self))
        self.ui.listWidget2.setToolTip("List of available graphs.")
        self.ui.listWidget2.itemClicked.connect(lambda: UI_Buttons_Graph.selectMulti(self))
        self.ui.plot.setToolTip("Expand the selected graph.")
        self.ui.plot.clicked.connect(lambda: UI_Buttons_Graph.expandGraph(self))

        # RECORDING PAGE FUNCTIONS
        self.ui.recordingButton_2.setToolTip("Start or stop audio recording.")
        self.ui.recordingButton_2.clicked.connect(lambda: UI_Buttons_Recorder.toggle_recording(self))
        self.ui.exportAudioButton.setToolTip("Export the recorded audio.")
        self.ui.exportAudioButton.clicked.connect(lambda: UI_Buttons_Recorder.save_audio(self))
        self.ui.setMicrophone_1.setToolTip("Select microphone 1 as the input source.")
        self.ui.setMicrophone_1.clicked.connect(lambda: UI_Buttons_Recorder.setMicrophone(self, 1))
        self.ui.setMicrophone_2.setToolTip("Select microphone 2 as the input source.")
        self.ui.setMicrophone_2.clicked.connect(lambda: UI_Buttons_Recorder.setMicrophone(self, 2))
        self.ui.setSource_1.setToolTip("Select the audio source.")
        self.ui.setSource_1.clicked.connect(lambda: UI_Buttons_Recorder.setSource(self))
        self.ui.playButton_2.setToolTip("Play the recorded audio.")
        self.ui.playButton_2.clicked.connect(lambda: UI_Buttons_Recorder.play_audio(self))

    def buttonCallbackGraphWindow(self):
        # Layout Callbacks
        self.clique = 0
        self.gp.closeAllButton.setToolTip("Close all open graph windows.")
        self.gp.closeAllButton.clicked.connect(lambda: MainSettings.closeAll(self))
        self.gp.minimizeButton.setToolTip("Minimize the current graph window.")
        self.gp.minimizeButton.clicked.connect(lambda: MainSettings.minimize(self))
        self.gp.maximizeButton.setToolTip("Maximize or restore the current graph window.")
        self.gp.maximizeButton.clicked.connect(lambda: MainSettings.maximize(self, window="expand"))
        self.gp.domainBox.setToolTip("Select the domain for the graph (e.g., time or frequency).")
        self.gp.domainBox.activated[int].connect(lambda: MainSettings.callFunctionsCalibration(self, "domainBox"))
        self.gp.mainBox.setToolTip("Select the main graph to display.")
        self.gp.mainBox.activated[int].connect(lambda: MainSettings.callFunctionsCalibration(self, "mainBox"))
        self.gp.automaticCheckBox.setToolTip("Enable or disable automatic calibration.")
        self.gp.automaticCheckBox.clicked.connect(lambda: MainSettings.callFunctionsCalibration(self, "automaticCheckBox"))

        # Functions Callbacks
        self.gp.exportFig.setToolTip("Export the current graph as an image.")
        self.gp.exportFig.clicked.connect(lambda: UI_Buttons_Graph.saveGraph(self))
        self.gp.exportData.setToolTip("Export the data from the current graph.")
        self.gp.exportData.clicked.connect(lambda: UI_Buttons_Graph.saveData(self))
        self.gp.mainBox.setToolTip("Change the main graph being displayed.")
        self.gp.mainBox.activated[int].connect(lambda: UI_Buttons_Graph.changeGraph(self))
        self.gp.domainBox.setToolTip("Change the domain of the graph (e.g., time or frequency).")
        self.gp.domainBox.activated[int].connect(lambda: UI_Buttons_Graph.changeGraph(self))
        self.gp.samplingBox.setToolTip("Select the sampling rate for the graph.")
        self.gp.samplingBox.activated[int].connect(lambda: UI_Buttons_Graph.changeGraph(self))
        self.gp.refresh.setToolTip("Refresh the graph with the latest data.")
        self.gp.refresh.clicked.connect(lambda: UI_Buttons_Graph.changeGraph(self))
        self.gp.windowButton.setToolTip("Open a window to select the signal window type.")
        self.gp.windowButton.clicked.connect(lambda: UI_Buttons_Graph.openWindowSelection(self))
