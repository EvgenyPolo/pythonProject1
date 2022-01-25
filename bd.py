print('\n')
company_name = 'SkillFactory'
for letter in company_name: 
    letter = letter.upper()
    print(f'* {letter} *', end='')

items = [1, 5, 76, 12, 123, 333, 5, 6, 7]
ok_items = []

print('\n\n')

for item in items:
    print('Груз весит ', item, ' килограмм')
    if item <= 100:
        ok_items.append(item) 
        print('Груз прошел проверку')
    else:
        print('Груз слишком большой')
print('\n', ok_items, "\n\n\n")


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Тула', 'Россия']},
    {'visit7': ['Курск', 'Россия']},
    {'visit8': ['Архангельск', 'Россия']}
]
result = []

for log in geo_logs:
    # print(list(log.values())[0])
    if 'Россия' in list(log.values())[0]:
        result.append(log);
        print(list(log.values())[0])


print('\n', result, '\n\n')

first_name = "Имя"#input("Введите ваше имя:")
last_name = "Фамилия"#input("Введите вашу фамилию:")
age = "54"#input("Введите ваш возраст:")
city = "Новосиб"#input("Введите город проживания:")
print("\n","Привет,", first_name, last_name, "!",'\n')
print("Ваш профиль:")

# Выводим возраст и город, которые указал пользователь
print("Возраст:", age, "\nГород:", city)
a = 3.14
b = '3.14'

print(type(a))
# <class 'float'>
print(type(b))
# <class 'str'>

s = "python"
print(s[0])
# p
print(s[1:4])
# yth
print(3 > 10)
# False

print(3 < 10)
# True

print(3 == 10) # равны ли объекты?
# False

print('r' in 'world') # проверяем отдельный символ
# True

print('th' in 'python') # проверяем целую подстроку
# True

print('the' in 'python')
# False

print(1.57*3/1.5 == 3.14)
# True

date = (1, 'january', 2022)
print(date)
print(date[0])
# 1
print(date[1])
# january
print(date[2])
# 2022

s1 = "foo"
print(id(s1), s1) #проверяем идентификатор
# 2653889525232, foo

t = (0,1,2)
#t[1]  =  1
print(t[1])

