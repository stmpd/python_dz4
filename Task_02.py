
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#Простые делители числа
#in
#54
#out
#[2, 3, 3, 3]
#in
#9990
#out
#[2, 3, 3, 3, 5, 37]
#in
#650
#out
#[2, 5, 5, 13]



def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def multiplier(number):
    if is_prime_number(number):
        return 'Простое число'

    multi = 2
    list = []
    while number != 1:
        if is_prime_number(multi) and number % multi == 0:
            number /= multi
            list.append(multi)
        else:
            multi += 1

    return list


num = int(input('Введите число: '))
print(multiplier(num))