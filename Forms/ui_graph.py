# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
        self.infoBar3 = QFrame(Form)
        self.infoBar3.setObjectName(u"infoBar3")
        self.infoBar3.setMinimumSize(QSize(0, 50))
        self.infoBar3.setMaximumSize(QSize(16777215, 50))
        self.infoBar3.setStyleSheet(u"QFrame{\n"
"	background-color : #006d34;\n"
"}")
        self.infoBar3.setFrameShape(QFrame.NoFrame)
        self.infoBar3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.infoBar3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.infoBar3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(115, 30))
        self.label_3.setMaximumSize(QSize(115, 30))
        self.label_3.setPixmap(QPixmap(u":/logos/img/nidecLogo.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.infoBar3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(75, 16777215))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.minimizeButton = QPushButton(self.frame_6)
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

        self.closeAllButton = QPushButton(self.frame_6)
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


        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.infoBar3)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_2)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.graphFrameView = QFrame(self.frame_2)
        self.graphFrameView.setObjectName(u"graphFrameView")
        self.graphFrameView.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(182, 182, 182);\n"
"}\n"
"")
        self.graphFrameView.setFrameShape(QFrame.NoFrame)
        self.graphFrameView.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.graphFrameView)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.graphFrameView)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_3)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 5, 5, 5)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(50, 50))
        self.label_4.setMaximumSize(QSize(50, 50))
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(70,70,70);\n"
"	border-radius: 25px;\n"
"}")
        self.label_4.setPixmap(QPixmap(u":/icons/img/graphicsEnabled.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setMargin(10)

        self.horizontalLayout_18.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"PF BeauSans Pro"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #009b4a;")

        self.horizontalLayout_18.addWidget(self.label_5)


        self.verticalLayout_18.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777206, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"PF BeauSans Pro"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_7)

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

        self.horizontalSpacer_2 = QSpacerItem(573, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_18.addWidget(self.frame)

        self.chartFrame = QFrame(self.frame_3)
        self.chartFrame.setObjectName(u"chartFrame")
        self.chartFrame.setFrameShape(QFrame.StyledPanel)
        self.chartFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.chartFrame)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.horizontalLayout_46.addLayout(self.gridLayout)


        self.verticalLayout_18.addWidget(self.chartFrame)

        self.frame_23 = QFrame(self.frame_3)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 30))
        self.frame_23.setMaximumSize(QSize(16777215, 30))
        self.frame_23.setStyleSheet(u"\n"
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
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_39.setSpacing(6)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer)

        self.exportFig = QPushButton(self.frame_23)
        self.exportFig.setObjectName(u"exportFig")
        self.exportFig.setEnabled(True)
        self.exportFig.setMinimumSize(QSize(125, 30))
        self.exportFig.setMaximumSize(QSize(125, 30))
        font3 = QFont()
        font3.setFamilies([u"PF BeauSans Pro"])
        font3.setPointSize(12)
        self.exportFig.setFont(font3)

        self.horizontalLayout_39.addWidget(self.exportFig)

        self.exportButton = QPushButton(self.frame_23)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setEnabled(True)
        self.exportButton.setMinimumSize(QSize(125, 30))
        self.exportButton.setMaximumSize(QSize(125, 30))
        self.exportButton.setFont(font3)

        self.horizontalLayout_39.addWidget(self.exportButton)


        self.verticalLayout_18.addWidget(self.frame_23)


        self.horizontalLayout_44.addWidget(self.frame_3)


        self.verticalLayout_67.addWidget(self.graphFrameView)


        self.verticalLayout.addWidget(self.frame_2)

        self.bottomContent = QFrame(Form)
        self.bottomContent.setObjectName(u"bottomContent")
        self.bottomContent.setMinimumSize(QSize(0, 50))
        self.bottomContent.setMaximumSize(QSize(16777215, 50))
        self.bottomContent.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(70, 70, 70);\n"
"}")
        self.bottomContent.setFrameShape(QFrame.NoFrame)
        self.bottomContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.bottomContent)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.bottomContent)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"PF BeauSans Pro"])
        font4.setPointSize(10)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_11.addWidget(self.label)

        self.label_6 = QLabel(self.bottomContent)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamilies([u"PF BeauSans Pro"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label_6.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout.addWidget(self.bottomContent)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText("")
        self.minimizeButton.setText("")
        self.closeAllButton.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Chart", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"domain:", None))
        self.domainBox.setCurrentText("")
        self.exportFig.setText(QCoreApplication.translate("Form", u"export figure", None))
        self.exportButton.setText(QCoreApplication.translate("Form", u"export data", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u00a9 2021 Nidec\n"
"All rights reserved to Nidec ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Develop by Henrique Silveira\n"
" and Ricardo Brum", None))
    # retranslateUi

