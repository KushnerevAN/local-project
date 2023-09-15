#Задача 1. Ошибка
#import copy
#import random

#def change_dict(dct):
#    num = random.randint(1, 100)
#    for i_key, i_value in dct.items():
#        if isinstance(i_value, list):
#            i_value.append(num)
#        if isinstance(i_value, dict):
#            i_value[num] = i_key
#        if isinstance(i_value, set):
#            i_value.add(num)

#nums_list = [1, 2, 3]
#some_dict = {1: 'text', 2: 'another text'}
#uniq_nums = {1, 2, 3}
#common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
#common_dict_2 = copy.deepcopy(common_dict)
#change_dict(common_dict_2)
#print(common_dict_2)
#print(nums_list, some_dict, uniq_nums)

#Задача 2. Непонятно!

data_names_dict = {
    "<class 'str'>": "строка",
    "<class 'dict'>": "словарь",
    "<class 'list'>": "список",
    "<class 'set'>": "множество"
}

mutable_check_helper = {
    "mutable": ("словарь", "список", "множество")
}

def check_info(data):
    type_of_data = type(data)
    name_of_data = ""
    if str(type_of_data) in data_names_dict:
        name_of_data = data_names_dict[str(type_of_data)]

    if name_of_data in mutable_check_helper["mutable"]:
        property_of_data = "Изменяемый (mutable)"
    else:
        property_of_data = "Неизменяемый (immutable)"

    print(f"Тип данных: {type_of_data} ({name_of_data})")
    print(property_of_data)
    print("Id объекта:", id(data))

data_in = 123
check_info(data_in)

