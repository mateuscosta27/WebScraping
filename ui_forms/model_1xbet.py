
import os, sys
import pandas as pd
from time import sleep
from selenium import webdriver
sys.path.insert(0,os.path.abspath(os.curdir))
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup



class OneBet:
    def __init__(self):
        ###Carregando driver, recebendo o web site, definindo diretorio###
        self.directory_file = 'C:\\tmp\\Arquivos'   ##Diretorio onde serão salvos os arquivos CSV com informações obtidas###     
        self.directory_driver = 'C:\\tmp\\Driver'   ##Diretorio onde esta localizado o driver do google chrome para operação com selenium###    
        self.path = self.directory_driver +'\\chromedriver.exe'
        self.web_site = 'https://br.1xbet.com/betsonyour/line/football/1268397-brazil-campeonato-brasileiro-serie-a' ##Site onde estamos buscando as informações###
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--window-size=1920,1080')
        #self.options.add_argument('--start-maximized')
        #self.options.add_argument('--headless')
        #self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options,executable_path=self.path)
        self.dic_jogos = {'TimeCasa':[], 'TimeVisitante':[], 'Odds1':[],'OddsX':[],'Odds2':[]}

          
        
    def open_web_site(self):
        ###Abrindo website##
        try:
            self.driver.get(self.web_site)
            print('executou')
            self.driver.maximize_window()
            sleep(5)
            print('executou')
            #self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            #print('executou')
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass    
    
    def parser_data(self):
        ###Analisando o html e capturando as informações desejadas###
        try:
            self.dic_jogos = {'Jogos':[]} ##Dicionario que armazenara as informações do parseamento do html##
            self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
          
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass
            
    def capture_teams(self):
        all = self.soup.find_all('span',{'class':'c-events__item c-events__item_game'})
        bets = self.soup.find_all('div',{'class':'c-bets'})
         
        for teste in all:
           t1 = teste.get_text().strip()
           print(t1)
        for bet in bets:
            tbet = bet.get_text().strip()
            print(tbet)    
        
         

  
onebet = OneBet()
onebet.open_web_site()
onebet.parser_data()
onebet.capture_teams()

