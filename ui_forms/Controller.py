
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.insert(0,os.path.abspath(os.curdir))
from ui_forms.Model import *
from ui_forms.Confdb import *
from ui_forms.database import *



class Controller:
    def __init__(self) -> None:
        pass
    
    
    def controller_confdb(self):
        conf = Confdb()
        conf.download_driver()
        conf.database()
        
    def controller_betano(self):
        betano = Betano()
        betano.open_web_site()
        betano.close_banner()
        betano.scroll_page()
        betano.parser_data()
        betano.insert_data_dic()
        betano.export_data()
        betano.data_transform()
        betano.parser_data_double_chance()
        betano.export_double_chance()
        betano.double_chance()
        betano.close_driver()
        betano.data_convert_types()
        betano.df_concat()
        betano.export_dataframe()
        betano.creating_index_betano()
        betano.remove_files()
    
    
    def controller_pixbet(self):
        pixbet = Pixbet()
        pixbet.open_web_site()
        pixbet.parser_data()
        pixbet.data_transform()
        pixbet.export_data()
        pixbet.split_columns()
        pixbet.rename_columns()
        pixbet.order_columns()
        pixbet.remove_space()
        pixbet.data_convert_types()
        pixbet.export_dataframe()
        pixbet.create_index_pixbet()
        pixbet.remove_file()
        
    def controller_probabilidades(self):
        controller = Probabilidades()
        controller.check_exists()
        controller.download_dataBase()
        controller.move_files()    
        
    def create_tables(self):
        controller = Database()
        controller.create_table_betano()
        controller.create_table_pixbet()
        controller.create_table_matches_latest() 
        controller.create_table_global_rankings()
        controller.create_table_global_rankings_intl()
               
        