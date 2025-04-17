# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import Resources.rc_resourceGUI

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1192, 789)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topContent = QFrame(self.centralwidget)
        self.topContent.setObjectName(u"topContent")
        self.topContent.setMinimumSize(QSize(0, 50))
        self.topContent.setMaximumSize(QSize(16777215, 70))
        self.topContent.setSizeIncrement(QSize(0, 0))
        self.topContent.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.topContent)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.topContent)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(50, 50))
        self.frame_3.setMaximumSize(QSize(50, 70))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QPushButton {\n"
"	padding-left: 10px;\n"
"	text-align: left;\n"
"	background-color: rgb(70,70,70);\n"
"	border:none;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(140,140,140)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 82, 26)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: rgb(70, 70, 70);\n"
"	padding-left: 5px;\n"
"	border-left: 5px solid  rgb(255, 82,26);\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame_3)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(50, 50))
        self.menuButton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"PF BeauSans Pro"])
        font.setPointSize(16)
        font.setBold(True)
        self.menuButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/img/menuEnabled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(30, 30))
        self.menuButton.setCheckable(False)
        self.menuButton.setChecked(False)
        self.menuButton.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.menuButton)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.infoBar = QFrame(self.topContent)
        self.infoBar.setObjectName(u"infoBar")
        self.infoBar.setStyleSheet(u"QFrame{\n"
"	background-color : rgb(117, 117, 117);\n"
"}")
        self.infoBar.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.infoBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.infoBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/logos/img/psychobox_logo2.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frameButtons = QFrame(self.infoBar)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setMaximumSize(QSize(120, 30))
        self.frameButtons.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"}")
        self.frameButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frameButtons)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.minimizeButton = QPushButton(self.frameButtons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffbe38;\n"
"	border: 2px solid  #d5a342;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 58)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeButton.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.frameButtons)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(20, 20))
        self.maximizeButton.setMaximumSize(QSize(20, 20))
        self.maximizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color:  rgb(237, 105, 59);\n"
"	border: 2px solid rgb(184, 80, 45) ;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(220, 147, 0)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/maximizar-janela.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeButton.setIcon(icon2)
        self.maximizeButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_7.addWidget(self.maximizeButton)

        self.closeAllButton = QPushButton(self.frameButtons)
        self.closeAllButton.setObjectName(u"closeAllButton")
        self.closeAllButton.setMaximumSize(QSize(20, 20))
        self.closeAllButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #fc5753;\n"
"	border: 2px solid  #cf5254;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 119, 119)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAllButton.setIcon(icon3)
        self.closeAllButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_7.addWidget(self.closeAllButton)


        self.horizontalLayout_5.addWidget(self.frameButtons)


        self.horizontalLayout_2.addWidget(self.infoBar)


        self.verticalLayout.addWidget(self.topContent)

        self.centerContent = QFrame(self.centralwidget)
        self.centerContent.setObjectName(u"centerContent")
        self.centerContent.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.centerContent)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.centerContent)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(50, 0))
        self.leftMenu.setMaximumSize(QSize(50, 16777215))
        self.leftMenu.setSizeIncrement(QSize(0, 0))
        self.leftMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenu)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setFamilies([u"PF BeauSans Pro"])
        font1.setBold(True)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"}\n"
"QPushButton {\n"
"	padding-left: 10px;\n"
"	text-align: left;\n"
"	background-color: rgb(182, 182, 182);\n"
"	border:none;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(80, 184, 158)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 184, 158);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:rgb(80, 184, 158);\n"
"	padding-left: 5px;\n"
"	border-left: 5px solid  rgb(80, 184, 158);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.frame)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(50, 49))
        self.homeButton.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"PF BeauSans Pro"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.homeButton.setFont(font2)
        self.homeButton.setStyleSheet(u"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:5px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/homeEnabled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeButton.setIcon(icon4)
        self.homeButton.setIconSize(QSize(30, 30))
        self.homeButton.setCheckable(True)
        self.homeButton.setChecked(True)
        self.homeButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.homeButton)

        self.recordingButton = QPushButton(self.frame)
        self.recordingButton.setObjectName(u"recordingButton")
        self.recordingButton.setMinimumSize(QSize(50, 50))
        self.recordingButton.setFont(font2)
        self.recordingButton.setStyleSheet(u"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:5px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/microfone.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.recordingButton.setIcon(icon5)
        self.recordingButton.setIconSize(QSize(30, 30))
        self.recordingButton.setCheckable(True)
        self.recordingButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.recordingButton)

        self.filterButton = QPushButton(self.frame)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setEnabled(True)
        self.filterButton.setMinimumSize(QSize(50, 50))
        self.filterButton.setMaximumSize(QSize(16777215, 16777215))
        self.filterButton.setFont(font2)
        self.filterButton.setToolTipDuration(-1)
        self.filterButton.setStyleSheet(u"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:5px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/img/equalizerEnable.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filterButton.setIcon(icon6)
        self.filterButton.setIconSize(QSize(30, 30))
        self.filterButton.setCheckable(True)
        self.filterButton.setChecked(False)
        self.filterButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.filterButton)

        self.calibrationButton = QPushButton(self.frame)
        self.calibrationButton.setObjectName(u"calibrationButton")
        self.calibrationButton.setEnabled(True)
        self.calibrationButton.setMinimumSize(QSize(50, 50))
        self.calibrationButton.setMaximumSize(QSize(16777215, 16777215))
        self.calibrationButton.setFont(font2)
        self.calibrationButton.setStyleSheet(u"QPushButton{\n"
"	padding-left:6px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:#rgb(80, 184, 158);\n"
"	padding-left:1px;\n"
"	border-left: 5px solid  rgb(241, 102, 55);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/img/calibration.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calibrationButton.setIcon(icon7)
        self.calibrationButton.setIconSize(QSize(40, 40))
        self.calibrationButton.setCheckable(True)
        self.calibrationButton.setChecked(False)
        self.calibrationButton.setAutoRepeat(False)
        self.calibrationButton.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.calibrationButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 100))
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 0, 0, -1)
        self.userButton = QPushButton(self.frame_9)
        self.userButton.setObjectName(u"userButton")
        self.userButton.setEnabled(False)
        self.userButton.setMinimumSize(QSize(50, 50))
        self.userButton.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"PF BeauSans Pro"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.userButton.setFont(font3)
        self.userButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.userButton.setStyleSheet(u"QPushButton:checked {\n"
"	color: rgb(0, 196, 204);\n"
"	border-radius:25px;\n"
"	padding-left:9px\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/img/userEnabled.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.userButton.setIcon(icon8)
        self.userButton.setIconSize(QSize(20, 20))
        self.userButton.setCheckable(True)
        self.userButton.setChecked(False)

        self.verticalLayout_4.addWidget(self.userButton)

        self.settingsButton = QPushButton(self.frame_9)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setEnabled(False)
        self.settingsButton.setMinimumSize(QSize(50, 50))
        self.settingsButton.setMaximumSize(QSize(16777215, 16777215))
        self.settingsButton.setFont(font3)
        self.settingsButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/icons/img/settingsEnable.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon9)
        self.settingsButton.setIconSize(QSize(20, 20))
        self.settingsButton.setCheckable(True)
        self.settingsButton.setChecked(False)

        self.verticalLayout_4.addWidget(self.settingsButton)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_2.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.rightContent = QStackedWidget(self.centerContent)
        self.rightContent.setObjectName(u"rightContent")
        self.rightContent.setEnabled(True)
        self.rightContent.setFont(font1)
        self.rightContent.setFrameShape(QFrame.Shape.NoFrame)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.horizontalLayout_10 = QHBoxLayout(self.welcomePage)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mainContent_2 = QFrame(self.welcomePage)
        self.mainContent_2.setObjectName(u"mainContent_2")
        self.mainContent_2.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.mainContent_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.mainContent_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.mainContent_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 10)
        self.welcomeUser = QFrame(self.frame_17)
        self.welcomeUser.setObjectName(u"welcomeUser")
        self.welcomeUser.setMinimumSize(QSize(0, 0))
        self.welcomeUser.setMaximumSize(QSize(16777215, 16777215))
        self.welcomeUser.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.welcomeUser)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 5, 0, 0)
        self.welcome = QLabel(self.welcomeUser)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(0, 50))
        self.welcome.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setFamilies([u"PF BeauSans Pro"])
        font4.setPointSize(28)
        font4.setBold(True)
        self.welcome.setFont(font4)
        self.welcome.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.verticalLayout_10.addWidget(self.welcome)


        self.horizontalLayout_12.addWidget(self.welcomeUser)


        self.verticalLayout_9.addWidget(self.frame_17)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 450))
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(30, 0, 0, 0)
        self.logo_2 = QLabel(self.frame_19)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setMinimumSize(QSize(300, 125))
        self.logo_2.setMaximumSize(QSize(300, 125))
        self.logo_2.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo_2.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.logo_2)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.settings = QFrame(self.frame_16)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 250))
        self.settings.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.settings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.settings)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(6, 0, 6, 6)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 0))
        self.frame_44.setMaximumSize(QSize(16777215, 16777215))
        self.frame_44.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.frame_44.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_23 = QVBoxLayout(self.frame_44)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(11, 11, 11, 11)
        self.label_43 = QLabel(self.frame_44)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 40))
        self.label_43.setMaximumSize(QSize(16777215, 40))
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(u"color: rgb(237, 237, 237);")

        self.verticalLayout_23.addWidget(self.label_43)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 0)
        self.label_32 = QLabel(self.frame_45)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 100))
        self.label_32.setMaximumSize(QSize(100, 100))
        self.label_32.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"\n"
"border-radius: 50px;\n"
"padding: 20px;\n"
"border: 5px  solid rgb(237, 237, 237);")
        self.label_32.setPixmap(QPixmap(u":/icons/img/importAudio.png"))
        self.label_32.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_32)


        self.verticalLayout_23.addWidget(self.frame_45)

        self.label_45 = QLabel(self.frame_44)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 70))
        self.label_45.setMaximumSize(QSize(16777215, 80))
        font5 = QFont()
        font5.setFamilies([u"PF BeauSans Pro"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.label_45.setFont(font5)
        self.label_45.setStyleSheet(u"color: rgb(237, 237, 237);")

        self.verticalLayout_23.addWidget(self.label_45)


        self.horizontalLayout_25.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.frame_46.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_24 = QVBoxLayout(self.frame_46)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_46 = QLabel(self.frame_46)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 40))
        self.label_46.setMaximumSize(QSize(16777215, 40))
        self.label_46.setFont(font)
        self.label_46.setStyleSheet(u"color: rgb(237, 237, 237);")

        self.verticalLayout_24.addWidget(self.label_46)

        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.label_47 = QLabel(self.frame_47)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(100, 100))
        self.label_47.setMaximumSize(QSize(100, 100))
        self.label_47.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"border-radius: 50px;\n"
