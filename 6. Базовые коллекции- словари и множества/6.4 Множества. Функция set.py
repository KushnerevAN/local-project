#Задача 1. Пунктуация

#signs = {'.',',',';',':','!','?'}
#str = input('Введите строку: ')
#str_set = set(str)
#print('Количество знаков пунктуации:', len(signs & str_set))

#Задача 2. Семинар
#import random
#nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
#nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
#set_nums_1 = set(nums_1)
#set_nums_2 = set(nums_2)
#set_nums_1_min = min(set_nums_1)
#set_nums_2_min = min(set_nums_2)
#set_nums_1.remove(set_nums_1_min)
#set_nums_2.remove(set_nums_2_min)
#random_num_1 = (random.randint(100, 200))
#set_nums_1.add(random_num_1)
#random_num_2 = (random.randint(100, 200))
#set_nums_2.add(random_num_2)
#print('Минимальный элемент 1-го множества:', set_nums_1_min)
#print('Минимальный элемент 1-го множества:', set_nums_2_min)
#print()
#print('Случайное число для 1-го множества:', random_num_1)
#print('Случайное число для 2-го множества:', random_num_2)
#print()
#print('Объединение множеств:', set_nums_1.union(set_nums_2))
#print('Пересечение множеств:', set_nums_1.intersection(set_nums_2))
#print('Элементы, входящие в nums_2, но не входящие в nums_1:', set_nums_2.difference(set_nums_1))

#Задача 3. Различные цифры

text_str = input('Введите строку: ')
result = {i for i in text_str if '0' <= i <= '9'}
print('Различные цифры строки:', ''.join(result))

