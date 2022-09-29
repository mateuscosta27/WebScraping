
from PyQt5 import QtCore, QtGui, QtWidgets
from formPrincipal import *


class Ui_formViewResult(object):
    def setupUi(self, formViewResult):
        formViewResult.setObjectName("formViewResult")
        formViewResult.resize(1200, 600)
        formViewResult.setMinimumSize(QtCore.QSize(1200, 600))
        formViewResult.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/principal_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formViewResult.setWindowIcon(icon)
        formViewResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        formViewResult.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        formViewResult.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(formViewResult)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(300, 1, 500, 50))
        self.lbl_title.setMinimumSize(QtCore.QSize(500, 50))
        self.lbl_title.setMaximumSize(QtCore.QSize(600, 50))
        self.lbl_title.setObjectName("lbl_title")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(800, 10, 375, 85))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(375, 85))
        self.groupBox.setMaximumSize(QtCore.QSize(375, 85))
        self.groupBox.setStyleSheet("background-color: rgb(3, 127, 140);\n"
"border-radius: 5px;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.rb_matchOdds = QtWidgets.QRadioButton(self.groupBox)
        self.rb_matchOdds.setGeometry(QtCore.QRect(20, 10, 140, 20))
        self.rb_matchOdds.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_matchOdds.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_matchOdds.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_matchOdds.setObjectName("rb_matchOdds")
        self.rb_DuplaChance = QtWidgets.QRadioButton(self.groupBox)
        self.rb_DuplaChance.setGeometry(QtCore.QRect(20, 50, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_DuplaChance.sizePolicy().hasHeightForWidth())
        self.rb_DuplaChance.setSizePolicy(sizePolicy)
        self.rb_DuplaChance.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_DuplaChance.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_DuplaChance.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_DuplaChance.setObjectName("rb_DuplaChance")
        self.rb_ambosMarcam = QtWidgets.QRadioButton(self.groupBox)
        self.rb_ambosMarcam.setGeometry(QtCore.QRect(210, 10, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_ambosMarcam.sizePolicy().hasHeightForWidth())
        self.rb_ambosMarcam.setSizePolicy(sizePolicy)
        self.rb_ambosMarcam.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_ambosMarcam.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_ambosMarcam.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_ambosMarcam.setObjectName("rb_ambosMarcam")
        self.rb_totalGols = QtWidgets.QRadioButton(self.groupBox)
        self.rb_totalGols.setGeometry(QtCore.QRect(210, 50, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_totalGols.sizePolicy().hasHeightForWidth())
        self.rb_totalGols.setSizePolicy(sizePolicy)
        self.rb_totalGols.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_totalGols.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_totalGols.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_totalGols.setChecked(True)
        self.rb_totalGols.setAutoRepeat(True)
        self.rb_totalGols.setObjectName("rb_totalGols")
        self.tb_view = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_view.setGeometry(QtCore.QRect(10, 110, 1170, 400))
        self.tb_view.setToolTipDuration(-3)
        self.tb_view.setObjectName("tb_view")
        self.tb_view.setColumnCount(0)
        self.tb_view.setRowCount(0)
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(1060, 540, 120, 45))
        self.btn_sair.setMinimumSize(QtCore.QSize(120, 45))
        self.btn_sair.setMaximumSize(QtCore.QSize(120, 45))
        self.btn_sair.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_sair.setObjectName("btn_sair")
        self.btn_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_voltar.setGeometry(QtCore.QRect(920, 540, 120, 45))
        self.btn_voltar.setMinimumSize(QtCore.QSize(120, 45))
        self.btn_voltar.setMaximumSize(QtCore.QSize(120, 45))
        self.btn_voltar.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_voltar.setObjectName("btn_voltar")
        self.btn_simular = QtWidgets.QPushButton(self.centralwidget)
        self.btn_simular.setGeometry(QtCore.QRect(780, 540, 120, 45))
        self.btn_simular.setMinimumSize(QtCore.QSize(120, 45))
        self.btn_simular.setMaximumSize(QtCore.QSize(120, 45))
        self.btn_simular.setStyleSheet("QPushButton{\n"
"    border-style: none;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 12px;\n"
"    border-bottom-color: rgb(4, 35, 38);\n"
"    border-right-color:  rgb(4, 35, 38);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-style: insetset;\n"
"    border-width: 2px;\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 8px;\n"
"    border-top-color: rgb(4, 35, 38);\n"
"    border-left-color:  rgb(4, 35, 38);\n"
"}")
        self.btn_simular.setObjectName("btn_simular")
        formViewResult.setCentralWidget(self.centralwidget)

        self.retranslateUi(formViewResult)
        QtCore.QMetaObject.connectSlotsByName(formViewResult)
        
        
        ###Botões do sistema##
        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_voltar.clicked.connect(self.comme_back)
        
        
    def comme_back(self):
        self.formPrincipal = QtWidgets.QMainWindow()
        self.ui = Ui_formPrincipal()
        self.ui.setupUi(self.formPrincipal)
        self.formPrincipal.show()
        formViewResult.close()
          
                
    def exit_system(self):
            sys.exit()

    def retranslateUi(self, formViewResult):
        _translate = QtCore.QCoreApplication.translate
        formViewResult.setWindowTitle(_translate("formViewResult", "Modulo Visualização"))
        self.lbl_title.setText(_translate("formViewResult", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">GERENCIADOR DE APOSTAS ESPORTIVAS</span></p></body></html>"))
        self.rb_matchOdds.setText(_translate("formViewResult", "Match Odds"))
        self.rb_DuplaChance.setText(_translate("formViewResult", "Dupla Chance"))
        self.rb_ambosMarcam.setText(_translate("formViewResult", "Ambos Marcam"))
        self.rb_totalGols.setText(_translate("formViewResult", "Total de Gols"))
        self.btn_sair.setText(_translate("formViewResult", "Sair"))
        self.btn_voltar.setText(_translate("formViewResult", "Voltar"))
        self.btn_simular.setText(_translate("formViewResult", "Simular Aposta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formViewResult = QtWidgets.QMainWindow()
    ui = Ui_formViewResult()
    ui.setupUi(formViewResult)
    formViewResult.show()
    sys.exit(app.exec_())
