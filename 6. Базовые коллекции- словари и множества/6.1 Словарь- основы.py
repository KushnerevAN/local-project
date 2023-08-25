#Задача 1. Словарь квадратов чисел

#number = int(input('Введите число: '))
#number_dict = {}
#for i in range(1, number + 1):
#    number_dict[i] = i ** 2
#print(number_dict)

#Задача 2. Студент

#student_info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):\n')
#student_list = student_info.split()

#student = {}
#student['Имя'] = student_list[0]
#student['Фамилия'] = student_list[1]
#student['Город'] = student_list[2]
#student['Место учебы'] = student_list[3]
#student['Оценки'] = []
#for i in student_list[4:]:
#    student['Оценки'].append(int(i))
#for i in (student):
#    print(i, '-', student[i])

#Задача 3. Контакты

current_contact_list = {}
while True:

    print('Текущие контакты в телефоне:')
    for i in current_contact_list:
        print(i, current_contact_list[i])
    print()

    name = input('Введите имя: ')
    if name not in current_contact_list:
        phone_num = int(input('Введите номер телефона: '))
        if name == 'Хватит':
            break
        current_contact_list[name] = phone_num

    else:
        print('Ошибка: такое имя уже существует.')

    print()











