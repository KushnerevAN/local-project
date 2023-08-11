#Задача 1. Анализ цен

#import random
#original_prices = [random.randint(-100, 100) for _ in range(5)]
#new_prices = original_prices[:]
#new_prices = [0 if i < 0 else i for i in new_prices ]
#print(original_prices)
#print(new_prices)
#print("Мы потеряли: ", sum(new_prices) - sum(original_prices))

#Задача 2. Срезы

#nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#print('Резульататы:')
#print(nums[:5])
#print(nums[:-2])
#print(nums[::2])
#print(nums[1::2])
#print(nums[::-1])
#print(nums[::-2])

#Задача 3. Удаление части

import random
numbers = int(input('Количество чисел: '))
number_list = [random.randint(1,30) for i in range(numbers)]
a = (random.randint(0,len(number_list) - 2))
b = (random.randint(a + 1,len(number_list) - 1))
print(number_list)
print(a,b)
number_list = number_list[0:a] + number_list[b + 1:]

print(number_list)

