import pandas as pd

from expandGraph import *
from Database.database import *
from Utils.graph_utils import *
from Utils.filter_utils import *
from new_project import *



class UI_Buttons_Layout():
    def __init__(self):
        super(UI_Buttons_Layout, self).__init__()

############################# GENERAL SETTINGS #############################
    def closeAll(self):
        self.close()

    def minimize(self):
        self.showMinimized()

    def maximize(self, window):
        self.clique = self.clique +1

        if self.clique%2 == 1:
            if window == "expand":
                self.gp.infoBar3.setMinimumSize(16777215, 70)
                self.gp.frame_21.setMinimumSize(400, 16777215)
                self.gp.minimizeButton.setMaximumSize(24, 24)
                self.gp.closeAllButton.setMaximumSize(24, 24)
                self.gp.maximizeButton.setMaximumSize(24, 24)
                self.gp.frameButtons.setMinimumSize(150, 30)
                self.gp.frameButtons.setStyleSheet(u"QPushButton {border-radius: 12px}")

            else:
                #GERAL
                self.ui.topContent.setMinimumSize(16777215, 50)
                self.ui.frame_3.setMinimumSize(50, 70)
                self.ui.minimizeButton.setMaximumSize(24, 24)
                self.ui.closeAllButton.setMaximumSize(24, 24)
                self.ui.maximizeButton.setMaximumSize(24, 24)
                self.ui.frameButtons.setMinimumSize(150, 30)
                self.ui.frameButtons.setStyleSheet(u"QPushButton {border-radius: 12px}")


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

                #WELCOME
                self.ui.frame_17.setMinimumSize(0, 100)
                self.ui.welcomeUser.setMinimumSize(0, 140)
                self.ui.welcome.setMinimumSize(0, 60)
                self.ui.logo_2.setMinimumSize(150, 75)
                self.ui.newProject.setMinimumSize(0, 420)
                self.ui.settings.setMinimumSize(0, 400)
                self.ui.label_41.setMinimumSize(150, 150)
                self.ui.label_41.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_35.setMinimumSize(150, 150)
                self.ui.label_35.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_38.setMinimumSize(150, 150)
                self.ui.label_38.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")

                #LOGIN
                self.ui.settingLogin.setMinimumSize(0, 400)
                self.ui.loginFrame.setMinimumSize(350, 200)
                self.ui.frame_8.setMinimumSize(16777215, 20)
                self.ui.label_50.setMinimumSize(150, 150)
                self.ui.label_50.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_47.setMinimumSize(150, 150)
                self.ui.label_47.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_32.setMinimumSize(150, 150)
                self.ui.label_32.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 75px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")

                #CALIBRATION
                self.ui.SupCalibrationSetup.setMinimumSize(0, 110)
                self.ui.logo_3.setMinimumSize(150, 75)
                self.ui.RightCalibrationSetup.setMinimumSize(400, 0)
                self.ui.controlGraphFrame_2.setMinimumSize(400, 0)

            #self.showMaximized()
            self.showFullScreen()

        elif self.clique%2 == 0:
            if window == "expand":
                self.gp.infoBar3.setMinimumSize(16777215, 50)
                self.gp.frame_21.setMinimumSize(250, 16777215)
                self.gp.minimizeButton.setMaximumSize(20, 20)
                self.gp.closeAllButton.setMaximumSize(20, 20)
                self.gp.maximizeButton.setMaximumSize(20, 20)
                self.gp.frameButtons.setMinimumSize(120, 30)
                self.gp.frameButtons.setStyleSheet(u"QPushButton {border-radius: 10px}")

            else:
                #GERAL
                self.ui.topContent.setMinimumSize(16777215, 50)
                self.ui.frame_3.setMinimumSize(50, 50)
                self.ui.minimizeButton.setMaximumSize(20, 20)
                self.ui.closeAllButton.setMaximumSize(20, 20)
                self.ui.maximizeButton.setMaximumSize(20, 20)
                self.ui.frameButtons.setMinimumSize(120, 30)
                self.ui.frameButtons.setStyleSheet(u"QPushButton {border-radius: 10px}")

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


                #WELCOME
                self.ui.frame_17.setMinimumSize(0, 100)
                self.ui.welcomeUser.setMinimumSize(464, 80)
                self.ui.welcome.setMinimumSize(0, 50)
                self.ui.logo_2.setMinimumSize(100, 50)
                self.ui.newProject.setMinimumSize(0, 120)
                self.ui.settings.setMinimumSize(0, 250)
                self.ui.label_41.setMinimumSize(100, 100)
                self.ui.label_41.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_35.setMinimumSize(100, 100)
                self.ui.label_35.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_38.setMinimumSize(100, 100)
                self.ui.label_38.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")

                #LOGIN
                self.ui.settingLogin.setMinimumSize(0, 250)
                self.ui.frame_8.setMinimumSize(0, 0)
                self.ui.loginFrame.setMinimumSize(350, 150)
                self.ui.label_50.setMinimumSize(100, 100)
                self.ui.label_50.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_47.setMinimumSize(100, 100)
                self.ui.label_47.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")
                self.ui.label_32.setMinimumSize(100, 100)
                self.ui.label_32.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
                                                "border-radius: 50px; padding: 20px; border: 5px  inset rgb(237, 237, 237);")

                #CALIBRATION
                self.ui.SupCalibrationSetup.setMinimumSize(0, 80)
                self.ui.logo_3.setMinimumSize(100, 50)
                self.ui.RightCalibrationSetup.setMinimumSize(300, 0)
                #self.ui.controlGraphFrame_2.setMinimumSize(300, 0)

            self.showNormal()


