import requests
import json
from time import sleep

from .API import api_key
from .utilits import make_log, http_status_descriptions

def make_request(data: dict):
    url = 'https://chat.fifty.su/api/v1/chat'
    headers = {
        'x-api-key': api_key
    }
    make_log('Начинаю запрос')
    try:
        responce = requests.post(url=url, headers=headers, data=data)
        status_code = responce.status_code
        make_log(f'Выполнен запрос по ссылке {url}. Код: {status_code}')
        make_log(f'{status_code} - {http_status_descriptions.get(status_code, 'Описание не найдено')}')
        if status_code >= 400:
            print(f'{http_status_descriptions.get(status_code, 'Описание не найдено')}')
            return

    except Exception as e:
        print(f'Произошла непредвиденная ошибка при запросе.')
        print(f'Текст ошибки: {e}')
        make_log(f'Произошла непредвиденная ошибка при запросе')
        make_log(f'Текст ошибки: {e}')

    answer = responce.json()
    if len(answer) == 1: print('Возникла непредвиденная ошибка!')
    else: print(answer)
