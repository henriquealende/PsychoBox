from BinauralTreatment.binaural_treatment import Calibration as cal
from PySide6.QtWidgets import QMessageBox

class SetCalibration():
    def __init__(self):
        super(SetCalibration, self).__init__()

    def changeTypeHead(self):
        type = self.ui.typeHeadBox_2.currentText()
        model_hats = self.ui.modelHatsBox_2.currentText()
        model_head = self.ui.modelHeadBox_2.currentText()
        if type == "Sennheiser":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHeadBox_2.addItems(['None', 'HD 600', 'HD 450X', 'HD 650'])
            self.ui.modelHeadBox_2.setEnabled(True)
        else:
            self.ui.modelHeadBox_2.clear()
            self.ui.modelHeadBox_2.setEnabled(False)
        if model_hats not in ("", "None") or model_head not in ("", "None"):
            self.ui.convolve.setEnabled(True)
        else: 
            self.ui.convolve.setEnabled(False)
            
    def changeTypeHats(self):
        type = self.ui.typeHatsBox_2.currentText()
        model_hats = self.ui.modelHatsBox_2.currentText()
        model_head = self.ui.modelHeadBox_2.currentText()
        if type == "HeadAcoustics":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.addItems(['None', 'HMS III.2', 'HMS III'])
            self.ui.modelHatsBox_2.setEnabled(True)
        elif type == "GRASS":
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.addItems(['None', 'Kemar'])
            self.ui.modelHatsBox_2.setEnabled(True)
        else:
            self.ui.modelHatsBox_2.clear()
            self.ui.modelHatsBox_2.setEnabled(False) 
        if model_hats not in ("", "None") or model_head not in ("", "None"):
            self.ui.convolve.setEnabled(True)
        else: 
            self.ui.convolve.setEnabled(False)
            
    def changeModelHeadHats(self):
        model_hats = self.ui.modelHatsBox_2.currentText()
        model_head = self.ui.modelHeadBox_2.currentText()
        if model_hats not in ("", "None") or model_head not in ("", "None"):
            self.ui.convolve.setEnabled(True)
        else: 
            self.ui.convolve.setEnabled(False)


        
        
        
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
            self.gp.domainBox.addItems(['Loudness Zwicker', 'Loudness ECMA', 'Sharpness DIN', 'Roughness DW', 'Roughness ECMA'])
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
                self.gp.y_min.setText('-1.0')
                self.gp.y_max.setText('1.0')
                self.gp.x_min.setText('0.0')
                self.gp.x_max.setText('10.0')
            elif domain == "Frequency":
                self.gp.y_min.setText('0.0')
                self.gp.y_max.setText('80.0')
                self.gp.x_min.setText('20.0')
                self.gp.x_max.setText('10000.0')
            elif domain == "Loudness Zwicker":
                self.gp.y_min.setText('0.0')
                self.gp.y_max.setText('10.0')
                self.gp.x_min.setText('0.0')
                self.gp.x_max.setText('25.0')
            elif domain == "Loudness ECMA":
                self.gp.y_min.setText('0.0')
                self.gp.y_max.setText('10.0')
                self.gp.x_min.setText('0.0')
                self.gp.x_max.setText('25.0')
            elif domain == "Sharpness":
                self.gp.y_min.setText('0.0')
                self.gp.y_max.setText('10.0')
                self.gp.x_min.setText('0.0')
                self.gp.x_max.setText('25.0')

    def convolve(self):
        model_hats = self.ui.modelHatsBox_2.currentText()
        model_head = self.ui.modelHeadBox_2.currentText()
        if model_hats not in ("", "None") or model_head not in ("", "None"):
            print("Convolvendo com os modelos:", model_hats, model_head)
            # Aqui você pode adicionar o código para a ação de convolução
        else:
            warning_box = QMessageBox()
            warning_box.setIcon(QMessageBox.Warning)
            warning_box.setWindowTitle("Atenção")
            warning_box.setText("Por favor, selecione um modelo para HATS ou Headphones antes de continuar.")
            warning_box.setStandardButtons(QMessageBox.Ok)
            warning_box.exec_()
