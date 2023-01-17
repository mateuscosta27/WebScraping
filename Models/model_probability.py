import os, sys
import shutil
from urllib import request



class Probability:
    
    def __init__(self):
        self.directory_file = 'C:\\tmp\\Arquivos' 
        self.get1 = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches_latest.csv'
        self.get2 ='https://projects.fivethirtyeight.com/soccer-api/club/spi_global_rankings.csv'
        self.get3 = 'https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv'
        self.names = ['matches_latest.csv','global_rankings.csv','global_rankings_intl.csv']

    def check_exists(self):
        try:
            for file in self.names:
                if(os.path.exists(self.directory_file+'\\'+file)):
                    os.remove(self.directory_file+'\\'+file)
        except OSError as e:
            print('Houve um erro inesperado: {}')
            pass            

    def download_dataBase(self):
        try:
            request.urlretrieve(self.get1, 'matches_latest.csv') 
            request.urlretrieve(self.get2, 'global_rankings.csv')
            request.urlretrieve(self.get2, 'global_rankings_intl.csv')
        except Exception as e:
            print('Houve um erro inesperado: {}')
            pass
        
    def move_files(self):
        try:
            for file in self.names:       
                shutil.move(file,self.directory_file)
        except Exception as e:
            print('Houve um erro inesperado: {}')
            pass   