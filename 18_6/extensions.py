from config import money
import requests
import json


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        err_user = f'Ошибка пользователя.\n'
        # проверяем валюты на идентичность
        try:
            if quote == base:
                raise APIException(f'Не конвертирую одинаковые валюты {base}.')
        except APIException as e:
            return err_user + str(e)
        # достаем из словаря валют код валюты выдачи
        try:
            quote_code = money[quote]
        except KeyError:
            return err_user + f'Не нашел валюту: {quote}'
        # достаем из словаря валют код базовой валюты
        try:
            base_code = money[base]
        except KeyError:
            return err_user + f'Не нашел валюту: {base}'
        # преобразовываем количество из текста в число
        try:
            amount = float(amount)
        except ValueError:
            return err_user + f'Вводите количество правильно. {amount} - это число?'
        # запрашиваем информацию с сервера и обрабатываем ответ
        try:
            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_code}'
                             f'&tsyms={quote_code}')
            total_base = json.loads(r.content)[quote_code] * amount
        # обработка возможных ошибок при запросе и обработке данных
        except Exception:
            total_base = "Ошибка обработки данных.\n Что-то с сервером или данными"

        return total_base
