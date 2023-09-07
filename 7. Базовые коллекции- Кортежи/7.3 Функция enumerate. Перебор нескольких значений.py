#Задача 1. Саботаж!

#str = input('Строка: ')
#for index, value in enumerate(str):
#    if value == '~':
#        print(index, end=' ')

#Задача 2. Словари из списков

#import random
#import string
#first_list = [random.choice(string.ascii_lowercase) for i in range(10)]
#second_list = [random.choice(string.ascii_lowercase) for i in range(10)]
#print('Первый список:', first_list)
#print('Второй список:', second_list)
#res_first = {}
#res_second = {}
#for index, value in enumerate(first_list):
#    res_first[index] = value
#for index, value in enumerate(second_list):
#    res_second[index] = value
#print()
#print('Первый словарь:', res_first)
#print('Второй словарь:', res_second)

#Задача 3. Универсальная программа

def return_even_elements(data):
    res = []
    if isinstance(data, dict):
        data = data.values()
    for index, value in enumerate(data):
        if index % 2 == 0:
            res.append(value)
    return res


#print(return_even_elements('О Дивный Новый мир!'))
print(return_even_elements([100, 200, 300, 'буква', 0, 2, 'а']))
#print(return_even_elements({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))

