# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Resources.rc_resourceGUI

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 800)
        Form.setMinimumSize(QSize(962, 665))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.infoBar3 = QFrame(Form)
        self.infoBar3.setObjectName(u"infoBar3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoBar3.sizePolicy().hasHeightForWidth())
        self.infoBar3.setSizePolicy(sizePolicy)
        self.infoBar3.setMinimumSize(QSize(0, 50))
        self.infoBar3.setMaximumSize(QSize(16777215, 300))
        self.infoBar3.setStyleSheet(u"QFrame{\n"
"	background-color : rgb(117, 117, 117);\n"
"}\n"
"")
        self.infoBar3.setFrameShape(QFrame.Shape.NoFrame)
        self.infoBar3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.infoBar3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.infoBar3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/logos/img/psychobox_logo2.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frameButtons = QFrame(self.infoBar3)
        self.frameButtons.setObjectName(u"frameButtons")
        self.frameButtons.setMaximumSize(QSize(120, 16777215))
        self.frameButtons.setStyleSheet(u"QPushButton {\n"
"	border-radius: 10px;\n"
"}")
        self.frameButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.frameButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
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
        icon = QIcon()
        icon.addFile(u":/icons/img/minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.frameButtons)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMaximumSize(QSize(20, 20))
        self.maximizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color:  rgb(237, 105, 59);\n"
"	border: 2px solid rgb(184, 80, 45) ;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(220, 147, 0)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/maximizar-janela.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeButton.setIcon(icon1)
        self.maximizeButton.setIconSize(QSize(12, 12))

        self.horizontalLayout.addWidget(self.maximizeButton)

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
        icon2 = QIcon()
        icon2.addFile(u":/icons/img/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAllButton.setIcon(icon2)
        self.closeAllButton.setIconSize(QSize(12, 12))

        self.horizontalLayout.addWidget(self.closeAllButton)


        self.horizontalLayout_5.addWidget(self.frameButtons)


        self.verticalLayout.addWidget(self.infoBar3)

        self.chart = QFrame(Form)
        self.chart.setObjectName(u"chart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chart.sizePolicy().hasHeightForWidth())
        self.chart.setSizePolicy(sizePolicy1)
        self.chart.setMaximumSize(QSize(16777215, 16777215))
        self.chart.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.chart.setFrameShape(QFrame.Shape.StyledPanel)
        self.chart.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.chart)
        self.horizontalLayout_47.setSpacing(5)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(5, 5, 5, 5)
        self.frame_17 = QFrame(self.chart)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px;\n"
"}\n"
"")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 2)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(235, 52))
        self.frame_18.setMaximumSize(QSize(16777215, 52))
        self.frame_18.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"		background-color: rgb(80, 184, 158);\n"
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
"QComboBox {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 10x 23px 5px 5x;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"	margin-right: 5px;\n"
"	padding-left: 8px\n"
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
"border: 3px solid  #009b4a;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/img/downArrow.png);\n"
"	width : 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" \n"
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"\n"
"")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(50, 50))
        self.label_12.setMaximumSize(QSize(50, 50))
        self.label_12.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_12.setPixmap(QPixmap(u":/icons/img/statistics.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setMargin(10)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 55))
        self.label_13.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"PF BeauSans Pro"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(70, 70, 70)")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.select_area = QPushButton(self.frame_18)
        self.select_area.setObjectName(u"select_area")
        self.select_area.setMinimumSize(QSize(30, 30))
        self.select_area.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/img/select_area.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_area.setIcon(icon3)
        self.select_area.setIconSize(QSize(18, 18))
        self.select_area.setCheckable(True)
        self.select_area.setChecked(False)

        self.horizontalLayout_4.addWidget(self.select_area)

        self.windowButton = QPushButton(self.frame_18)
        self.windowButton.setObjectName(u"windowButton")
        self.windowButton.setEnabled(False)
        self.windowButton.setMinimumSize(QSize(30, 30))
        self.windowButton.setMaximumSize(QSize(30, 30))
        self.windowButton.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/img/gaussian-function.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.windowButton.setIcon(icon4)
        self.windowButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.windowButton)

        self.comboBox = QComboBox(self.frame_18)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)
        self.comboBox.setMinimumSize(QSize(150, 30))
        self.comboBox.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(11)
        self.comboBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.frame_18)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(873, 545))
        self.frame_19.setStyleSheet(u"")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.frame_19)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_10.addWidget(self.frame_19)

        self.frame_axis = QFrame(self.frame_17)
        self.frame_axis.setObjectName(u"frame_axis")
        self.frame_axis.setMaximumSize(QSize(16777215, 40))
        self.frame_axis.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_axis.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	background:  rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	background-color: rgb(80, 184, 158);\n"
