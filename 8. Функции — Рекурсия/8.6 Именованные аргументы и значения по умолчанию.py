#Задача 1. Работа с файлом

#def function(question, error='Неверный ввод. Пожалуйста, введите да или нет.', counter=3):
#    while True:
#        answer = (input(question) ).lower()
#        if answer == 'да':
#            return 1
#        if answer == 'нет':
#            return 0
#        counter -= 1
#        if counter == 0:
#            print('Количество попыток истекло.')
#            break
#        print(error)
#        print('Количество попыток', counter)

#function('Вы действительно хотите выйти?')
#function('Удалить файл?', 'Так удалить или нет?')
#function('Записать файл?')

#Задача 2. Накопление значений

#def add_num(num, num_list=None):
#    num_list.append(num)
#    print(num_list)

#add_num(5)
#add_num(10)
#add_num(15)

#Задача 3. Помощь другу

def create_dict(data, template=None):
    if not template:
        template = dict()
    if isinstance(data, dict):
        return data
    elif isinstance(data, (int, float, str)):

        template[data] = data
        return template
    #else:
        #return None

def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_elem = create_dict(i_element)
        if new_elem:
            new_list.append(new_elem)
    return new_list

data = ["sad", {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)
print(data)