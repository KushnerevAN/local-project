#Задача 1. Свой for (ну почти)

spisok = [1, 2, 3, 4, 5]

iterator = iter(spisok)
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        print('Конец')
        break



