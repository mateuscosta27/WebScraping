
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




class Betano:
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

    def parser_data(self):
        teste = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div/section[2]/div[5]/div[2]/section/div[4]/div/div[1]/div[2]/table/tr[2]/th/a/div/div[1]/div[1]/span')
        print('executou')
        print(teste)
   

teste = Betano()
teste.open_web_site()
teste.close_banner()
teste.parser_data()