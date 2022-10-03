import sqlite3
from formPrincipal import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formViewResult(object):
    def setupUi(self, formViewResult):
        formViewResult.setObjectName("formViewResult")
        formViewResult.resize(1275, 650)
        formViewResult.setMinimumSize(QtCore.QSize(1200, 600))
        formViewResult.setMaximumSize(QtCore.QSize(2000, 1500))
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
        self.groupBox.setGeometry(QtCore.QRect(800, 10, 375, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(375, 85))
        self.groupBox.setMaximumSize(QtCore.QSize(375, 150))
        self.groupBox.setStyleSheet("background-color: rgb(3, 127, 140);\n"
"border-radius: 5px;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.rb_matchOdds = QtWidgets.QRadioButton(self.groupBox)
        self.rb_matchOdds.setGeometry(QtCore.QRect(210, 10, 140, 20))
        self.rb_matchOdds.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_matchOdds.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_matchOdds.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_matchOdds.setObjectName("rb_matchOdds")
        self.rb_DuplaChance = QtWidgets.QRadioButton(self.groupBox)
        self.rb_DuplaChance.setGeometry(QtCore.QRect(20, 100, 140, 20))
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
        self.rb_ambosMarcam.setGeometry(QtCore.QRect(210, 40, 140, 20))
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
        self.rb_totalGols.setGeometry(QtCore.QRect(210, 70, 140, 20))
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
        self.rb_jogosBetano = QtWidgets.QRadioButton(self.groupBox)
        self.rb_jogosBetano.setGeometry(QtCore.QRect(20, 10, 140, 20))
        self.rb_jogosBetano.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_jogosBetano.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_jogosBetano.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_jogosBetano.setObjectName("rb_jogosBetano")
        self.rb_jogosPixbet = QtWidgets.QRadioButton(self.groupBox)
        self.rb_jogosPixbet.setGeometry(QtCore.QRect(20, 40, 140, 20))
        self.rb_jogosPixbet.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_jogosPixbet.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_jogosPixbet.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_jogosPixbet.setObjectName("rb_jogosPixbet")
        self.rb_matchJogos = QtWidgets.QRadioButton(self.groupBox)
        self.rb_matchJogos.setGeometry(QtCore.QRect(20, 70, 140, 20))
        self.rb_matchJogos.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_matchJogos.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_matchJogos.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.rb_matchJogos.setObjectName("rb_matchJogos")
        self.tb_view = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_view.setGeometry(QtCore.QRect(10, 180, 1251, 400))
        self.tb_view.setToolTipDuration(-3)
        self.tb_view.setObjectName("tb_view")
        self.tb_view.setColumnCount(15)
        self.tb_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_view.setHorizontalHeaderItem(14, item)
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(1139, 597, 120, 45))
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
        self.btn_voltar.setGeometry(QtCore.QRect(999, 597, 120, 45))
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
        self.btn_simular.setGeometry(QtCore.QRect(859, 597, 120, 45))
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
        self.lbl_table = QtWidgets.QLabel(self.centralwidget)
        self.lbl_table.setGeometry(QtCore.QRect(10, 111, 221, 41))
        self.lbl_table.setStyleSheet("\n"
"    font: 75 11pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(3, 127, 140);\n"
"    border-radius: 12px;\n"
"    ")
        self.lbl_table.setObjectName("lbl_table")
        formViewResult.setCentralWidget(self.centralwidget)

        self.retranslateUi(formViewResult)
        QtCore.QMetaObject.connectSlotsByName(formViewResult)

    def retranslateUi(self, formViewResult):
        _translate = QtCore.QCoreApplication.translate
        formViewResult.setWindowTitle(_translate("formViewResult", "Modulo Visualização"))
        self.lbl_title.setText(_translate("formViewResult", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">GERENCIADOR DE APOSTAS ESPORTIVAS</span></p></body></html>"))
        self.rb_matchOdds.setText(_translate("formViewResult", "Match Odds"))
        self.rb_DuplaChance.setText(_translate("formViewResult", "Dupla Chance"))
        self.rb_ambosMarcam.setText(_translate("formViewResult", "Ambos Marcam"))
        self.rb_totalGols.setText(_translate("formViewResult", "Total de Gols"))
        self.rb_jogosBetano.setText(_translate("formViewResult", "Jogos Betano"))
        self.rb_jogosPixbet.setText(_translate("formViewResult", "Jogos Pixbet"))
        self.rb_matchJogos.setText(_translate("formViewResult", "Match Jogos"))
        item = self.tb_view.horizontalHeaderItem(0)
        item.setText(_translate("formViewResult", "ind"))
        item = self.tb_view.horizontalHeaderItem(1)
        item.setText(_translate("formViewResult", "Hora"))
        item = self.tb_view.horizontalHeaderItem(2)
        item.setText(_translate("formViewResult", "Data"))
        item = self.tb_view.horizontalHeaderItem(3)
        item.setText(_translate("formViewResult", "TimeCasa"))
        item = self.tb_view.horizontalHeaderItem(4)
        item.setText(_translate("formViewResult", "TimeVisitante"))
        item = self.tb_view.horizontalHeaderItem(5)
        item.setText(_translate("formViewResult", "Odds1"))
        item = self.tb_view.horizontalHeaderItem(6)
        item.setText(_translate("formViewResult", "OddsX"))
        item = self.tb_view.horizontalHeaderItem(7)
        item.setText(_translate("formViewResult", "Odds2"))
        item = self.tb_view.horizontalHeaderItem(8)
        item.setText(_translate("formViewResult", "MaisGols"))
        item = self.tb_view.horizontalHeaderItem(9)
        item.setText(_translate("formViewResult", "MenosGols"))
        item = self.tb_view.horizontalHeaderItem(10)
        item.setText(_translate("formViewResult", "MarcamS"))
        item = self.tb_view.horizontalHeaderItem(11)
        item.setText(_translate("formViewResult", "MarcamN"))
        item = self.tb_view.horizontalHeaderItem(12)
        item.setText(_translate("formViewResult", "Dupla1"))
        item = self.tb_view.horizontalHeaderItem(13)
        item.setText(_translate("formViewResult", "Dupla12"))
        item = self.tb_view.horizontalHeaderItem(14)
        item.setText(_translate("formViewResult", "Dupla2"))
        self.btn_sair.setText(_translate("formViewResult", "Sair"))
        self.btn_voltar.setText(_translate("formViewResult", "Voltar"))
        self.btn_simular.setText(_translate("formViewResult", "Simular Aposta"))
        self.lbl_table.setText(_translate("formViewResult", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Jogos</span></p></body></html>"))




###Botões do sistema##
        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_voltar.clicked.connect(self.comme_back)
        self.rb_jogosBetano.clicked.connect(self.list_betano)
        self.rb_jogosPixbet.clicked.connect(self.list_pixbet)
        self.rb_matchJogos.clicked.connect(self.list_match_jogos)
        
        
    def comme_back(self):
        self.formPrincipal = QtWidgets.QMainWindow()
        self.ui = self.Ui_formPrincipal()
        self.ui.setupUi(self.formPrincipal)
        self.formPrincipal.show()
        formViewResult.close()
        
    def list_betano(self):
        self.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Jogos Betano</span></p></body></html>")   
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("SELECT ind,Hora,Data,TimeCasa,TimeVisitante,Odds1,Oddsx,Odds2 FROM tb_betano")
        resultSet = mycursor.fetchall()
        self.tb_view.setRowCount(len(resultSet))
        self.tb_view.setColumnCount(8)
        
        for i in range(0,len(resultSet)):
                for j in range(0,8):
                        self.tb_view.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultSet[i][j])))              
        con_db.close()
            
    def list_pixbet(self):
        self.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Jogos Pixbet</span></p></body></html>")   
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("SELECT ind,Hora,Data,TimeCasa,TimeVisitante,Odds1,Oddsx,Odds2 FROM tb_pixbet")
        resultSet = mycursor.fetchall()
        self.tb_view.setRowCount(len(resultSet))
        self.tb_view.setColumnCount(8)
        
        for i in range(0,len(resultSet)):
                for j in range(0,8):
                        self.tb_view.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultSet[i][j])))              
        con_db.close()
        
    def list_match_jogos(self):
        self.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Jogos Pixbet</span></p></body></html>")   
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute(""" select DISTINCT p.ind, p.Hora,p.Data ,p.timecasa as TimeCasa, p.timevisitante as TimeVisitante            
            from tb_pixbet p
                inner join tb_betano b
                on instr(p.ind ,b.ind)>0;""")
        resultSet = mycursor.fetchall()
        self.tb_view.setRowCount(len(resultSet))
        self.tb_view.setColumnCount(5)
        
        for i in range(0,len(resultSet)):
                for j in range(0,5):
                        self.tb_view.setItem(i,j,QtWidgets.QTableWidgetItem(str(resultSet[i][j])))              
        con_db.close()
                                           
    def exit_system(self):
            sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formViewResult = QtWidgets.QMainWindow()
    ui = Ui_formViewResult()
    ui.setupUi(formViewResult)
    formViewResult.show()
    sys.exit(app.exec_())
