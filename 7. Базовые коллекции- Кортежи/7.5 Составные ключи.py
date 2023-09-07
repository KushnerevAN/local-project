#Задача 1. Паспортные данные

#data = {
#    (5000, 123456): ('Иванов', 'Василий'),
#    (6000, 111111): ('Иванов', 'Петр'),
#    (7000, 222222): ('Медведев', 'Алексей'),
#    (8000, 333333): ('Алексеев', 'Георгий'),
#    (9000, 444444): ('Георгиева', 'Мария')
#}

#series = int(input('Введите серию паспорта: '))
#number = int(input('Введите номер паспорта: '))
#series_and_number = (series, number)
#if series_and_number in data:
#        print(' '.join(data[series_and_number]))
#else:
#    print('Такого человека нет.')

#Задача 2. Контакты 2
phone_list = {}
while True:
    name = input('Введите имя контакта: ')
    surname = input('Введите фамилию контакта: ')
    check = (name, surname)
    if check in phone_list:
            print('Такой контакт уже существует в телефонной книге.')
            name = input('Введите имя контакта: ')
            surname = input('Введите фамилию контакта: ')
    else:
        num_phone = int(input('Введите номер телефона: '))
        data = {}
        data[check] = num_phone
        phone_list.update(data)
    print(phone_list)
