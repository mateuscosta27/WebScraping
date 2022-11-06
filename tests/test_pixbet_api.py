from urllib import request

cookies = {
    'PHPSESSID': '22k3mdhpap3rmiqu27klmpu4o4',
    '_ga_WEBN9SL7PJ': 'GS1.1.1667777441.1.0.1667777441.0.0.0',
    '_ga': 'GA1.1.1286014255.1667777442',
    '__cf_bm': 'Ifng5pQY9PhlRQtjt37nMGOdoTbtFYENO0Y5ICKPwLI-1667777442-0-AU7NT2Y6bEbuULfV/JM3ysxN2+rVwQ1lrNOd5c3+ZpuqhdKpv03rHFMiVyC7WFtv46QtDf37egak5eFCkLmwU8m++frb3wJG4QOSTxi45+lPIk58bTNZYs/zYjizxnJupUsonwiLUrQv58qxGmsLEkeOxPXUssNc+FE1yWL1WWRU',
}

headers = {
    'authority': 'pixbet.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=22k3mdhpap3rmiqu27klmpu4o4; _ga_WEBN9SL7PJ=GS1.1.1667777441.1.0.1667777441.0.0.0; _ga=GA1.1.1286014255.1667777442; __cf_bm=Ifng5pQY9PhlRQtjt37nMGOdoTbtFYENO0Y5ICKPwLI-1667777442-0-AU7NT2Y6bEbuULfV/JM3ysxN2+rVwQ1lrNOd5c3+ZpuqhdKpv03rHFMiVyC7WFtv46QtDf37egak5eFCkLmwU8m++frb3wJG4QOSTxi45+lPIk58bTNZYs/zYjizxnJupUsonwiLUrQv58qxGmsLEkeOxPXUssNc+FE1yWL1WWRU',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

response = request.urlopen('https://pixbet.com/prejogo/')



print(response)