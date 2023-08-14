#Задача 1. Заказ

#user_name = input('Введите имя: ')
#user_code = int(input('Введите номер заказа: '))
#result = 'Здравствуйте, {name}! Ваш номер заказа: {code}. Приятного дня!'.format(name = user_name,code = user_code)
#print(result)

#Задача 2. Долги

#name = input('Введите имя: ')
#debt = int(input('Введите долг: '))
#message = f'{name}! {name}, привет! Как дела, {name}? Где мои {debt} рублей? {name}!'.format(name = name, debt = debt)
#print(message)

#Задача 3. IP-адрес

ip_adress = '{0}.{1}.{2}.{3}'
count = 0
number_list = []
while count < 4:
    number = int(input('Введите число: '))
    if 0 <= number <= 255:
        number_list.append(number)
        count += 1
print(ip_adress.format(number_list[0], number_list[1], number_list[2], number_list[3]))



