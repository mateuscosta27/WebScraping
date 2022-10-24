
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



class Bet365:
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
        self.dic_jogos = {'Mandante':[], 'Visitante':[], 'Odds1':[],'OddsX':[],'Odds2':[]}

                      
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
    
    
    def select_futebol(self):
          
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

    # teste      
    def teste(self):
        
        try:
            mandantes = self.driver.find_elements('xpath',  '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[1]/div[1]/div[2]/div[1]/span')
            visitantes = self.driver.find_elements('xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[1]/div[1]/div[2]/div[2]/span')
            odds1 = self.driver.find_elements('xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[2]/app-odd-button-plus2[1]/div/div/button/div')
            oddsX = self.driver.find_elements('xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[2]/app-odd-button-plus2[2]/div/div/button/div')
            odds2 = self.driver.find_elements('xpath', '//*[@id="agsVirtual"]/app-event-item-desktop-plus2/app-event-item-soccer-desktop-plus2/div/div/div[2]/app-odd-button-plus2[3]/div/div/button/div')
            for i in range(len(mandantes)):
                team1 = mandantes[i].text
                self.dic_jogos['Mandante'].append(team1)
            for j in range(len(visitantes)):
                team2 = visitantes[j].text
                self.dic_jogos['Visitante'].append(team2)               
            self.driver.close()
        except Exception as e:
            self.driver.close()
            
            print(e)
            pass    

              
    def export_data(self):
        try:
            df = pd.DataFrame(self.dic_jogos) ##transformando dicionario em dataframe##
            df.to_csv(
                self.directory_file+'\\teste.csv',encoding='utf-8', sep=';', index=False) ##exportando arquivo CSV para o diretorio definido a cima##
        except Exception as e:
            print(f'Houve um erro inesperado: {e}')
            pass
                

teste = Bet365()
teste.open_web_site()
sleep(10)
teste.select_futebol()
sleep(5)
teste.select_all()
sleep(5)
teste.teste()
teste.export_data()
