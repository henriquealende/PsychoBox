class SetEditor():
    def __init__(self):
        super(SetEditor, self).__init__()

    def windowLayout(self, parameter):
        if parameter == "maximazed":
            #FILTER
            self.ui.playerFrame.setMinimumSize(16777215, 300)
            self.ui.playerFrame_2.setMinimumSize(16777215, 300)
            self.ui.importAudio.setMinimumSize(1000, 16777215)
            self.ui.buttons.setMinimumSize(700, 16777215)
            self.ui.title.setMinimumSize(16777215, 150)
            self.ui.logo.setMinimumSize(150, 75)
            self.ui.frame_100.setMinimumSize(16777215, 50)

            self.ui.stopButton.setMinimumSize(60, 60)
            self.ui.playButton.setMinimumSize(60, 60)
            self.ui.pauseButton.setMinimumSize(60, 60)
            self.ui.frameButtonsSE.setStyleSheet(u"QPushButton {padding-left: 2px; text-align: center; background-color:#006d34;\n"
                                                                "border: 3px solid #009b4a; border-radius:30px; color: rgb(255, 255, 255)}\n")
            self.ui.muteButton.setMinimumSize(40, 40)
            self.ui.muteButton.setStyleSheet(u"QPushButton {border-radius: 20px;}")
            #self.ui.volumeSlider.setStyleSheet(u"QSlider::groove:horizontal {width:250px;}")

            self.ui.resetButton.setMinimumSize(150, 40)
            self.ui.filterAudioButton.setMinimumSize(150, 40)
            #self.ui.frame_68.setMinimumSize(600, 40)

        else:
            #FILTER
            self.ui.playerFrame.setMinimumSize(0, 160)
            self.ui.playerFrame_2.setMinimumSize(0, 0)
            self.ui.importAudio.setMinimumSize(0, 100)
            self.ui.buttons.setMinimumSize(0, 100)
            self.ui.title.setMinimumSize(0, 80)
            self.ui.logo.setMinimumSize(100, 50)
            self.ui.frame_100.setMinimumSize(0, 0)


            self.ui.stopButton.setMinimumSize(36, 36)
            self.ui.playButton.setMinimumSize(36, 36)
            self.ui.pauseButton.setMinimumSize(36, 36)
            self.ui.frameButtonsSE.setStyleSheet(u"QPushButton {padding-left: 2px; text-align: center; background-color:#006d34;\n"
                                                                "border: 3px solid #009b4a; border-radius:18px; color: rgb(255, 255, 255)}\n")
            self.ui.muteButton.setMinimumSize(20, 20)
            self.ui.muteButton.setStyleSheet(u"QPushButton {border-radius: 10px;}")
            self.ui.resetButton.setMinimumSize(100, 30)
            self.ui.filterAudioButton.setMinimumSize(100, 30)


    def filterButton(self):
        self.ui.rightContent.setCurrentWidget(self.ui.filterPage)

    def pauseAndStopLayout(self, button):
        if button == "play":
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)
        else:
            self.ui.playButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)
            self.ui.pauseButton.setDisabled(True)

    def VolumeButton(self, currentVolume):
            if currentVolume == 0:
                self.ui.muteButton.setChecked(True)
            else:
                self.ui.muteButton.setChecked(False)

    def resetButton(self):
        for slider in self.sliders:
            eval("self.ui.slider_{}.setValue(0)".format(slider))
        self.ui.resetButton.setDisabled(True)
        self.ui.filterAudioButton.setEnabled(False)


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
                self.ui.calibrationButton.setDisabled(True)
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
            self.ui.calibrationButton.setDisabled(True)
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

    def selectItemLayout(self):
            self.ui.playButton.setEnabled(True)
            self.ui.calibrationButton.setEnabled(True)
            self.ui.muteButton.setEnabled(True)
            self.ui.volumeSlider.setEnabled(True)
