from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import os

class Pixbet:
    
    def __init__(self):
        
        
        self.directory_file = 'C:\\tmp\\Arquivos'   ##Diretorio onde serão salvos os arquivos CSV com informações obtidas###     
        self.directory_driver = 'C:\\tmp\\Driver'   ##Diretorio onde esta localizado o driver do google chrome para operação com selenium###    
        self.path = self.directory_driver +'\\chromedriver.exe'
        self.web_site = 'https://pixbet.com/prejogo/#league/2417-undefined' ##Site onde estamos buscando as informações###
        self.options = webdriver.ChromeOptions()
        
       
       
        
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        #self.options.add_argument("--window-size=1920,1080")
        #self.options.add_argument('--start-maximized')
        #self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options,executable_path=self.path)
        
       


    def open_web_site(self):
        self.driver.get(self.web_site)
        self.driver.maximize_window()
        sleep(5)
        print('sem erro open')

    def parser_data(self):
        self.soup = BeautifulSoup(self.driver.page_source, 'lxml')
        self.partidas =self.soup.find_all('table',{'class':'odds_table'})
        print('sem erro parser')
        
          
    def data_transform(self):
        self.dic_jogos = {'Jogos':[]}
        for sub in self.soup.find_all('tr', {'class': 'odds_tr'}):
            jogos = sub.get_text().strip().replace('\n\n\n\n',';').replace('\n\n\n',';').replace('\n\n',';')
            self.dic_jogos['Jogos'].append(jogos) 
        self.driver.close()
        print('sem erro transform')
        
        
           
    def export_data(self):
        df = pd.DataFrame(self.dic_jogos)
        df.to_csv(self.directory_file+'\\scraping_pixbet.csv',encoding='utf-8', sep=';', index=False)
        print('sem erro export')
        self.df = pd.read_csv(self.directory_file+'\\scraping_pixbet.csv',encoding='utf-8', sep=';')
        print(self.df)
        
    def split_columns(self):
        self.df = pd.read_csv(self.directory_file+'\\scraping_pixbet.csv',encoding='utf-8', sep=';')
        self.df_split = self.df['Jogos'].str.split(';',expand= True)
        self.df_split[['Data','Hora']] = self.df_split[0].str.split('|',expand=True)
        self.df_split[['TimeCasa','TimeVisitante']] = self.df_split[1].str.split(' - ',expand=True)
        self.df_split = self.df_split.drop(columns=[0,1,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,27])
        print('sem erro split')
        
        
    def rename_columns(self):
        self.df_split.columns=['Odds1','OddsX','Odds2','MaisGols',
               'MenosGols','Dupla1x','Dupla12','Dupla2x','AmbosMarcamSim',
               'AmbosMarcamNao','Data','Hora','TimeCasa','TimeVisitante']
        print('sem erro')
        
    def order_columns(self):
        self.df = pd.DataFrame(data=self.df_split)
        self.df = self.df[['Hora','Data','TimeCasa','TimeVisitante','Odds1','OddsX','Odds2',
                           'MaisGols','MenosGols','AmbosMarcamSim','AmbosMarcamNao','Dupla1x','Dupla12','Dupla2x']]
        print('sem erro')
        
        
    def remove_space(self):
        for column_remove in self.df.columns:
            self.df[column_remove] = self.df[column_remove].apply(lambda x:str(x).strip())
        print('sem erro')
    
    def data_convert_types(self):
        #self.df['Data'] = pd.to_datetime(self.df['Data'],format="%d/%m")
        for column_float in self.df.columns[4:]:
           self.df[column_float] = pd.Series(self.df[column_float], dtype=float)
        print('sem erro')   
        
    def export_dataframe(self):
        self.df.to_csv(self.directory_file+'\\df_pixbet.csv',encoding='utf-8', sep=';', index=False)
        print('sem erro')
        
    def create_index_pixbet(self):
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
        print('sem erro')
        
    def remove_file(self):
        try:
            os.remove(self.directory_file+'\\scraping_pixbet.csv')
            os.remove(self.directory_file+'\\df_pixbet.csv')
        except OSError as e:
            print(f"Error:{e.strerror}")
            print('Algo deu errado')
        print('sem erro')
        
        
        
pixbet = Pixbet()
pixbet.open_web_site()
pixbet.parser_data()
pixbet.data_transform()
pixbet.export_data()
"""pixbet.split_columns()
pixbet.rename_columns()
pixbet.order_columns()
pixbet.remove_space()
pixbet.data_convert_types()
pixbet.export_dataframe()
pixbet.create_index_pixbet()
pixbet.remove_file() """       