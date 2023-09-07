#Задача 1. Кризис миновал

#incomes = {
#    'apple': 5600.20,
#    'orange': 3500.45,
#    'banana': 5000.00,
#    'bergamot': 3700.56,
#    'durian': 5987.23,
#    'peach': 10000.50,
#    'pear': 1020.00,
#    'persimmon': 310.00,
#}
#for i_name, i_score in incomes.items():
#    print(i_name, '--', i_score)

#Задача 2. Сервер

#server_data = {
#    "server": {
#        "host": "127.0.0.1",
#        "port": "10"
#    },
#    "configuration": {
#        "access": "true",
#        "login": "Ivan",
#        "password": "qwerty"
#    }
#}
#for i_name, value in server_data.items():
#    print(i_name, ':')
#    for j, k in server_data[i_name].items():
#        print('\t',j, ':', k)

#Задача 3. В одну строчку

print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])