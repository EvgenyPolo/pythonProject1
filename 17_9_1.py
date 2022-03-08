def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if left > right:  # если левая граница > правой, значит элемент отсутствует в списке
        return left - 1  # возвращаем индекс предыдущего элемента

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle - 1  # возвращаем индекс предыдущего элемента
    elif element < array[middle]:  # если элемент < элемента в середине, ищем слева
        return binary_search(array, element, left, middle - 1)
    else:  # иначе cправa
        return binary_search(array, element, middle + 1, right)


def input_int(inp):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for n in inp.split():
        if len(str(n)) > 1:
            for i in range(0, len(str(n))):
                if n[i] not in numbers:
                    print("Вводить можно только целые числа!")
                    return False
        else:
            if n not in numbers:
                print("Вводить можно только целые числа:", n)
                return False
    return inp


str_i = False
while not str_i:
    str_i = input_int(input('Введите последовательность чисел через пробел:'))

int_array = list(map(int, str_i.split()))
print(f'несорт. список: {int_array}')
qsort(int_array, 0, len(int_array) - 1)
print(f'  сорт. список: {int_array}')
number = False
while not number:
    number = int(input_int(input('Введите число:')))
    if number:
        if int_array[0] > number or int_array[len(int_array) - 1] < number:
            print(f"Число не попадает в заданный интервал[{int_array[0]}..{int_array[len(int_array) - 1]}]")
            number = False

print(f'Индекс числа, предыдущего введенному: {binary_search(int_array, number, 0, len(int_array) - 1)}')