"padding: 20px;\n"
"border: 5px  inset rgb(237, 237, 237);")
        self.label_47.setPixmap(QPixmap(u":/icons/img/filter.png"))
        self.label_47.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_47)


        self.verticalLayout_24.addWidget(self.frame_47)

        self.label_48 = QLabel(self.frame_46)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 70))
        self.label_48.setMaximumSize(QSize(16777215, 80))
        self.label_48.setFont(font5)
        self.label_48.setStyleSheet(u"color: rgb(237, 237, 237);")

        self.verticalLayout_24.addWidget(self.label_48)


        self.horizontalLayout_25.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.frame_43)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.frame_48.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_25 = QVBoxLayout(self.frame_48)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_49 = QLabel(self.frame_48)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 40))
        self.label_49.setMaximumSize(QSize(16777215, 40))
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"color: rgb(237, 237, 237);")

        self.verticalLayout_25.addWidget(self.label_49)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, 0)
        self.label_50 = QLabel(self.frame_49)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(100, 100))
        self.label_50.setMaximumSize(QSize(100, 100))
        self.label_50.setStyleSheet(u"background-color:  qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"border-radius: 50px;\n"
"padding: 20px;\n"
"border: 5px  inset rgb(237, 237, 237);")
        self.label_50.setPixmap(QPixmap(u":/icons/img/metricas.png"))
        self.label_50.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_50)


        self.verticalLayout_25.addWidget(self.frame_49)

        self.label_51 = QLabel(self.frame_48)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 70))
        self.label_51.setMaximumSize(QSize(16777215, 80))
        self.label_51.setFont(font5)
        self.label_51.setStyleSheet(u"color: rgb(237, 237, 237);")

        self.verticalLayout_25.addWidget(self.label_51)


        self.horizontalLayout_25.addWidget(self.frame_48)


        self.verticalLayout_13.addWidget(self.frame_43)


        self.verticalLayout_11.addWidget(self.settings)


        self.horizontalLayout_13.addWidget(self.frame_16)


        self.verticalLayout_9.addWidget(self.frame_10)


        self.verticalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_10.addWidget(self.mainContent_2)

        self.rightContent.addWidget(self.welcomePage)
        self.recordingPage = QWidget()
        self.recordingPage.setObjectName(u"recordingPage")
        self.verticalLayout_14 = QVBoxLayout(self.recordingPage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.recordingPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 80))
        self.frame_11.setMaximumSize(QSize(16777215, 80))
        self.frame_11.setStyleSheet(u"color: rgb(70, 70, 70); ")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 9, -1)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 50))
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.logo_4 = QLabel(self.frame_11)
        self.logo_4.setObjectName(u"logo_4")
        self.logo_4.setMinimumSize(QSize(130, 50))
        self.logo_4.setMaximumSize(QSize(130, 50))
        self.logo_4.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo_4.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.logo_4)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 100))
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"QPushButton {\n"
"	padding-left: 2px;\n"
"	text-align: center;\n"
"	background-color:rgb(80, 184, 158);\n"
"	border: 3px solid rgb(237, 105, 59);\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"")
        self.frame_18.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setSpacing(9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.recordingButton_2 = QPushButton(self.frame_18)
        self.recordingButton_2.setObjectName(u"recordingButton_2")
        self.recordingButton_2.setEnabled(False)
        self.recordingButton_2.setMinimumSize(QSize(50, 50))
        self.recordingButton_2.setMaximumSize(QSize(50, 50))
        self.recordingButton_2.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(94, 217, 186);\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/img/botao-de-gravacao_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/img/botao-de-gravacao.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon10.addFile(u":/icons/img/botao-de-gravacao_2_w.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        icon10.addFile(u":/icons/img/botao-de-gravacao_w.png", QSize(), QIcon.Mode.Disabled, QIcon.State.On)
        self.recordingButton_2.setIcon(icon10)
        self.recordingButton_2.setIconSize(QSize(30, 32))
        self.recordingButton_2.setCheckable(True)
        self.recordingButton_2.setChecked(False)

        self.horizontalLayout_16.addWidget(self.recordingButton_2)

        self.playButton_2 = QPushButton(self.frame_18)
        self.playButton_2.setObjectName(u"playButton_2")
        self.playButton_2.setEnabled(False)
        self.playButton_2.setMinimumSize(QSize(36, 36))
        self.playButton_2.setMaximumSize(QSize(36, 36))
        self.playButton_2.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/img/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playButton_2.setIcon(icon11)
        self.playButton_2.setIconSize(QSize(15, 25))

        self.horizontalLayout_16.addWidget(self.playButton_2)

        self.pauseButton_2 = QPushButton(self.frame_18)
        self.pauseButton_2.setObjectName(u"pauseButton_2")
        self.pauseButton_2.setEnabled(False)
        self.pauseButton_2.setMinimumSize(QSize(36, 36))
        self.pauseButton_2.setMaximumSize(QSize(36, 36))
        self.pauseButton_2.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/img/pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pauseButton_2.setIcon(icon12)
        self.pauseButton_2.setIconSize(QSize(15, 25))

        self.horizontalLayout_16.addWidget(self.pauseButton_2)

        self.stopButton_2 = QPushButton(self.frame_18)
        self.stopButton_2.setObjectName(u"stopButton_2")
        self.stopButton_2.setEnabled(False)
        self.stopButton_2.setMinimumSize(QSize(36, 36))
        self.stopButton_2.setMaximumSize(QSize(36, 36))
        self.stopButton_2.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/img/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stopButton_2.setIcon(icon13)
        self.stopButton_2.setIconSize(QSize(13, 25))

        self.horizontalLayout_16.addWidget(self.stopButton_2)

        self.frame_23 = QFrame(self.frame_18)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 3px 23px 3px 3px;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"	color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"	image: url(:/icons/img/downArrowDis.png);\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border : 3px solid rgb(255, 161, 78);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/img/downArrow.png);\n"
"	width : 12px;\n"
"}\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" \n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"")
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_5 = QLabel(self.frame_23)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"PF BeauSans Pro"])
        font6.setPointSize(14)
        self.label_5.setFont(font6)

        self.horizontalLayout_19.addWidget(self.label_5)

        self.samplingRate_Combo = QComboBox(self.frame_23)
        self.samplingRate_Combo.addItem("")
        self.samplingRate_Combo.addItem("")
        self.samplingRate_Combo.addItem("")
        self.samplingRate_Combo.setObjectName(u"samplingRate_Combo")
        self.samplingRate_Combo.setEnabled(True)
        self.samplingRate_Combo.setMinimumSize(QSize(208, 30))
        self.samplingRate_Combo.setMaximumSize(QSize(150, 30))
        font7 = QFont()
        font7.setFamilies([u"PF BeauSans Pro"])
        font7.setPointSize(12)
        self.samplingRate_Combo.setFont(font7)
        self.samplingRate_Combo.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.samplingRate_Combo.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.horizontalLayout_19.addWidget(self.samplingRate_Combo)

        self.label_6 = QLabel(self.frame_23)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)

        self.horizontalLayout_19.addWidget(self.label_6)


        self.horizontalLayout_16.addWidget(self.frame_23)


        self.horizontalLayout_14.addWidget(self.frame_18)

        self.frame_22 = QFrame(self.frame_13)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QPushButton {\n"
"	padding-left: 2px;\n"
"	text-align: center;\n"
"	background-color:rgb(80, 184, 158);\n"
"	border: 3px solid rgb(237, 105, 59);\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"")
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_19 = QVBoxLayout(self.frame_24)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.setMicrophone_1 = QPushButton(self.frame_24)
        self.setMicrophone_1.setObjectName(u"setMicrophone_1")
        self.setMicrophone_1.setEnabled(True)
        self.setMicrophone_1.setMinimumSize(QSize(50, 50))
        self.setMicrophone_1.setMaximumSize(QSize(50, 50))
        self.setMicrophone_1.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	  background-color: rgb(94, 217, 186);\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/img/microfone_w.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/icons/img/microfone.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setMicrophone_1.setIcon(icon14)
        self.setMicrophone_1.setIconSize(QSize(26, 26))
        self.setMicrophone_1.setCheckable(True)
        self.setMicrophone_1.setChecked(False)

        self.verticalLayout_19.addWidget(self.setMicrophone_1)

        self.label_8 = QLabel(self.frame_24)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.verticalLayout_19.addWidget(self.label_8)


        self.horizontalLayout_20.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_20 = QVBoxLayout(self.frame_25)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.setMicrophone_2 = QPushButton(self.frame_25)
        self.setMicrophone_2.setObjectName(u"setMicrophone_2")
        self.setMicrophone_2.setEnabled(False)
        self.setMicrophone_2.setMinimumSize(QSize(50, 50))
        self.setMicrophone_2.setMaximumSize(QSize(50, 50))
        self.setMicrophone_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	  background-color: rgb(94, 217, 186);\n"
"}\n"
"")
        self.setMicrophone_2.setIcon(icon14)
        self.setMicrophone_2.setIconSize(QSize(26, 26))
        self.setMicrophone_2.setCheckable(True)
        self.setMicrophone_2.setChecked(False)

        self.verticalLayout_20.addWidget(self.setMicrophone_2)

        self.label_10 = QLabel(self.frame_25)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.verticalLayout_20.addWidget(self.label_10)


        self.horizontalLayout_20.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_21 = QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.setSource_1 = QPushButton(self.frame_26)
        self.setSource_1.setObjectName(u"setSource_1")
        self.setSource_1.setEnabled(False)
        self.setSource_1.setMinimumSize(QSize(50, 50))
        self.setSource_1.setMaximumSize(QSize(50, 50))
        self.setSource_1.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	  background-color: rgb(94, 217, 186);\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/img/dodecaedro.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon15.addFile(u":/icons/img/dodecaedro_o.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setSource_1.setIcon(icon15)
        self.setSource_1.setIconSize(QSize(32, 32))
        self.setSource_1.setCheckable(True)
        self.setSource_1.setChecked(False)

        self.verticalLayout_21.addWidget(self.setSource_1)

        self.label_11 = QLabel(self.frame_26)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font7)

        self.verticalLayout_21.addWidget(self.label_11)


        self.horizontalLayout_20.addWidget(self.frame_26)

        self.horizontalSpacer_3 = QSpacerItem(244, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_3)

        self.exportAudioButton = QPushButton(self.frame_22)
        self.exportAudioButton.setObjectName(u"exportAudioButton")
        self.exportAudioButton.setEnabled(False)
        self.exportAudioButton.setMinimumSize(QSize(50, 50))
        self.exportAudioButton.setMaximumSize(QSize(50, 50))
        self.exportAudioButton.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(94, 217, 186);\n"
