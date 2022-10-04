
#Задайте последовательность чисел. Напишите программу,
#которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
#in
#7
#out
#[4, 5, 3, 3, 4, 1, 2]
#[5, 1, 2]
#in
#-1
#out
#Negative value of the number of numbers!
#[]
#in
#10
#out
#[4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#[6, 2, 3, 0, 9]


from random import randrange
from collections import Counter


def random_lst(number):
    list = []
    if number < 0:
        return list

    for i in range(number):
        list.append(randrange(0, number // 2))
    print(list)
    return list


def uni_val(values):
    cnt = Counter(values)
    list = []
    for val in values:
        if cnt.get(val) == 1:
            list.append(val)
    return list

def negative(number):
    if number < 0:
        return("Negative value of the number of numbers!")
    return uni_val(random_lst(number))


n = int(input('Введите число: '))

print(negative(n))