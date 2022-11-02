import requests
from pandas import json_normalize


class Esporte365:
    def __init__(self) -> None:
        self.directory_file = 'C:\\tmp\\Arquivos' 
        
    
    
    def request(self):
        headers = {
            'authority': 'vip.ngx.bet',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'if-none-match': 'W/"1d033-6Y9vpm1geQPAaRW8KANZySpPu10"',
            'origin': 'https://www.esporte365.com',
            'referer': 'https://www.esporte365.com/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        params = {
            'type': 'SOCCER',
            'external_championship_id': '20913',
        }

        response = requests.get('https://vip.ngx.bet/event', params=params, headers=headers)

        esporte365 = json_normalize(response.json())
        df = esporte365[[
                    'home_team', 
                    'away_team',
                    'odds.full_time.home.value',
                    'odds.full_time.draw.value',
                    'odds.full_time.away.value',
                    'odds.full_time.home_or_draw.value',
                    'odds.full_time.draw_or_away.value']]

        df.columns = [
                    'TimeCasa',
                    'TimeVisitante',
                    'Odds1',
                    'OddsX',
                    'Odds2',
                    '1x',
                    '2x']
        self.Data_Frame = df
        
    def export_data(self):
        for column_remove in self.Data_Frame.columns:
                self.Data_Frame[column_remove] = self.Data_Frame[column_remove].apply(lambda x:str(x).strip())
                
        self.Data_Frame.to_csv(
                self.directory_file+'\\Data_Frame_esporte.csv',encoding='utf-8', sep=';', index=False)
       
       
esport = Esporte365()
esport.request()
esport.export_data()       