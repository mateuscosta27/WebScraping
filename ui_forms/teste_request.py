import os
from time import sleep
from urllib import request
import sys,os
import shutil
sys.path.insert(0,os.path.abspath(os.curdir))

class Teste:
    def __init__(self) :
         ###Criando diretorios padrao###      
        self.directory_file = 'C:\\tmp\\Arquivos'
        self.names = ['matches_latest.csv','global_rankings.csv','global_rankings_intl.csv']
                
    def download_driver(self):
        ###baixando driver do google###
     
        get1 = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv'
        get2 ='https://projects.fivethirtyeight.com/soccer-api/club/spi_global_rankings.csv'
        get3 = 'https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv'    
        request.urlretrieve(get1, 'matches_latest.csv') 
        request.urlretrieve(get2, 'global_rankings.csv')
        request.urlretrieve(get2, 'global_rankings_intl.csv')
        
        
    def check(self):
        for file in self.names:
         if(os.path.exists(self.directory_file+'\\'+file)):
                os.remove(self.directory_file+'\\'+file)
       
        
    def move(self):
        for file in self.names:       
         shutil.move(file,self.directory_file)
           
 
teste = Teste()
teste.check()
teste.download_driver()
teste.move()
