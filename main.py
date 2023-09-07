line = 'abcd'
tuple_list = (10, 20, 30, 40)
print('Строка:', line)
print('Кортеж чисел:', tuple_list)
res = ((line[i], tuple_list[i]) for i in range(min(len(line), len(tuple_list))))
print('Результат:')
for i in res:
    print(i)















