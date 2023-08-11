#Задача 1. Кубы и квадраты

#left = int(input('Левая граница: '))
#reith = int(input('Правая граница: '))

#left_list = [i_left ** 3 for i_left in range(left, reith + 1)]
#reith_list = [i_reiht ** 2 for i_reiht in range(left, reith + 1)]

#print('Список кубов чисел в диапазоне от', left, 'до', reith, ':', left_list)
#print('Список квадратов чисел в диапазоне от', left, 'до', reith, ':', reith_list)

#Задача 2. Сообщение

#line = input('Введите строку: ')
#sym = input('Введите дополнительный символ: ')
#line_list = [i_line + i_line for i_line in line]
#sym_list = [i_line + sym for i_line in line_list]
#print('Список удвоенных символов: ', line_list)
#print('Склейка с дополнительным символом: ', sym_list)

#Задача 3. Повышение цен

prices_list = [float(input('Введите цену: ')) for i in range(5)]
raise_first = int(input('Повышение на первый год: '))
raise_second = int(input('Повышение на второй год: '))
raise_first_list = [round(i_first * (1 + raise_first/100), 2) for i_first in prices_list]
raise_second_list = [round(i_second * (1 + raise_second/100), 2) for i_second in raise_first_list]
print('Сумма цен за каждый год: ', round(sum(prices_list), 2), round(sum(raise_first_list), 2), round(sum(raise_second_list), 2))