"	border-radius:25px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/icons/img/exportar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportAudioButton.setIcon(icon16)
        self.exportAudioButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_20.addWidget(self.exportAudioButton)


        self.horizontalLayout_14.addWidget(self.frame_22)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.recordingFrame = QFrame(self.frame_14)
        self.recordingFrame.setObjectName(u"recordingFrame")
        self.recordingFrame.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout.addWidget(self.recordingFrame, 0, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 100))
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_17.addWidget(self.frame_15)


        self.verticalLayout_15.addWidget(self.frame_12)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.rightContent.addWidget(self.recordingPage)
        self.filterPage = QWidget()
        self.filterPage.setObjectName(u"filterPage")
        self.filterPage.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.filterPage)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.title = QFrame(self.filterPage)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 80))
        self.title.setMaximumSize(QSize(16777215, 80))
        self.title.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.title)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.title)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(464, 80))
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.frame_20)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 10, 0, 0)
        self.label_9 = QLabel(self.frame_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 0))
        self.label_9.setMaximumSize(QSize(16777215, 50))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.verticalLayout_22.addWidget(self.label_9)


        self.horizontalLayout_15.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.title)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_26 = QVBoxLayout(self.frame_21)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(9, 9, 9, 9)
        self.logo = QLabel(self.frame_21)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(130, 50))
        self.logo.setMaximumSize(QSize(130, 50))
        self.logo.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo.setScaledContents(True)

        self.verticalLayout_26.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_15.addWidget(self.frame_21)


        self.verticalLayout_28.addWidget(self.title)

        self.controlFrame = QFrame(self.filterPage)
        self.controlFrame.setObjectName(u"controlFrame")
        self.controlFrame.setEnabled(True)
        self.controlFrame.setMinimumSize(QSize(0, 0))
        self.controlFrame.setSizeIncrement(QSize(0, 0))
        self.controlFrame.setStyleSheet(u"\n"
"\n"
"QSlider::groove:vertical {\n"
"				background:  rgb(80, 184, 158);\n"
"                 width:10px;\n"
"				height: 100px;\n"
"				border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"            border: 0px rgb(255, 255, 255);\n"
"            border-style: outset;\n"
"			 border-radius: 2px;\n"
"            margin: 0px -2px;\n"
"            width: 10px;\n"
"            height: 10px;\n"
"            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"       background-color:  rgb(182,182,182);\n"
"	   border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:disabled{\n"
"			background-color: rgb(32, 59, 60); \n"
"}\n"
"QSlider::groove:vertical:disabled {\n"
"           background-color:  #006d34;\n"
"			\n"
"}\n"
"QSlider::sub-page:vertical:disabled{\n"
"		background: #4B4B4B;\n"
"}\n"
"")
        self.controlFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_29 = QVBoxLayout(self.controlFrame)
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 6)
        self.playerFrame = QFrame(self.controlFrame)
        self.playerFrame.setObjectName(u"playerFrame")
        self.playerFrame.setMaximumSize(QSize(16777212, 160))
        self.playerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_59 = QVBoxLayout(self.playerFrame)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 6, -1)
        self.playerFrame_2 = QFrame(self.playerFrame)
        self.playerFrame_2.setObjectName(u"playerFrame_2")
        self.playerFrame_2.setEnabled(True)
        self.playerFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.playerFrame_2.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.playerFrame_2)
        self.horizontalLayout_17.setSpacing(30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, 0, 20, 0)
        self.importAudio = QFrame(self.playerFrame_2)
        self.importAudio.setObjectName(u"importAudio")
        self.importAudio.setMinimumSize(QSize(0, 100))
        self.importAudio.setMaximumSize(QSize(16777215, 16777215))
        self.importAudio.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_29 = QHBoxLayout(self.importAudio)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.importAudio)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 0))
        self.frame_52.setMaximumSize(QSize(16777215, 16777215))
        self.frame_52.setSizeIncrement(QSize(0, 0))
        self.frame_52.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.frame_52)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"PF BeauSans Pro"])
        font8.setPointSize(14)
        font8.setBold(True)
        self.listWidget.setFont(font8)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	border : 4px solid rgb(80, 184, 158);\n"
"	border-radius:10px;\n"
"	background : rgb(70, 70, 70);\n"
"}\n"
"\n"
"QListWidget:hover {\n"
"	border : 4px solid rgb(255, 161, 78);\n"
"}\n"
"\n"
"\n"
" QListView::item:selected {\n"
"	border : 2px solid #009b4a;\n"
"	background : rgb(97, 176, 155);\n"
"}\n"
"\n"
"QListView::item {\n"
"	padding-right:10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"")
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)

        self.horizontalLayout_30.addWidget(self.listWidget)


        self.horizontalLayout_29.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.importAudio)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMinimumSize(QSize(150, 0))
        self.frame_53.setMaximumSize(QSize(16777215, 16777215))
        self.frame_53.setStyleSheet(u"\n"
"QPushButton {\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"	background-color: rgb(80, 184, 158);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(237, 105, 59)\n"
"}\n"
"")
        self.frame_53.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_55 = QVBoxLayout(self.frame_53)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.importButton = QPushButton(self.frame_53)
        self.importButton.setObjectName(u"importButton")
        self.importButton.setMinimumSize(QSize(0, 30))
        self.importButton.setFont(font5)
        self.importButton.setIconSize(QSize(20, 20))

        self.verticalLayout_55.addWidget(self.importButton)

        self.removeButton = QPushButton(self.frame_53)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setMinimumSize(QSize(0, 30))
        self.removeButton.setFont(font5)
        self.removeButton.setIconSize(QSize(16, 16))

        self.verticalLayout_55.addWidget(self.removeButton)

        self.removeAllButton = QPushButton(self.frame_53)
        self.removeAllButton.setObjectName(u"removeAllButton")
        self.removeAllButton.setMinimumSize(QSize(0, 30))
        self.removeAllButton.setFont(font5)

        self.verticalLayout_55.addWidget(self.removeAllButton)


        self.horizontalLayout_29.addWidget(self.frame_53)


        self.horizontalLayout_17.addWidget(self.importAudio)

        self.buttons = QFrame(self.playerFrame_2)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 0))
        self.buttons.setMaximumSize(QSize(300, 16777215))
        self.buttons.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"")
        self.buttons.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.buttons)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.buttons)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"")
        self.frame_55.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_57 = QVBoxLayout(self.frame_55)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frameButtonsSE = QFrame(self.frame_55)
        self.frameButtonsSE.setObjectName(u"frameButtonsSE")
        self.frameButtonsSE.setEnabled(True)
        self.frameButtonsSE.setStyleSheet(u"QPushButton {\n"
"	padding-left: 2px;\n"
"	text-align: center;\n"
"	background-color:rgb(80, 184, 158);\n"
"	border: 3px solid rgb(237, 105, 59);\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"")
        self.frameButtonsSE.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_31 = QHBoxLayout(self.frameButtonsSE)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.playButton = QPushButton(self.frameButtonsSE)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setEnabled(False)
        self.playButton.setMinimumSize(QSize(36, 36))
        self.playButton.setMaximumSize(QSize(36, 36))
        self.playButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        self.playButton.setIcon(icon11)
        self.playButton.setIconSize(QSize(15, 25))

        self.horizontalLayout_31.addWidget(self.playButton)

        self.pauseButton = QPushButton(self.frameButtonsSE)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setEnabled(False)
        self.pauseButton.setMinimumSize(QSize(36, 36))
        self.pauseButton.setMaximumSize(QSize(36, 36))
        self.pauseButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        self.pauseButton.setIcon(icon12)
        self.pauseButton.setIconSize(QSize(15, 25))

        self.horizontalLayout_31.addWidget(self.pauseButton)

        self.stopButton = QPushButton(self.frameButtonsSE)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        self.stopButton.setMinimumSize(QSize(36, 36))
        self.stopButton.setMaximumSize(QSize(36, 36))
        self.stopButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(79,186,160);\n"
"	border: 3px solid rgb(0,124,132);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(70,70,70);\n"
"	border: 3px solid rgb(136,138,133);\n"
"}\n"
"\n"
"")
        self.stopButton.setIcon(icon13)
        self.stopButton.setIconSize(QSize(13, 25))

        self.horizontalLayout_31.addWidget(self.stopButton)


        self.verticalLayout_57.addWidget(self.frameButtonsSE)


        self.verticalLayout_5.addWidget(self.frame_55)

        self.frame_27 = QFrame(self.buttons)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setEnabled(True)
        self.frame_27.setStyleSheet(u"QSlider::groove:horizontal {				\n"
"				background-color: rgb(218, 218, 218);\n"
"				height: 10px;\n"
"				 border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"            border: 0px rgb(255, 255, 255);\n"
"            border-style: outset;\n"
"			 border-radius: 2px;\n"
"            margin: -2px 0;\n"
"            width: 20px;\n"
"            height: 20px;\n"
"            background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"       background-color: rgb(80, 184, 158);\n"
"	   border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:disabled{\n"
"			background-color: rgb(32, 59, 60); \n"
"	 		border: 0px rgb(48, 82, 83);\n"
"}\n"
"QSlider::groove:horizontal:disabled {\n"
"           background-color: #4B4B4B;\n"
"			\n"
"}\n"
"QSlider::sub-page:horizontal:disabled{\n"
"		background:  #006d34;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: qradi"
                        "algradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color:#fc5753;	\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color:#006d34;	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #009b4a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"")
        self.frame_27.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(50, 0, 50, 0)
        self.muteButton = QPushButton(self.frame_27)
        self.muteButton.setObjectName(u"muteButton")
        self.muteButton.setEnabled(False)
        self.muteButton.setMinimumSize(QSize(20, 20))
        self.muteButton.setMaximumSize(QSize(20, 20))
        self.muteButton.setStyleSheet(u"QPushButton {\n"
"	border-radius:10px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/img/volume-alto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon17.addFile(u":/icons/img/volume-mute.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon17.addFile(u":/icons/img/volume-mute.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        self.muteButton.setIcon(icon17)
        self.muteButton.setCheckable(True)
        self.muteButton.setChecked(False)
        self.muteButton.setAutoRepeat(False)

        self.horizontalLayout_18.addWidget(self.muteButton)

        self.volumeSlider = QSlider(self.frame_27)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setEnabled(False)
        self.volumeSlider.setValue(50)
        self.volumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_18.addWidget(self.volumeSlider)


        self.verticalLayout_5.addWidget(self.frame_27)

        self.frame_2 = QFrame(self.buttons)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 150))
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(79,186,160,255), stop:1 rgba(0,124,132, 255));\n"
"	}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"	background-color:rgb(70, 70, 70);\n"
"	color: rgb(136,138,133);\n"
"	}\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.filterAudioButton = QPushButton(self.frame_2)
        self.filterAudioButton.setObjectName(u"filterAudioButton")
        self.filterAudioButton.setEnabled(False)
        self.filterAudioButton.setMinimumSize(QSize(100, 30))
        self.filterAudioButton.setMaximumSize(QSize(100, 30))
        self.filterAudioButton.setFont(font5)

        self.horizontalLayout_21.addWidget(self.filterAudioButton)

        self.resetButton = QPushButton(self.frame_2)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setEnabled(False)
        self.resetButton.setMinimumSize(QSize(100, 30))
        self.resetButton.setMaximumSize(QSize(100, 30))
        self.resetButton.setFont(font5)
        self.resetButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.resetButton.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.resetButton)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_17.addWidget(self.buttons)


        self.verticalLayout_59.addWidget(self.playerFrame_2)


        self.verticalLayout_29.addWidget(self.playerFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_2)

        self.uperSliders = QFrame(self.controlFrame)
        self.uperSliders.setObjectName(u"uperSliders")
        self.uperSliders.setEnabled(True)
        self.uperSliders.setMaximumSize(QSize(16777215, 160))
        self.uperSliders.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	background-color: rgb(80, 184, 158);\n"
