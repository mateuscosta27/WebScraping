import requests
import pandas as pd
import mysql.connector
from mysql.connector import Error


class Api_betano:
    def __init__(self):


        self.connection = mysql.connector.connect(
            host='localhost',
            user = 'root',
            password = 'B@tata2020',
            database = 'dbapostas'
        )

        self.cookies = {
                'sticky': 'stx30.033',
                'sticky': 'stx11.100',
                'sb_landing': 'true',
                'sb_cookieConsent': 'true',
                '_gid': 'GA1.2.1631329719.1671720792',
                'lc-session': '1',
                '_lr_uf_-7hhr6m': '477528a9-feb3-426a-80a0-35cc679c6f33',
                'siteid': 'undefined',
                '__cf_bm': 'HdYSgcRWrDS4vlI5DkHEXEIEOmZfBBwFLMywTVDoFLw-1671889099-0-AUPgLMkaQsVDWutfJi6p4SzhYUNAfqlTQBK5d1nebRH0FPLCCmpxAEtEFh5oXbVE/N+5d8zX7Rwk9nu2doRi2uOd7miijGF3ZE2q2YA5meOnTWbw46mCvrFPbD4utCQphz0HjvYzFh8SyhPepXCIaOTQFRXjbcTfPRIS2NH8J/TWm0U7GwbFiCDEXzFp6JcbeA==',
                '_lr_hb_-7hhr6m%2Fbetanobr': '{%22heartbeat%22:1671889312510}',
                '_ga': 'GA1.2.1565399312.1666719160',
                '_lr_tabs_-7hhr6m%2Fbetanobr': '{%22sessionID%22:0%2C%22recordingID%22:%225-2541c924-0637-410b-b05b-6fec30fec603%22%2C%22recordingConditionThreshold%22:%2222.465372880147317%22%2C%22lastActivity%22:1671889403632}',
                '_gat_UA-164922849-1': '1',
                '_ga_CHR7RP8E7T': 'GS1.1.1671888500.25.1.1671889405.59.0.0',
                }

        self.headers = {
                'authority': 'br.betano.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                # 'cookie': 'sticky=stx30.033; sticky=stx11.100; sb_landing=true; sb_cookieConsent=true; _gid=GA1.2.1631329719.1671720792; lc-session=1; _lr_uf_-7hhr6m=477528a9-feb3-426a-80a0-35cc679c6f33; siteid=undefined; __cf_bm=HdYSgcRWrDS4vlI5DkHEXEIEOmZfBBwFLMywTVDoFLw-1671889099-0-AUPgLMkaQsVDWutfJi6p4SzhYUNAfqlTQBK5d1nebRH0FPLCCmpxAEtEFh5oXbVE/N+5d8zX7Rwk9nu2doRi2uOd7miijGF3ZE2q2YA5meOnTWbw46mCvrFPbD4utCQphz0HjvYzFh8SyhPepXCIaOTQFRXjbcTfPRIS2NH8J/TWm0U7GwbFiCDEXzFp6JcbeA==; _lr_hb_-7hhr6m%2Fbetanobr={%22heartbeat%22:1671889312510}; _ga=GA1.2.1565399312.1666719160; _lr_tabs_-7hhr6m%2Fbetanobr={%22sessionID%22:0%2C%22recordingID%22:%225-2541c924-0637-410b-b05b-6fec30fec603%22%2C%22recordingConditionThreshold%22:%2222.465372880147317%22%2C%22lastActivity%22:1671889403632}; _gat_UA-164922849-1=1; _ga_CHR7RP8E7T=GS1.1.1671888500.25.1.1671889405.59.0.0',
                'referer': 'https://br.betano.com/sport/futebol/',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                }
    def request(self):
        self.response = requests.get('https://br.betano.com/api/sport/futebol/jogos-de-hoje/?req=la,s,stnf,c,mb',
        cookies=self.cookies,
        headers=self.headers)

    def insert_database(self):
        cursor =  self.connection.cursor()
        betano = self.response.json()
        blocks = betano['data']['blocks']
        for block in range(len(blocks)):
            select_block = blocks[block]
            events = select_block['events']
            for event in range(len(events)):
                select_event = events[event]
                markets = select_event['markets'][0]['selections']

                regionName = select_event['regionName']
                regionId =select_event['regionId']
                leagueDescription = select_event['leagueDescription'] 
                mandate = markets[0]['fullName']
                visitante = markets[2]['fullName']
                odds1 = markets[0]['price']
                oddsx = markets[1]['price']
                odds2 = markets[2]['price']

                sql = (f"""
                      SELECT EXISTS(SELECT * FROM tb_betano WHERE home = '{mandate}' and away = '{visitante}') 

                            """)
                cursor.execute(sql)
                
                result = cursor.fetchall()
               
                if result[0][0] == 0:       
                    insert = (f"""
                            insert into tb_betano(regionName, regionId, 
                            leagueDescription, home, Away, odds1, oddsx, odds2) values(
                                "{regionName}", {regionId},"{leagueDescription}",
                                "{mandate}","{visitante}",{odds1},{oddsx},{odds2}
                            )

                                """)
                    cursor.execute(insert)
                    self.connection.commit()
                    print('Dados inseridos com sucesso!')
                else:
                    update = (f"""
                            update tb_betano
                            set     odds1 = {odds1},
                                    oddsx = {oddsx},
                                    odds2 = {odds2}
                            where home = '{mandate}' and
                                    away = '{visitante}' 

                                """)
                    cursor.execute(update)
                    self.connection.commit()
                    print('Dados ja existiam e foram atualizados')  


                    
              
                

                



         
betano = Api_betano()
betano.request()
betano.insert_database()