
import sys
import os
import sqlite3
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import Qt
from PyQt5.QtGui import *
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ui_main import *



    
class ModuloPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
    
    ############################################################################################
    #Setando a paginas iniciais
    ############################################################################################    
        self.ui.pages.setCurrentWidget(self.ui.page_home)
        self.ui.btn_visProbabilidades.clicked.connect(self.double_odds)
        self.ui.rb_DuplaChance.setChecked(True)
        
    ############################################################################################
    #Toggle Buton
    ############################################################################################ 
        self.ui.btn_menu.clicked.connect(self.side_menu)
        self.ui.btn_menu.clicked.connect(self.side_btn_menu)
    ############################################################################################
    #Qpush Buton
    ############################################################################################ 
        self.ui.btn_coletar.clicked.connect(self.create_animation_icon)
        self.ui.btn_coletar.clicked.connect(self.create_animation_text)
    ################################################################################################   
    #Radio buttons 
    ################################################################################################
        self.ui.rb_DuplaChance.clicked.connect(self.double_odds)
        self.ui.rb_matchOdds.clicked.connect(self.list_match_odds)
        self.ui.rb_totalGols.clicked.connect(self.lis_total_goals)
        
    ################################################################################################   
    #Animações
    ################################################################################################
    def create_animation_icon(self):
        self.loading_animation_icon = QMovie("src/collect_icon.gif")
        self.ui.lb_collect_animation.setMovie(self.loading_animation_icon)
        self.loading_animation_icon.start()
    
    def create_animation_text(self):
        self.loading_animation_text = QMovie("src/text_icon.gif")
        self.ui.lb_text_animation.setMovie(self.loading_animation_text)
        self.loading_animation_text.start()        
        

        
    def side_menu(self):
        width = self.ui.frame_side.width() 
        if width == 0:
            new_width = 230
        else:
            new_width = 0 
        self.animation_side_menu = QtCore.QPropertyAnimation(self.ui.frame_side,b"maximumWidth")
        self.animation_side_menu.setDuration(250)
        self.animation_side_menu.setStartValue(width)
        self.animation_side_menu.setEndValue(new_width)
   
        self.animation_side_menu.setEasingCurve(QtCore.QEasingCurve.Type(5))
        self.animation_side_menu.start()
        
    def side_btn_menu(self):
        width = self.ui.frame_btn_menu.width()
        if width == 100:
            new_width = 230
        else:
            new_width = 100
        self.animation_btn_menu = QtCore.QPropertyAnimation(self.ui.frame_btn_menu,b"maximumWidth")
        self.animation_btn_menu.setDuration(350)
        self.animation_btn_menu.setStartValue(width)
        self.animation_btn_menu.setEndValue(new_width)
        self.animation_btn_menu.setEasingCurve(QtCore.QEasingCurve.Type(2))
        self.animation_btn_menu.start()

    ################################################################################################   
    #Paginas do sistema  
    ################################################################################################
        self.ui.btn_visProbabilidades.clicked.connect(self.showPossibilites)
        self.ui.btn_coletar.clicked.connect(self.showHome)
        
    def showPossibilites(self):
        self.ui.pages.setCurrentWidget(self.ui.page_possibilities)
        
    def showHome(self):
        self.ui.pages.setCurrentWidget(self.ui.page_home)
    ################################################################################################   
    #realizar o webscraping nos sites
    ################################################################################################
            
    
    ################################################################################################   
    #Renomear colunas da tabela
    ################################################################################################
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
    def match_odds_name(self):
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
        item.setText('Odds1_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(5)
        item.setText('Odds2_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(6)
        item.setText('Possibilidade1')
        item = self.ui.tb_view.horizontalHeaderItem(7)
        item.setText('Odds1_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(8)
        item.setText('Odds2_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')
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
                   
    ################################################################################################   
    #Exibir tabelas do sistema
    ################################################################################################
    def double_odds(self):
        """Lista as probabilidades boas para apostas
           List good odds for betting
        """
        
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

    def list_match_odds(self):
        """Lista as probabilidades boas para apostas
           List good odds for betting
        """
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

    def lis_total_goals(self):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ModuloPrincipal()
    w.show()
    sys.exit(app.exec_())