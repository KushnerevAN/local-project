# Задача 1. Список чётных чисел

#a = int(input('Введите число А: '))
#b = int(input('Введите число В: '))
#list = [i for i in range(a, b + 1 ) if i % 2 == 0]
#print(list)

#Задача 2. Магазин

#original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#new_prices = [(0 if i < 0 else i) for i in original_prices ]
#print(new_prices)

#Задача 3. Отряды

import random
crew_1 = [random.randint(50, 80) for i in range(10)]
crew_2 = [random.randint(30, 60) for i in range(10)]
crew_3 = ['Погиб' if crew_1[i] + crew_2[i] > 100
          else 'Выжил'
          for i in range(10)]
print('Урон первого отряда:', crew_1)
print('Урон первого отряда:', crew_2)
print('Состояние третьего отряда:', crew_3)