"	padding: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(237, 105, 59)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255))\n"
"};\n"
"\n"
"\n"
"")
        self.uperSliders.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.uperSliders)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.uperSliders)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(76, 150))
        self.frame_56.setMaximumSize(QSize(76, 150))
        self.frame_56.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_32 = QVBoxLayout(self.frame_56)
        self.verticalLayout_32.setSpacing(3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.switch_50 = QPushButton(self.frame_56)
        self.switch_50.setObjectName(u"switch_50")
        self.switch_50.setEnabled(True)
        self.switch_50.setMinimumSize(QSize(66, 20))
        self.switch_50.setMaximumSize(QSize(65, 20))
        font9 = QFont()
        font9.setFamilies([u"PF BeauSans Pro"])
        font9.setPointSize(11)
        font9.setBold(False)
        self.switch_50.setFont(font9)
        self.switch_50.setCheckable(True)
        self.switch_50.setChecked(False)

        self.verticalLayout_32.addWidget(self.switch_50)

        self.slider_50 = QSlider(self.frame_56)
        self.slider_50.setObjectName(u"slider_50")
        self.slider_50.setEnabled(False)
        self.slider_50.setMinimumSize(QSize(45, 100))
        self.slider_50.setStyleSheet(u"")
        self.slider_50.setMinimum(-50)
        self.slider_50.setMaximum(50)
        self.slider_50.setValue(0)

        self.verticalLayout_32.addWidget(self.slider_50)

        self.label_12 = QLabel(self.frame_56)
        self.label_12.setObjectName(u"label_12")
        font10 = QFont()
        font10.setFamilies([u"PF BeauSans Pro"])
        font10.setPointSize(10)
        font10.setBold(True)
        self.label_12.setFont(font10)
        self.label_12.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_32.addWidget(self.label_12)


        self.horizontalLayout_22.addWidget(self.frame_56)

        self.frame_57 = QFrame(self.uperSliders)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(76, 150))
        self.frame_57.setMaximumSize(QSize(76, 150))
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_33 = QVBoxLayout(self.frame_57)
        self.verticalLayout_33.setSpacing(3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.switch_63 = QPushButton(self.frame_57)
        self.switch_63.setObjectName(u"switch_63")
        self.switch_63.setMinimumSize(QSize(66, 20))
        self.switch_63.setMaximumSize(QSize(65, 20))
        self.switch_63.setFont(font9)
        self.switch_63.setCheckable(True)
        self.switch_63.setChecked(False)

        self.verticalLayout_33.addWidget(self.switch_63)

        self.slider_63 = QSlider(self.frame_57)
        self.slider_63.setObjectName(u"slider_63")
        self.slider_63.setEnabled(False)
        self.slider_63.setMinimumSize(QSize(45, 100))
        self.slider_63.setMinimum(-50)
        self.slider_63.setMaximum(50)
        self.slider_63.setValue(0)

        self.verticalLayout_33.addWidget(self.slider_63)

        self.label_13 = QLabel(self.frame_57)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font10)
        self.label_13.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_33.addWidget(self.label_13)


        self.horizontalLayout_22.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.uperSliders)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(76, 150))
        self.frame_58.setMaximumSize(QSize(76, 150))
        self.frame_58.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_34 = QVBoxLayout(self.frame_58)
        self.verticalLayout_34.setSpacing(3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.switch_80 = QPushButton(self.frame_58)
        self.switch_80.setObjectName(u"switch_80")
        self.switch_80.setMinimumSize(QSize(66, 20))
        self.switch_80.setMaximumSize(QSize(65, 20))
        self.switch_80.setFont(font9)
        self.switch_80.setCheckable(True)
        self.switch_80.setChecked(False)

        self.verticalLayout_34.addWidget(self.switch_80)

        self.slider_80 = QSlider(self.frame_58)
        self.slider_80.setObjectName(u"slider_80")
        self.slider_80.setEnabled(False)
        self.slider_80.setMinimumSize(QSize(45, 100))
        self.slider_80.setMinimum(-50)
        self.slider_80.setMaximum(50)
        self.slider_80.setValue(0)

        self.verticalLayout_34.addWidget(self.slider_80)

        self.label_14 = QLabel(self.frame_58)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font10)
        self.label_14.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_34.addWidget(self.label_14)


        self.horizontalLayout_22.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.uperSliders)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMinimumSize(QSize(76, 150))
        self.frame_59.setMaximumSize(QSize(76, 150))
        self.frame_59.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_59.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_35 = QVBoxLayout(self.frame_59)
        self.verticalLayout_35.setSpacing(3)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.switch_100 = QPushButton(self.frame_59)
        self.switch_100.setObjectName(u"switch_100")
        self.switch_100.setMinimumSize(QSize(66, 20))
        self.switch_100.setMaximumSize(QSize(65, 20))
        self.switch_100.setFont(font9)
        self.switch_100.setCheckable(True)
        self.switch_100.setChecked(False)

        self.verticalLayout_35.addWidget(self.switch_100)

        self.slider_100 = QSlider(self.frame_59)
        self.slider_100.setObjectName(u"slider_100")
        self.slider_100.setEnabled(False)
        self.slider_100.setMinimumSize(QSize(45, 100))
        self.slider_100.setMinimum(-50)
        self.slider_100.setMaximum(50)
        self.slider_100.setValue(0)

        self.verticalLayout_35.addWidget(self.slider_100)

        self.label_15 = QLabel(self.frame_59)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font10)
        self.label_15.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_35.addWidget(self.label_15)


        self.horizontalLayout_22.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.uperSliders)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(76, 150))
        self.frame_60.setMaximumSize(QSize(76, 150))
        self.frame_60.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_37 = QVBoxLayout(self.frame_60)
        self.verticalLayout_37.setSpacing(3)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.switch_125 = QPushButton(self.frame_60)
        self.switch_125.setObjectName(u"switch_125")
        self.switch_125.setMinimumSize(QSize(66, 20))
        self.switch_125.setMaximumSize(QSize(65, 20))
        self.switch_125.setFont(font9)
        self.switch_125.setCheckable(True)
        self.switch_125.setChecked(False)

        self.verticalLayout_37.addWidget(self.switch_125)

        self.slider_125 = QSlider(self.frame_60)
        self.slider_125.setObjectName(u"slider_125")
        self.slider_125.setEnabled(False)
        self.slider_125.setMinimumSize(QSize(45, 100))
        self.slider_125.setMinimum(-50)
        self.slider_125.setMaximum(50)
        self.slider_125.setValue(0)

        self.verticalLayout_37.addWidget(self.slider_125)

        self.label_16 = QLabel(self.frame_60)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font10)
        self.label_16.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_37.addWidget(self.label_16)


        self.horizontalLayout_22.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.uperSliders)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(76, 150))
        self.frame_61.setMaximumSize(QSize(76, 150))
        self.frame_61.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_38 = QVBoxLayout(self.frame_61)
        self.verticalLayout_38.setSpacing(3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.switch_160 = QPushButton(self.frame_61)
        self.switch_160.setObjectName(u"switch_160")
        self.switch_160.setMinimumSize(QSize(66, 20))
        self.switch_160.setMaximumSize(QSize(65, 20))
        self.switch_160.setFont(font9)
        self.switch_160.setCheckable(True)
        self.switch_160.setChecked(False)

        self.verticalLayout_38.addWidget(self.switch_160)

        self.slider_160 = QSlider(self.frame_61)
        self.slider_160.setObjectName(u"slider_160")
        self.slider_160.setEnabled(False)
        self.slider_160.setMinimumSize(QSize(45, 100))
        self.slider_160.setMinimum(-50)
        self.slider_160.setMaximum(50)
        self.slider_160.setValue(0)

        self.verticalLayout_38.addWidget(self.slider_160)

        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_38.addWidget(self.label_17)


        self.horizontalLayout_22.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.uperSliders)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(76, 150))
        self.frame_62.setMaximumSize(QSize(76, 150))
        self.frame_62.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_39 = QVBoxLayout(self.frame_62)
        self.verticalLayout_39.setSpacing(3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.switch_200 = QPushButton(self.frame_62)
        self.switch_200.setObjectName(u"switch_200")
        self.switch_200.setMinimumSize(QSize(66, 20))
        self.switch_200.setMaximumSize(QSize(65, 20))
        self.switch_200.setFont(font9)
        self.switch_200.setCheckable(True)
        self.switch_200.setChecked(False)

        self.verticalLayout_39.addWidget(self.switch_200)

        self.slider_200 = QSlider(self.frame_62)
        self.slider_200.setObjectName(u"slider_200")
        self.slider_200.setEnabled(False)
        self.slider_200.setMinimumSize(QSize(45, 100))
        self.slider_200.setMinimum(-50)
        self.slider_200.setMaximum(50)
        self.slider_200.setValue(0)

        self.verticalLayout_39.addWidget(self.slider_200)

        self.label_18 = QLabel(self.frame_62)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font10)
        self.label_18.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_39.addWidget(self.label_18)


        self.horizontalLayout_22.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.uperSliders)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(76, 150))
        self.frame_63.setMaximumSize(QSize(76, 150))
        self.frame_63.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_40 = QVBoxLayout(self.frame_63)
        self.verticalLayout_40.setSpacing(3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.switch_250 = QPushButton(self.frame_63)
        self.switch_250.setObjectName(u"switch_250")
        self.switch_250.setMinimumSize(QSize(66, 20))
        self.switch_250.setMaximumSize(QSize(65, 20))
        self.switch_250.setFont(font9)
        self.switch_250.setCheckable(True)
        self.switch_250.setChecked(False)

        self.verticalLayout_40.addWidget(self.switch_250)

        self.slider_250 = QSlider(self.frame_63)
        self.slider_250.setObjectName(u"slider_250")
        self.slider_250.setEnabled(False)
        self.slider_250.setMinimumSize(QSize(45, 100))
        self.slider_250.setMinimum(-50)
        self.slider_250.setMaximum(50)
        self.slider_250.setValue(0)

        self.verticalLayout_40.addWidget(self.slider_250)

        self.label_19 = QLabel(self.frame_63)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)
        self.label_19.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_40.addWidget(self.label_19)


        self.horizontalLayout_22.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.uperSliders)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(76, 150))
        self.frame_64.setMaximumSize(QSize(76, 150))
        self.frame_64.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_41 = QVBoxLayout(self.frame_64)
        self.verticalLayout_41.setSpacing(3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.switch_315 = QPushButton(self.frame_64)
        self.switch_315.setObjectName(u"switch_315")
        self.switch_315.setEnabled(True)
        self.switch_315.setMinimumSize(QSize(66, 20))
        self.switch_315.setMaximumSize(QSize(65, 20))
        self.switch_315.setFont(font9)
        self.switch_315.setCheckable(True)
        self.switch_315.setChecked(False)

        self.verticalLayout_41.addWidget(self.switch_315)

        self.slider_315 = QSlider(self.frame_64)
        self.slider_315.setObjectName(u"slider_315")
        self.slider_315.setEnabled(False)
        self.slider_315.setMinimumSize(QSize(45, 100))
        self.slider_315.setMinimum(-50)
        self.slider_315.setMaximum(50)
        self.slider_315.setValue(0)

        self.verticalLayout_41.addWidget(self.slider_315)

        self.label_22 = QLabel(self.frame_64)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font10)
        self.label_22.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_41.addWidget(self.label_22)


        self.horizontalLayout_22.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.uperSliders)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setEnabled(True)
        self.frame_65.setMinimumSize(QSize(76, 150))
        self.frame_65.setMaximumSize(QSize(76, 150))
        self.frame_65.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_42 = QVBoxLayout(self.frame_65)
        self.verticalLayout_42.setSpacing(3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.switch_400 = QPushButton(self.frame_65)
        self.switch_400.setObjectName(u"switch_400")
        self.switch_400.setMinimumSize(QSize(66, 20))
        self.switch_400.setMaximumSize(QSize(65, 20))
        self.switch_400.setFont(font9)
        self.switch_400.setCheckable(True)
        self.switch_400.setChecked(False)

        self.verticalLayout_42.addWidget(self.switch_400)

        self.slider_400 = QSlider(self.frame_65)
        self.slider_400.setObjectName(u"slider_400")
        self.slider_400.setEnabled(False)
        self.slider_400.setMinimumSize(QSize(45, 100))
        self.slider_400.setMinimum(-50)
        self.slider_400.setMaximum(50)
        self.slider_400.setValue(0)

        self.verticalLayout_42.addWidget(self.slider_400)

        self.label_52 = QLabel(self.frame_65)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font10)
        self.label_52.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_42.addWidget(self.label_52)


        self.horizontalLayout_22.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.uperSliders)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setEnabled(True)
        self.frame_66.setMinimumSize(QSize(76, 150))
        self.frame_66.setMaximumSize(QSize(76, 150))
        self.frame_66.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_43 = QVBoxLayout(self.frame_66)
        self.verticalLayout_43.setSpacing(3)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.switch_500 = QPushButton(self.frame_66)
        self.switch_500.setObjectName(u"switch_500")
        self.switch_500.setEnabled(True)
        self.switch_500.setMinimumSize(QSize(66, 20))
        self.switch_500.setMaximumSize(QSize(65, 20))
        self.switch_500.setFont(font9)
        self.switch_500.setCheckable(False)
        self.switch_500.setChecked(False)

        self.verticalLayout_43.addWidget(self.switch_500)

        self.slider_500 = QSlider(self.frame_66)
        self.slider_500.setObjectName(u"slider_500")
        self.slider_500.setEnabled(False)
        self.slider_500.setMinimumSize(QSize(45, 100))
        self.slider_500.setMinimum(-50)
        self.slider_500.setMaximum(50)
        self.slider_500.setValue(0)

        self.verticalLayout_43.addWidget(self.slider_500)

        self.label_53 = QLabel(self.frame_66)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font10)
        self.label_53.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_43.addWidget(self.label_53)


        self.horizontalLayout_22.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.uperSliders)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(76, 150))
        self.frame_67.setMaximumSize(QSize(76, 150))
        self.frame_67.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_44 = QVBoxLayout(self.frame_67)
        self.verticalLayout_44.setSpacing(3)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.switch_630 = QPushButton(self.frame_67)
        self.switch_630.setObjectName(u"switch_630")
        self.switch_630.setEnabled(True)
        self.switch_630.setMinimumSize(QSize(66, 20))
        self.switch_630.setMaximumSize(QSize(65, 20))
        self.switch_630.setFont(font9)
        self.switch_630.setCheckable(True)
        self.switch_630.setChecked(False)

        self.verticalLayout_44.addWidget(self.switch_630)

        self.slider_630 = QSlider(self.frame_67)
        self.slider_630.setObjectName(u"slider_630")
        self.slider_630.setEnabled(False)
        self.slider_630.setMinimumSize(QSize(45, 100))
        self.slider_630.setMinimum(-50)
        self.slider_630.setMaximum(50)
        self.slider_630.setValue(0)

        self.verticalLayout_44.addWidget(self.slider_630)

        self.label_54 = QLabel(self.frame_67)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font10)
        self.label_54.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_44.addWidget(self.label_54)


        self.horizontalLayout_22.addWidget(self.frame_67)


        self.verticalLayout_29.addWidget(self.uperSliders)

        self.lowerSliders = QFrame(self.controlFrame)
        self.lowerSliders.setObjectName(u"lowerSliders")
        self.lowerSliders.setMaximumSize(QSize(16777215, 160))
        self.lowerSliders.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"	background-color: rgb(80, 184, 158);\n"
