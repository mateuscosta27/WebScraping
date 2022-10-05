import sqlite3
import pandas as pd





class Database:
    
    def __init__(self):
        self.directory_database = 'C:\\tmp\\Bancos'
        self.directory_file = 'C:\\tmp\\Arquivos'
        self.con_db = sqlite3.connect(self.directory_database+'\\DADOS.db')
        
    def create_table_betano(self):
        self.con_db
        betano = pd.read_csv(self.directory_file+'\\DataFrame_betano.csv',encoding='utf-8', sep=';')
        betano.to_sql(
            name= 'tb_betano',
            if_exists='replace',
            index=False,
            con = self.con_db       
        )
       
    
    
    def create_table_pixbet(self):
        
        self.con_db
        betano = pd.read_csv(self.directory_file+'\\DataFrame_pixbet.csv',encoding='utf-8', sep=';')
        betano.to_sql(
            name= 'tb_pixbet',
            if_exists='replace',
            index=False,
            con = self.con_db       
        )
            
        
        