print(1 // 3)
# 0
print(3 // 3)
# 1
print(29 // 3)
# 9

print(1 % 3) # ближайшее число, которое нацело делится на 3 - это ноль
# 1
print(3 % 3) # в этом примере сам делитель может нацело разделиться
# 0
print(29 % 3) # здесь ближайшее число - 27, и поэтому результат 29-27=2
# 2

a = 5
b = 2
q = a // b # q = 2
r = a % b  # r = 1
print(a, b, q, r, b*q+r) # a = b*q+r

a = -5
b = 2
q = a // b # хочется получить 2, как и в прошлый раз, но q = -3
r = a % b # а остаток остался тот же r = 1
#Дело в том, что максимальное число, которое можно нацело разделить на число при условии, что остаток будет положительным — это -6. При его делении на 2 получаем -3 и соответствующий остаток, равный 1.
print(a, b, q, r, b*q+r) # a = b*q+r

total_seconds = 119
seconds = total_seconds % 60
minutes = total_seconds // 60
print(f'{minutes}:{seconds}')  # 1:59

print (13 % -3 * 3 - 3**2)
print (13 % -3, 13//-3)
print (13 % -3 * 3)

a, b = [10, -10], [3, -3]
for x in a:
  for y in b:
    print(f'{x} // {y} = {x // y}')
    print(f'{x} % {y} = {x % y}')
    print()

"""def mod_python(a, b):
  return int(a - math.floor(a / b) * b)
# на С++ работает так:
def mod_cpp(a, b):
  return int(a - math.trunc(a / b) * b)
"""

print(int(2.8)) # ожидается 3, т.к. 2.8>2.5 но будет
# 2
print(int(3.14))
# 3
print(float(1))
# 1.0

print(1.00+0.01-3.01) # ожидается -2.0
# -1.9999999999999998 # значит целое от этого выражения будет -1
print(int(1.00+0.01-3.01))
# -1
print(round(1.00+0.01-3.01))
# -2
print(3.14/2)
# 1.57
print(round(3.14/2, 1)) # второй аргумент - желаемое количество знаков
# 1.6

pi=3.14159
print(round(pi**2/2, 1))


s = "Hello!"    # [начало:конец:шаг], конец — индекс символа, следующего сразу после подстроки
print(s[0])
# H
print(s[4])
# o
print(s[1:4])
# ell
print(s[2:])
# llo!
print(s[:4])
# Hell
print(s[::2])
# Hlo
print(s[::-1])
# !olleH    Отрицательный шаг позволяет развернуть строку
print(s[-1])
# !     Отрицательным может быть не только шаг, но и сам индекс.
print(s[-3:-1])
# lo    Отрицательные индексы нумеруются от последнего символа к первому:

print(len(s))
# 6     Встроенная функция len() позволяет узнать длину строки

print(s.find('e')) # возвращает индекс
# 1     Метод find(substr), определённый для строк, позволяет находить символы и подстроки
print(s.find('o!')) # в случае подстроки возвращает индекс первого символа
# 4
print(s.find('l')) # встречается в индексах 2 и 3
# 2     Если символ или подстрока встречаются несколько раз, то возвращается индекс первого вхождения

print(s.isdigit()) # строка состоит из цифр?
# False

print(s.isalpha()) # строка состоит из букв?
# False

print(s.isalnum()) # строка состоит из цифр и букв?
# False


print(s.upper())
# HELLO!

print(s.lower())
# hello!

print(s)
# Hello!        Обратите внимание, что исходная строка не изменяется


colors = 'red blue green'
print(colors.split())   # Результат работы этого метода — список строк.
# ['red', 'blue', 'green']
path = '/home/user/documents/file.txt'
print(path.split('/')) # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']


colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности
# метод join(). Применяется (через точку, как и все методы) к символу (строке)-разделителю,
# а в аргумент метода помещается список строк
colors_joined = ' разделитель '.join(colors_split) # объединение строк, которые нужно объединить.
print(colors_joined)
# red разделитель green разделитель blue


str0 = "12 15 17"  #input ("Введите числа через пробел:")
str_split = str0.split()
str_joined = '\n'.join(str_split)
print(str_joined)


int_num = 256 # int(input("Введите целое число: ")) # вводим, например, 256
print(int_num)
# 256
print(type(int_num)) # убеждаемся, что тип данных в переменной - int
# <class 'int'>

age = 25
my_age = "I'm " + str(age)
print(my_age)
# I'm 25

wow = 'ypa!'
print(wow*5) # никакой ошибки не возникает
# ypa!ypa!ypa!ypa!ypa!

age = 54
my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
print(my_age)
# I'm 54 years old

pi = 31.4159265
print ("%.4e" % (pi))


day = 14
month = 2
year = 2012

print("%d.%02d.%d" % (day, month, year))
# 14.02.2012
print("%d-%02d-%d" % (year, month, day))
# 2012-02-14
print("%d/%d/%d" % (year, day, month))
# 2012/14/2


# допустим, у нас есть список, содержащий первые 4 буквы латинского алфавита
letters = ['a', 'b', 'c', 'd']
# Метод — это функция, которая применяется к определённому объекту, используя символ точку:
# объект.метод()
# с помощью метода append() мы добавляем ещё один элемент в список
letters.append('e')

print(letters)
# ['a', 'b', 'c', 'd', 'e']
print(letters[1])
# b
print(letters[len(letters)-1])
# e
letters.append('f') # добавляем ещё одну букву
letters.append('g') # и ещё одну
print(letters[len(letters)-1])
# g
print(letters[-1])
# g
print(letters[-4])
# d
print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters.pop() # вызов метода без аргументов удаляет последний элемент списка

print(letters)
# ['a', 'b', 'c', 'd', 'e', 'f']
# был удалён последний элемент

letters.pop(0) # или можно удалить элемент по его индексу

print(letters)
# ['b', 'c', 'd', 'e', 'f']
# был удалён нулевой элемент

letters.pop(3) # и не обязательно удалять из начала или конца списка

print(letters)
# ['b', 'c', 'd', 'f']
# был удалён элемент с индексом 3


L = ["а", "б", "в", 1, 2, 3, 4]
print (L[ -4::-1 ])
print (L[ 3::-1 ])


# имеем список с числами с плавающей точкой
L = [3.3, 4.4, 5.5, 6.6]

# печатаем сам объект map
print(map(round, L)) # к каждому элементу применяем функцию округления
# <map object at 0x7fd7e86eb6a0>

# и результат его преобразования в список
print(list(map(round, L)))
# [3, 4, 6, 7]
print (list (map ( float , L)))


#string = input("Введите числа через пробел:")
string = "1 1 2 3 5 8 13 21 34 55"
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

"""
map(function, list)
Первый аргумент map() — функция, которую нужно применить к каждому элементу списка, 
а сам список — второй аргумент. Возвращаемое значение этой функции — объект map, 
который можно преобразовать, например, обратно в список."""

str0 = "12 15 17 25"  #input ("Введите числа через пробел:")
str_split = str0.split()
a = str_split[0]
str_split[0] = str_split[-1]
str_split[len(str_split)-1] = a
list_of_numbers = list(map(int, str_split)) # список чисел
list_of_numbers.append(sum(list_of_numbers[::])) # добавляем сумму чисел в конец
print(list_of_numbers[len(list_of_numbers)-1])  # вывод суммы
print(list_of_numbers)

#**************************************************************************************
# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
#L = list(map(float, input().split()))
#L = list(map(float, '12 15 17 25'.split()))
L = list(map(float, '1 1 2 3 5 8 13 21 34 55'.split()))

# обмениваем первое и последнее число
# с помощью множественного присваивания
L[0], L[-1] = L[-1], L[0]

# находим сумму и добавляем её в конец списка
L.append(sum(L))

print(L)


d = {'day' : 22, 'month' : 6, 'year' : 2015}
print("||".join(d.keys()))
# day||month||year

#********************************************************************
person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
print(person.keys())
# dict_keys(['name', 'age', 'email', 'phone'])

print(person.values())
# dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])
print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

person.pop('phone')

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}


Books = {}
Books['name_book'] = "Utro"     #input("Input book name:")
Books['author_book'] = "Иванов" #input("Input author name:")
Books['year_book'] = "2012"     #input("Input year of release book:")
print(Books)

"""А МОЖНО и ВОТ ТАК!
Books = {'name_book':input("Input book name:"),
         'author_book':input("Input author name:"),
         'year_book': input("Input year of release book:")}
print(Books)
"""


abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}

abits = [abit1, abit2, abit3] # список

print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True}, {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False}, {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}]
#Этот список, по мере поступления документов, можно пополнять:

