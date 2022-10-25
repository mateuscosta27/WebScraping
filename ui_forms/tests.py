
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class Betano:
    def __init__(self):
        ###Carregando driver, recebendo o web site, definindo diretorio###
        self.directory_file = 'C:\\tmp\\Arquivos'   ##Diretorio onde serão salvos os arquivos CSV com informações obtidas###     
        self.directory_driver = 'C:\\tmp\\Driver'   ##Diretorio onde esta localizado o driver do google chrome para operação com selenium###    
        self.path = self.directory_driver +'\\chromedriver.exe'
        self.web_site = 'www.google.com' ##Site onde estamos buscando as informações###
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
            action = ActionChains(self.driver)
            action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
                
            print('executou')

            self.driver.maximize_window()
            print('executou')
            #self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            #print('executou')
        except Exception as e:
            print('Houve um erro inesperado:  '+ e)
            pass    
   

teste = Betano()
teste.open_web_site()
