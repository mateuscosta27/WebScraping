
import shutil
import os, sys
import pandas as pd
from time import sleep
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
sys.path.insert(0,os.path.abspath(os.curdir))
from selenium.webdriver.chrome.options import Options



class Betano:
    def __init__(self):
        ###Carregando driver, recebendo o web site, definindo diretorio###
        self.directory_file = 'C:\\tmp\\Arquivos'   ##Diretorio onde serão salvos os arquivos CSV com informações obtidas###     
        self.directory_driver = 'C:\\tmp\\Driver'   ##Diretorio onde esta localizado o driver do google chrome para operação com selenium###    
        self.path = self.directory_driver +'\\chromedriver.exe'
        self.web_site = 'https://br.betano.com/sport/futebol/ligas/10016r,10016o,10017r,1r,1o,216r,216o,1635r,1635o,5r,5o/?bt=0' ##Site onde estamos buscando as informações###
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
            for page in range(5):
                scroll = self.driver.execute_script("window.scrollBy(0,450)","")
                sleep(2)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass        
            
    def parser_data(self):
        ###Analisando o html e capturando as informações desejadas###
        try:
            self.dic_jogos = {'Jogos':[]} ##Dicionario que armazenara as informações do parseamento do html##
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            table = soup.find('table', {'class': 'events-list__grid'}) ##classe onde se encontram as informações##
            self.tr_element = table.find_all('tr',{'class':'events-list__grid__event'})
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass
                
    def insert_data_dic(self):
        try:
            for jogo in self.tr_element:
                jogos = jogo.get_text().strip()
                self.dic_jogos['Jogos'].append(jogos)
            self.dic_jogos = self.dic_jogos
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass

               
    def export_data(self):
        try:
            df = pd.DataFrame(self.dic_jogos) ##transformando dicionario em dataframe##
            df.to_csv(
                self.directory_file+'\\scraping_betano.csv',encoding='utf-8', sep=';', index=False) ##exportando arquivo CSV para o diretorio definido a cima##
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass
        
    def data_transform(self):
        ###Limpeza dos dados###
        try:
            df = pd.read_csv(self.directory_file+'\\scraping_betano.csv',encoding='utf-8', sep=';') ##importação do CSV###
            df = df['Jogos'].str.split('\n ', expand= True)
            df = df.drop(columns=[1,3,5,7,8,9,11,13,15,16,17,19,21,22,23,25,27]) ##Removendo as colunas desnecessárias##
            df.columns = ['Data','Hora','TimeCasa','TimeVisitante','Odds1','OddsX','Odds2','MaisGols','MenosGols',
                            'AmbosMarcamSim','AmbosMarcamNao'] ##Renomeando as colunas##
            self.df = df
            for column_remove in self.df.columns:
                self.df[column_remove] = self.df[column_remove].apply(lambda x:str(x).strip()) ##Removendo espaços da direita e da esquerda das strings##
            ##inserindo ano para formatar padrão a data
            ano = '/2022'
            self.df['Data'] =  self.df['Data'].apply(lambda x: (x+ano).replace('/','-'))
        except Exception as e:
            print(f'Houve um erro inesperado:{e}')
            pass

    def parser_data_double_chance(self):
        ###Obtendo dados da dupla chance##
        try:
            self.driver.execute_script("window.open('https://br.betano.com/sport/futebol/ligas/10016r,10016o,10017r,1r,1o,216r,216o,1635r,1635o,5r,5o/?bt=1')")
            self.driver._switch_to.window(self.driver.window_handles[1])
            sleep(5)
            #btn_dupla_chance = self.driver.find_element('xpath', '/html/body/div[1]/div/section[2]/div[5]/div[2]/section/div[3]/div/div[1]/div/ul/li[3]/div') ##path do botão de dupla chance##
            #btn_dupla_chance.click()
            sleep(3)
            for page in range(2):
                scroll = self.driver.execute_script("window.scrollBy(0,350)","")
            sleep(2)
            ##mesmo processo de tratamento dos dados com dicionario ##
            dic_duplachance = {'Dupla':[]} 
            soup_dupla = BeautifulSoup(self.driver.page_source, 'lxml')
            table = soup_dupla.find('table', {'class': 'events-list__grid'})
            tr_element = table.find_all('tr',{'class':'events-list__grid__event'})
            for jogo in tr_element:
                jogos = jogo.get_text().strip()
                dic_duplachance['Dupla'].append(jogos)
            self.dic_duplachance = dic_duplachance
        except Exception as e:
            print(e)
            print('passou')
            self.except_button()
            pass
            
    def except_button(self):
        try:
            self.driver.refresh()
            self.driver.execute_script("window.open('https://br.betano.com/sport/futebol/ligas/10016r,10016o,10017r,1r,1o,216r,216o,1635r,1635o,5r,5o/?bt=2')")
            self.driver._switch_to.window(self.driver.window_handles[2])
            sleep(3)
            
            for page in range(3):
                scroll = self.driver.execute_script("window.scrollBy(0,400)","")
            sleep(2)
            ##mesmo processo de tratamento dos dados com dicionario ##
            dic_duplachance = {'Dupla':[]} 
            soup_dupla = BeautifulSoup(self.driver.page_source, 'lxml')
            table = soup_dupla.find('table', {'class': 'events-list__grid'})
            tr_element = table.find_all('tr',{'class':'events-list__grid__event'})
            for jogo in tr_element:
                jogos = jogo.get_text().strip()
                dic_duplachance['Dupla'].append(jogos)
            self.dic_duplachance = dic_duplachance
        except Exception as e:
            print(e)
            print('passou')
            pass
        
                     
    def close_driver(self):
        try:    
            self.driver.close() ##fechando o driver##
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass

    def export_double_chance(self): 
        ###Exportando os dados coletados da dupla chance##
        try:
            df_odds = pd.DataFrame(self.dic_duplachance)
            df_odds.to_csv(self.directory_file+'\\scraping_betano_dupla.csv',encoding='utf-8', sep=';', index=False)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass

    def double_chance(self):
        ##limpando os dados##
        try:
            self.DuplaChance = pd.read_csv(self.directory_file+'\\scraping_betano_dupla.csv',encoding='utf-8', sep=';')
            self.DuplaChance = self.DuplaChance['Dupla'].str.split('\n ', expand= True)
            self.DuplaChance = self.DuplaChance[[10,12,14]]
            self.DuplaChance.columns = ['Dupla1x','Dupla2x','Dupla12'] ##renomenando as colunas
            for convertion in self.DuplaChance:
                self.DuplaChance[convertion] = pd.Series(self.DuplaChance[convertion], dtype=float)
            self.df_dupla = self.DuplaChance
            self.df_dupla.to_csv(self.directory_file+'\\DataFrame_betano_dupla.csv',encoding='utf-8', sep=';', index=False) ##exportando csv##
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass    
       
               
    def data_convert_types(self):
        try:
            self.df['Data'] = self.df['Data'].apply(lambda x: pd.to_datetime(x, format='%d-%m-%Y')) 
            for column_float in self.df.columns[4:]:
                self.df[column_float] = pd.Series(self.df[column_float], dtype=float)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass

    def df_concat(self):
        ##concatenando dupla chance com os dados de odds
        try:
            self.df_full = pd.concat([self.df, self.df_dupla], axis=1)   
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass

    def export_dataframe(self):
        ##exportando o datafreme com todos os dados###
        try:
            self.df_full.to_csv(self.directory_file+'\\df_betano.csv',encoding='utf-8', sep=';', index=False)
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass
        
    def creating_index_betano(self):
        
        ###criando indice no data frame devido aos nomes dos times estarem escritos diferentes nos sites###
        try:
            betano = pd.read_csv(self.directory_file+'\\df_betano.csv', encoding = 'utf-8', sep=';')
            ind_betano={'Timec':[], 'Timev':[]}
            df1 = betano['TimeCasa']
            for nome in df1:
                abrev = nome[0:3]
                ind_betano['Timec'].append(abrev)
                
            df1 = betano['TimeVisitante']
            for nome in df1:
                abrev = nome[0:3]  
                ind_betano['Timev'].append(abrev)
                
            df_betano = pd.DataFrame(ind_betano,columns=['Timec', 'Timev'])
            df_betano['Index'] = df_betano['Timec'].map(str)+'x'+df_betano['Timev']

            df_betano = df_betano.drop(['Timec', 'Timev'], axis=1)
            betano.insert(0,'ind',df_betano)
            betano.to_csv(self.directory_file+'\\DataFrame_betano.csv',encoding='utf-8', sep=';', index=False)  ##exportando dataframe final##
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass

    def remove_files(self):         
        try:
            #os.remove(self.directory_file+'\\scraping_betano.csv')
            os.remove(self.directory_file+'\\df_betano.csv')
            os.remove(self.directory_file+'\\DataFrame_betano_dupla.csv')
            os.remove(self.directory_file+'\\scraping_betano_dupla.csv')
            os.remove(self.directory_file+'\\scraping_betano.csv')
        except OSError as e:
            print(f"Error:{e.strerror}")
            print('Algo deu errado')

