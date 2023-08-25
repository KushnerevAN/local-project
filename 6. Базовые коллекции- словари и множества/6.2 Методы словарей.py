#Задача 1. Склады

#small_storage = {
#    'гвозди': 5000,
#    'шурупы': 3040,
#    'саморезы': 2000
#}
#big_storage = {
#    'доски': 1000,
#    'балки': 150,
#    'рейки': 600
#}
#big_storage.update(small_storage)
#question = input('Введите название товара: ')
#print(big_storage.get(question))

#Задача 2. Кризис фруктов

#incomes = {
#    'apple': 5600.20,
#    'orange': 3500.45,
#    'banana': 5000.00,
#    'bergamot': 3700.56,
#    'durian': 5987.23,
#    'grapefruit': 300.40,
#    'peach': 10000.50,
#    'pear': 1020.00,
#    'persimmon': 310.00,
#}
#print('Искомый словарь:', incomes)
#print('Итоговый доход за год составил:', sum(incomes.values()), 'рублей.')

#print('Самый маленький доход у', (list(incomes.keys())[list(incomes.values()).index(min(incomes.values()))]),
#      '. Он составляет', min(incomes.values()), 'рублей.')

#incomes.pop((list(incomes.keys())[list(incomes.values()).index(min(incomes.values()))]))

#print('Итоговый словарь: ', incomes)

#Задача 3. Гистограмма частоты

text = input('Введите текст: ').lower()
result = {}
for i in text:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

for i in sorted(result.keys()):
    print(i, ':', result[i])
print('Максимальная частота:' , max(result.values()))