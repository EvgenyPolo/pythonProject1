from config import token, money
from extensions import APIException, CryptoConverter
import telebot

bot = telebot.TeleBot(token)


# обработка команд /start и /help
@bot.message_handler(commands=['start', 'help', 'h'])
def echo_test(message: telebot.types.Message):
    text = '''Чтобы конвертировать введите команду боту в формате:\n  "Какая валюта"  \
"в какой валюте"  "количество первой"\nНапример: \nдоллар рубль 10  => Получите \
цену 10 долларов в рублях\n\nПосмотреть это сообщение: /start или /help \nСписок \
доступных валют: /values '''

    bot.reply_to(message, text)


# выводим доступные валюты
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in money.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


# обрабатываем запрос из сообщения
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    # преобразуем текст сообщения в список параметров
    list_values = message.text.split(' ')

    try:
        if len(list_values) != 3:
            # поднимаем ошибку по кол. параметров
            raise APIException('Введите команду или запрос.')
    # обрабатываем ошибку
    except APIException as e:
        # ответ по ошибке
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
        return
    # заполняем параметры
    base, quote, amount = list_values
    # проверяем и конвертируем
    total_base = CryptoConverter.get_price(base, quote, amount)

    # разбираем результат работы CryptoConverter
    if 'float' in str(type(total_base)):
        # результат конвертации:
        text = f'Цена {amount} {base} = {round(total_base, 2)} {quote}'
    else:
        # фиксация ошибки
        text = total_base

    # ответ на запрос или ошибке
    bot.reply_to(message, text)


bot.polling(none_stop=True)
