# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StringConnection.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_StringConnection(object):
    def setupUi(self, StringConnection):
        if not StringConnection.objectName():
            StringConnection.setObjectName(u"StringConnection")
        StringConnection.resize(730, 200)
        StringConnection.setMinimumSize(QSize(730, 200))
        StringConnection.setMaximumSize(QSize(730, 200))
        self.centralwidget = QWidget(StringConnection)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fram_content = QFrame(self.centralwidget)
        self.fram_content.setObjectName(u"fram_content")
        self.fram_content.setFrameShape(QFrame.StyledPanel)
        self.fram_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fram_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.fram_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.btn_testConnection = QPushButton(self.frame_3)
        self.btn_testConnection.setObjectName(u"btn_testConnection")
        self.btn_testConnection.setGeometry(QRect(461, 88, 150, 45))
        self.btn_testConnection.setMinimumSize(QSize(150, 45))
        self.btn_testConnection.setMaximumSize(QSize(150, 45))
        self.btn_testConnection.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.btn_testConnection.setFont(font)
        self.btn_testConnection.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_testConnection.setInputMethodHints(Qt.ImhNone)
        icon = QIcon()
        icon.addFile(u"../src/icon_uncheck.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"../src/icon_uncheck.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_testConnection.setIcon(icon)
        self.btn_testConnection.setIconSize(QSize(20, 20))
        self.btn_exit = QPushButton(self.frame_3)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(620, 41, 100, 45))
        self.btn_exit.setMinimumSize(QSize(100, 45))
        self.btn_exit.setMaximumSize(QSize(100, 45))
        self.btn_exit.setBaseSize(QSize(0, 0))
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #F2163E;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #BF0404;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_exit.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u"../../Utilitario/src/icon_cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon1)
        self.btn_exit.setIconSize(QSize(20, 20))
        self.lb_localDb = QLabel(self.frame_3)
        self.lb_localDb.setObjectName(u"lb_localDb")
        self.lb_localDb.setGeometry(QRect(10, 39, 201, 31))
        self.le_localDb = QLineEdit(self.frame_3)
        self.le_localDb.setObjectName(u"le_localDb")
        self.le_localDb.setGeometry(QRect(210, 41, 241, 35))
        self.le_localDb.setMinimumSize(QSize(0, 35))
        self.le_localDb.setMaximumSize(QSize(16777215, 35))
        self.le_localDb.setSizeIncrement(QSize(200, 35))
        self.le_localDb.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.btn_instalation = QPushButton(self.frame_3)
        self.btn_instalation.setObjectName(u"btn_instalation")
        self.btn_instalation.setGeometry(QRect(460, 41, 150, 45))
        self.btn_instalation.setMinimumSize(QSize(150, 45))
        self.btn_instalation.setMaximumSize(QSize(150, 45))
        self.btn_instalation.setBaseSize(QSize(0, 0))
        self.btn_instalation.setFont(font)
        self.btn_instalation.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_instalation.setInputMethodHints(Qt.ImhNone)
        icon2 = QIcon()
        icon2.addFile(u"../src/icon_folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_instalation.setIcon(icon2)
        self.btn_instalation.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.fram_content)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMinimumSize(QSize(0, 55))
        self.frame_2.setMaximumSize(QSize(16777215, 55))
        self.frame_2.setSizeIncrement(QSize(0, 10))
        self.frame_2.setStyleSheet(u"background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.lb_commom = QLabel(self.frame_2)
        self.lb_commom.setObjectName(u"lb_commom")
        self.lb_commom.setMinimumSize(QSize(0, 35))
        self.lb_commom.setMaximumSize(QSize(16777215, 35))
        self.lb_commom.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.lb_commom.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_commom)

        self.btn_statusConection = QPushButton(self.frame_2)
        self.btn_statusConection.setObjectName(u"btn_statusConection")
        self.btn_statusConection.setMinimumSize(QSize(45, 45))
        self.btn_statusConection.setMaximumSize(QSize(45, 45))
        self.btn_statusConection.setBaseSize(QSize(0, 0))
        self.btn_statusConection.setFont(font)
        self.btn_statusConection.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 12px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: insetset;\n"
"	border-width: 2px;\n"
"	font: 75 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #4195FF;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_statusConection.setInputMethodHints(Qt.ImhNone)
        icon3 = QIcon()
        icon3.addFile(u"../src/icon_disconnectDB.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_statusConection.setIcon(icon3)
        self.btn_statusConection.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_statusConection)


        self.verticalLayout.addWidget(self.frame_2)

        StringConnection.setCentralWidget(self.centralwidget)

        self.retranslateUi(StringConnection)

        QMetaObject.connectSlotsByName(StringConnection)
    # setupUi

    def retranslateUi(self, StringConnection):
        StringConnection.setWindowTitle(QCoreApplication.translate("StringConnection", u"MainWindow", None))
        self.btn_testConnection.setText(QCoreApplication.translate("StringConnection", u"Testar conex\u00e3o", None))
        self.btn_exit.setText(QCoreApplication.translate("StringConnection", u"Sair", None))
        self.lb_localDb.setText(QCoreApplication.translate("StringConnection", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">Local de Instala\u00e7\u00e3o:</span></p></body></html>", None))
        self.le_localDb.setPlaceholderText(QCoreApplication.translate("StringConnection", u"Name Database", None))
        self.btn_instalation.setText(QCoreApplication.translate("StringConnection", u"Local de instala\u00e7\u00e3o", None))
        self.lb_commom.setText(QCoreApplication.translate("StringConnection", u"Utilitario de servi\u00e7os - vers\u00e3o 0.0.1 | Campo Grande -MS | 20:19", None))
        self.btn_statusConection.setText("")
    # retranslateUi

