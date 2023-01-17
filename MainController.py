
import sys
import os
from urllib import response
from Views.Main import *
from Views.CalculatorView import *
import sqlite3
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve




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
        self.ui.btn_calc.clicked.connect(self.logical_test)
        
   
    ############################################################################################
    #Chamando a main Window
    ############################################################################################
    
    def logical_test(self):
        self.my_while = True
        
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
        try:
            self.my_while = True
            while self.my_while == True:
                
                if(self.ui.le_value_invest.text() != '') and (self.ui.le_value_invest.text() != str):
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
                else:
                    self.ui.le_value_invest.setPlaceholderText("Valor Inválido")  
                self.my_while = False
            else:
                pass
        except:
           
            self.ui.le_value_invest.setPlaceholderText("Valor Inválido")
            pass        
    
    def comparet(self):
        if self.profit < 0:
            
            self.ui.le_value_invest.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")                                            
            self.ui.le_profit.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            self.ui.le_return1.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            self.ui.le_return2.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")
            self.ui.le_tot_return.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color:  rgb(217, 7, 45);")   
        else:
            self.ui.le_value_invest.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: #03A688;")
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
        
        self.ui.rb_games_betano.setChecked(True)
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
        self.ui.btn_calculator.clicked.connect(self.showCalculator)
        self.ui.btn_side_options_pssib.clicked.connect(self.side_frame_options)
        self.ui.btn_side_options_season.clicked.connect(self.side_frame_search)


    ################################################################################################   
    #Radio buttons 
    ################################################################################################
        #self.ui.rb_games_betano.clicked.connect(self.games_betano)
        #self.ui.rb_games_pixbet.clicked.connect(self.games_pixbet)

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
        
    def showCalculator(self):
       
        self.calculator.show()
        self.hide()
           
        
    ################################################################################################   
    #Animações
    ################################################################################################
    def create_animation_icon(self):
        ##Animação de coleta de dados
        self.ui.lb_collect_animation.setVisible(True)
        self.loading_animation_icon = QPropertyAnimation.QMovie("src/collect_icon.gif")
        self.ui.lb_collect_animation.setMovie(self.loading_animation_icon)
        
    def create_animation_text(self):
        ##Animação de coleta de dados
        self.ui.lb_text_animation.setVisible(True)
        self.loading_animation_text =QPropertyAnimation.QMovie("src/text_icon.gif")
        self.ui.lb_text_animation.setMovie(self.loading_animation_text)
               
    def star_animations(self):
        ##Aniciando a animação de coleta de dados
        self.loading_animation_icon.start()
        self.loading_animation_text.start()
        
    def stop_animations(self):
        ##Parando a animação de coleta de dados
        self.loading_animation_icon.stop()
        self.loading_animation_text.stop()
         
    def animation(self):
        ##Função para executar a animação
        self.create_animation_icon()
        self.create_animation_text()
        self.star_animations()
                     
    def side_menu(self):
        ##Animação do menu lateral
        width = self.ui.frame_side.width() 
        if width == 0:
            new_width = 185
        else:
            new_width = 0 
        self.animation_side_menu = QPropertyAnimation(self.ui.frame_side,b"maximumWidth")
        self.animation_side_menu.setDuration(400)
        self.animation_side_menu.setStartValue(width)
        self.animation_side_menu.setEndValue(new_width)
        self.animation_side_menu.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation_side_menu.start()
        
    def side_btn_menu(self):
        ##Animação do botão do menu lateral
        width = self.ui.btn_menu.width()
        if width == 75 :
            
            self.ui.btn_menu.setText("Menu")
            new_width = 220
        else:
            new_width = 75
            self.ui.btn_menu.setText("")
        self.animation_btn_menu = QPropertyAnimation(self.ui.btn_menu,b"minimumWidth")
        self.animation_btn_menu.setDuration(350)
        self.animation_btn_menu.setStartValue(width)
        self.animation_btn_menu.setEndValue(new_width)
        self.animation_btn_menu.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation_btn_menu.start()
        
        
    def side_frame_options(self):
        ##Animação do menu de opções
        height = self.ui.frame_side_options.height()
        if height == 0 :
            new_height = 80
        else:
            new_height = 0
        self.animation_frame_option = QPropertyAnimation(self.ui.frame_side_options,b"maximumHeight")
        self.animation_frame_option.setDuration(350)
        self.animation_frame_option.setStartValue(height)
        self.animation_frame_option.setEndValue(new_height)
        self.animation_frame_option.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation_frame_option.start()
        
        
    def side_frame_search(self):
        ##Animação do menu de opções
        height = self.ui.frame_side_season.height()
        if height == 0 :
            new_height = 80
        else:
            new_height = 0
        self.animation_frame_search = QPropertyAnimation(self.ui.frame_side_season,b"maximumHeight")
        self.animation_frame_search.setDuration(200)
        self.animation_frame_search.setStartValue(height)
        self.animation_frame_search.setEndValue(new_height)
        self.animation_frame_search.setEasingCurve(QEasingCurve.Type.Linear)
        self.animation_frame_search.start()         
        
    
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
    """ def collect_odds(self):
        controller = Controller()
        controller.controller_betano()
        controller.controller_pixbet()
        controller.create_tables()
        self.stop_animations()
        self.ui.lb_collect_animation.setVisible(False)
        self.ui.lb_text_animation.setVisible(False)"""
        

        ################################################################################################   
        #Coletando dados do five
        ################################################################################################
    """def collect_forecasts(self):
        controller = Controller()
        controller.controller_probabilidades()
        controller.create_table_matches()
        self.side_frame_search()"""
    
       
        
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
 
                                                      
                                                                         
        
        
        
        
        
        
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ModuloPrincipal()
    w.show()
    sys.exit(app.exec())