"	padding: 2px;\n"
"	border-radius: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255))\n"
"};\n"
"\n"
"")
        self.lowerSliders.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_23 = QHBoxLayout(self.lowerSliders)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_84 = QFrame(self.lowerSliders)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(76, 150))
        self.frame_84.setMaximumSize(QSize(76, 150))
        self.frame_84.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_30 = QVBoxLayout(self.frame_84)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.switch_800 = QPushButton(self.frame_84)
        self.switch_800.setObjectName(u"switch_800")
        self.switch_800.setMinimumSize(QSize(66, 20))
        self.switch_800.setMaximumSize(QSize(65, 20))
        self.switch_800.setFont(font9)
        self.switch_800.setCheckable(True)
        self.switch_800.setChecked(False)

        self.verticalLayout_30.addWidget(self.switch_800)

        self.slider_800 = QSlider(self.frame_84)
        self.slider_800.setObjectName(u"slider_800")
        self.slider_800.setEnabled(False)
        self.slider_800.setMinimumSize(QSize(45, 100))
        self.slider_800.setMinimum(-50)
        self.slider_800.setMaximum(50)
        self.slider_800.setValue(0)

        self.verticalLayout_30.addWidget(self.slider_800)

        self.label_7 = QLabel(self.frame_84)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font10)
        self.label_7.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_30.addWidget(self.label_7)


        self.horizontalLayout_23.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.lowerSliders)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(76, 150))
        self.frame_85.setMaximumSize(QSize(76, 150))
        self.frame_85.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_31 = QVBoxLayout(self.frame_85)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.switch_1000 = QPushButton(self.frame_85)
        self.switch_1000.setObjectName(u"switch_1000")
        self.switch_1000.setMinimumSize(QSize(66, 20))
        self.switch_1000.setMaximumSize(QSize(65, 20))
        self.switch_1000.setFont(font9)
        self.switch_1000.setCheckable(True)
        self.switch_1000.setChecked(False)

        self.verticalLayout_31.addWidget(self.switch_1000)

        self.slider_1000 = QSlider(self.frame_85)
        self.slider_1000.setObjectName(u"slider_1000")
        self.slider_1000.setEnabled(False)
        self.slider_1000.setMinimumSize(QSize(45, 100))
        self.slider_1000.setMinimum(-50)
        self.slider_1000.setMaximum(50)
        self.slider_1000.setValue(0)

        self.verticalLayout_31.addWidget(self.slider_1000)

        self.label_20 = QLabel(self.frame_85)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font10)
        self.label_20.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_31.addWidget(self.label_20)


        self.horizontalLayout_23.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.lowerSliders)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMinimumSize(QSize(76, 150))
        self.frame_86.setMaximumSize(QSize(76, 150))
        self.frame_86.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_45 = QVBoxLayout(self.frame_86)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.switch_1250 = QPushButton(self.frame_86)
        self.switch_1250.setObjectName(u"switch_1250")
        self.switch_1250.setMinimumSize(QSize(66, 20))
        self.switch_1250.setMaximumSize(QSize(65, 20))
        self.switch_1250.setFont(font9)
        self.switch_1250.setCheckable(True)
        self.switch_1250.setChecked(False)

        self.verticalLayout_45.addWidget(self.switch_1250)

        self.slider_1250 = QSlider(self.frame_86)
        self.slider_1250.setObjectName(u"slider_1250")
        self.slider_1250.setEnabled(False)
        self.slider_1250.setMinimumSize(QSize(45, 100))
        self.slider_1250.setMinimum(-50)
        self.slider_1250.setMaximum(50)
        self.slider_1250.setValue(0)

        self.verticalLayout_45.addWidget(self.slider_1250)

        self.label_55 = QLabel(self.frame_86)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font10)
        self.label_55.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_45.addWidget(self.label_55)


        self.horizontalLayout_23.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.lowerSliders)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(76, 150))
        self.frame_87.setMaximumSize(QSize(76, 150))
        self.frame_87.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_46 = QVBoxLayout(self.frame_87)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.switch_1600 = QPushButton(self.frame_87)
        self.switch_1600.setObjectName(u"switch_1600")
        self.switch_1600.setMinimumSize(QSize(66, 20))
        self.switch_1600.setMaximumSize(QSize(65, 20))
        self.switch_1600.setFont(font9)
        self.switch_1600.setCheckable(True)
        self.switch_1600.setChecked(False)

        self.verticalLayout_46.addWidget(self.switch_1600)

        self.slider_1600 = QSlider(self.frame_87)
        self.slider_1600.setObjectName(u"slider_1600")
        self.slider_1600.setEnabled(False)
        self.slider_1600.setMinimumSize(QSize(45, 100))
        self.slider_1600.setMinimum(-50)
        self.slider_1600.setMaximum(50)
        self.slider_1600.setValue(0)

        self.verticalLayout_46.addWidget(self.slider_1600)

        self.label_56 = QLabel(self.frame_87)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font10)
        self.label_56.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_46.addWidget(self.label_56)


        self.horizontalLayout_23.addWidget(self.frame_87)

        self.frame_88 = QFrame(self.lowerSliders)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(76, 150))
        self.frame_88.setMaximumSize(QSize(76, 150))
        self.frame_88.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_47 = QVBoxLayout(self.frame_88)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.switch_2000 = QPushButton(self.frame_88)
        self.switch_2000.setObjectName(u"switch_2000")
        self.switch_2000.setMinimumSize(QSize(66, 20))
        self.switch_2000.setMaximumSize(QSize(65, 20))
        self.switch_2000.setFont(font9)
        self.switch_2000.setCheckable(True)
        self.switch_2000.setChecked(False)

        self.verticalLayout_47.addWidget(self.switch_2000)

        self.slider_2000 = QSlider(self.frame_88)
        self.slider_2000.setObjectName(u"slider_2000")
        self.slider_2000.setEnabled(False)
        self.slider_2000.setMinimumSize(QSize(45, 100))
        self.slider_2000.setMinimum(-50)
        self.slider_2000.setMaximum(50)
        self.slider_2000.setValue(0)

        self.verticalLayout_47.addWidget(self.slider_2000)

        self.label_57 = QLabel(self.frame_88)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font10)
        self.label_57.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_47.addWidget(self.label_57)


        self.horizontalLayout_23.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.lowerSliders)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(76, 150))
        self.frame_89.setMaximumSize(QSize(76, 150))
        self.frame_89.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_48 = QVBoxLayout(self.frame_89)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.switch_2500 = QPushButton(self.frame_89)
        self.switch_2500.setObjectName(u"switch_2500")
        self.switch_2500.setMinimumSize(QSize(66, 20))
        self.switch_2500.setMaximumSize(QSize(65, 20))
        self.switch_2500.setFont(font9)
        self.switch_2500.setCheckable(True)
        self.switch_2500.setChecked(False)

        self.verticalLayout_48.addWidget(self.switch_2500)

        self.slider_2500 = QSlider(self.frame_89)
        self.slider_2500.setObjectName(u"slider_2500")
        self.slider_2500.setEnabled(False)
        self.slider_2500.setMinimumSize(QSize(45, 100))
        self.slider_2500.setMinimum(-50)
        self.slider_2500.setMaximum(50)
        self.slider_2500.setValue(0)

        self.verticalLayout_48.addWidget(self.slider_2500)

        self.label_58 = QLabel(self.frame_89)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font10)
        self.label_58.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_48.addWidget(self.label_58)


        self.horizontalLayout_23.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.lowerSliders)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(76, 150))
        self.frame_90.setMaximumSize(QSize(76, 150))
        self.frame_90.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_49 = QVBoxLayout(self.frame_90)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.switch_3150 = QPushButton(self.frame_90)
        self.switch_3150.setObjectName(u"switch_3150")
        self.switch_3150.setMinimumSize(QSize(66, 20))
        self.switch_3150.setMaximumSize(QSize(65, 20))
        self.switch_3150.setFont(font9)
        self.switch_3150.setCheckable(True)
        self.switch_3150.setChecked(False)

        self.verticalLayout_49.addWidget(self.switch_3150)

        self.slider_3150 = QSlider(self.frame_90)
        self.slider_3150.setObjectName(u"slider_3150")
        self.slider_3150.setEnabled(False)
        self.slider_3150.setMinimumSize(QSize(45, 100))
        self.slider_3150.setMinimum(-50)
        self.slider_3150.setMaximum(50)
        self.slider_3150.setValue(0)

        self.verticalLayout_49.addWidget(self.slider_3150)

        self.label_59 = QLabel(self.frame_90)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font10)
        self.label_59.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_49.addWidget(self.label_59)


        self.horizontalLayout_23.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.lowerSliders)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(76, 150))
        self.frame_91.setMaximumSize(QSize(76, 150))
        self.frame_91.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_50 = QVBoxLayout(self.frame_91)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.switch_4000 = QPushButton(self.frame_91)
        self.switch_4000.setObjectName(u"switch_4000")
        self.switch_4000.setMinimumSize(QSize(66, 20))
        self.switch_4000.setMaximumSize(QSize(65, 20))
        self.switch_4000.setFont(font9)
        self.switch_4000.setCheckable(True)
        self.switch_4000.setChecked(False)

        self.verticalLayout_50.addWidget(self.switch_4000)

        self.slider_4000 = QSlider(self.frame_91)
        self.slider_4000.setObjectName(u"slider_4000")
        self.slider_4000.setEnabled(False)
        self.slider_4000.setMinimumSize(QSize(45, 100))
        self.slider_4000.setMinimum(-50)
        self.slider_4000.setMaximum(50)
        self.slider_4000.setValue(0)

        self.verticalLayout_50.addWidget(self.slider_4000)

        self.label_60 = QLabel(self.frame_91)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font10)
        self.label_60.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_50.addWidget(self.label_60)


        self.horizontalLayout_23.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.lowerSliders)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(76, 150))
        self.frame_92.setMaximumSize(QSize(76, 150))
        self.frame_92.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_51 = QVBoxLayout(self.frame_92)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.switch_5000 = QPushButton(self.frame_92)
        self.switch_5000.setObjectName(u"switch_5000")
        self.switch_5000.setMinimumSize(QSize(66, 20))
        self.switch_5000.setMaximumSize(QSize(65, 20))
        self.switch_5000.setFont(font9)
        self.switch_5000.setCheckable(True)
        self.switch_5000.setChecked(False)

        self.verticalLayout_51.addWidget(self.switch_5000)

        self.slider_5000 = QSlider(self.frame_92)
        self.slider_5000.setObjectName(u"slider_5000")
        self.slider_5000.setEnabled(False)
        self.slider_5000.setMinimumSize(QSize(45, 100))
        self.slider_5000.setMinimum(-50)
        self.slider_5000.setMaximum(50)
        self.slider_5000.setValue(0)

        self.verticalLayout_51.addWidget(self.slider_5000)

        self.label_61 = QLabel(self.frame_92)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font10)
        self.label_61.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_51.addWidget(self.label_61)


        self.horizontalLayout_23.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.lowerSliders)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(76, 150))
        self.frame_93.setMaximumSize(QSize(76, 150))
        self.frame_93.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_52 = QVBoxLayout(self.frame_93)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.switch_6300 = QPushButton(self.frame_93)
        self.switch_6300.setObjectName(u"switch_6300")
        self.switch_6300.setMinimumSize(QSize(66, 20))
        self.switch_6300.setMaximumSize(QSize(65, 20))
        self.switch_6300.setFont(font9)
        self.switch_6300.setCheckable(True)
        self.switch_6300.setChecked(False)

        self.verticalLayout_52.addWidget(self.switch_6300)

        self.slider_6300 = QSlider(self.frame_93)
        self.slider_6300.setObjectName(u"slider_6300")
        self.slider_6300.setEnabled(False)
        self.slider_6300.setMinimumSize(QSize(45, 100))
        self.slider_6300.setMinimum(-50)
        self.slider_6300.setMaximum(50)
        self.slider_6300.setValue(0)

        self.verticalLayout_52.addWidget(self.slider_6300)

        self.label_62 = QLabel(self.frame_93)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font10)
        self.label_62.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_52.addWidget(self.label_62)


        self.horizontalLayout_23.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.lowerSliders)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(76, 150))
        self.frame_94.setMaximumSize(QSize(76, 150))
        self.frame_94.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_53 = QVBoxLayout(self.frame_94)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.switch_8000 = QPushButton(self.frame_94)
        self.switch_8000.setObjectName(u"switch_8000")
        self.switch_8000.setMinimumSize(QSize(66, 20))
        self.switch_8000.setMaximumSize(QSize(65, 20))
        self.switch_8000.setFont(font9)
        self.switch_8000.setCheckable(True)
        self.switch_8000.setChecked(False)

        self.verticalLayout_53.addWidget(self.switch_8000)

        self.slider_8000 = QSlider(self.frame_94)
        self.slider_8000.setObjectName(u"slider_8000")
        self.slider_8000.setEnabled(False)
        self.slider_8000.setMinimumSize(QSize(45, 100))
        self.slider_8000.setMinimum(-50)
        self.slider_8000.setMaximum(50)
        self.slider_8000.setValue(0)

        self.verticalLayout_53.addWidget(self.slider_8000)

        self.label_63 = QLabel(self.frame_94)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font10)
        self.label_63.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_53.addWidget(self.label_63)


        self.horizontalLayout_23.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.lowerSliders)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(76, 150))
        self.frame_95.setMaximumSize(QSize(76, 140))
        self.frame_95.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_54 = QVBoxLayout(self.frame_95)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.switch_10000 = QPushButton(self.frame_95)
        self.switch_10000.setObjectName(u"switch_10000")
        self.switch_10000.setMinimumSize(QSize(66, 20))
        self.switch_10000.setMaximumSize(QSize(65, 20))
        self.switch_10000.setFont(font9)
        self.switch_10000.setCheckable(True)
        self.switch_10000.setChecked(False)

        self.verticalLayout_54.addWidget(self.switch_10000)

        self.slider_10000 = QSlider(self.frame_95)
        self.slider_10000.setObjectName(u"slider_10000")
        self.slider_10000.setEnabled(False)
        self.slider_10000.setMinimumSize(QSize(45, 100))
        self.slider_10000.setMinimum(-50)
        self.slider_10000.setMaximum(50)
        self.slider_10000.setValue(0)

        self.verticalLayout_54.addWidget(self.slider_10000)

        self.label_64 = QLabel(self.frame_95)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font10)
        self.label_64.setStyleSheet(u"color: rgb(80, 184, 158)")

        self.verticalLayout_54.addWidget(self.label_64)


        self.horizontalLayout_23.addWidget(self.frame_95)


        self.verticalLayout_29.addWidget(self.lowerSliders)


        self.verticalLayout_28.addWidget(self.controlFrame)

        self.rightContent.addWidget(self.filterPage)
        self.calibrationPage = QWidget()
        self.calibrationPage.setObjectName(u"calibrationPage")
        self.calibrationPage.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.verticalLayout_89 = QVBoxLayout(self.calibrationPage)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.SupCalibrationSetup = QFrame(self.calibrationPage)
        self.SupCalibrationSetup.setObjectName(u"SupCalibrationSetup")
        self.SupCalibrationSetup.setMinimumSize(QSize(0, 80))
        self.SupCalibrationSetup.setMaximumSize(QSize(16777215, 140))
        self.SupCalibrationSetup.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_65 = QHBoxLayout(self.SupCalibrationSetup)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_128 = QFrame(self.SupCalibrationSetup)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(8, 14, 0, 0)
        self.label_96 = QLabel(self.frame_128)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(0, 50))
        self.label_96.setMaximumSize(QSize(16777215, 50))
        self.label_96.setFont(font4)
        self.label_96.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.horizontalLayout_66.addWidget(self.label_96)


        self.horizontalLayout_65.addWidget(self.frame_128)

        self.frame_129 = QFrame(self.SupCalibrationSetup)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_88 = QVBoxLayout(self.frame_129)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 9, 9, 9)
        self.logo_3 = QLabel(self.frame_129)
        self.logo_3.setObjectName(u"logo_3")
        self.logo_3.setMinimumSize(QSize(130, 50))
        self.logo_3.setMaximumSize(QSize(130, 50))
        self.logo_3.setPixmap(QPixmap(u":/logos/img/psychobox_logo.png"))
        self.logo_3.setScaledContents(True)

        self.verticalLayout_88.addWidget(self.logo_3, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_65.addWidget(self.frame_129)


        self.verticalLayout_89.addWidget(self.SupCalibrationSetup)

        self.InfCalibrationSetup = QFrame(self.calibrationPage)
        self.InfCalibrationSetup.setObjectName(u"InfCalibrationSetup")
        self.InfCalibrationSetup.setMinimumSize(QSize(0, 0))
        self.InfCalibrationSetup.setStyleSheet(u"b")
        self.InfCalibrationSetup.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_54 = QHBoxLayout(self.InfCalibrationSetup)
        self.horizontalLayout_54.setSpacing(6)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(6, 6, 6, 6)
        self.Import = QFrame(self.InfCalibrationSetup)
        self.Import.setObjectName(u"Import")
        self.Import.setMaximumSize(QSize(16777215, 16777215))
        self.Import.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px\n"
"}")
        self.Import.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_84 = QVBoxLayout(self.Import)
        self.verticalLayout_84.setSpacing(5)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(10, 5, 5, 5)
        self.frame_121 = QFrame(self.Import)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMinimumSize(QSize(0, 50))
        self.frame_121.setMaximumSize(QSize(16777215, 50))
        self.frame_121.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_121)
        self.horizontalLayout_59.setSpacing(5)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_121)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(50, 50))
        self.label_86.setMaximumSize(QSize(50, 50))
        self.label_86.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_86.setPixmap(QPixmap(u":/icons/img/shopping-basket.png"))
        self.label_86.setScaledContents(True)
        self.label_86.setMargin(10)

        self.horizontalLayout_59.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_121)
        self.label_87.setObjectName(u"label_87")
        font11 = QFont()
        font11.setFamilies([u"PF BeauSans Pro"])
        font11.setPointSize(18)
        font11.setBold(True)
        self.label_87.setFont(font11)
        self.label_87.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.horizontalLayout_59.addWidget(self.label_87)

        self.checkHold = QCheckBox(self.frame_121)
        self.checkHold.setObjectName(u"checkHold")
        self.checkHold.setMinimumSize(QSize(75, 0))
        self.checkHold.setMaximumSize(QSize(75, 16777215))
        font12 = QFont()
        font12.setFamilies([u"PF BeauSans Pro"])
        font12.setPointSize(11)
        self.checkHold.setFont(font12)
        self.checkHold.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QCheckBox::indicator{\n"
"	background-color: rgb(70,70,70);\n"
"	color: rgb(241,102,55);\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	background-color: rgb(241,102,55);\n"
"	border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"QCheckBox:disabled{\n"
" color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled{\n"
"	background-color: rgb(136, 138, 133);\n"
"}")
        self.checkHold.setChecked(False)

        self.horizontalLayout_59.addWidget(self.checkHold)


        self.verticalLayout_84.addWidget(self.frame_121)

        self.frame_122 = QFrame(self.Import)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_85 = QVBoxLayout(self.frame_122)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.listWidget2 = QListWidget(self.frame_122)
        self.listWidget2.setObjectName(u"listWidget2")
        self.listWidget2.setFont(font8)
        self.listWidget2.setStyleSheet(u"QListWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	border : 4px solid rgb(80, 184, 158);\n"
"	border-radius:10px;\n"
"	background : rgb(70, 70, 70);\n"
"}\n"
"\n"
"QListWidget:hover {\n"
"	border : 4px solid rgb(255, 161, 78);\n"
"}\n"
"\n"
"\n"
" QListView::item:selected {\n"
"	border : 2px solid #009b4a;\n"
"	background : rgb(97, 176, 155);\n"
"}\n"
"\n"
"QListView::item {\n"
"	padding-right:10px;\n"
"	text-align: right;\n"
"}\n"
"\n"
"")

        self.verticalLayout_85.addWidget(self.listWidget2)

        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setStyleSheet(u"\n"
"QPushButton {\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"	background-color: rgb(80, 184, 158);\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 161, 78);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(237, 105, 59)\n"
"}\n"
"")
        self.frame_123.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_86 = QVBoxLayout(self.frame_123)
        self.verticalLayout_86.setSpacing(6)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.importGraph = QPushButton(self.frame_123)
        self.importGraph.setObjectName(u"importGraph")
        self.importGraph.setMinimumSize(QSize(0, 30))
        self.importGraph.setMaximumSize(QSize(120, 16777215))
        self.importGraph.setFont(font7)

        self.verticalLayout_86.addWidget(self.importGraph)

        self.removeGraph = QPushButton(self.frame_123)
        self.removeGraph.setObjectName(u"removeGraph")
        self.removeGraph.setMinimumSize(QSize(0, 30))
        self.removeGraph.setMaximumSize(QSize(120, 16777215))
        self.removeGraph.setFont(font7)

        self.verticalLayout_86.addWidget(self.removeGraph)

        self.removeAllGraph = QPushButton(self.frame_123)
        self.removeAllGraph.setObjectName(u"removeAllGraph")
        self.removeAllGraph.setMinimumSize(QSize(0, 30))
        self.removeAllGraph.setMaximumSize(QSize(120, 16777215))
        self.removeAllGraph.setFont(font7)

        self.verticalLayout_86.addWidget(self.removeAllGraph)


        self.verticalLayout_85.addWidget(self.frame_123)


        self.verticalLayout_84.addWidget(self.frame_122)


        self.horizontalLayout_54.addWidget(self.Import)

        self.RightCalibrationSetup = QFrame(self.InfCalibrationSetup)
        self.RightCalibrationSetup.setObjectName(u"RightCalibrationSetup")
        self.RightCalibrationSetup.setMinimumSize(QSize(0, 0))
        self.RightCalibrationSetup.setMaximumSize(QSize(16777215, 16777215))
        self.RightCalibrationSetup.setStyleSheet(u"")
        self.RightCalibrationSetup.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_90 = QVBoxLayout(self.RightCalibrationSetup)
        self.verticalLayout_90.setSpacing(6)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.Headphones = QFrame(self.RightCalibrationSetup)
        self.Headphones.setObjectName(u"Headphones")
        self.Headphones.setMaximumSize(QSize(16777215, 16777215))
        self.Headphones.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px;\n"
