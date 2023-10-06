#Задача 1. Простая программа
file = None
try:
    file = open('ages_2.txt', 'w')
    text = input('Введите строку: ')
    file.write(text)
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)
else:
    print("Запись прошла без ошибок")
finally:
    if file and not file.closed:
        file.close()
