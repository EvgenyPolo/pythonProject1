F = open("test.txt", 'w')
F.write('Однажды в студеную зимнюю пору')
F.close()

F = open("test.txt", 'a')
F.write("\nЯ из лесу вышел. Был сильный мороз!")
F.close()

F = open("test.txt", 'r')
#print(F.readlines())
print(F.read(7))
print(F.read())
F.close()

F = open("test.txt", 'rt', encoding="cp1251")
print(F.readlines())
F.close()

import time
F = open("D:\Tests\songs.txt", 'rt', encoding="utf8")
for str in F:
    print(str, end="")
    # time.sleep(1)
F.close()

F = open("D:\Tests\songs.txt", 'rt', encoding="utf8")

print(F.read())
F.close()

with open("D:\Tests\songs.txt", 'rt', encoding="utf8") as F:
    for str in F:
        print(str, end="")

def caesars_cipher(number, infile, outfile):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    summary = ''

    def changeChar(char):
        if char in alpha:
            return alpha[(alpha.index(char) + number) % len(alpha)]
        elif char in alphaUp:
            return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
        else:
            return char

    with open(infile, encoding="utf8") as myFile:
        for line in myFile:
            for char in line:
                summary += changeChar(char)

    with open(outfile, 'w', encoding="utf8") as myFile:
        myFile.write(summary)

caesars_cipher(5,"D:\Tests\songs.txt","D:\Tests\songs5.txt")

with open("D:\Tests\songs5.txt", encoding="utf8") as myFile:
    for line in myFile:
        print(line, end="")

import os

print(os.path.join('..', 'test', 'filename.txt'))

# Лабиринт
# global pozOut, pozIn
def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1

                        # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1

                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1

                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1

                    # Конечная точка
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight + 1
                        return True
        weight += 1
    return False


def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            result[weight] = 'Вниз'
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'Вверх'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'Вправо'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'Влево'
            x += 1

    return result[1:]


labirint = []
# print(os.listdir('..'))
with open(os.path.join('..', "labirint.txt")) as myFile:
    for line in myFile:
        labirint.append(line.replace('\n', '').split(' '))
        # print(labirint)

ii = 0
for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            pozIn = (ii, jj)
        elif j == 'B':
            labirint[ii][jj] = 0
            pozOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
        jj += 1
    ii += 1

if not found(labirint, pozOut):
    print("Путь не найден!")
else:
    result = printPath(labirint, pozOut)

    for i in labirint:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()
    print(result)