"}	\n"
"")
        self.Headphones.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_91 = QVBoxLayout(self.Headphones)
        self.verticalLayout_91.setSpacing(5)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_133 = QFrame(self.Headphones)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setMinimumSize(QSize(0, 50))
        self.frame_133.setMaximumSize(QSize(16777215, 50))
        self.frame_133.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_67.setSpacing(5)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.frame_133)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(50, 50))
        self.label_98.setMaximumSize(QSize(50, 50))
        self.label_98.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_98.setPixmap(QPixmap(u":/icons/img/headphones.png"))
        self.label_98.setScaledContents(True)
        self.label_98.setMargin(9)

        self.horizontalLayout_67.addWidget(self.label_98)

        self.label_99 = QLabel(self.frame_133)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font11)
        self.label_99.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.horizontalLayout_67.addWidget(self.label_99)


        self.verticalLayout_91.addWidget(self.frame_133)

        self.frame_134 = QFrame(self.Headphones)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 3px 23px 3px 3px;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"	color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"	image: url(:/icons/img/downArrowDis.png);\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border : 3px solid rgb(255, 161, 78);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/img/downArrow.png);\n"
"	width : 12px;\n"
"}\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" \n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"")
        self.frame_134.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_92 = QVBoxLayout(self.frame_134)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_100 = QLabel(self.frame_134)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(0, 20))
        self.label_100.setMaximumSize(QSize(16777215, 20))
        self.label_100.setFont(font7)
        self.label_100.setStyleSheet(u"color: white;")

        self.verticalLayout_92.addWidget(self.label_100)

        self.typeHeadBox_2 = QComboBox(self.frame_134)
        self.typeHeadBox_2.addItem("")
        self.typeHeadBox_2.addItem("")
        self.typeHeadBox_2.setObjectName(u"typeHeadBox_2")
        self.typeHeadBox_2.setMinimumSize(QSize(208, 30))
        self.typeHeadBox_2.setMaximumSize(QSize(16777215, 30))
        self.typeHeadBox_2.setFont(font7)
        self.typeHeadBox_2.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.typeHeadBox_2.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        self.verticalLayout_92.addWidget(self.typeHeadBox_2)

        self.label_101 = QLabel(self.frame_134)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(0, 20))
        self.label_101.setMaximumSize(QSize(16777215, 20))
        self.label_101.setFont(font7)
        self.label_101.setStyleSheet(u"color: white;")

        self.verticalLayout_92.addWidget(self.label_101)

        self.modelHeadBox_2 = QComboBox(self.frame_134)
        self.modelHeadBox_2.setObjectName(u"modelHeadBox_2")
        self.modelHeadBox_2.setEnabled(False)
        self.modelHeadBox_2.setMinimumSize(QSize(208, 30))
        self.modelHeadBox_2.setMaximumSize(QSize(16777215, 30))
        self.modelHeadBox_2.setFont(font7)

        self.verticalLayout_92.addWidget(self.modelHeadBox_2)


        self.verticalLayout_91.addWidget(self.frame_134)


        self.verticalLayout_90.addWidget(self.Headphones)

        self.Hats = QFrame(self.RightCalibrationSetup)
        self.Hats.setObjectName(u"Hats")
        self.Hats.setMaximumSize(QSize(16777215, 16777215))
        self.Hats.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px;\n"
