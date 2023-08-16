#Задача 1. Улучшенная лингвистика 2

#words = [input("Введите слово: ") for _ in range(3)]
#text = input("Введите текст: ")
#words_count = [text.count(word) for word in words]
#print(words_count)

#Задача 2. Бабушка

#text = input('Введите текст: ')
#print(' '.join(text.split()))

#Задача 3. Разделители символов

pattern = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
named_list = input('Список людей через запятую: ').split(", ")
age_str = input('Возраст людей через пробел: ').split()
age = [int(age) for age in age_str]
for i in range(len(named_list)):
    print(pattern.format(name=named_list[i], age=age[i]))

people = [" ".join([named_list[i], str(age[i])]) for i in range(len(named_list))]
print("Именинники:", ", ".join(people))
