
from asyncio.base_futures import _FINISHED
import sys
import os
import sqlite3
from PyQt5 import Qt
from PyQt5.QtCore import ( 
    pyqtSignal, 
    QObject,
    QThread
    )

from PyQt5.QtWidgets import(
    QApplication, 
    QMainWindow,
    )

from PyQt5.QtGui import *
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from ui_forms.ui_main import *
from ui_forms.Controller import *
import threading
from ui_forms.ui_calculator import *

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def showCalculator(self):
        self.calculator = Calculator()
        self.calculator.show()
          
global finish

finish = True

class Calculator(QMainWindow,QObject):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainCalculator()
        self.ui.setupUi(self)

    ############################################################################################
    #Qpush Buton
    ############################################################################################
   



        self.ui.btn_calc.clicked.connect(self.results)
        self.ui.btn_back.clicked.connect(self.closeEvent)   
        
    ############################################################################################
    #Chamando a main Window
    ############################################################################################

    def closeEvent(self, event):
        self.return_main = ModuloPrincipal()
        self.return_main.show()
        self.close()
        
    
    
    def calculate_investment(self):
        
        self.invest = float(self.ui.le_value_invest.text())
        self.odds1 = float(self.ui.le_odds1.text())
        self.odds2 = float(self.ui.le_odds2.text())
        prob = ((1/self.odds1) + (1/self.odds2))
        self.calc_odds1 = round(((1/self.odds1)/prob)*self.invest,2)
        self.calc_odds2 = round(((1/self.odds2)/prob)*self.invest,2)
        
    def calculate_return(self):
        self.return_odds1 = round(self.calc_odds1 * self.odds1,2)
        self.return_odds2 = round(self.calc_odds2 * self.odds2,2)
    
    def calculate_tot_return(self):
        self.tot_return = round((self.return_odds1 + self.return_odds2)/2,2)
    
    
    def calculate_profit(self):
        self.profit = round(self.tot_return - self.invest,2)    
        
    def results(self):
        self.calculate_investment()
        self.calculate_return()
        self.calculate_tot_return()
        self.calculate_profit()
        self.ui.le_invest1.setText(str(f'R$ {self.calc_odds1}'))
        self.ui.le_invest2.setText(str(f'R$ {self.calc_odds2}'))
        self.ui.le_return1.setText(str(f'R$ {self.return_odds1}'))
        self.ui.le_return2.setText(str(f'R$ {self.return_odds2}'))
        self.ui.le_tot_return.setText(str(f'R$ {self.tot_return}'))
        self.ui.le_profit.setText(str(f'R$ {self.profit}'))
        self.comparet()
    
    def comparet(self):
        if self.profit < 0:
            
            self.ui.le_profit.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            self.ui.le_return1.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            self.ui.le_return2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            self.ui.le_tot_return.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            
        else:
            self.ui.le_profit.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: #03A688;")
            self.ui.le_return1.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: #03A688;")
            self.ui.le_return2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: #03A688;")
            self.ui.le_tot_return.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: #03A688;")
            
         

    
class ModuloPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
    
        
             
    ############################################################################################
    #Instanciando calculadora
    ############################################################################################ 
    
        self.calculator = Calculator()    
    
    ############################################################################################
    #Setando a paginas iniciais
    ############################################################################################    
        self.ui.pages.setCurrentWidget(self.ui.page_home)
        
        self.ui.btn_visJogos.clicked.connect(self.games_betano)
        self.ui.btn_previsoes.clicked.connect(self.all_leagues)
        self.ui.rb_jogos_betano.setChecked(True)
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
        self.ui.btn_coletar.clicked.connect(self.thread_process)
        self.ui.btn_coletar.clicked.connect(self.animation)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.btn_calculator.clicked.connect(self.showCalculator)
        self.ui.btn_visProbabilidades.clicked.connect(self.list_match_odds)

    ################################################################################################   
    #Radio buttons 
    ################################################################################################
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
    #Chamando outra tela
    ################################################################################################
    def createThread(self):
        cr_thread = threading.Thread(target=self.showCalculator, name='Calculator', daemon=True)
        cr_thread.start()
        
    def showCalculator(self):
       
        self.calculator.show()
        self.hide()
           
        
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
            new_width = 185
        else:
            new_width = 0 
        self.animation_side_menu = QtCore.QPropertyAnimation(self.ui.frame_side,b"maximumWidth")
        self.animation_side_menu.setDuration(400)
        self.animation_side_menu.setStartValue(width)
        self.animation_side_menu.setEndValue(new_width)
        self.animation_side_menu.setEasingCurve(QtCore.QEasingCurve.Type(5))
        self.animation_side_menu.start()
        
    def side_btn_menu(self):
        width = self.ui.btn_menu.width()
        if width == 75 :
            
            self.ui.btn_menu.setText("      Menu        ")
            new_width = 220
        else:
            new_width = 75
            self.ui.btn_menu.setText("")
        self.animation_btn_menu = QtCore.QPropertyAnimation(self.ui.btn_menu,b"minimumWidth")
        self.animation_btn_menu.setDuration(350)
        self.animation_btn_menu.setStartValue(width)
        self.animation_btn_menu.setEndValue(new_width)
        self.animation_btn_menu.setEasingCurve(QtCore.QEasingCurve.Type(5))
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
    
        ################################################################################################   
        #Coletando os dados da Pixbet e Betano
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
        Finish = False

        ################################################################################################   
        #Coletando dados do five
        ################################################################################################
    def collect_forecasts(self):
        controller = Controller()
        controller.controller_probabilidades()
        controller.create_table_matches()
        
        ################################################################################################   
        #Thread da aplicação
        ################################################################################################    
    def thread_process(self):
        """Trabalha com thread na coleta
           Works with thread in the collection
        """
        self.thread1 = threading.Thread(target=self.collect_odds, name= 'ScrapingSites')
        self.thread1.start()
       

    def thread_forecasts(self):
        self.thread2 = threading.Thread(target=self.collect_forecasts, name= 'DownloadCSV')
        self.thread2.start()


    ################################################################################################   
    #Renomear colunas da tabela
    ################################################################################################
 
    def match_odds_name(self):
        """Renomeia as colunas de acordo com a seleção
           Renaming the columns according to the selection
        """
        try:
            item = self.ui.tb_view.horizontalHeaderItem(0)
            item.setText('Data')
            item = self.ui.tb_view.horizontalHeaderItem(1)
            item.setText('Hora')
            item = self.ui.tb_view.horizontalHeaderItem(2)
            item.setText('Mandante')
            item = self.ui.tb_view.horizontalHeaderItem(3)
            item.setText('Visitante')
            item = self.ui.tb_view.horizontalHeaderItem(4)
            item.setText('Odds1_PIXBET')
            item = self.ui.tb_view.horizontalHeaderItem(5)
            item.setText('X2_PIXBET')
            item = self.ui.tb_view.horizontalHeaderItem(6)
            item.setText('Odds2_PIXBET')
            item = self.ui.tb_view.horizontalHeaderItem(7)
            item.setText('X1_PIXBET')
            item = self.ui.tb_view.horizontalHeaderItem(8)
            item.setText('Odds1_BETANO')
            item = self.ui.tb_view.horizontalHeaderItem(9)
            item.setText('X2_BETNAO')
            item = self.ui.tb_view.horizontalHeaderItem(10)
            item.setText('Odds2_BETANO')
            item = self.ui.tb_view.horizontalHeaderItem(11)
            item.setText('X1_BETANO')
        except Exception as e:
            print(e)  
            pass  
        
        
  
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
            
    def list_match_odds(self):
        """Lista as probabilidades boas para apostas
           List good odds for betting
        """
        directory_database = 'C:\\tmp\\Bancos'
        con_db = sqlite3.connect(directory_database+'\\DADOS.db')
        mycursor = con_db.cursor()
        mycursor.execute("""
                         SELECT p.data,
                                p.hora,
                                p.TimeCasa as Mandante,
                                p.TimeVisitante  as Visitante,
                                p.Odds1  as odds1_pixbet,
                                p.Dupla2x as X2_pixbet,
                                p.Odds2  as odds2_pixbet,
                                p.Dupla1x as X1_pixbet,
                                b.Odds1 as odds1_betano,
                                b.Dupla2x as X2_betano,
                                b.Odds2 as odds2_betano,
                                b.Dupla1x as X1_betano
	
                        from tb_pixbet p		
                        inner join tb_betano b
                        on instr(p.ind, b.ind)>0;
                        """)

        resultSet = mycursor.fetchall()
        self.ui.tb_view.setRowCount(len(resultSet))
        self.ui.tb_view.setColumnCount(12)
        self.match_odds_name()  # função para renomear as colunas
        for i in range(0, len(resultSet)):
            for j in range(0, 12):
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


            
        elif (self.ui.cb_games.currentText() == 'Jogos Futuros'):
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

                
        elif (self.ui.cb_games.currentText() == 'Jogos Passados'):
            
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
                    WHERE
                        score1 NOTNULL AND
                        league = '{self.ui.cb_camp.currentText()}' AND
                        team1 LIKE "%{self.ui.le_team1.text()}%" AND 
                        team2 LIKE "%{self.ui.le_team2.text()}%"
                                """)
        else:
            pass                        

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