"}	\n"
"")
        self.Hats.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_93 = QVBoxLayout(self.Hats)
        self.verticalLayout_93.setSpacing(5)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.frame_136 = QFrame(self.Hats)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 3px 23px 3px 3px;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"QComboBox::disabled{\n"
"	color: rgb(136, 138, 133)\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {    \n"
"	image: url(:/icons/img/downArrowDis.png);\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"border : 2px solid rgb(255, 161, 78);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/img/downArrow.png);\n"
"	width : 12px;\n"
"}\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" \n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"")
        self.frame_136.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_94 = QVBoxLayout(self.frame_136)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.frame_137 = QFrame(self.frame_136)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(0, 50))
        self.frame_137.setMaximumSize(QSize(16777215, 50))
        self.frame_137.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_68.setSpacing(5)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.frame_137)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(50, 50))
        self.label_102.setMaximumSize(QSize(50, 50))
        self.label_102.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_102.setPixmap(QPixmap(u":/icons/img/HATS.png"))
        self.label_102.setScaledContents(True)
        self.label_102.setMargin(8)

        self.horizontalLayout_68.addWidget(self.label_102)

        self.label_103 = QLabel(self.frame_137)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font11)
        self.label_103.setStyleSheet(u"color: rgb(70, 70, 70); ")

        self.horizontalLayout_68.addWidget(self.label_103)


        self.verticalLayout_94.addWidget(self.frame_137)

        self.label_104 = QLabel(self.frame_136)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(0, 20))
        self.label_104.setMaximumSize(QSize(16777215, 20))
        self.label_104.setFont(font7)
        self.label_104.setStyleSheet(u"color: white;")

        self.verticalLayout_94.addWidget(self.label_104)

        self.typeHatsBox_2 = QComboBox(self.frame_136)
        self.typeHatsBox_2.addItem("")
        self.typeHatsBox_2.addItem("")
        self.typeHatsBox_2.addItem("")
        self.typeHatsBox_2.setObjectName(u"typeHatsBox_2")
        self.typeHatsBox_2.setMinimumSize(QSize(208, 30))
        self.typeHatsBox_2.setMaximumSize(QSize(16777215, 30))
        self.typeHatsBox_2.setFont(font7)

        self.verticalLayout_94.addWidget(self.typeHatsBox_2)

        self.label_105 = QLabel(self.frame_136)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(0, 20))
        self.label_105.setMaximumSize(QSize(16777215, 20))
        self.label_105.setFont(font7)
        self.label_105.setStyleSheet(u"color: white;")

        self.verticalLayout_94.addWidget(self.label_105)

        self.modelHatsBox_2 = QComboBox(self.frame_136)
        self.modelHatsBox_2.setObjectName(u"modelHatsBox_2")
        self.modelHatsBox_2.setEnabled(False)
        self.modelHatsBox_2.setMinimumSize(QSize(208, 30))
        self.modelHatsBox_2.setMaximumSize(QSize(16777215, 30))
        self.modelHatsBox_2.setFont(font7)

        self.verticalLayout_94.addWidget(self.modelHatsBox_2)


        self.verticalLayout_93.addWidget(self.frame_136)


        self.verticalLayout_90.addWidget(self.Hats)

        self.frame_28 = QFrame(self.RightCalibrationSetup)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 150))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px;\n"