abit4 = {"ФИО" : 'Любимчиков А.Я.', "Количество баллов" : 269, "Заявление" : True}

abits.append(abit4)

print(abits)
# [{'ФИО': 'Фадеев О.Е.', 'Количество баллов': 283, 'Заявление': True}, {'ФИО': 'Дружинин И.Я.', 'Количество баллов': 278, 'Заявление': False}, {'ФИО': 'Афанасьев Д.Н.', 'Количество баллов': 276, 'Заявление': True}, {'ФИО': 'Любимчиков А.Я.', 'Количество баллов': 269, 'Заявление': True}]


#Создать МНОЖЕСТВО можно несколькими способами:
a = {'a', 'b', 'c', 'd'} # используя синтаксис { }
#Или, что нам будет более полезно, множество можно создать из списка с помощью приведения типов:
L = [1,3,2,3,2]
b = set(L)
print(b)
# {1,2,3}
b_list = list(b)    #вернуть обратно в списковое представление
print(b_list)
# [1,2,3]
# ИЛИ
print(list(set(L)))


L = "Вася шел гулять на речку"
print("Уникальные символы:", list(set(L)))
print("Количество уникальных символов:" , len(list(set(L))))


abons = {"Иванов", "Петров", "Васильев", "Антонов"}
debtors = {"Петров", "Антонов", "Сидоров", "Козлов"}
print(abons.union(debtors))     # Объединение
# {'Антонов', 'Сидоров', 'Васильев', 'Иванов', 'Козлов', 'Петров'}
non_debtors = abons.difference(debtors)     # Возвращает множество элементов abons, которые не встречаются в debtors.
print(non_debtors)
# {'Иванов', 'Васильев'}
non_debtors = abons.symmetric_difference(debtors)   # Возвращает множество элементов,
print(non_debtors)          # встречающиеся в одном из множеств, но не в обоих одновременно.
# {'Васильев', 'Иванов', 'Сидоров', 'Козлов'}
print(abons.intersection(debtors))     # Пересечение
# {'Петров', 'Антонов'}


