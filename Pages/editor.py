import os
import numpy as np

from pygame import mixer
from PySide6.QtWidgets import QFileDialog

from Utils.filter_utils import FilterUtils
from PagesSetup.mainSettings import MainSettings

class UI_Buttons_Filter():
    def __init__(self):
        super(UI_Buttons_Filter, self).__init__()

    def importButton(self):
        global path
        importAdress = QFileDialog.getOpenFileName(self,'Open file','','WAV files (*.wav)')
        importPathname = importAdress[0]
        filename = os.path.basename(str(importPathname))
        path = os.path.dirname(str(importPathname))
        self.ui.listWidget.addItem(filename)

    def selectItem(self):
        global path
        self.sliders = FilterUtils.getInitParameters(self)
        for _, slider in enumerate(self.sliders):
            eval('self.ui.switch_{}.setChecked(True)'.format(slider))
            eval('self.ui.slider_{}.setEnabled(True)'.format(slider))
            db = ' dB'
            txt = 'str(round(self.ui.slider_{}.value()*.3, 2))+db'.format(slider)
            eval('self.ui.switch_{}.setText({})'.format(slider, txt))
        filename = str(self.ui.listWidget.currentItem().text())
        MainSettings.callFunctionsEditor(self, "selectItem")
        print(path, filename)
        self.timeData, self.samplingRate = FilterUtils.getAudio(path + '/' + filename)
        mixer.music.load(path + '/' + filename)
        self.pause = False

    def playButton(self):
        self.currentVolume = self.ui.volumeSlider.value()
        mixer.music.set_volume(self.currentVolume/100)
        if self.pause:
            mixer.music.unpause()
        else:
            mixer.music.play()
        MainSettings.callFunctionsEditor(self, "play")
        self.pause = False


    def pauseButton(self):
        mixer.music.pause()
        MainSettings.callFunctionsEditor(self, "pause/stop")
        self.pause = True

    def stopButton(self):
        mixer.music.stop()
        MainSettings.callFunctionsEditor(self, "pause/stop")
        self.pause = False

    def setVolume(self):
        self.currentVolume = self.ui.volumeSlider.value()
        mixer.music.set_volume(self.currentVolume/100)
        MainSettings.callFunctionsEditor(self, "currentVolume")

    def setMute(self):
        self.currentVolume = self.ui.volumeSlider.value()
        if self.ui.muteButton.isChecked():
            self.ui.volumeSlider.setValue(0)
            mixer.music.set_volume(0)
        else:
            self.ui.volumeSlider.setValue(50)
            mixer.music.set_volume(0.5)

    def switchSlider(self):
        self.sliderValue = np.zeros(len(self.sliders))
        for index, slider in enumerate(self.sliders):
            exec('self.sliderValue[{}] = round(self.ui.slider_{}.value()*.3, 2)'.format(index, slider))
            db = ' dB'
            txt = 'str(round(self.ui.slider_{}.value()*.3, 2))+db'.format(slider)
            eval('self.ui.switch_{}.setText({})'.format(slider, txt))
            self.ui.resetButton.setEnabled(True)
        self.linearSliderValue = 10**(self.sliderValue/20)
        self.ui.filterAudioButton.setEnabled(True)

    def filterAudioButton(self):
        self.bandEnergy = FilterUtils.applyOctaveFilter(self)
        filteredSignal = FilterUtils.applySliders(self, self.linearSliderValue)
        savedFile = FilterUtils.saveAudio(self, filteredSignal, self.samplingRate)
        self.ui.listWidget.addItem(savedFile)
