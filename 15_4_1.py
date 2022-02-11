"""
Функция принимает строку с текстом.
Убирает все знаки препинания и возвращает
список, состоящий из слов текста.
"""

def changeText(text):
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')

    return text.split()

"""
Функция принимает список и ограничение по длине.
Возвращает самый часто встречающийся элемент.
Если есть несколько элементов с одинаковой самой большой частотой, 
то вернёт их все."""
def mostCommon(text, lenght=0):
    most_common = []
    qty_most_common = 0

    for item in text:
        if len(item) > lenght:
            qty = text.count(item) #определить количество слов item в тексте
            # print(qty)
            if qty > qty_most_common and qty > 2:
                qty_most_common = qty
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)

    most_common = list(set(most_common))
    most_common.append(qty)
    most_common.append('раз')
    return most_common

"""
Функция принимает список.
Возвращает самый длинный элемент и на 1 короче.
Если есть несколько элементов с одинаковой самой большой длиной
или на 1 короче, то вернёт их все.
"""
def mostLenght(text):
    most_lenght = []
    qty_most_lenght = 0
    charEn = False
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for char in item:
            if char not in alphabet:
                charEn = False
            else:
                charEn = True

        if charEn:
            qty = len(item)
            if qty > qty_most_lenght:
                qty_most_lenght = qty
                most_lenght = [item]
            elif qty == qty_most_lenght:
                most_lenght.append(item)
            elif qty == qty_most_lenght - 1:
                if item not in most_lenght:
                    # print('-1 in', most_lenght)
                    most_lenght.append(item)

    return list(set(most_lenght))

import os
nameFile = input('Введите название файла: ')
# print(os.path.join('..', nameFile))

with open(os.path.join('..', nameFile), encoding='utf8') as f:
    fileText = f.read()

fileText = changeText(fileText)
print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
print(f'Список самых длинных английских слов: {mostLenght(fileText)}')
