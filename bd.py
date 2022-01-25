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