"}	\n"
"\n"
"QPushButton {\n"
"	padding-left: 8px;\n"
"	text-align: left;\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"	border-radius:18px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(79,186,160,255), stop:1 rgba(0,124,132, 255));\n"
"	}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"	color: rgb(136,138,133);\n"
"	background-color:rgb(70, 70, 70);\n"
"}\n"
"")
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.plot = QPushButton(self.frame_28)
        self.plot.setObjectName(u"plot")
        self.plot.setEnabled(False)
        self.plot.setMinimumSize(QSize(130, 36))
        self.plot.setMaximumSize(QSize(130, 36))
        font13 = QFont()
        font13.setFamilies([u"PF BeauSans Pro"])
        font13.setPointSize(13)
        font13.setBold(False)
        self.plot.setFont(font13)
        icon18 = QIcon()
        icon18.addFile(u":/icons/img/bar-graph.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon18.addFile(u":/icons/img/bar-graph_dis.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.plot.setIcon(icon18)
        self.plot.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.plot)

        self.convolve = QPushButton(self.frame_28)
        self.convolve.setObjectName(u"convolve")
        self.convolve.setEnabled(False)
        self.convolve.setMinimumSize(QSize(130, 36))
        self.convolve.setMaximumSize(QSize(130, 36))
        self.convolve.setFont(font13)
        icon19 = QIcon()
        icon19.addFile(u":/icons/img/puzzle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon19.addFile(u":/icons/img/puzzle_disabled.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.convolve.setIcon(icon19)
        self.convolve.setIconSize(QSize(25, 25))

        self.horizontalLayout_24.addWidget(self.convolve)


        self.verticalLayout_90.addWidget(self.frame_28)


        self.horizontalLayout_54.addWidget(self.RightCalibrationSetup)


        self.verticalLayout_89.addWidget(self.InfCalibrationSetup)

        self.rightContent.addWidget(self.calibrationPage)

        self.horizontalLayout.addWidget(self.rightContent)


        self.verticalLayout.addWidget(self.centerContent)

        self.bottomContent = QFrame(self.centralwidget)
        self.bottomContent.setObjectName(u"bottomContent")
        self.bottomContent.setMinimumSize(QSize(0, 50))
        self.bottomContent.setMaximumSize(QSize(16777215, 70))
        self.bottomContent.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.bottomContent.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.bottomContent)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 10, 0)
        self.label_23 = QLabel(self.bottomContent)
        self.label_23.setObjectName(u"label_23")
        font14 = QFont()
        font14.setFamilies([u"PF BeauSans Pro"])
        font14.setPointSize(10)
        font14.setBold(False)
        self.label_23.setFont(font14)
        self.label_23.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_23)


        self.verticalLayout.addWidget(self.bottomContent)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1192, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.rightContent.setCurrentIndex(0)
        self.samplingRate_Combo.setCurrentIndex(0)
        self.typeHeadBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.label_2.setText("")
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.closeAllButton.setText("")
        self.homeButton.setText("")
        self.recordingButton.setText("")
#if QT_CONFIG(tooltip)
        self.filterButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.filterButton.setText("")
        self.calibrationButton.setText("")
#if QT_CONFIG(accessibility)
        self.userButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.userButton.setText("")
#if QT_CONFIG(accessibility)
        self.settingsButton.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.settingsButton.setText("")
#if QT_CONFIG(accessibility)
        self.rightContent.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.logo_2.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"IMPORT YOUR FILES", None))
        self.label_32.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Work directly \n"
"with audio extensions \n"
"(.wav, .acc, .mp3)", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"EDIT YOUR SIGNAL", None))
        self.label_47.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\n"
"Process and listen to \n"
" signals using filters and windows", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"APPLY METRICS", None))
        self.label_50.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Use psychoacoustic \n"
" metrics to analyze your signal", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Recording", None))
        self.logo_4.setText("")
        self.recordingButton_2.setText("")
        self.playButton_2.setText("")
        self.pauseButton_2.setText("")
        self.stopButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"sampling rate:", None))
        self.samplingRate_Combo.setItemText(0, QCoreApplication.translate("MainWindow", u"44100", None))
        self.samplingRate_Combo.setItemText(1, QCoreApplication.translate("MainWindow", u"48000", None))
        self.samplingRate_Combo.setItemText(2, QCoreApplication.translate("MainWindow", u"22050", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.setMicrophone_1.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ch. 1", None))
        self.setMicrophone_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ch. 2", None))
        self.setSource_1.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.exportAudioButton.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Signal Editor", None))
        self.logo.setText("")
        self.importButton.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"remove", None))
        self.removeAllButton.setText(QCoreApplication.translate("MainWindow", u"remove all", None))
        self.playButton.setText("")
        self.pauseButton.setText("")
        self.stopButton.setText("")
        self.muteButton.setText("")
        self.filterAudioButton.setText(QCoreApplication.translate("MainWindow", u"filter", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.switch_50.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"50 Hz", None))
        self.switch_63.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"63 Hz", None))
        self.switch_80.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"80 Hz", None))
        self.switch_100.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"100 Hz", None))
        self.switch_125.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"125 Hz", None))
        self.switch_160.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"160 Hz", None))
        self.switch_200.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.switch_250.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"250 Hz", None))
        self.switch_315.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"315 Hz", None))
        self.switch_400.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"400 Hz", None))
        self.switch_500.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"500 Hz", None))
        self.switch_630.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"630 Hz", None))
        self.switch_800.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"800 Hz", None))
        self.switch_1000.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"1 kHz", None))
        self.switch_1250.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"1.25 kHz", None))
        self.switch_1600.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"1.6 kHz", None))
        self.switch_2000.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"2 kHz", None))
        self.switch_2500.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"2.5 kHz", None))
        self.switch_3150.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"3.15 kHz", None))
        self.switch_4000.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"4 kHz", None))
        self.switch_5000.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"5 kHz", None))
        self.switch_6300.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"6.3 kHz", None))
        self.switch_8000.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"8 kHz", None))
        self.switch_10000.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"10 kHz", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Calibration Setup", None))
        self.logo_3.setText("")
        self.label_86.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Basket", None))
        self.checkHold.setText(QCoreApplication.translate("MainWindow", u"Hold on", None))
        self.importGraph.setText(QCoreApplication.translate("MainWindow", u"import", None))
        self.removeGraph.setText(QCoreApplication.translate("MainWindow", u"remove", None))
        self.removeAllGraph.setText(QCoreApplication.translate("MainWindow", u"remove all", None))
        self.label_98.setText("")
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Headphones", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"type:", None))
        self.typeHeadBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.typeHeadBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Sennheiser", None))

        self.label_101.setText(QCoreApplication.translate("MainWindow", u"model:", None))
        self.label_102.setText("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"HATS", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"type:", None))
        self.typeHatsBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.typeHatsBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"HeadAcoustics", None))
        self.typeHatsBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"GRASS", None))

        self.label_105.setText(QCoreApplication.translate("MainWindow", u"model:", None))
        self.plot.setText(QCoreApplication.translate("MainWindow", u"plot", None))
        self.convolve.setText(QCoreApplication.translate("MainWindow", u"convolve", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Develop by Henrique Silveira\n"
"Juc\u00e9lio Tavares and Ricardo Brum", None))
    # retranslateUi

