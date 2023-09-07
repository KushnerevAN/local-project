#Задача 1. Создание кортежей

#tuple_1 = (0, 2, 4, 5, 1, 3, 0, 2, 4, 0)
#tuple_2 = (-5, -3, -1, 0, -2, -4, 0, -3, -5, 0)
#tuple_1 += tuple_2
#print(tuple_1)
#print(tuple_1.count(0))

#Задача 2. Цилиндр
#import math
#def calculation(r,h):
#    side = (2 * math.pi) * r * h
#    s = math.pi * (r ** 2)
#    full = side + (2 * s)
#    return side, full

#radius = float(input('Введите радиус: '))
#height = float(input('Введите высоту: '))
#side, full = calculation(radius,height)
#print(round(side, 2), round(full, 2))

#Задача 3. Неправильный код

import random

def change(nums):
    nums_list = list(nums)
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    nums_list[index] = value
    return nums_list, value
sum_nums = 0
my_nums = (1, 2, 3, 4, 5)
nums_list, value = change(my_nums)
print(nums_list, value)
sum_nums += value
num_list, value = change(nums_list)
sum_nums += value
print(num_list, sum_nums)



