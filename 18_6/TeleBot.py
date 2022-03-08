from config import token, money
from extensions import APIException, CryptoConverter
import telebot

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help', 'h'])
def echo_test(message: telebot.types.Message):
    text = '''Чтобы конвертировать введите команду боту в формате:\n  "Какая валюта"  \
"в какой валюте"  "количество первой"\nНапример: \nдоллар рубль 10  => Получите \
цену 10 долларов в рублях\n\nПосмотреть это сообщение: /start или /help \nСписок \
доступных валют: /values '''

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in money.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров.')
    except APIException as e:
        print(e)
        bot.reply_to(message, e)
        return
    base, quote, amount = values

    total_base = CryptoConverter.get_price(base, quote, amount)

    if 'float' in str(type(total_base)):
        text = f'Цена {amount} {base} = {round(total_base, 2)} {quote}'
    else:
        text = total_base

    print(text)
    bot.reply_to(message, text)
    # bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
