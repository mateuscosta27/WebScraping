import sys
import os
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from formMain import *
from formPossibility import *

class ViewResult(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formViewResult()
        self.ui.setupUi(self)
        ###PushButtons##
        self.ui.btn_sair.clicked.connect(self.return_main)
        ###RadioButtons###
        self.ui.rb_DuplaChance.clicked.connect(self.list_double_odds)
        self.ui.rb_matchOdds.clicked.connect(self.list_match_odds)
        self.ui.rb_totalGols.clicked.connect(self.lis_total_goals)
        
    ##Functions of system###
        
    def double_odds_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.ui.tb_view.horizontalHeaderItem(0)
        item.setText('Data')
        item = self.ui.tb_view.horizontalHeaderItem(1)
        item.setText('Hora')
        item = self.ui.tb_view.horizontalHeaderItem(2)
        item.setText('Mandante')
        item = self.ui.tb_view.horizontalHeaderItem(3)
        item.setText('Visitante')
        item = self.ui.tb_view.horizontalHeaderItem(4)
        item.setText('Dupla1x_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(5)
        item.setText('Dupla2x_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(6)
        item.setText('Possibilidade1')
        item = self.ui.tb_view.horizontalHeaderItem(7)
        item.setText('Dupla1x_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(8)
        item.setText('Dupla2x_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')
            
    def list_double_odds(self):
        """Lista as probabilidades boas para apostas
           List good odds for betting
        """
        self.ui.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Odds com Dupla Chance</span></p></body></html>")
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""select p.Data, p.Hora ,p.timecasa as TimeCasa_pixbet, p.timevisitante as TimeVisitante_pixbet ,p.Dupla1x  as Dupla1x_pixbet, b.Dupla2X  as Dupla2X_betano,
                                CASE 
                                    when ((1/p.Dupla1x) + (1/b.Dupla2x)) < 1 then 'PixbetXBetano'
                                    when b.Odds1 = 'None' then 'Sem dados'
                                    when p.Odds2 = 'None' then 'Sem dados'
                                    ELSE "Sem Oportunidades"
                                    END as Aportunidade1,
                                    b.Odds1 as Odds1_betano, p.Odds2 as Odds2_pixbet,	
                                Case
                                    when ((1/b.Dupla1x) + (1/p.Dupla2x)) < 1 then 'BetanoXPixbet'
                                    when p.Odds1 = 'None' then 'Sem dados'
                                    when b.Odds2 = 'None' then 'Sem dados'
                                    ELSE "Sem Oportunidades"
                                    END as Aportunidade2
                                    
                                    
                                            from tb_pixbet p
                                                inner join tb_betano b
                                                on instr(p.ind ,b.ind)>0;""")

        resultSet = mycursor.fetchall()
        self.ui.tb_view.setRowCount(len(resultSet))
        self.ui.tb_view.setColumnCount(10)
        self.double_odds_name()  # função para renomear as colunas
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.ui.tb_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()
                   
    def match_odds_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.ui.tb_view.horizontalHeaderItem(0)
        item.setText('Data')
        item =self.ui.tb_view.horizontalHeaderItem(1)
        item.setText('Hora')
        item =self.ui.tb_view.horizontalHeaderItem(2)
        item.setText('Mandante')
        item =self.ui.tb_view.horizontalHeaderItem(3)
        item.setText('Visitante')
        item =self.ui.tb_view.horizontalHeaderItem(4)
        item.setText('Odds1_Pixbet')
        item =self.ui.tb_view.horizontalHeaderItem(5)
        item.setText('Odds2_Betano')
        item =self.ui.tb_view.horizontalHeaderItem(6)
        item.setText('Possibilidade1')
        item =self.ui.tb_view.horizontalHeaderItem(7)
        item.setText('Odds1_Betano')
        item =self.ui.tb_view.horizontalHeaderItem(8)
        item.setText('Odds2_Pixbet')
        item =self.ui.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')   

    def list_match_odds(self):
        """Lista as probabilidades boas para apostas
           List good odds for betting
        """
        self.ui.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Odds Boas para aposta</span></p></body></html>")
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
        self.ui.tb_view.setRowCount(len(resultSet))
        self.ui.tb_view.setColumnCount(10)
        self.match_odds_name()  # função para renomear as colunas
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.ui.tb_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()
                
    def total_goals_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.ui.tb_view.horizontalHeaderItem(0)
        item.setText('Data')
        item = self.ui.tb_view.horizontalHeaderItem(1)
        item.setText('Hora')
        item = self.ui.tb_view.horizontalHeaderItem(2)
        item.setText('Mandante')
        item = self.ui.tb_view.horizontalHeaderItem(3)
        item.setText('Visitante')
        item = self.ui.tb_view.horizontalHeaderItem(4)
        item.setText('MaisGols_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(5)
        item.setText('MenosGols_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(6)
        item.setText('Possibilidade1')
        item = self.ui.tb_view.horizontalHeaderItem(7)
        item.setText('MaisGolsBetano_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(8)
        item.setText('MenosGols_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')    
              
    def lis_total_goals(self):
        self.ui.lbl_table.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">+-2,5 Gols</span></p></body></html>")
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
        self.ui.tb_view.setRowCount(len(resultSet))
        self.ui.tb_view.setColumnCount(10)
        self.total_goals_name()  # função para renomear as colunas 
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.ui.tb_view.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()    
    
    def closeEvent(self, event):
        """
        Esta função chama o modulo principal
        This function call main module
        """
        self.main = ModuloPrincipal()
        self.main.show()
        event.accept()
    
    def return_main(self):
        
        """Close viewResult
        """
        self.close()








    
class ModuloPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_formPrincipal()
        self.ui.setupUi(self)
        self.formMain = self.ui

        self.viewResult = ViewResult()
        ###Buttons###
        self.ui.btn_sair.clicked.connect(self.exit_system)
        self.ui.btn_visPossibilidades.clicked.connect(self.open_possibilities)
        
    ###Functions###
    def open_possibilities(self):
        """Abre o forma de visualização de possibilidades
           Open the possibilities viewer 
        """
        self.viewResult.show()    
        self.hide()
        self.viewResult.lis_total_goals()
              
    def exit_system(self):
        """Sai do sistema
           Exit system
        """
        sys.exit()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ModuloPrincipal()
    w.show()
    sys.exit(app.exec_())