"\n"
"}\n"
"QLineEdit {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 12px;\n"
"	background:  rgb(70, 70, 70);\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 3px 0px 2px 2px\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"border: 3px solid  #009b4a;\n"
"}\n"
"\n"
"\n"
"QLineEdit:disabled{\n"
"	color: rgb(136, 138, 133);\n"
"}\n"
"\n"
"")
        self.frame_axis.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_axis.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_axis)
        self.horizontalLayout_6.setSpacing(50)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_20 = QFrame(self.frame_axis)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_20)
        self.label_77.setObjectName(u"label_77")
        font2 = QFont()
        font2.setFamilies([u"PF BeauSans Pro"])
        font2.setPointSize(12)
        self.label_77.setFont(font2)
        self.label_77.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_43.addWidget(self.label_77)

        self.label_78 = QLabel(self.frame_20)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(30, 16777215))
        font3 = QFont()
        font3.setFamilies([u"PF BeauSans Pro"])
        self.label_78.setFont(font3)
        self.label_78.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_43.addWidget(self.label_78)

        self.x_min = QLineEdit(self.frame_20)
        self.x_min.setObjectName(u"x_min")
        self.x_min.setMinimumSize(QSize(100, 24))
        self.x_min.setMaximumSize(QSize(100, 24))

        self.horizontalLayout_43.addWidget(self.x_min)

        self.label_79 = QLabel(self.frame_20)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(30, 0))
        self.label_79.setMaximumSize(QSize(30, 16777215))
        self.label_79.setFont(font3)
        self.label_79.setStyleSheet(u"color: rgb(255,255,255);")

        self.horizontalLayout_43.addWidget(self.label_79)

        self.x_max = QLineEdit(self.frame_20)
        self.x_max.setObjectName(u"x_max")
        self.x_max.setMinimumSize(QSize(100, 24))
        self.x_max.setMaximumSize(QSize(100, 24))

        self.horizontalLayout_43.addWidget(self.x_max)


        self.horizontalLayout_6.addWidget(self.frame_20)

        self.frame_100 = QFrame(self.frame_axis)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_48.setSpacing(10)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.frame_100)
        self.label_66.setObjectName(u"label_66")
        font4 = QFont()
        font4.setFamilies([u"PF BeauSans Pro"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_66.setFont(font4)
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_48.addWidget(self.label_66)

        self.label_80 = QLabel(self.frame_100)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(30, 0))
        self.label_80.setMaximumSize(QSize(30, 16777215))
        self.label_80.setFont(font3)
        self.label_80.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_48.addWidget(self.label_80)

        self.y_min = QLineEdit(self.frame_100)
        self.y_min.setObjectName(u"y_min")
        self.y_min.setMinimumSize(QSize(100, 24))
        self.y_min.setMaximumSize(QSize(100, 24))

        self.horizontalLayout_48.addWidget(self.y_min)

        self.label_81 = QLabel(self.frame_100)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(30, 0))
        self.label_81.setMaximumSize(QSize(30, 16777215))
        self.label_81.setFont(font3)
        self.label_81.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_48.addWidget(self.label_81)

        self.y_max = QLineEdit(self.frame_100)
        self.y_max.setObjectName(u"y_max")
        self.y_max.setMinimumSize(QSize(100, 24))
        self.y_max.setMaximumSize(QSize(100, 24))

        self.horizontalLayout_48.addWidget(self.y_max)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_3)

        self.refresh = QPushButton(self.frame_100)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setMinimumSize(QSize(24, 24))
        self.refresh.setMaximumSize(QSize(24, 24))
        self.refresh.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/img/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh.setIcon(icon5)
        self.refresh.setIconSize(QSize(12, 12))

        self.horizontalLayout_48.addWidget(self.refresh)


        self.horizontalLayout_6.addWidget(self.frame_100)


        self.verticalLayout_10.addWidget(self.frame_axis)


        self.horizontalLayout_47.addWidget(self.frame_17)

        self.frame_21 = QFrame(self.chart)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(300, 0))
        self.frame_21.setMaximumSize(QSize(500, 16777215))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 10x 23px 5px 5x;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 5px;\n"
