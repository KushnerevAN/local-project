#Задача 1. Challenge
#def factorial(num):
#    if num == 1:
#        return num
#    fact_n_min_1 = factorial(num - 1)
#    return num * fact_n_min_1

#res = factorial(6)
#print(res)

#Задача 2. Степень числа
#def power(a, n):
#    if n == 0:
#        return 1
#    up = power(a, n - 1)
#    return a * up

#float_num = float(input('Введите вещественное число: '))
#int_num = int(input('Введите степень числа: '))
#print(float_num, '**', int_num, '=', power(float_num, int_num))

#Задача 3. Поиск элемента

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input('Искомый ключ: ')

def function(structure, meaning):
    if meaning in structure:
        return structure[meaning]
    for i in structure.values():
        if isinstance(i, dict):
            res = function(i, meaning)
            if res:
                break
    else:
        res = None
    return res

value = function(site, key)
if value:
    print(value)
else:
    print('Такого ключа в словаре нет.')
