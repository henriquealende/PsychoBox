class SetCalibration():
    def __init__(self):
        super(SetCalibration, self).__init__()

    def changeTypeHead(self):
        type = self.ui.typeHeadBox_2.currentText()
        if type == "Sennheiser":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHeadBox_2.addItems(['HD 600', 'HD 450X', 'HD 650'])
            self.ui.modelHeadBox_2.setEnabled(True)
        else:
            self.ui.modelHeadBox_2.clear()
            self.ui.modelHeadBox_2.setEnabled(False)

    def changeTypeHats(self):
        type = self.ui.typeHatsBox_2.currentText()
        if type == "HeadAcoustics":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.addItems(['HMS III.2', 'HMS III'])
            self.ui.modelHatsBox_2.setEnabled(True)
        elif type == "GRASS":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.addItems(['Kemar'])
            self.ui.modelHatsBox_2.setEnabled(True)
        else:
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.setEnabled(False)

    def windowLayout(self, parameter):
        if parameter == "maximazed":
            self.ui.SupCalibrationSetup.setMinimumSize(0, 110)
            self.ui.logo_3.setMinimumSize(150, 75)
            self.ui.RightCalibrationSetup.setMinimumSize(400, 0)
        else:
            self.ui.SupCalibrationSetup.setMinimumSize(0, 80)
            self.ui.logo_3.setMinimumSize(100, 50)
            self.ui.RightCalibrationSetup.setMinimumSize(300, 0)

    def selectMetrics(self):
        metrics = self.gp.mainBox.currentText()
        if metrics == "Metrics":
            self.gp.domainBox.clear()
            self.gp.domainBox.addItems(['Loudness Zwicker', 'Loudness ECMA', 'Sharpness', 'IPM'])
            self.gp.frame_samplingBox.hide()
        else:
            self.gp.domainBox.clear()
            self.gp.domainBox.addItems(['Time', 'Frequency'])
            self.gp.samplingBox.addItems(['Linear', '1/3 octave'])

    def selectDomain(self):
        domain = self.gp.domainBox.currentText()
        if domain == "Frequency":
            self.gp.frame_samplingBox.show()
        else:
            self.gp.frame_samplingBox.hide()

    def automaticCheckBox(self):
        domain = self.gp.domainBox.currentText()
        if self.gp.automaticCheckBox.isChecked():
            self.gp.frame_axis.hide()
        else:
            self.gp.frame_axis.show()
            if domain == 'Time':
                self.gp.spinBox.setValue(-1)
                self.gp.spinBox_2.setValue(1)
                self.gp.spinBox_3.setValue(0)
                self.gp.spinBox_4.setValue(10)
            elif domain == "Frequency":
                self.gp.spinBox.setValue(0)
                self.gp.spinBox_2.setValue(80)
                self.gp.spinBox_3.setValue(20)
                self.gp.spinBox_4.setValue(10000)
            elif domain == "Loudness Zwicker":
                self.gp.spinBox.setValue(0)
                self.gp.spinBox_2.setValue(10)
                self.gp.spinBox_3.setValue(0)
                self.gp.spinBox_4.setValue(25)
            elif domain == "Loudness ECMA":
                self.gp.spinBox.setValue(0)
                self.gp.spinBox_2.setValue(10)
                self.gp.spinBox_3.setValue(0)
                self.gp.spinBox_4.setValue(25)
            elif domain == "Sharpness":
                self.gp.spinBox.setValue(0)
                self.gp.spinBox_2.setValue(10)
                self.gp.spinBox_3.setValue(0)
                self.gp.spinBox_4.setValue(25)