a = list(map(int, '1 1 2 3 5 8 13 212 34 55'.split()))
b = list(map(int, '1 11 2 32 5 8 13 21 34 55'.split()))
a_set, b_set = set(a), set(b) # используем множественное присваивание
a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)


L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

a = 1+4
b = 3+2
print(id(a), id(b), id(b)-id(a))        # ИДЕНТИЧНЫ


list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)       # ['a', 'b', 'c']
print(list_2)       # ['a', 'b', 'c']
print(list_3)       # ['a', 'b', 'c']
print(list_1 == list_2)     # True  проверяем равенство этих списков.
print(list_1 == list_3)     # True  РАВНЫ!
print(list_1 is list_2)     # True  проверяем идентичность этих списков.
print(list_1 is list_3)     # False
# list_1 и list_3 указывают на два разных объекта, даже если их содержимое может быть одинаковым.

L = ['Hello', 'world']
M = L
M.append('!')
print(L)
print(M is L)
# True

M = L.copy()
print(M is L)
# False
M.append('!')
print(L)
print(M)


shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])

shopping_center[-1].append("Uniqlo")

print(shopping_center)
# ('Галерея', 'Санкт-Петербург', 'Лиговский пр., 30', ['H&M', 'Zara', 'Uniqlo'])


shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print( list_id_before == list_id_after, list_id_before, list_id_after)


bodycount = {
    'Проклятие Черной жемчужины': {
        'человек': 17
    },

    'Сундук мертвеца': {
        'человек': 56,
        'раков-отшельников': 1
    },

    'На краю света': {
        'человек': 88
    },

    'На странных берегах': {
        'человек': 56,
        'русалок': 2,
        'ядовитых жаб': 3,
        'пиратов зомби': 2
    }
}

dead = 0
for info in bodycount.values():
    print(info)
    for name, count in info.items():
        print(name, count, dead);
        if name != 'ядовитых жаб':
            dead += count
    # dead += sum(info.values())

print(dead)


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'кратно 3 и 5')
    elif i % 5 == 0:
        print(i, 'кратно 5')
    elif i % 3 == 0:
        print(i, 'кратно 3')
    else:
        print(i)


"""dic1 = {'2' : "два", '3' : "три"}
dic1['5'] = "пять"
print(dic1)
for i in 1, 2, 3:
    key = input("Key:")
    value = input("Value:")
    if key in dic1:
        print("есть:", dic1[key])
    else:
        dic1[key] = value
        print("Новое:", dic1[key])
print (dic1)
"""


dic1 = {'2' : "два", '3' : "три"}
dic1['5'] = "пять"
print(dic1)

for key in dic1.keys():
    print(key)

for value in dic1.values():
    print(value)

for keyval in dic1.items():
    print(keyval)



