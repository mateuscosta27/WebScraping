import os
from time import sleep
from urllib import request
import sys,os
import shutil
sys.path.insert(0,os.path.abspath(os.curdir))

class Teste:
    def __init__(self) :
         ###Criando diretorios padrao###      
        self.directpry_file = 'C:\\tmp\\Arquivos' 
                
    def download_driver(self):
        ###baixando driver do google###
     
        get1 = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv'
        get2 ='https://projects.fivethirtyeight.com/soccer-api/club/spi_global_rankings.csv'
        get3 = 'https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv'    
        matches_latest =  request.urlretrieve(get1, 'matches_latest.csv') 
        global_rankings = request.urlretrieve(get2, 'global_rankings.csv')
        global_rankings_intl = request.urlretrieve(get2, 'global_rankings_intl.csv')

        names = ['matches_latest.csv','global_rankings.csv','global_rankings_intl.csv']
        for name in names:
            shutil.move(name, self.directpry_file) 
 
teste = Teste()
teste.download_driver()