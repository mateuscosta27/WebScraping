import requests

cookies = {
    '_ga': 'GA1.1.1160083581.1661427204',
    'PHPSESSID': 'pn1ngs43ig1t72aidj9hva8f93',
    '__cf_bm': '7VgB41yS.V0LoiB41XjQ8deq7vMVFegJ3sU5g24el5M-1667509359-0-AarNlPCPLT8lezblgIlxmMZ836XFeK9a2Mio18vje6JyChFJ0gqpnyqWg1yR0lAJOjuKycotaF0f/13X0N6r1VybWPiP6i8EQIzmvKcDg56gsx51Pwj422+5B2YZKopbr6ZARAxoKM3VYP535tjt9op2K6Y5hdfGBsstKFG3rCS1',
    '_ga_WEBN9SL7PJ': 'GS1.1.1667509358.5.1.1667509750.0.0.0',
}

headers = {
    'authority': 'pixbet.com',
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.1.1160083581.1661427204; PHPSESSID=pn1ngs43ig1t72aidj9hva8f93; __cf_bm=7VgB41yS.V0LoiB41XjQ8deq7vMVFegJ3sU5g24el5M-1667509359-0-AarNlPCPLT8lezblgIlxmMZ836XFeK9a2Mio18vje6JyChFJ0gqpnyqWg1yR0lAJOjuKycotaF0f/13X0N6r1VybWPiP6i8EQIzmvKcDg56gsx51Pwj422+5B2YZKopbr6ZARAxoKM3VYP535tjt9op2K6Y5hdfGBsstKFG3rCS1; _ga_WEBN9SL7PJ=GS1.1.1667509358.5.1.1667509750.0.0.0',
    'referer': 'https://pixbet.com/prejogo/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'action': 'get_odds',
    'json': '1',
    'lid': '2417',
    'append': '1',
}

response = requests.get('https://pixbet.com/modules/sports/ajax.php', params=params, cookies=cookies, headers=headers)

print(response.content)