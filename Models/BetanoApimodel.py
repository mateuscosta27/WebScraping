import requests
import json
import os


with open("./Data/Startup.json") as directory_files:
    DataFut = json.load(directory_files)
    files = DataFut['Files']


url = "https://br.betano.com/api/sport/futebol/jogos-de-hoje/?sort=Leagues&req=la,s,tn,stnf,c,mb"
response = requests.get(url)
data = response.json()
with open(os.path.join(files,"data.json"), "w") as outfile:
    json.dump(data, outfile)   

with open(os.path.join(files,'data.json')) as StringFiles:
    DataPartidas = json.load(StringFiles)
    matchs = DataPartidas

blocks = matchs['data']['blocks']


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

        print(home_team,tie, away_team)