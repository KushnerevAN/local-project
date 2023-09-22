#Задача 1. Сисадмин

#import os
#path = os.path.join('access', 'admin.bat')
#print('Относительный путь до файла:', path)
#abs_path = os.path.abspath('admin.bat')
#print('Абсолютный путь до файла:', abs_path)

#Задача 2. Содержимое

import os
project = 'Python_Basic'
path = os.path.abspath(os.path.join('..', '..', project))
#path = os.path.abspath(project)
print('\nСодержимое директории:', path)
for i_elem in os.listdir(path):
    print(i_elem)
    res = os.path.join(path, i_elem)
    #print(' ', res)

#Задача 3. Корень диска

#Корень диска: G:\
#import os
# Решение для Windows:
#print("Корень диска:", os.path.abspath(os.sep).split(os.sep)[0])