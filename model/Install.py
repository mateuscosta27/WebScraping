from opcode import opname
import os
import sqlite3
import requests as rq
from io import BytesIO
import zipfile

import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))

class Install:
    def __init__(self) :
         ###Criando diretorios padrao###      
        diretorios = ['C:\\tmp\\Arquivos','C:\\tmp\\Bancos','C:\\tmp\\Driver']
        for diretorio in diretorios:
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)
                
    def download_driver(self):
        ###baixando driver do google###
        directory_driver = 'C:\\tmp\\Driver'
        url = 'https://chromedriver.storage.googleapis.com/106.0.5249.21/chromedriver_win32.zip'
        filebyte = BytesIO(rq.get(url).content)
        myzip = zipfile.ZipFile(filebyte)
        myzip.extractall(directory_driver)

                
    def database(self):
        ###criando database###
        directory_database = 'C:\\tmp\\Bancos'
        con = sqlite3.connect(directory_database+'\\DADOS.db')           
                



install = Install()
install.download_driver()
install.database()