import json
import sys
import sys,os
import sqlite3
import zipfile
from io import BytesIO
from datetime import date
from PySide6.QtWidgets import QApplication, QFileDialog


class ConfigConnection:

    def __init__(self) :

        data = date.today()
        dataAtual = data.strftime('%d/%m/%Y')
        self.data = dataAtual

    def selectDir(self):
        _selected_directory = QFileDialog.getExistingDirectory(dir="C:\\")
        self.selected_dir = _selected_directory
        self.pathConnection = os.path.join(_selected_directory,'Bancos')
       
        
    def create_directory(self):

        default_directorys = [
                os.path.join(self.selected_dir,'tmp','Arquivos'),
                os.path.join(self.selected_dir,'tmp','Bancos'),
                os.path.join(self.selected_dir,'tmp','Driver')   
             ]
        
        for directory in default_directorys:
            if not os.path.exists(directory):
                os.makedirs(directory)
        self.save_StringConnection()


    def save_StringConnection(self):

        defautlConnection =os.path.join(self.selected_dir,'tmp','Bancos','ApostasEsportivas.db')
        defaultFiles = os.path.join(self.selected_dir, 'tmp','Arquivos')
        defulLocaleDriver = os.path.join(self.selected_dir,'tmp','Driver')
        dicConnection = {'StartConnection':defautlConnection, 'Files':defaultFiles, 'Driver': defulLocaleDriver}
        Staturp = json.dumps(dicConnection, indent=4)
        with open("./Data/Startup.json", "w") as outfile:
            outfile.write(Staturp)


"""       default_directorys = [selected_directory+'\\tmp\\Arquivos',selected_directory+'\\tmp\\Bancos',selected_directory+'\\tmp\\Driver']
                for diretorio in diretorios:
                    if not os.path.exists(diretorio):
                        os.makedirs(diretorio)

                with open("Startup.json", encoding='utf8') as stringConnection:
                    connection = json.load(stringConnection)
                connectionPath= connection['']
        """
        


      
                
""" def download_driver(self):
        ###baixando driver do google###
        directory_driver = 'C:\\tmp\\Driver'
        url = 'https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_win32.zip'
        filebyte = BytesIO(rq.get(url).content)
        myzip = zipfile.ZipFile(filebyte)
        myzip.extractall(directory_driver)
"""