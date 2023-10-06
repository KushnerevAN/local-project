#Задача 1. Пятый элемент

#BRUCE_WILLIS = 42
#try:
#    input_data = input('Введите строку: ')
#    leeloo = int(input_data[4])
#    result = BRUCE_WILLIS * leeloo
#    print(f'- Leeloo Dallas! Multi-pass № {result}!')
#except ValueError as i:
#    print(i, 'Невозможно преобразовать элемент в число.')
#except IndexError:
#    print('Вы ввели строку длинной меньше 4-х символов.')
#except KeyboardInterrupt:
#    print('Работы программы прервана.')
#except IndentationError:
#    print('Неправильные отступы.')

#Задача 2. Возраст
import random
open_file = None
result_file = None
try:
    open_file = open('ages.txt', 'r', encoding='utf-8')
    result_file = open('result.txt', 'x') # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
except FileExistsError as s:
    print(s, 'Файл с аналогичным названием уже существует.')
except IsADirectoryError as w:
    print(w, 'На чтение ожидался файл, но это оказалась директория.')
if open_file and result_file:
    for i in open_file:
        try:
            int(i)
            cyrillic_up = chr(random.randint(ord('А'), ord('Я') + 1))
            result_file.write(cyrillic_up + ' ' + i)
        except ValueError:
            print('Невозможно преобразовать элемент в число.')
        except TypeError:
            print('Операция применена к объекту несоответствующего типа.')