############################# LEFT MENU #############################
    def toogleMenu(self):
        enable = True
        if enable:
            self.width = self.ui.leftMenu.width()
            self.widthMenu = self.ui.frame_3.width()
            maxWidth = 170
            minWidth = 50

            if self.width == minWidth:
                widthExtended = maxWidth
                self.ui.menuButton.setText('Menu')
                self.ui.menuButton.setMinimumWidth(maxWidth)
                self.ui.homeButton.setText('Home')
                self.ui.homeButton.setMinimumWidth(maxWidth)
                self.ui.settingsButton.setText('Settings')
                self.ui.settingsButton.setMinimumWidth(maxWidth)
                self.ui.filterButton.setText('Filters')
                self.ui.filterButton.setMinimumWidth(maxWidth)
                self.ui.calibrationButton.setText('Psycho')
                self.ui.calibrationButton.setMinimumWidth(maxWidth)
                if self.ui.userButton.isChecked():
                    self.ui.userButton.setText(
                        self.ui.usernameLabel.text()+'\nSair')
                else:
                    self.ui.userButton.setText("Offline")
                self.ui.userButton.setMinimumWidth(maxWidth)

            else:
                widthExtended = minWidth
                self.ui.menuButton.setText('')
                self.ui.menuButton.setMinimumWidth(maxWidth)
                self.ui.homeButton.setText('')
                self.ui.homeButton.setMinimumWidth(minWidth)
                self.ui.settingsButton.setText('')
                self.ui.settingsButton.setMinimumWidth(minWidth)
                self.ui.filterButton.setText('')
                self.ui.filterButton.setMinimumWidth(minWidth)
                self.ui.userButton.setText('')
                self.ui.userButton.setMinimumWidth(minWidth)
                self.ui.calibrationButton.setText('')
                self.ui.calibrationButton.setMinimumWidth(minWidth)
            # ANIMATION
            self.animation = QPropertyAnimation(
                self.ui.leftMenu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(self.width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()

            self.animation2 = QPropertyAnimation(
                self.ui.frame_3, b"minimumWidth")
            self.animation2.setDuration(400)
            self.animation2.setStartValue(self.widthMenu)
            self.animation2.setEndValue(widthExtended)
            self.animation2.start()

    def userButton(self):
        self.online = False
        self.ui.rightContent.setCurrentWidget(self.ui.loginPage)
        fadeIn = QGraphicsOpacityEffect(self.ui.mainContent)
        self.animation = QPropertyAnimation(
           fadeIn, b"opacity")
        self.ui.mainContent.setGraphicsEffect(fadeIn)
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        self.ui.userButton.setDisabled(True)
        self.ui.userButton.setChecked(False)
        self.ui.calibrationButton.setDisabled(True)
        self.ui.calibrationButton.setChecked(False)
        self.ui.filterButton.setDisabled(True)
        self.ui.filterButton.setChecked(False)
        self.ui.homeButton.setChecked(True)
        if self.ui.leftMenu.width() > 50:
            self.ui.userButton.setText("Offline")
        else:
            self.ui.userButton.setText("")

    def homeButton(self):
        if self.online:
            self.ui.rightContent.setCurrentWidget(self.ui.welcomePage)


############################# CALIBRATION PAGE SETTINGS #############################
    def selectGraph(self):
        condition = self.ui.mainBox.currentText()
        if condition != 'Time-Frequency':
            self.ui.domainBox.setDisabled(True)
            self.ui.samplingBox.setDisabled(True)
            self.ui.automaticCheckBox.setDisabled(True)
            self.ui.automaticCheckBox.setChecked(True)
            self.ui.spinBox.setDisabled(True)
            self.ui.spinBox_2.setDisabled(True)
            self.ui.spinBox_3.setDisabled(True)
            self.ui.spinBox_4.setDisabled(True)
            self.ui.applyButton.setDisabled(False)
        elif condition == 'Time-Frequency':
            self.ui.domainBox.setEnabled(True)
            self.ui.domainBox.setCurrentIndex(0)
            self.ui.samplingBox.setEnabled(False)
            self.ui.samplingBox.setCurrentIndex(0)
            self.ui.automaticCheckBox.setEnabled(True)
            self.ui.automaticCheckBox.setChecked(True)
            self.ui.applyButton.setEnabled(True)

    def selectMetrics(self):
        metrics = self.gp.mainBox.currentText()
        if metrics == "Metrics":
            self.gp.domainBox.clear()
            self.gp.domainBox.addItems(['Loudness', 'Sharpness', 'MPI'])
            self.gp.frame_samplingBox.hide()
        else:
            self.gp.domainBox.clear()
            self.gp.samplingBox.addItems(['Linear', '1/3 octave'])

    def selectDomain(self):
                domain = self.gp.domainBox.currentText()
                if domain == "Frequency":
                    self.gp.frame_samplingBox.show()
                else:
                    self.gp.frame_samplingBox.hide()

    def automaticCheckBox(self, window):
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


