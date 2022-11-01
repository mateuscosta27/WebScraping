
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
        self.web_site = 'https://br.betano.com/sport/futebol/brasil/brasileirao-serie-a/10016/?bt=0' ##Site onde estamos buscando as informações###
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--window-size=1920,1080')
        #self.options.add_argument('--start-maximized')
        #self.options.add_argument('--headless')
        #self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options,executable_path=self.path)
        self.dic_jogos = {'TimeCasa':[]}
          
        
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
    def close_banner(self):
        ###fechando o banner que é exibido###
        try:
            btn_fechar = self.driver.find_element(
                'xpath', '/html/body/div[1]/div/section[2]/div[7]/div/div/div[1]/button') ##path do botão de fechar do banner que é exibido##
            sleep(5)
            btn_fechar.click()
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
        team1 = self.driver.find_element(
            'xpath',  '//*[@class="events-list__grid__info__main__participants__participant-name"]')
        print(team1[0].text)    
        #for i in range(len(team1)):
            #t1 = team1[i].text
            #self.dic_jogos['TimeCasa'].append(t1)


teste = Esporte365()
teste.open_web_site()
teste.close_banner()
teste.scroll_page()
teste.capture_teams()            