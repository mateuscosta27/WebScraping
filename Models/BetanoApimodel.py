import requests
import json
import os
import pandas as pd


class ApiBetano:
    def __init__(self):


        
        dic_jogos_betano = {"name":[],'region_name':[],'region_id':[],'leagueDescription':[],
        'home_team':[],'tie':[],'away_team':[]}
        self.dic_jogos_betano = dic_jogos_betano

        with open("./Data/Startup.json") as directory_files:
            DataFut = json.load(directory_files)
            _files = DataFut['Files']
            self.files = _files

            

    def request_api(self):

        url = "https://br.betano.com/api/sport/futebol/jogos-de-hoje/?sort=Leagues&req=la,s,tn,stnf,c,mb"
        response = requests.get(url)
        data = response.json()
        with open(os.path.join(self.files,"data.json"), "w") as outfile:
            json.dump(data, outfile)  


    def read_json(self):

        with open(os.path.join(self.files,'data.json')) as StringFiles:
            DataPartidas = json.load(StringFiles)
            _matchs = DataPartidas
            self.matchs = _matchs

    def data_api(self):

        blocks = self.matchs['data']['blocks']
        for index_events in range(len(blocks)):
            name = blocks[index_events]['name']
            events = blocks[index_events]['events']
            for event in range(len(events)):  
                region_name = events[event]['regionName']
                region_id = events[event]['regionId']
                leagueDescription = events[event]['shortName']
                participants = events[event]['markets'][0]['selections']
                home_team = participants[0]['fullName']
                tie = participants[1]['fullName']
                away_team = participants[2]['fullName']

                print(name,region_name, region_id,leagueDescription,participants,home_team,tie,away_team)

                self.dic_jogos_betano['name'].append(name)
                self.dic_jogos_betano['region_name'].append(region_name)
                self.dic_jogos_betano['region_id'].append(region_id)
                self.dic_jogos_betano['leagueDescription'].append(leagueDescription)
                self.dic_jogos_betano['home_team'].append(home_team)
                self.dic_jogos_betano['tie'].append(tie)
                self.dic_jogos_betano['away_team'].append(away_team)


                

    def export_data(self):

        df = pd.DataFrame(self.dic_jogos_betano) ##transformando dicionario em dataframe##
        df.to_csv(os.path.join(self.files,'test.csv'),encoding='utf-16', sep=';', index=False)
                

Betano = ApiBetano()
Betano.request_api()
Betano.read_json()
Betano.data_api()
Betano.export_data()
