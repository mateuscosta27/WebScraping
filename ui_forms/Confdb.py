import os
import sqlite3
import requests as rq
from io import BytesIO
import zipfile
import sys,os
sys.path.insert(0,os.path.abspath(os.curdir))

import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
class Confdb:


  
    def __init__(self) :


        app = QApplication(sys.argv)
        selected_directory = QFileDialog.getExistingDirectory(directory="/C:")
        print(selected_directory) 
        diretorios = [selected_directory+'\\tmp\\Arquivos',selected_directory+'\\tmp\\Bancos',selected_directory+'\\tmp\\Driver']
        for diretorio in diretorios:
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)
                
    def download_driver(self):
        ###baixando driver do google###
        directory_driver = 'C:\\tmp\\Driver'
        url = 'https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_win32.zip'
        filebyte = BytesIO(rq.get(url).content)
        myzip = zipfile.ZipFile(filebyte)
        myzip.extractall(directory_driver)

                
    def database(self):
        ###criando database###
        directory_database = 'C:\\tmp\\Bancos'
        con = sqlite3.connect(directory_database+'\\DADOS.db')
        con.close()           


teste = Confdb()