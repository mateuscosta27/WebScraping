import requests
from pandas import json_normalize

headers = {
    'authority': 'stats.fn.sportradar.com',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9',
    'origin': 'https://s5.sir.sportradar.com',
    'referer': 'https://s5.sir.sportradar.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

response = requests.get('https://stats.fn.sportradar.com/betano/br/America:Montevideo/gismo/stats_team_lastx/273669/30', headers=headers)



print(response.content)