"	margin-right: 5px;\n"
"	padding-left: 8px\n"
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
"border: 3px solid  #009b4a;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 20px;\n"
" \n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {    \n"
"	image: url(:/icons/img/downArrow.png);\n"
"	width : 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractView{\n"
"	background-color: #4f4f4f;\n"
"	color: #999999;\n"
" \n"
"	selection-background-color: "
                        "rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"\n"
"QCheckBox{\n"
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
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 0)
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(235, 52))
        self.frame_22.setMaximumSize(QSize(16777215, 52))
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 50))
        self.label_14.setMaximumSize(QSize(50, 50))
        self.label_14.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_14.setPixmap(QPixmap(u":/icons/img/settingsEnable.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setMargin(10)

        self.horizontalLayout_8.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_22)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(70, 70, 70)")

        self.horizontalLayout_8.addWidget(self.label_15)


        self.verticalLayout_12.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(225, 80))
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_23)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_16)

        self.mainBox = QComboBox(self.frame_23)
        self.mainBox.addItem("")
        self.mainBox.addItem("")
        self.mainBox.setObjectName(u"mainBox")
        self.mainBox.setMinimumSize(QSize(203, 30))
        self.mainBox.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamilies([u"PF BeauSans Pro"])
        font5.setPointSize(11)
        self.mainBox.setFont(font5)
        self.mainBox.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.mainBox)


        self.verticalLayout_12.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(225, 80))
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_24)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_24)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 20))
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_17)

        self.domainBox = QComboBox(self.frame_24)
        self.domainBox.addItem("")
        self.domainBox.addItem("")
        self.domainBox.setObjectName(u"domainBox")
        self.domainBox.setEnabled(True)
        self.domainBox.setMinimumSize(QSize(203, 30))
        self.domainBox.setMaximumSize(QSize(16777215, 30))
        self.domainBox.setFont(font5)
        self.domainBox.setEditable(False)

        self.verticalLayout_14.addWidget(self.domainBox)


        self.verticalLayout_12.addWidget(self.frame_24)

        self.frame_samplingBox = QFrame(self.frame_21)
        self.frame_samplingBox.setObjectName(u"frame_samplingBox")
        self.frame_samplingBox.setMinimumSize(QSize(225, 80))
        self.frame_samplingBox.setMaximumSize(QSize(16777215, 16777215))
        self.frame_samplingBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_samplingBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_samplingBox)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_samplingBox)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_15.addWidget(self.label_18)

        self.samplingBox = QComboBox(self.frame_samplingBox)
        self.samplingBox.addItem("")
        self.samplingBox.addItem("")
        self.samplingBox.setObjectName(u"samplingBox")
        self.samplingBox.setEnabled(True)
        self.samplingBox.setMinimumSize(QSize(203, 30))
        self.samplingBox.setMaximumSize(QSize(16777215, 30))
        self.samplingBox.setFont(font5)
        self.samplingBox.setEditable(False)

        self.verticalLayout_15.addWidget(self.samplingBox)


        self.verticalLayout_12.addWidget(self.frame_samplingBox)

        self.frame_98 = QFrame(self.frame_21)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(225, 50))
        self.frame_98.setMaximumSize(QSize(16777215, 100))
        self.frame_98.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.usernameLabel_9 = QLabel(self.frame_98)
        self.usernameLabel_9.setObjectName(u"usernameLabel_9")
        self.usernameLabel_9.setMaximumSize(QSize(16777215, 20))
        self.usernameLabel_9.setFont(font4)
        self.usernameLabel_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usernameLabel_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.usernameLabel_9)

        self.automaticCheckBox = QCheckBox(self.frame_98)
        self.automaticCheckBox.setObjectName(u"automaticCheckBox")
        self.automaticCheckBox.setEnabled(True)
        font6 = QFont()
        font6.setFamilies([u"PF BeauSans Pro"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.automaticCheckBox.setFont(font6)
        self.automaticCheckBox.setStyleSheet(u"")
        self.automaticCheckBox.setCheckable(True)
        self.automaticCheckBox.setChecked(True)

        self.horizontalLayout_49.addWidget(self.automaticCheckBox)


        self.verticalLayout_12.addWidget(self.frame_98)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.frame_25 = QFrame(self.frame_21)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(225, 100))
        self.frame_25.setMaximumSize(QSize(16777215, 100))
        self.frame_25.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_25.setStyleSheet(u"\n"
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
        self.frame_25.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_25)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.exportFig = QPushButton(self.frame_25)
        self.exportFig.setObjectName(u"exportFig")
        self.exportFig.setEnabled(True)
        self.exportFig.setMinimumSize(QSize(220, 30))
        self.exportFig.setMaximumSize(QSize(16777215, 30))
        self.exportFig.setFont(font2)

        self.verticalLayout_16.addWidget(self.exportFig, 0, Qt.AlignmentFlag.AlignHCenter)

        self.exportData = QPushButton(self.frame_25)
        self.exportData.setObjectName(u"exportData")
        self.exportData.setEnabled(True)
        self.exportData.setMinimumSize(QSize(220, 30))
        self.exportData.setMaximumSize(QSize(16777215, 30))
        self.exportData.setFont(font2)

        self.verticalLayout_16.addWidget(self.exportData, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_25)


        self.horizontalLayout_47.addWidget(self.frame_21)


        self.verticalLayout.addWidget(self.chart)

        self.bottomContent = QFrame(Form)
        self.bottomContent.setObjectName(u"bottomContent")
        sizePolicy.setHeightForWidth(self.bottomContent.sizePolicy().hasHeightForWidth())
        self.bottomContent.setSizePolicy(sizePolicy)
        self.bottomContent.setMinimumSize(QSize(0, 50))
        self.bottomContent.setMaximumSize(QSize(16777215, 150))
        self.bottomContent.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.bottomContent.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.bottomContent)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.bottomContent)
        self.label.setObjectName(u"label")
        font7 = QFont()
        font7.setFamilies([u"PF BeauSans Pro"])
        font7.setPointSize(10)
        self.label.setFont(font7)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.horizontalLayout_11.addWidget(self.label)

        self.label_6 = QLabel(self.bottomContent)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.bottomContent)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText("")
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.closeAllButton.setText("")
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"Chart", None))
        self.select_area.setText("")
        self.windowButton.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Rectangular", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Hanning", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Hamming", None))

        self.pushButton.setText("")
        self.label_77.setText(QCoreApplication.translate("Form", u"x-axis", None))
        self.label_78.setText(QCoreApplication.translate("Form", u"from:", None))
        self.label_79.setText(QCoreApplication.translate("Form", u"to:", None))
        self.label_66.setText(QCoreApplication.translate("Form", u"y-axis", None))
        self.label_80.setText(QCoreApplication.translate("Form", u"from:", None))
        self.label_81.setText(QCoreApplication.translate("Form", u"to:", None))
        self.refresh.setText("")
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"Settings", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"metrics:", None))
        self.mainBox.setItemText(0, QCoreApplication.translate("Form", u"Time-Frequency", None))
        self.mainBox.setItemText(1, QCoreApplication.translate("Form", u"Metrics", None))

        self.label_17.setText(QCoreApplication.translate("Form", u"domain:", None))
        self.domainBox.setItemText(0, QCoreApplication.translate("Form", u"Time", None))
        self.domainBox.setItemText(1, QCoreApplication.translate("Form", u"Frequency", None))

        self.domainBox.setCurrentText(QCoreApplication.translate("Form", u"Time", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"format:", None))
        self.samplingBox.setItemText(0, QCoreApplication.translate("Form", u"Linear", None))
        self.samplingBox.setItemText(1, QCoreApplication.translate("Form", u"1/3 octave", None))

        self.usernameLabel_9.setText(QCoreApplication.translate("Form", u"limits:", None))
        self.automaticCheckBox.setText(QCoreApplication.translate("Form", u"automatic", None))
        self.exportFig.setText(QCoreApplication.translate("Form", u"export figure", None))
        self.exportData.setText(QCoreApplication.translate("Form", u"export data", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Develop by Henrique Silveira\n"
"Juc\u00e9lio Tavares and Ricardo Brum", None))
    # retranslateUi

