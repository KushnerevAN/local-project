#Задача 1. Шифр Цезаря 2

#alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]

#message_list = input('Введите сообщение: ').lower()
#print(message_list)
#shift = int(input('Введите сдвиг: '))
#result = [alphabet[(alphabet.index(i) + shift) % len(alphabet)]
#         if i in alphabet
#         else ' '
#         for i in message_list]
#print('Зашифрованное сообщение:', ''.join(result))

#Задача 2. Путь к файлу

#path = 'C:/user/docs/folder/new_file.txt'
#disk = input('На каком диске должен лежать файл: ')
#extension_file = input('Требуемое расширение файла: ')

#if path.startswith(disk) and path.endswith(extension_file):
#    print('Путь корректен.')
#else:
#    print('Путь некорректен.')

#Задача 3. Удаление части

text_str = input('Введите строку: ')
text_list = list(text_str)
count_low = 0
count_up = 0
for i in text_list:
    if i.islower() == True:
        count_low += 1
    else:
        count_up += 1
if count_low > count_up:
    print(text_str.lower())
elif count_low < count_up:
    print(text_str.upper())
elif count_low == count_up:
    print('Число заглавных и строчных букв одинаково.')




