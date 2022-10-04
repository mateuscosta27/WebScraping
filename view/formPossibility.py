import os
import sys
import sqlite3


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formViewResult(object):
    def setupUi(self, formViewResult):
        formViewResult.setObjectName("formViewResult")
        formViewResult.resize(1275, 650)
        formViewResult.setMinimumSize(QtCore.QSize(1200, 600))
        formViewResult.setMaximumSize(QtCore.QSize(2000, 1500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/principal_icon.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.groupBox.setGeometry(QtCore.QRect(1060, 10, 170, 140))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(170)
        sizePolicy.setVerticalStretch(140)
        sizePolicy.setHeightForWidth(
            self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(170, 140))
        self.groupBox.setMaximumSize(QtCore.QSize(170, 140))
        self.groupBox.setStyleSheet("background-color: rgb(3, 127, 140);\n"
                                    "border-radius: 5px;\n"
                                    "")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.rb_matchOdds = QtWidgets.QRadioButton(self.groupBox)
        self.rb_matchOdds.setGeometry(QtCore.QRect(14, 45, 140, 20))
        self.rb_matchOdds.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_matchOdds.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_matchOdds.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);")
        self.rb_matchOdds.setObjectName("rb_matchOdds")
        self.rb_DuplaChance = QtWidgets.QRadioButton(self.groupBox)
        self.rb_DuplaChance.setGeometry(QtCore.QRect(14, 10, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.rb_DuplaChance.sizePolicy().hasHeightForWidth())
        self.rb_DuplaChance.setSizePolicy(sizePolicy)
        self.rb_DuplaChance.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_DuplaChance.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_DuplaChance.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(0, 0, 0);")
        self.rb_DuplaChance.setObjectName("rb_DuplaChance")
        self.rb_ambosMarcam = QtWidgets.QRadioButton(self.groupBox)
        self.rb_ambosMarcam.setGeometry(QtCore.QRect(14, 75, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.rb_ambosMarcam.sizePolicy().hasHeightForWidth())
        self.rb_ambosMarcam.setSizePolicy(sizePolicy)
        self.rb_ambosMarcam.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_ambosMarcam.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_ambosMarcam.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(0, 0, 0);")
        self.rb_ambosMarcam.setObjectName("rb_ambosMarcam")
        self.rb_totalGols = QtWidgets.QRadioButton(self.groupBox)
        self.rb_totalGols.setGeometry(QtCore.QRect(14, 100, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.rb_totalGols.sizePolicy().hasHeightForWidth())
        self.rb_totalGols.setSizePolicy(sizePolicy)
        self.rb_totalGols.setMinimumSize(QtCore.QSize(140, 20))
        self.rb_totalGols.setMaximumSize(QtCore.QSize(140, 20))
        self.rb_totalGols.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(0, 0, 0);")
        self.rb_totalGols.setChecked(True)
        self.rb_totalGols.setAutoRepeat(True)
        self.rb_totalGols.setObjectName("rb_totalGols")
        self.tb_view = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_view.setGeometry(QtCore.QRect(10, 180, 1251, 400))
        self.tb_view.setToolTipDuration(-3)
        self.tb_view.setObjectName("tb_view")
        self.tb_view.setColumnCount(14)
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
        formViewResult.setWindowTitle(_translate(
            "formViewResult", "Modulo Visualização"))
        self.lbl_title.setText(_translate("formViewResult", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#037f8c;\">\n"
                                          "APOSTADORPRO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#037f8c;\">GERENCIADOR DE APOSTAS ESPORTIVAS</span></p></body></html>"))
        self.rb_matchOdds.setText(_translate("formViewResult", "Match Odds"))
        self.rb_DuplaChance.setText(
            _translate("formViewResult", "Dupla Chance"))
        self.rb_ambosMarcam.setText(
            _translate("formViewResult", "Ambos Marcam"))
        self.rb_totalGols.setText(_translate(
            "formViewResult", "Total de Gols"))
        item = self.tb_view.horizontalHeaderItem(0)
        item.setText(_translate("formViewResult", "Hora"))
        item = self.tb_view.horizontalHeaderItem(1)
        item.setText(_translate("formViewResult", "Data"))
        item = self.tb_view.horizontalHeaderItem(2)
        item.setText(_translate("formViewResult", "TimeCasa"))
        item = self.tb_view.horizontalHeaderItem(3)
        item.setText(_translate("formViewResult", "TimeVisitante"))
        item = self.tb_view.horizontalHeaderItem(4)
        item.setText(_translate("formViewResult", "Odds1"))
        item = self.tb_view.horizontalHeaderItem(5)
        item.setText(_translate("formViewResult", "OddsX"))
        item = self.tb_view.horizontalHeaderItem(6)
        item.setText(_translate("formViewResult", "Odds2"))
        item = self.tb_view.horizontalHeaderItem(7)
        item.setText(_translate("formViewResult", "MaisGols"))
        item = self.tb_view.horizontalHeaderItem(8)
        item.setText(_translate("formViewResult", "MenosGols"))
        item = self.tb_view.horizontalHeaderItem(9)
        item.setText(_translate("formViewResult", "MarcamS"))
        item = self.tb_view.horizontalHeaderItem(10)
        item.setText(_translate("formViewResult", "MarcamN"))
        item = self.tb_view.horizontalHeaderItem(11)
        item.setText(_translate("formViewResult", "Dupla1"))
        item = self.tb_view.horizontalHeaderItem(12)
        item.setText(_translate("formViewResult", "Dupla12"))
        item = self.tb_view.horizontalHeaderItem(13)
        item.setText(_translate("formViewResult", "Dupla2"))
        self.btn_sair.setText(_translate("formViewResult", "Sair"))
        self.btn_voltar.setText(_translate("formViewResult", "Voltar"))
        self.btn_simular.setText(_translate(
            "formViewResult", "Simular Aposta"))
        self.lbl_table.setText(_translate(
            "formViewResult", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Jogos</span></p></body></html>"))


        ###Botões do sistema##
        self.btn_sair.clicked.connect(self.exit_system)
        self.btn_voltar.clicked.connect(self.return_main_screen)
        ###Radio Buttons###
        self.rb_matchOdds.clicked.connect(self.list_match_odds)
        self.rb_totalGols.clicked.connect(self.lis_total_goals)

 ###Funções do Sistema###

    def match_odds_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.tb_view.horizontalHeaderItem(4)
        item.setText('Odds1_Pixbet')
        item = self.tb_view.horizontalHeaderItem(5)
        item.setText('Odds2_Betano')
        item = self.tb_view.horizontalHeaderItem(6)
        item.setText('Possibilidade1')
        item = self.tb_view.horizontalHeaderItem(7)
        item.setText('Odds1_Betano')
        item = self.tb_view.horizontalHeaderItem(8)
        item.setText('Odds2_Pixbet')
        item = self.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')
        
    def total_goals_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.tb_view.horizontalHeaderItem(4)
        item.setText('MaisGols_Pixbet')
        item = self.tb_view.horizontalHeaderItem(5)
        item.setText('MenosGols_Betano')
        item = self.tb_view.horizontalHeaderItem(6)
        item.setText('Possibilidade1')
        item = self.tb_view.horizontalHeaderItem(7)
        item.setText('MaisGolsBetano_Betano')
        item = self.tb_view.horizontalHeaderItem(8)
        item.setText('MenosGols_Pixbet')
        item = self.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')    
    
    def list_match_odds(self):
        """Lista as probabilidades boas para apostas
           List good odds for betting
        """
        self.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Odds Boas para aposta</span></p></body></html>")
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""select p.Data, p.Hora ,p.timecasa as TimeCasa_pixbet, p.timevisitante as TimeVisitante_pixbet ,p.Odds1  as Odds1_pixbet, b.Odds2  as Odds2_betano,
                                CASE 
                                        when ((1/p.Odds1) + (1/b.Odds2)) < 1 then 'PixbetXBetano'
                                        when p.Odds1 = 'None' then 'Sem dados'
	                                when b.Odds2 = 'None' then 'Sem dados'
                                        ELSE "Sem Possibilidades"
                                        END as Possibilidade1,
                                        b.Odds1 as Odds1_betano, p.Odds2 as Odds2_pixbet,	
                                Case
                                        when ((1/b.Odds1) + (1/p.Odds2)) < 1 then 'BetanoXPixbet'
                                        when b.Odds1 = 'None' then 'Sem dados'
	                                when p.Odds2 = 'None' then 'Sem dados'
                                        ELSE "Sem Possibilidades"
                                        END as 'Possibilidade2'
                                        
                                        
                                        from tb_pixbet p
                                                inner join tb_betano b
                                                on instr(p.ind ,b.ind)>0;""")

        resultSet = mycursor.fetchall()
        self.tb_view.setRowCount(len(resultSet))
        self.tb_view.setColumnCount(10)
        self.match_odds_name()  # função para renomear as colunas
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.tb_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()

    def lis_total_goals(self):
        self.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">+-2,5 Gols</span></p></body></html>")
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""select p.Data, p.Hora ,p.timecasa as TimeCasa_pixbet, p.timevisitante as TimeVisitante_pixbet ,p.MaisGols  as MaisGols_pixbet, b.MenosGols  as MenosGols_betano,
                                CASE 
                                        when ((1/p.MaisGols) + (1/b.MenosGols)) < 1 then 'PixbetXBetano'
                                        when p.MaisGols = 'None' then 'Sem dados'
	                                when b.MenosGols = 'None' then 'Sem dados'
                                        ELSE "Sem Possibilidades"
                                        END as Aportunidade1,
                                        b.Odds1 as Odds1_betano, p.Odds2 as Odds2_pixbet,	
                                Case
                                        when ((1/b.MaisGols) + (1/p.MenosGols)) < 1 then 'BetanoXPixbet'
                                        when b.MaisGols = 'None' then 'Sem dados'
	                                when p.MenosGols = 'None' then 'Sem dados'
                                        ELSE "Sem Possibilidades"
                                        END as Aportunidade2
                                        
                                        
                                        from tb_pixbet p
                                                inner join tb_betano b
                                                on instr(p.ind ,b.ind)>0;""")

        resultSet = mycursor.fetchall()
        self.tb_view.setRowCount(len(resultSet))
        self.tb_view.setColumnCount(10)
        self.total_goals_name()  # função para renomear as colunas 
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.tb_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()    

    def return_main_screen(self):
        formViewResult.close()
        
                            
    def exit_system(self):
        """Sai do sistema
           Exit of System
        """
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formViewResult = QtWidgets.QMainWindow()
    ui = Ui_formViewResult()
    ui.setupUi(formViewResult)
    formViewResult.show()
    sys.exit(app.exec_())
