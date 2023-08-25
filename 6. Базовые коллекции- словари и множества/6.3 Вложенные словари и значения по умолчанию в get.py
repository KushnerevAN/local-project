#Задача 1. Заказ фруктов

#order = {'apple': 2,
#         'banana': 3,
#         'pear': 1,
#         'watermelon': 10,
#         'chocolate': 5}

#incomes = {
#    'apple': 5600.20,
#    'orange': 3500.45,
#    'banana': 5000.00,
#    'bergamot': 3700.56,
#    'durian': 5987.23,
#    'grapefruit': 300.40,
#    'peach': 10000.50,
#    'pear': 1020.00,
#    'persimmon': 310.00,
#}

#result = 0
#for j in order.keys():
#    summ = incomes.get(j, 1) * order[j]
#    result += summ
#print('Итоговая сумма:', result)

#Задача 2. Игроки

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}
team_a_rest = [i['name']
              for i in players_dict.values()
              if i['team'] == 'A' and i['status'] == 'Rest']
team_b_training = [i['name'] for i in players_dict.values() if i['team'] == 'B' and i['status'] == 'Training']
team_c_travel = [i['name'] for i in players_dict.values() if i['team'] == 'C' and i['status'] == 'Travel']
print(team_a_rest)
print(team_b_training)
print(team_c_travel)