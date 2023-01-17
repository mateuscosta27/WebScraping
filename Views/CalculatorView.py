# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalculatorView.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainCalculator(object):
    def setupUi(self, MainCalculator):
        if not MainCalculator.objectName():
            MainCalculator.setObjectName(u"MainCalculator")
        MainCalculator.resize(800, 717)
        MainCalculator.setMaximumSize(QSize(800, 16777215))
        self.centralwidget = QWidget(MainCalculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 100))
        self.frame_header.setMaximumSize(QSize(16777215, 100))
        self.frame_header.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: #0954B2;")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_header)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lb_title = QLabel(self.frame_header)
        self.lb_title.setObjectName(u"lb_title")

        self.verticalLayout_2.addWidget(self.lb_title)


        self.verticalLayout.addWidget(self.frame_header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_investment = QFrame(self.frame_2)
        self.frame_investment.setObjectName(u"frame_investment")
        self.frame_investment.setMaximumSize(QSize(16777215, 300))
        self.frame_investment.setSizeIncrement(QSize(0, 300))
        self.frame_investment.setFrameShape(QFrame.StyledPanel)
        self.frame_investment.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_investment)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(70, 15, 0, 0)
        self.lb_profit = QLabel(self.frame_investment)
        self.lb_profit.setObjectName(u"lb_profit")
        self.lb_profit.setMinimumSize(QSize(100, 0))
        self.lb_profit.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout.addWidget(self.lb_profit, 1, 1, 1, 1)

        self.le_profit = QLineEdit(self.frame_investment)
        self.le_profit.setObjectName(u"le_profit")
        self.le_profit.setMinimumSize(QSize(200, 50))
        self.le_profit.setMaximumSize(QSize(80, 50))
        self.le_profit.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_profit.setReadOnly(True)

        self.gridLayout.addWidget(self.le_profit, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 5, 1, 1)

        self.le_tot_return = QLineEdit(self.frame_investment)
        self.le_tot_return.setObjectName(u"le_tot_return")
        self.le_tot_return.setMinimumSize(QSize(200, 50))
        self.le_tot_return.setMaximumSize(QSize(80, 50))
        self.le_tot_return.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_tot_return.setReadOnly(True)

        self.gridLayout.addWidget(self.le_tot_return, 2, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 2, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(463, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 5, 1, 1)

        self.le_value_invest = QLineEdit(self.frame_investment)
        self.le_value_invest.setObjectName(u"le_value_invest")
        self.le_value_invest.setMinimumSize(QSize(200, 50))
        self.le_value_invest.setMaximumSize(QSize(80, 16777215))
        self.le_value_invest.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")

        self.gridLayout.addWidget(self.le_value_invest, 0, 4, 1, 1)

        self.lb_tot_return = QLabel(self.frame_investment)
        self.lb_tot_return.setObjectName(u"lb_tot_return")
        self.lb_tot_return.setMinimumSize(QSize(100, 0))
        self.lb_tot_return.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout.addWidget(self.lb_tot_return, 2, 1, 1, 1)

        self.lb_investment = QLabel(self.frame_investment)
        self.lb_investment.setObjectName(u"lb_investment")
        self.lb_investment.setMinimumSize(QSize(150, 0))
        self.lb_investment.setMaximumSize(QSize(150, 16777215))
        self.lb_investment.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout.addWidget(self.lb_investment, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_investment)

        self.fram_odds = QFrame(self.frame_2)
        self.fram_odds.setObjectName(u"fram_odds")
        self.fram_odds.setMaximumSize(QSize(800, 16777215))
        self.fram_odds.setFrameShape(QFrame.StyledPanel)
        self.fram_odds.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.fram_odds)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(0, 25, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 3, 5, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_10, 4, 6, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 4, 0, 1, 1)

        self.le_return2 = QLineEdit(self.fram_odds)
        self.le_return2.setObjectName(u"le_return2")
        self.le_return2.setMinimumSize(QSize(200, 50))
        self.le_return2.setMaximumSize(QSize(200, 16777215))
        self.le_return2.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_return2.setAlignment(Qt.AlignCenter)
        self.le_return2.setDragEnabled(False)
        self.le_return2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_return2, 2, 5, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(100, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.lb_odds2 = QLabel(self.fram_odds)
        self.lb_odds2.setObjectName(u"lb_odds2")
        self.lb_odds2.setMinimumSize(QSize(100, 50))
        self.lb_odds2.setMaximumSize(QSize(100, 50))
        self.lb_odds2.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout_2.addWidget(self.lb_odds2, 1, 1, 1, 1)

        self.lb_parcial_investment = QLabel(self.fram_odds)
        self.lb_parcial_investment.setObjectName(u"lb_parcial_investment")
        self.lb_parcial_investment.setMinimumSize(QSize(0, 50))
        self.lb_parcial_investment.setMaximumSize(QSize(16777215, 50))
        self.lb_parcial_investment.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout_2.addWidget(self.lb_parcial_investment, 0, 3, 1, 1)

        self.lb_parcial_return = QLabel(self.fram_odds)
        self.lb_parcial_return.setObjectName(u"lb_parcial_return")
        self.lb_parcial_return.setMinimumSize(QSize(0, 50))
        self.lb_parcial_return.setMaximumSize(QSize(16777215, 50))
        self.lb_parcial_return.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout_2.addWidget(self.lb_parcial_return, 0, 5, 1, 1)

        self.le_odds1 = QLineEdit(self.fram_odds)
        self.le_odds1.setObjectName(u"le_odds1")
        self.le_odds1.setMinimumSize(QSize(0, 50))
        self.le_odds1.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_odds1.setAlignment(Qt.AlignCenter)
        self.le_odds1.setDragEnabled(False)
        self.le_odds1.setReadOnly(False)

        self.gridLayout_2.addWidget(self.le_odds1, 1, 2, 1, 1)

        self.le_invest1 = QLineEdit(self.fram_odds)
        self.le_invest1.setObjectName(u"le_invest1")
        self.le_invest1.setMinimumSize(QSize(200, 50))
        self.le_invest1.setMaximumSize(QSize(200, 16777215))
        self.le_invest1.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_invest1.setAlignment(Qt.AlignCenter)
        self.le_invest1.setDragEnabled(False)
        self.le_invest1.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_invest1, 1, 3, 1, 1)

        self.le_odds2 = QLineEdit(self.fram_odds)
        self.le_odds2.setObjectName(u"le_odds2")
        self.le_odds2.setMinimumSize(QSize(0, 50))
        self.le_odds2.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_odds2.setAlignment(Qt.AlignCenter)
        self.le_odds2.setDragEnabled(False)
        self.le_odds2.setReadOnly(False)

        self.gridLayout_2.addWidget(self.le_odds2, 2, 2, 1, 1)

        self.le_return1 = QLineEdit(self.fram_odds)
        self.le_return1.setObjectName(u"le_return1")
        self.le_return1.setMinimumSize(QSize(200, 50))
        self.le_return1.setMaximumSize(QSize(200, 16777215))
        self.le_return1.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_return1.setAlignment(Qt.AlignCenter)
        self.le_return1.setDragEnabled(False)
        self.le_return1.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_return1, 1, 4, 1, 2)

        self.horizontalSpacer_14 = QSpacerItem(43, 27, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 2, 0, 1, 1)

        self.lb_odds1 = QLabel(self.fram_odds)
        self.lb_odds1.setObjectName(u"lb_odds1")
        self.lb_odds1.setMinimumSize(QSize(100, 50))
        self.lb_odds1.setMaximumSize(QSize(100, 50))
        self.lb_odds1.setStyleSheet(u"background-color: #0954B2;")

        self.gridLayout_2.addWidget(self.lb_odds1, 2, 1, 1, 1)

        self.le_invest2 = QLineEdit(self.fram_odds)
        self.le_invest2.setObjectName(u"le_invest2")
        self.le_invest2.setMinimumSize(QSize(200, 50))
        self.le_invest2.setMaximumSize(QSize(200, 16777215))
        self.le_invest2.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(231, 231, 231);")
        self.le_invest2.setAlignment(Qt.AlignCenter)
        self.le_invest2.setDragEnabled(False)
        self.le_invest2.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_invest2, 2, 3, 1, 2)

        self.btn_calc = QPushButton(self.fram_odds)
        self.btn_calc.setObjectName(u"btn_calc")
        self.btn_calc.setMinimumSize(QSize(200, 100))
        self.btn_calc.setMaximumSize(QSize(170, 100))
        self.btn_calc.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")

        self.gridLayout_2.addWidget(self.btn_calc, 3, 3, 1, 1)

        self.btn_back = QPushButton(self.fram_odds)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setMinimumSize(QSize(200, 45))
        self.btn_back.setMaximumSize(QSize(200, 45))
        self.btn_back.setStyleSheet(u"QPushButton{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #0954B2;\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(26, 60, 102);\n"
"	border-radius: 8px;\n"
"	border-bottom-color: rgb(4, 35, 38);\n"
"	border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	border-style: none;\n"
"	border-width: 2px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:#0954B2;\n"
"	border-radius: 8px;\n"
"	border-top-color: rgb(4, 35, 38);\n"
"	border-left-color:  rgb(4, 35, 38);\n"
"}")

        self.gridLayout_2.addWidget(self.btn_back, 4, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.fram_odds)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_footer = QFrame(self.centralwidget)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMaximumSize(QSize(16777215, 40))
        self.frame_footer.setStyleSheet(u"background-color: #0954B2;\n"
"border-radius: 2px;\n"
"")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_footer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_commom = QLabel(self.frame_footer)
        self.lb_commom.setObjectName(u"lb_commom")
        self.lb_commom.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #fff;\n"
