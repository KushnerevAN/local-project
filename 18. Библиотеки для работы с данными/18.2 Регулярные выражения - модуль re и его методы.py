#Задача 1. Скороговорка
import re
#text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

#result = re.match(r'wo', text)
#print('Поиск шаблона в начале строки: ', result)
#print('=' * 40)
#result = re.search(r'wo', text)
#print('Поиск первого найденного совпадения по шаблону: ', result)
#print('=' * 40)
#print('Содержимое найденной подстроки: ', result.group())
#print('=' * 40)
#print('Начальная позиция: ', result.start())
#print('=' * 40)
#print('Конечная позиция: ', result.end())
#print('=' * 40)
#result = re.findall(r'wo', text)
#print('Список всех упоминаний шаблона: ', result)
#print('=' * 40)
#result = re.sub(r'wo', 'ЗАМЕНА', text)
#print(result)

#Задача 2. Экранирование спецсимволов

text = "How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,"

result = re.findall(r"\\wwood\+\?,", text)
print("Список всех упоминаний шаблона:", result)




