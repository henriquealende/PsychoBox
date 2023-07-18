# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'expand.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resourceGui_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(962, 665)
        Form.setMinimumSize(QSize(962, 665))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topContent = QFrame(Form)
        self.topContent.setObjectName(u"topContent")
        self.topContent.setMinimumSize(QSize(0, 50))
        self.topContent.setMaximumSize(QSize(16777215, 50))
        self.topContent.setSizeIncrement(QSize(0, 0))
        self.topContent.setFrameShape(QFrame.NoFrame)
        self.topContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topContent)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.infoBar = QFrame(self.topContent)
        self.infoBar.setObjectName(u"infoBar")
        self.infoBar.setStyleSheet(u"QFrame{\n"
"	background-color : #006d34;\n"
"}")
        self.infoBar.setFrameShape(QFrame.NoFrame)
        self.infoBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.infoBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_1 = QFrame(self.infoBar)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.label_1 = QLabel(self.frame_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(115, 30))
        self.label_1.setMaximumSize(QSize(115, 30))
        self.label_1.setPixmap(QPixmap(u":/logos/img/nidecLogo.png"))
        self.label_1.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.label_1)


        self.horizontalLayout_5.addWidget(self.frame_1)

        self.frame_2 = QFrame(self.infoBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(75, 16777215))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.minimizeButton = QPushButton(self.frame_2)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMaximumSize(QSize(20, 20))
        self.minimizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #ffbe38;\n"
"	border-radius: 10px;\n"
"	border: 2px solid  #d5a342;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 58)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/img/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.minimizeButton, 0, Qt.AlignRight)

        self.closeAllButton = QPushButton(self.frame_2)
        self.closeAllButton.setObjectName(u"closeAllButton")
        self.closeAllButton.setMaximumSize(QSize(20, 20))
        self.closeAllButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #fc5753;\n"
"	border-radius: 10px;\n"
"	border: 2px solid  #cf5254;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 119, 119)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAllButton.setIcon(icon1)
        self.closeAllButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_7.addWidget(self.closeAllButton, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_2.addWidget(self.infoBar)


        self.verticalLayout.addWidget(self.topContent)

        self.graphFrameView = QFrame(Form)
        self.graphFrameView.setObjectName(u"graphFrameView")
        self.graphFrameView.setMinimumSize(QSize(0, 0))
        self.graphFrameView.setMaximumSize(QSize(16777215, 16777215))
        self.graphFrameView.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"}\n"
"")
        self.graphFrameView.setFrameShape(QFrame.StyledPanel)
        self.graphFrameView.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.graphFrameView)
        self.verticalLayout_18.setSpacing(7)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.graphFrameView)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 50))
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_5.setPixmap(QPixmap(u":/icons/img/graphicsEnabled.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setMargin(10)

        self.horizontalLayout_18.addWidget(self.label_5)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setFamilies([u"PF BeauSans Pro"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: #009b4a;")

        self.horizontalLayout_18.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 50))
        self.label_6.setMaximumSize(QSize(100, 50))
        self.label_6.setPixmap(QPixmap(u":/logos/img/logo.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_6)


        self.verticalLayout_18.addWidget(self.frame_3)

        self.frame = QFrame(self.graphFrameView)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usernameLabel_5 = QLabel(self.frame)
        self.usernameLabel_5.setObjectName(u"usernameLabel_5")
        self.usernameLabel_5.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"PF BeauSans Pro"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.usernameLabel_5.setFont(font1)
        self.usernameLabel_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.usernameLabel_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.usernameLabel_5)

        self.domainBox = QComboBox(self.frame)
        self.domainBox.setObjectName(u"domainBox")
        self.domainBox.setEnabled(True)
        self.domainBox.setMinimumSize(QSize(260, 30))
        self.domainBox.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"PF BeauSans Pro"])
        font2.setPointSize(11)
        self.domainBox.setFont(font2)
        self.domainBox.setStyleSheet(u"QComboBox {\n"
"	border: 1px solid #333333;\n"
"	border-radius: 15px;\n"
"	background:  rgb(70, 70, 70);\n"
"	padding: 10x 23px 5px 5x;\n"
"	min-width: 10em;\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left: 30px;\n"
"	margin-right: 5px;\n"
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
"	selection-background-color: rgb(70, 70, 70);\n"
"	selection-color: #4f4f4f;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.domainBox)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"QPushButton {	\n"
"	image: url(:/icons/img/refresh.png);\n"
"	background-color: rgb(180,180,180);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.pushButton.setIconSize(QSize(15, 15))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(593, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_18.addWidget(self.frame)

        self.chartFrame = QFrame(self.graphFrameView)
        self.chartFrame.setObjectName(u"chartFrame")
        self.chartFrame.setFrameShape(QFrame.StyledPanel)
        self.chartFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.chartFrame)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalLayout_46.addLayout(self.gridLayout)


        self.verticalLayout_18.addWidget(self.chartFrame)

        self.frame_4 = QFrame(self.graphFrameView)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 30))
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setStyleSheet(u"\n"
"QPushButton {\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"	background-color: #006d34;\n"
"	border:none;\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
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
"QPushButton:disabled{\n"
"	background-color:rgb(70, 70, 70);\n"
"	color: rgb(136,138,133);\n"
"	}\n"
"")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_39.setSpacing(6)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer)

        self.exportFig = QPushButton(self.frame_4)
        self.exportFig.setObjectName(u"exportFig")
        self.exportFig.setEnabled(False)
        self.exportFig.setMinimumSize(QSize(125, 30))
        self.exportFig.setMaximumSize(QSize(125, 30))
        font3 = QFont()
        font3.setFamilies([u"PF BeauSans Pro"])
        font3.setPointSize(12)
        self.exportFig.setFont(font3)

        self.horizontalLayout_39.addWidget(self.exportFig)

        self.exportButton = QPushButton(self.frame_4)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setEnabled(False)
        self.exportButton.setMinimumSize(QSize(125, 30))
        self.exportButton.setMaximumSize(QSize(125, 30))
        self.exportButton.setFont(font3)

        self.horizontalLayout_39.addWidget(self.exportButton)


        self.verticalLayout_18.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.graphFrameView)

        self.bottomContent = QFrame(Form)
        self.bottomContent.setObjectName(u"bottomContent")
        self.bottomContent.setMinimumSize(QSize(0, 50))
        self.bottomContent.setMaximumSize(QSize(16777215, 50))
        self.bottomContent.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.bottomContent.setFrameShape(QFrame.NoFrame)
        self.bottomContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.bottomContent)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.bottomContent)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"PF BeauSans Pro"])
        font4.setPointSize(10)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_11.addWidget(self.label_2)

        self.label_4 = QLabel(self.bottomContent)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamilies([u"PF BeauSans Pro"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_11.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.bottomContent)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_1.setText("")
        self.minimizeButton.setText("")
        self.closeAllButton.setText("")
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Chart", None))
        self.label_6.setText("")
        self.usernameLabel_5.setText(QCoreApplication.translate("Form", u"Domain", None))
        self.domainBox.setCurrentText("")
        self.pushButton.setText("")
        self.exportFig.setText(QCoreApplication.translate("Form", u"export figure", None))
        self.exportButton.setText(QCoreApplication.translate("Form", u"export data", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u00a9 2021 Nidec\n"
"All rights reserved to Nidec ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Develop by Henrique Silveira\n"
" e Ricardo Brum", None))
    # retranslateUi

