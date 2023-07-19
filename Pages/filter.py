import os

from pygame import mixer
from Utils.filter_utils import *
from PySide2.QtWidgets import (QFileDialog)
##############################################################################


class UI_Buttons_Filter():
    def __init__(self):
        super(UI_Buttons_Filter, self).__init__()

    def filterButton(self):
        self.ui.rightContent.setCurrentWidget(self.ui.filterPage)

    def importButton(self):
        global path
        importAdress = QFileDialog.getOpenFileName(self,'Open file','','WAV files (*.wav)')
        importPathname = importAdress[0]
        filename = os.path.basename(str(importPathname))
        path = os.path.dirname(str(importPathname))        
        self.ui.listWidget.addItem(filename)


    def remove(self, where):
        if where == 'filter':
            allItems = self.ui.listWidget.count()
            listItems = self.ui.listWidget.selectedItems()
            if not listItems:
                return
            for item in listItems:
                self.ui.listWidget.takeItem(self.ui.listWidget.row(item))
            if allItems == 1:
                self.ui.playButton.setDisabled(True)
                self.ui.pauseButton.setDisabled(True)
                self.ui.stopButton.setDisabled(True)
                self.ui.filterAudioButton.setDisabled(True)
                self.ui.graphButton.setDisabled(True)
                self.ui.resetButton.setDisabled(True)
                self.ui.muteButton.setDisabled(True)
                self.ui.volumeSlider.setDisabled(True)
                for _, slider in enumerate(self.sliders):
                    eval('self.ui.switch_{}.setChecked(False)'.format(slider))
                    eval("self.ui.slider_{}.setDisabled(True)".format(slider))
                    eval("self.ui.switch_{}.setText('off')".format(slider))
        elif where == 'graph':
            allItems = self.ui.listWidget2.count()
            listItems = self.ui.listWidget2.selectedItems()
            if not listItems:
                return
            for item in listItems:
                self.ui.listWidget2.takeItem(self.ui.listWidget2.row(item))

        elif where == 'calibration':
            allItems = self.ui.listWidget2_3.count()
            listItems = self.ui.listWidget2_3.selectedItems()
            if not listItems:
                return
            for item in listItems:
                self.ui.listWidget2_3.takeItem(self.ui.listWidget2_3.row(item))

    def removeAllButton(self, where):
        if where == 'filter':
            self.ui.listWidget.clear()
            self.ui.playButton.setDisabled(True)
            self.ui.pauseButton.setDisabled(True)
            self.ui.stopButton.setDisabled(True)
            self.ui.filterAudioButton.setDisabled(True)
            self.ui.graphButton.setDisabled(True)
            self.ui.resetButton.setDisabled(True)
            self.ui.muteButton.setDisabled(True)
            self.ui.volumeSlider.setDisabled(True)
            for _, slider in enumerate(self.sliders):
                eval('self.ui.switch_{}.setChecked(False)'.format(slider))
                eval("self.ui.slider_{}.setDisabled(True)".format(slider))
                eval("self.ui.switch_{}.setText('off')".format(slider))
        elif where == 'graph':
            self.ui.listWidget2.clear()

        elif where == 'calibration':
            self.ui.listWidget2.clear()

    def selectItem(self):
        global path
        self.sliders = getInitParameters(self)
        for _, slider in enumerate(self.sliders):
            eval('self.ui.switch_{}.setChecked(True)'.format(slider))
            eval('self.ui.slider_{}.setEnabled(True)'.format(slider))
            db = ' dB'
            txt = 'str(round(self.ui.slider_{}.value()*.3, 2))+db'.format(slider)
            eval('self.ui.switch_{}.setText({})'.format(slider, txt))
        self.ui.playButton.setEnabled(True)
        filename = str(self.ui.listWidget.currentItem().text())
        self.ui.graphButton.setEnabled(True)
        self.ui.muteButton.setEnabled(True)
        self.ui.volumeSlider.setEnabled(True)
        self.timeData, self.samplingRate = getAudio(path + '/' + filename)
        mixer.music.load(path + '/' + filename)
        self.pause = False

    def playButton(self):
        self.currentVolume = self.ui.volumeSlider.value()
        mixer.music.set_volume(self.currentVolume/100)
        if self.pause:
            mixer.music.unpause()
        else:
            mixer.music.play()
        self.ui.pauseButton.setEnabled(True)
        self.ui.stopButton.setEnabled(True)
        self.pause = False

    def pauseButton(self):
        mixer.music.pause()
        self.ui.playButton.setEnabled(True)
        self.ui.stopButton.setEnabled(True)
        self.ui.pauseButton.setDisabled(True)
        self.pause = True

    def stopButton(self):
        mixer.music.stop()
        self.ui.playButton.setEnabled(True)
        self.ui.pauseButton.setEnabled(True)
        self.ui.stopButton.setDisabled(True)
        self.pause = False

    def setVolume(self):
        self.currentVolume = self.ui.volumeSlider.value()
        mixer.music.set_volume(self.currentVolume/100)
        if self.currentVolume == 0:
            self.ui.muteButton.setChecked(True)
        else:
            self.ui.muteButton.setChecked(False)

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


    def resetButton(self):
        for slider in self.sliders:
            eval("self.ui.slider_{}.setValue(0)".format(slider))
        self.ui.resetButton.setDisabled(True)
        self.ui.filterAudioButton.setEnabled(False)


    def filterAudioButton(self):
        self.bandEnergy = applyOctaveFilter(self)
        filteredSignal = applySliders(self, self.linearSliderValue)
        savedFile = saveAudio(self, filteredSignal, self.samplingRate)
        self.ui.listWidget.addItem(savedFile)
