print('Укажите имя персонажа:')
name = input()
print('Здравствуйте', name, 'вы очнулись в комнате.')
print('Вам нужно сбежать из этой заброшенной тюрьмы, выберите в какую дверь пойдете')
print('Введите целое число: 1 2 или 3?')
door = int(input())
while door != 1 and door != 2 and door != 3:
    door = int(input('Вы ввели некорректный номер!:'))
else:
    print('Вы выбрали', door, 'дверь')
    if door == 1:
        print('Оглянувшись, вы увидели собаку ваши действия:')
        print('1. Попробывать убежать')
        print('2. Попробывать погладить')
        do = int(input())
        while do != 1:
            print('''Собака вас бы укусила,выберете другой вариант.
            1. Попробывать убежать 
            2. Попробывать погладить''')
            do = int(input())
        else:
            print('Собака вас не увидела, пробежавшись по коридору, вы вышли из тюрьмы')
    elif door == 2:
        print('Развилка, куда вы пойдете? 1.Налево или 2.Направо')
        fork = int(input())
        while fork != 2:
            print('''Двери бы за вами захлопнулись, выберите другой вариант 
            1. Налево 
            2. Направо''')
            fork = int(input())
        else:
            print('Вы нашли телефон, позвонив в полицию,', name, ', вас нашли')
    elif door == 3:
        print('Вы увидели человека, это был охраник, ваши действия?')
        print('1. Просто пройти мимо')
        print('2. Узнать дорогу из тюрьмы')
        road = int(input())
        while road != 2:
            print('''Вы бы потерялись в лабиринте, выберите другой вариант 
            1. Просто пройти мимо 
            2. Узнать дорогу''')
            road = int(input())
        else:
            print('Охраник, помог вам выйти из тюрьмы, поздравляю!')