from config import token, money
from extensions import APIException, CryptoConverter
import telebot

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help', 'h'])# обработка команд /start и /help
def echo_test(message: telebot.types.Message):
    text = '''Чтобы конвертировать введите команду боту в формате:\n  "Какая валюта"  \
"в какой валюте"  "количество первой"\nНапример: \nдоллар рубль 10  => Получите \
цену 10 долларов в рублях\n\nПосмотреть это сообщение: /start или /help \nСписок \
доступных валют: /values '''

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])# выводим доступные валюты
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in money.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])# обрабатываем запрос из сообщения
def convert(message: telebot.types.Message):
    values = message.text.split(' ')# преобразуем текст сообщения в параметры

    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров.')# поднимаем ошибку по кол. параметров
    except APIException as e:# обрабатываем ошибку
        print(e)# копия в консольку
        bot.reply_to(message, e)# ответ по ошибке
        return
    base, quote, amount = values# заполняем параметры

    total_base = CryptoConverter.get_price(base, quote, amount)# проверяем и конвертируем


    if 'float' in str(type(total_base)):# разбираем результат работы CryptoConverter
        text = f'Цена {amount} {base} = {round(total_base, 2)} {quote}'# результат конвертации
    else:
        text = total_base# фиксация ошибки

    print(text)# копия в консольку
    bot.reply_to(message, text)# ответ на запрос или ошибке
    # bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
