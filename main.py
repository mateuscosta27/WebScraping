
import sys
import os
import sqlite3
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import Qt
from PyQt5.QtGui import *
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ui_forms.ui_main import *
from ui_forms.Controller import *
import threading





    
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
        self.ui.btn_visJogos.clicked.connect(self.games_betano)
        self.ui.btn_previsoes.clicked.connect(self.all_leagues)
        self.ui.rb_jogos_betano.setChecked(True)
        self.ui.rb_DuplaChance.setChecked(True)
        self.ui.lb_collect_animation.setVisible(False)
        self.ui.lb_text_animation.setVisible(False)
        
    ############################################################################################
    #Toggle Buton
    ############################################################################################ 
        self.ui.btn_menu.clicked.connect(self.side_menu)
        self.ui.btn_menu.clicked.connect(self.side_btn_menu)
    ############################################################################################
    #Qpush Buton
    ############################################################################################ 
        self.ui.btn_coletar.clicked.connect(self.thred_process)
        self.ui.btn_coletar.clicked.connect(self.animation)
        self.ui.btn_forecast.clicked.connect(self.thread_forecasts)
        self.ui.btn_forecast.clicked.connect(self.animation)
        self.ui.btn_search.clicked.connect(self.search)

    ################################################################################################   
    #Radio buttons 
    ################################################################################################
        self.ui.rb_DuplaChance.clicked.connect(self.double_odds)
        self.ui.rb_matchOdds.clicked.connect(self.list_match_odds)
        self.ui.rb_totalGols.clicked.connect(self.lis_total_goals)
        self.ui.rb_jogos_betano.clicked.connect(self.games_betano)
        self.ui.rb_jogos_pixbet.clicked.connect(self.games_pixbet)

    ################################################################################################   
    #Paginas do sistema  Botões
    ################################################################################################
        self.ui.btn_visProbabilidades.clicked.connect(self.showPossibilites)
        self.ui.btn_coletar.clicked.connect(self.showHome)
        self.ui.btn_visJogos.clicked.connect(self.showGames)
        self.ui.btn_previsoes.clicked.connect(self.showPreviews)
        
    ################################################################################################   
    #Animações
    ################################################################################################
    def create_animation_icon(self):
        self.ui.lb_collect_animation.setVisible(True)
        self.loading_animation_icon = QMovie("src/collect_icon.gif")
        self.ui.lb_collect_animation.setMovie(self.loading_animation_icon)
        
    def create_animation_text(self):
        self.ui.lb_text_animation.setVisible(True)
        self.loading_animation_text = QMovie("src/text_icon.gif")
        self.ui.lb_text_animation.setMovie(self.loading_animation_text)
               
    def star_animations(self):
        self.loading_animation_icon.start()
        self.loading_animation_text.start()
        
    def stop_animations(self):
        self.loading_animation_icon.stop()
        self.loading_animation_text.stop()
         
    def animation(self):
        self.create_animation_icon()
        self.create_animation_text()
        self.star_animations()
                     
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
    def showPossibilites(self):
        self.ui.pages.setCurrentWidget(self.ui.page_possibilities)
        
    def showHome(self):
        self.ui.pages.setCurrentWidget(self.ui.page_home)
    
    def showGames(self):
        self.ui.pages.setCurrentWidget(self.ui.page_view_games)
    
    def showPreviews(self):
        self.ui.pages.setCurrentWidget(self.ui.page_preview)        
    ################################################################################################   
    #realizar o webscraping nos sites
    ################################################################################################
    def collect_odds(self):
        controller = Controller()
        controller.controller_probabilidades()
        controller.controller_pixbet()
        controller.controller_betano()
        controller.create_tables()
        self.stop_animations()
        self.ui.lb_collect_animation.setVisible(False)
        self.ui.lb_text_animation.setVisible(False)


    def collect_forecasts(self):
        controller = Controller()
        controller.controller_probabilidades()
        controller.create_table_matches()
        self.ui.lb_collect_animation.setVisible(False)
        self.ui.lb_text_animation.setVisible(False)

    def thred_process(self):
        """Trabalha com thread na coleta
           Works with thread in the collection
        """
        self.thread1 = threading.Thread(target=self.collect_odds)
        self.thread1.start()

    def thread_forecasts(self):
        self.thread2 = threading.Thread(target=self.collect_forecasts)
        self.thread2.start()


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
        item.setText('MaisGols_Betano')
        item = self.ui.tb_view.horizontalHeaderItem(8)
        item.setText('MenosGols_Pixbet')
        item = self.ui.tb_view.horizontalHeaderItem(9)
        item.setText('Possibilidade2')     
    def games_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.ui.tb_view_games.horizontalHeaderItem(0)
        item.setText('Data')
        item = self.ui.tb_view_games.horizontalHeaderItem(1)
        item.setText('Hora')
        item = self.ui.tb_view_games.horizontalHeaderItem(2)
        item.setText('Mandante')
        item = self.ui.tb_view_games.horizontalHeaderItem(3)
        item.setText('Visitante')
        item = self.ui.tb_view_games.horizontalHeaderItem(4)
        item.setText('Odds1')
        item = self.ui.tb_view_games.horizontalHeaderItem(5)
        item.setText('OddsX')
        item = self.ui.tb_view_games.horizontalHeaderItem(6)
        item.setText('Odds2')
        item = self.ui.tb_view_games.horizontalHeaderItem(7)
        item.setText('+2,5Gols')
        item = self.ui.tb_view_games.horizontalHeaderItem(8)
        item.setText('-2,5Gols')
        item = self.ui.tb_view_games.horizontalHeaderItem(9)
        item.setText('AmbosMarcamS')
        item = self.ui.tb_view_games.horizontalHeaderItem(10)
        item.setText('AmbosMarcamN')
        item = self.ui.tb_view_games.horizontalHeaderItem(11)
        item.setText('Dupla1x')
        item = self.ui.tb_view_games.horizontalHeaderItem(12)
        item.setText('Dupla2x')
        item = self.ui.tb_view_games.horizontalHeaderItem(13)
        item.setText('Dupla12')


    def search_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        item = self.ui.tb_preview.horizontalHeaderItem(0)
        item.setText('Data')
        item = self.ui.tb_preview.horizontalHeaderItem(1)
        item.setText('Mandante')
        item = self.ui.tb_preview.horizontalHeaderItem(2)
        item.setText('Visitante')
        item = self.ui.tb_preview.horizontalHeaderItem(3)
        item.setText('spi1')
        item = self.ui.tb_preview.horizontalHeaderItem(4)
        item.setText('sp2')
        item = self.ui.tb_preview.horizontalHeaderItem(5)
        item.setText('VitoriaMandante')
        item = self.ui.tb_preview.horizontalHeaderItem(6)
        item.setText('Empate')
        item = self.ui.tb_preview.horizontalHeaderItem(7)
        item.setText('VitoriaVisitante')
        item = self.ui.tb_preview.horizontalHeaderItem(8)
        item.setText('GolsMandante')
        item = self.ui.tb_preview.horizontalHeaderItem(9)
        item.setText('GolsVisitante')
        
    def all_leagues_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        names = ['Data','Campeonato','Mandante','Visitante','SPI1','SPI2','VitoriaMandante','Empate',
        'VitoriaVisitante','GolsMandante', 'Golsvisitante']

        try:
            item = self.ui.tb_preview.horizontalHeaderItem(0)
            item.setText('Data')
            item = self.ui.tb_preview.horizontalHeaderItem(1)
            item.setText('Mandante')
            item = self.ui.tb_preview.horizontalHeaderItem(2)
            item.setText('Visitante')
            item = self.ui.tb_preview.horizontalHeaderItem(3)
            item.setText('spi1')
            item = self.ui.tb_preview.horizontalHeaderItem(4)
            item.setText('spi2')
            item = self.ui.tb_preview.horizontalHeaderItem(5)
            item.setText('VitoriaMandante')
            item = self.ui.tb_preview.horizontalHeaderItem(6)
            item.setText('Empate')
            item = self.ui.tb_preview.horizontalHeaderItem(7)
            item.setText('VitoriaVisitante')
            item = self.ui.tb_preview.horizontalHeaderItem(8)
            item.setText('GolsMandante')
            item = self.ui.tb_preview.horizontalHeaderItem(9)
            item.setText('GolsVisitante')
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass   




                   
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
        self.match_odds_name()  # função para renomear as colunas
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
    def games_betano(self):
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""select 
                                Data, 
                                Hora, 
                                TimeCasa, 
                                TimeVisitante, 
                                Odds1 ,
                                OddsX , 
                                Odds2 ,
                                MaisGols,
                                MenosGols,
                                AmbosMarcamSim,
                                AmbosMarcamNao,
                                Dupla1x,
                                Dupla2x,
                                Dupla12  
                            from tb_betano;
                            """)

        resultSet = mycursor.fetchall()
        self.ui.tb_view_games.setRowCount(len(resultSet))
        self.ui.tb_view_games.setColumnCount(14)
        self.games_name()  # função para renomear as colunas 
        for i in range(0, len(resultSet)):
            for j in range(0, 14):
                self.ui.tb_view_games.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()        
    def games_pixbet(self):
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""select 
                                Data, 
                                Hora, 
                                TimeCasa, 
                                TimeVisitante, 
                                Odds1 ,
                                OddsX , 
                                Odds2 ,
                                MaisGols,
                                MenosGols,
                                AmbosMarcamSim,
                                AmbosMarcamNao,
                                Dupla1x,
                                Dupla2x,
                                Dupla12  
                            from tb_pixbet;
                            """)

        resultSet = mycursor.fetchall()
        self.ui.tb_view_games.setRowCount(len(resultSet))
        self.ui.tb_view_games.setColumnCount(14)
        self.games_name()  # função para renomear as colunas 
        for i in range(0, len(resultSet)):
            for j in range(0, 14):
                self.ui.tb_view_games.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()



    def search(self):
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        
        if (self.ui.le_team1.text() == "") and (self.ui.le_team2.text() == "") and (self.ui.cb_games.currentText() == 'Todos'):
            mycursor.execute(f"""
                        select 
                                date,
                                team1,
                                team2,
                                spi1,
                                spi2,
                                prob1,
                                probtie,
                                prob2,
                                proj_score1,
                                proj_score2
                from tb_matches_latest 
                where league = "{self.ui.cb_camp.currentText()}"
        
                            """)
            print(self.ui.cb_games.currentText())
            print(self.ui.cb_camp.currentText())


            
        if (self.ui.cb_games.currentText() == 'Jogos Futuros'):
            mycursor.execute(f"""
                        select 
                                date,
                                team1,
                                team2,
                                spi1,
                                spi2,
                                prob1,
                                probtie,
                                prob2,
                                proj_score1,
                                proj_score2
                from tb_matches_latest 
                where
                score1 ISNULL AND
                score2 ISNULL AND
                league = '{self.ui.cb_camp.currentText()}' AND 
                team1 LIKE "%{self.ui.le_team1.text()}%" AND 
                team2 LIKE "%{self.ui.le_team2.text()}%"
                
                            """)

                
        else:
            
            mycursor.execute(f"""
                            select 
                                    date,
                                    team1,
                                    team2,
                                    spi1,
                                    spi2,
                                    prob1,
                                    probtie,
                                    prob2,
                                    proj_score1,
                                    proj_score2
                    from tb_matches_latest 

                                """)

        resultSet = mycursor.fetchall()
        self.ui.tb_preview.setRowCount(len(resultSet))
        self.ui.tb_preview.setColumnCount(10)
        self.search_name()  # função para renomear as colunas 
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.ui.tb_preview.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()         
    
    def all_leagues(self):

        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""
                        select 
                                date,
                                team1,
                                team2,
                                spi1,
                                spi2,
                                prob1,
                                probtie,
                                prob2,
                                proj_score1,
                                proj_score2
                from tb_matches_latest 
                where
                score1 isnull and
                score2 isnull
                            """)

        resultSet = mycursor.fetchall()
        self.ui.tb_preview.setRowCount(len(resultSet))
        self.ui.tb_preview.setColumnCount(10)
        self.all_leagues_name()  # função para renomear as colunas 
        for i in range(0, len(resultSet)):
            for j in range(0, 10):
                self.ui.tb_preview.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultSet[i][j])))
        con_db.close()         

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ModuloPrincipal()
    w.show()
    sys.exit(app.exec_())