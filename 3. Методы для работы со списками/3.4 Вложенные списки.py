#Задача 1. Матрица

#matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]
#for i in matrix:
#    for n in i:
#        print(n, end=' ')
#    print()

#Задача 2. Олимпиада

#num = 1
#general_list = []
#num_participants = int(input('Количество участников: '))
#num_people_team = int(input('Количество человек в команде: '))
#if num_participants % num_people_team != 0:
#    print(num_participants, 'участников невозможно поделить на команды по', num_people_team, 'человек.')
#else:
#    num_team = num_participants / num_people_team
#    for i in range(int(num_team)):
#        general_list.append(list(range(num, num + num_people_team)))
#        num += num_people_team
#    print('Общий список команд:', general_list)

#Задача 3. Лавка
count = 0
goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))
print('Новый ассортимент:', end='')
goods.append([fruit_name, price])
print(goods)
for i in goods:
    i[1] = round(i[1] * 1.08, 2)

print('Новый ассортимент с увел. ценой:', goods)