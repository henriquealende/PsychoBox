# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newProject.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resourceGui_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 400)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.infoBar2 = QFrame(Form)
        self.infoBar2.setObjectName(u"infoBar2")
        self.infoBar2.setMinimumSize(QSize(0, 50))
        self.infoBar2.setMaximumSize(QSize(16777215, 50))
        self.infoBar2.setStyleSheet(u"QFrame{\n"
"	background-color : #006d34;\n"
"}")
        self.infoBar2.setFrameShape(QFrame.NoFrame)
        self.infoBar2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.infoBar2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.infoBar2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(115, 30))
        self.label_2.setMaximumSize(QSize(115, 30))
        self.label_2.setPixmap(QPixmap(u":/logos/img/nidecLogo.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.infoBar2)
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


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.infoBar2)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(237, 237, 237);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.newProjectLabel = QLabel(self.frame_4)
        self.newProjectLabel.setObjectName(u"newProjectLabel")
        font = QFont()
        font.setFamilies([u"PF BeauSans Pro"])
        font.setPointSize(20)
        font.setBold(True)
        self.newProjectLabel.setFont(font)
        self.newProjectLabel.setStyleSheet(u"color: #009b4a;")

        self.verticalLayout_3.addWidget(self.newProjectLabel)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.loginFrame = QFrame(self.frame_2)
        self.loginFrame.setObjectName(u"loginFrame")
        self.loginFrame.setMinimumSize(QSize(0, 0))
        self.loginFrame.setMaximumSize(QSize(16777215, 16777215))
        self.loginFrame.setStyleSheet(u"QLineEdit{\n"
"	border: 2px solid #006d34;\n"
"	border-radius: 15px;\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(182, 182, 182);\n"
"	padding-left: 10px;\n"
"	padding-right:20px;\n"
"}\n"
"QLineEdit:hover{\n"
"	border: 2px solid  #009b4a;\n"
"}")
        self.loginFrame.setFrameShape(QFrame.NoFrame)
        self.loginFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.loginFrame)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.projectLineEdit = QLineEdit(self.loginFrame)
        self.projectLineEdit.setObjectName(u"projectLineEdit")
        self.projectLineEdit.setMinimumSize(QSize(240, 30))
        font1 = QFont()
        font1.setFamilies([u"PF BeauSans Pro"])
        font1.setPointSize(14)
        self.projectLineEdit.setFont(font1)
        self.projectLineEdit.setStyleSheet(u"")

        self.verticalLayout_36.addWidget(self.projectLineEdit)

        self.commentLlineEdit = QLineEdit(self.loginFrame)
        self.commentLlineEdit.setObjectName(u"commentLlineEdit")
        self.commentLlineEdit.setMinimumSize(QSize(240, 150))
        self.commentLlineEdit.setFont(font1)
        self.commentLlineEdit.setStyleSheet(u"")
        self.commentLlineEdit.setEchoMode(QLineEdit.Normal)
        self.commentLlineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_36.addWidget(self.commentLlineEdit)

        self.applyButton = QPushButton(self.loginFrame)
        self.applyButton.setObjectName(u"applyButton")
        self.applyButton.setMinimumSize(QSize(0, 30))
        self.applyButton.setFont(font1)
        self.applyButton.setStyleSheet(u"QPushButton {\n"
"	padding-left:12px;\n"
"	text-align: left;\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(252, 175, 62,255), stop:1 rgba(241, 102, 55, 255));\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(79,186,160,255), stop:1 #009b4a);\n"
"	}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(241, 102, 55)\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_36.addWidget(self.applyButton)


        self.verticalLayout_2.addWidget(self.loginFrame)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.minimizeButton.setText("")
        self.closeAllButton.setText("")
        self.newProjectLabel.setText(QCoreApplication.translate("Form", u"New Project", None))
        self.projectLineEdit.setText("")
        self.projectLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"project name", None))
        self.commentLlineEdit.setText("")
        self.commentLlineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"input a comment", None))
        self.applyButton.setText(QCoreApplication.translate("Form", u"apply", None))
    # retranslateUi

