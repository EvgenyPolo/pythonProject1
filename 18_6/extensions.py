from config import money
import requests
import json


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        # проверяем валюты на идентичность
        try:
            if quote == base:
                raise APIException(f'Невозможно конвертировать одинаковые валюты {base}.')
        except APIException as e:
            return e
        # достаем из словаря валют код валюты выдачи
        try:
            quote_code = money[quote]
        except KeyError:
            return f'Ошибка обработки валюты: {quote}'
        # достаем из словаря валют код базовой валюты
        try:
            base_code = money[base]
        except KeyError:
            return f'Ошибка обработки валюты: {base}'
        # преобразовываем количество из текста в число
        try:
            amount = float(amount)
        except ValueError:
            return f'Ошибка обработки количества: {amount}'
        # запрашиваем информацию с сервера и обрабатываем ответ
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_code}'
                             f'&tsyms={quote_code}')
            total_base = json.loads(r.content)[quote_code] * amount
        # обработка возможных ошибок при запросе и обработке данных
        except:
            total_base = "Ошибка обработки данных."

        return total_base