"")
        self.lb_commom.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_commom)


        self.verticalLayout.addWidget(self.frame_footer)

        MainCalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainCalculator)

        QMetaObject.connectSlotsByName(MainCalculator)
    # setupUi

    def retranslateUi(self, MainCalculator):
        MainCalculator.setWindowTitle(QCoreApplication.translate("MainCalculator", u"MainWindow", None))
        self.lb_title.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Calcular Aposta</span></p></body></html>", None))
        self.lb_profit.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Lucro</span></p></body></html>", None))
        self.le_profit.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"R$", None))
        self.le_tot_return.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"R$", None))
        self.le_value_invest.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"R$", None))
        self.lb_tot_return.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Retorno</span></p></body></html>", None))
        self.lb_investment.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Investimento</span></p></body></html>", None))
        self.le_return2.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"Odds", None))
        self.lb_odds2.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Odds1</span></p></body></html>", None))
        self.lb_parcial_investment.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Investimento</span></p></body></html>", None))
        self.lb_parcial_return.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Retorno</span></p></body></html>", None))
        self.le_odds1.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"Odds", None))
        self.le_invest1.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"Odds", None))
        self.le_odds2.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"Odds", None))
        self.le_return1.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"Odds", None))
        self.lb_odds1.setText(QCoreApplication.translate("MainCalculator", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Odds2</span></p></body></html>", None))
        self.le_invest2.setPlaceholderText(QCoreApplication.translate("MainCalculator", u"Odds", None))
        self.btn_calc.setText(QCoreApplication.translate("MainCalculator", u"Calcular", None))
        self.btn_back.setText(QCoreApplication.translate("MainCalculator", u"Voltar", None))
        self.lb_commom.setText(QCoreApplication.translate("MainCalculator", u"Todos os direitos reservados \u00a9  MaTTecnologia Aplicada 2022", None))
    # retranslateUi

