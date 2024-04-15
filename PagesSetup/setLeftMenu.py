from PySide2.QtCore import QPropertyAnimation
from PySide2.QtWidgets import QGraphicsOpacityEffect

class SetLeftMenu():
    def __init__(self):
        super(SetLeftMenu, self).__init__()

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
        #if self.online:
        self.ui.rightContent.setCurrentWidget(self.ui.welcomePage)
        self.ui.homeButton.setChecked(True)

    def calibrationButton(self):
        #if self.online:
        self.ui.rightContent.setCurrentWidget(self.ui.calibrationPage)
        self.ui.calibrationButton.setChecked(True)
        
    def filterButton(self):
        #if self.online:
        self.ui.rightContent.setCurrentWidget(self.ui.filterPage)
        self.ui.filterButton.setChecked(True)

