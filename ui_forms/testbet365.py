
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
        self.web_site = 'https://www.bet365.com/#/HO/' ##Site onde estamos buscando as informações###
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--window-size=1920,1080')
        #self.options.add_argument('--start-maximized')
        #self.options.add_argument('--headless')
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options,executable_path=self.path)
    
                      
    def open_web_site(self):
        ###Abrindo website##
        try:
            self.driver.get(self.web_site)
            self.driver.maximize_window()
            self.driver.execute_script("window.open('https://www.bet365.com/#/AC/B1/C1/D1002/E71022033/G40/')")
            self.driver._switch_to.window(self.driver.window_handles[1])
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass    
    



teste = Bet365()
teste.open_web_site()