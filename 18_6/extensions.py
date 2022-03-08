from config import money
import requests
import json


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        # total_base = None
        try:
            if quote == base:
                raise APIException(f'Невозможно конвертировать одинаковые валюты {base}.')
        except APIException as e:
            return e
        try:
            quote_code = money[quote]
        except KeyError:
            return f'Ошибка обработки валюты: {quote}'
        try:
            base_code = money[base]
        except KeyError:
            return f'Ошибка обработки валюты: {base}'
        try:
            amount = float(amount)
        except ValueError:
            return f'Ошибка обработки количества: {amount}'
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_code}'
                             f'&tsyms={quote_code}')
            total_base = json.loads(r.content)[quote_code] * amount
        except:
            total_base = "Ошибка обработки данных."

        return total_base

