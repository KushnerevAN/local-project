#Задача № 1
#Одна IT-компания решила расшириться и взяла под своё крыло ещё три таких же, но поменьше. Конечно же, все выполненные и невыполненные задачи этих компаний перетекли в основную компанию.
#Даны четыре списка компаний, в которых для каждой задачи написано, выполнена (1) она или нет (0):

#main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
#first_company = [0, 0, 0]
#second_company = [1, 0, 0, 1, 1]
#third_company = [1, 1, 1, 0, 1]

#Напишите программу, которая расширяет список main элементами остальных списков, выведите итоговый список, а также выведите количество невыполненных
#задач. Результат работы программы:
#Общий список задач: [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1]
#Кол - во невыполненных задач: 10

#Решение:

#main.extend(first_company)
#main.extend(second_company)
#main.extend(third_company)
#main.count(0)
#print('Общий список задач:', main)
#print('Кол-во невыполненных задач:', main.count(0))

#Задача № 2 Вредоносное ПО

#first_message = input('Первое сообщение:')
#second_message = input('Второе сообщение:')
#count_first_message = []
#count_second_message = []
#for i in first_message:
#    if i == '!' or i == '?':
#        count_first_message.append(0)
#for i in second_message:
#    if i == '!' or i == '?':
#        count_second_message.append(0)
#if count_first_message.count(0) > count_second_message.count(0):
#    print('Третье сообщение:', first_message, second_message)
#elif count_second_message.count(0) > count_first_message.count(0):
#    print('Третье сообщение:', second_message, first_message)
#elif count_first_message.count(0) == count_second_message.count(0):
#    print('Третье сообщение: Ой')

#Задача № 3

number_packages = int(input('Количество пакетов: '))
package = []
decoding_list = []
wastes = 0
for i_package in range(number_packages):
    print('\nПакет', i_package + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end='')
        bit = int(input())
        package.append(bit)
    if package.count(- 1) <= 1:
        decoding_list.extend(package)
    else:
        print('Много ошибок в пакете.')
        wastes += 1
    package = []
print()
print('Полученное сообщение:', decoding_list)
print('Количество ошибок в сообщении:', decoding_list.count(- 1))
print('Количество потерянных пакетов:', wastes)






