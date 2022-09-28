import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from model.Model import Betano
from model.Model import Pixbet


class Controller:
    def __init__(self) -> None:
        pass
    
    def controller_betano(self):
        betano = Betano()
        betano.open_web_site()
        betano.close_banner()
        betano.scroll_page()
        betano.parser_data()
        betano.export_data()
        betano.data_transform()
        betano.parser_data_double_chance()
        betano.export_double_chance()
        betano.double_chance()
        betano.data_convert_types()
        betano.df_concat()
        betano.export_dataframe()
        betano.creating_index_betano()
    
    
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
        