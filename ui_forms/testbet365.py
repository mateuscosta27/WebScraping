
from select import select
import shutil
import os, sys
from wsgiref import headers
import pandas as pd
from time import sleep
from urllib import request
import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
sys.path.insert(0,os.path.abspath(os.curdir))
from selenium.webdriver.chrome.options import Options



class Esporte365:
    def __init__(self):
        ###Carregando driver, recebendo o web site, definindo diretorio###
        self.directory_file = 'C:\\tmp\\Arquivos'   ##Diretorio onde serão salvos os arquivos CSV com informações obtidas###     
        self.directory_driver = 'C:\\tmp\\Driver'   ##Diretorio onde esta localizado o driver do google chrome para operação com selenium###    
        self.path = self.directory_driver +'\\chromedriver.exe'
        self.web_site = 'https://www.esporte365.com/' ##Site onde estamos buscando as informações###
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
            print('executou')
            #self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            #print('executou')
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass    
    
    
    def select_football(self):
          
        try:
            btn_list = self.driver.find_element(
                'xpath', '//*[@id="app-component-view"]/app-window-plus2/div/app-home-desktop-plus2/div/div/div/app-events-area-plus2/div/app-events-area-desktop-plus2/div[1]/div[1]/app-game-selection-plus2/div/div[1]/app-game-button-plus2[1]/button/div') ##path do botão de fechar do banner que é exibido##
            sleep(2)
            btn_list.click()
            sleep(5)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass
        
    def select_all(self):
          
        try:
            btn_select_all = self.driver.find_element(
                'xpath', '//*[@id="app-component-view"]/app-window-plus2/div/app-home-desktop-plus2/div/div/div/app-events-area-plus2/div/app-events-area-desktop-plus2/div[1]/div[2]/div/div/app-events-list-desktop-plus2/app-card-plus2/div/div[2]/nav/div[2]/div/div/a[4]') ##path do botão de fechar do banner que é exibido##
            sleep(2)
            btn_select_all.click()
            sleep(5)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass      
        
    def scroll_page(self):
        ###Rolando a pagina para obtenção do html###
        try:
            sleep(2)
            for page in range(2):
                scroll = self.driver.execute_script("window.scrollBy(0,350)","")
                sleep(2)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass  

    def capture_teams(self):
        team1 = self.driver.find_elements(
            'xpath',  '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[1]/div[1]/div[2]/div[1]/span')
        team2 = self.driver.find_elements(
            'xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[1]/div[1]/div[2]/div[2]/span')
        for i in range(len(team1)):
            t1 = team1[i].text
            self.dic_jogos['TimeCasa'].append(t1)
        for j in range(len(team1)):
            t2 = team2[j].text
            self.dic_jogos['TimeVisitante'].append(t2)    
            
    def capture_odds(self):
        odds1 = self.driver.find_elements(
            'xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[2]/app-odd-button-plus2[1]/div/div/button/div')
        oddsX = self.driver.find_elements(
            'xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[2]/app-odd-button-plus2[2]/div/div/button/div')
        odds2 = self.driver.find_elements(
            'xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[2]/app-odd-button-plus2[3]/div/div/button/div')
        for i in range(len(odds1)):
            odd1 = odds1[i].text
            self.dic_jogos['Odds1'].append(odd1)
        print('funcionou')    
            
        for j in range(len(oddsX)):
            oddx = oddsX[j].text
            self.dic_jogos['OddsX'].append(oddx)
        print('funcionou')                    
        for k in range(len(odds2)):
            odd2 = odds2[k].text
            self.dic_jogos['Odds2'].append(odd2)
        print('funcionou')                    
            
    def export_data(self):
        try:
            df = pd.DataFrame(self.dic_jogos) ##transformando dicionario em dataframe##
            df.to_csv(
                self.directory_file+'\\esporte365.csv',encoding='utf-8', sep=';', index=False) ##exportando arquivo CSV para o diretorio definido a cima##
        except Exception as e:
            print(f'Houve um erro inesperado: {e}')
            pass      
    
        
    def creating_index_esport365(self):
        
        ###criando indice no data frame devido aos nomes dos times estarem escritos diferentes nos sites###
        try:
            esport365 = pd.read_csv(self.directory_file+'\\esporte365.csv', encoding = 'utf-8', sep=';')
            ind_esport365={'Timec':[], 'Timev':[]}
            df1 = esport365['TimeCasa']
            for nome in df1:
                abrev = nome[0:3]
                ind_esport365['Timec'].append(abrev)
                
            df1 = esport365['TimeVisitante']
            for nome in df1:
                abrev = nome[0:3]  
                ind_esport365['Timev'].append(abrev)
                
            df_esport365 = pd.DataFrame(ind_esport365,columns=['Timec', 'Timev'])
            df_esport365['Index'] = df_esport365['Timec'].map(str)+'x'+df_esport365['Timev']

            df_esport365 = df_esport365.drop(['Timec', 'Timev'], axis=1)
            esport365.insert(0,'ind',df_esport365)
            esport365.to_csv(self.directory_file+'\\DataFrame_esport365.csv',encoding='utf-8', sep=';', index=False)  ##exportando dataframe final##
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
  