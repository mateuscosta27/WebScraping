
import shutil
import os, sys
from xml.etree.ElementTree import PI
import pandas as pd
from time import sleep
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
sys.path.insert(0,os.path.abspath(os.curdir))
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


class Pixbet:
    
    def __init__(self):
        
        
        self.directory_file = 'C:\\tmp\\Arquivos'   ##Diretorio onde serão salvos os arquivos CSV com informações obtidas###     
        self.directory_driver = 'C:\\tmp\\Driver'   ##Diretorio onde esta localizado o driver do google chrome para operação com selenium###    
        self.path = self.directory_driver +'\\chromedriver.exe'
        self.web_site = 'https://pixbet.com/prejogo/#league/2417-undefined' ##Site onde estamos buscando as informações###
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver = webdriver.Chrome(options=self.options,executable_path=self.path)
        #self.driver = uc.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), options=self.options)

        
    def open_web_site(self):
        try:
            self.driver.get(self.web_site)           
            self.driver.maximize_window()
            sleep(10)   
        except Exception as e:
            print(e)
            pass

    def parser_data(self):
        try:
            self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
            self.partidas =self.soup.find_all('table',{'class':'odds_table'})
        except Exception as e:
            print(e)
            pass
        
          
    def data_transform(self):
        try:
            self.dic_jogos = {'Jogos':[]}
            for sub in self.soup.find_all('tr', {'class': 'odds_tr'}):
                jogos = sub.get_text().strip().replace('\n\n\n\n',';').replace('\n\n\n',';').replace('\n\n',';')
                self.dic_jogos['Jogos'].append(jogos) 
            self.driver.close()
        except Exception as e:
            print(e)
            pass
        
               
    def export_data(self):
        try:
            df = pd.DataFrame(self.dic_jogos)
            df.to_csv(self.directory_file+'\\scraping_pixbet.csv',encoding='utf-8', sep=';', index=False)
        except Exception as e:
            print(e)
            pass
    def split_columns(self):
        try:
            self.df = pd.read_csv(self.directory_file+'\\scraping_pixbet.csv',encoding='utf-8', sep=';')
            self.df_split = self.df['Jogos'].str.split(';',expand= True)
            self.df_split[['Data','Hora']] = self.df_split[0].str.split('|',expand=True)
            self.df_split[['TimeCasa','TimeVisitante']] = self.df_split[1].str.split(' - ',expand=True)
            self.df_split = self.df_split.drop(columns=[0,1,5,6,7,9,10,11,12,13,14,16,17,18,19,23,24,27])
        except Exception as e:
            print(e)
            pass    
        
    def rename_columns(self):
        try:
            self.df_split.columns=['Odds1','OddsX','Odds2','MaisGols',
               'MenosGols','Dupla1x','Dupla12','Dupla2x','AmbosMarcamSim',
               'AmbosMarcamNao','Data','Hora','TimeCasa','TimeVisitante']
        except Exception as e:
            print(e)
            pass 
    def order_columns(self):
        try:
            self.df = pd.DataFrame(data=self.df_split)
            self.df = self.df[['Hora','Data','TimeCasa','TimeVisitante','Odds1','OddsX','Odds2',
                           'MaisGols','MenosGols','AmbosMarcamSim','AmbosMarcamNao','Dupla1x','Dupla12','Dupla2x']]
        except  Exception as e:
            print(e)
            pass
        
        
    def remove_space(self):
        try:
            for column_remove in self.df.columns:
                self.df[column_remove] = self.df[column_remove].apply(lambda x:str(x).strip())
            ano = '/2022'
            self.df['Data'] =  self.df['Data'].apply(lambda x: (x+ano).replace('/','-'))
        except Exception as e:
            print(e)
            pass
    def data_convert_types(self):
        try:
            self.df['Data'] = self.df['Data'].apply(lambda x: pd.to_datetime(x, format='%d-%m-%Y')) 
            for column_float in self.df.columns[4:]:
                self.df[column_float] = pd.Series(self.df[column_float], dtype=float)
        except Exception as e:
            print(e)
            pass
        
    def export_dataframe(self):
        try:
            self.df.to_csv(self.directory_file+'\\df_pixbet.csv',encoding='utf-8', sep=';', index=False)
        except Exception as e:
            print(e)
            pass
        
    def create_index_pixbet(self):
        try:
            pixbet = pd.read_csv(self.directory_file+'\\df_pixbet.csv', encoding = 'utf-8', sep=';')
            ind_pixbet={'Timec':[], 'Timev':[]}
            df1 = pixbet['TimeCasa']
            for nome in df1:
                abrev = nome[0:3]
                ind_pixbet['Timec'].append(abrev)
                    
            df1 = pixbet['TimeVisitante']
            for nome in df1:
                abrev = nome[0:3]  
                ind_pixbet['Timev'].append(abrev)
                    
            df_pixbet = pd.DataFrame(ind_pixbet,columns=['Timec', 'Timev'])
            df_pixbet['Index'] = df_pixbet['Timec'].map(str)+'x'+df_pixbet['Timev']
            df_pixbet = df_pixbet.drop(['Timec', 'Timev'], axis=1)
            pixbet.insert(0,'ind',df_pixbet)
            pixbet.to_csv(self.directory_file+'\\DataFrame_pixbet.csv',encoding='utf-8', sep=';', index=False)
        except Exception as e:
            print(e)
            pass
        
    def remove_file(self):
        try:
            os.remove(self.directory_file+'\\scraping_pixbet.csv')
            os.remove(self.directory_file+'\\df_pixbet.csv')
        except OSError as e:
            print(f"Error:{e.strerror}")
            print('Algo deu errado')
