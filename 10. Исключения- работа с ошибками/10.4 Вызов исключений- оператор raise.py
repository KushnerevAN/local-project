#Задача 1. Имена
#summ_sym = 0
#count = 0
#file = open('people.txt', 'r', encoding='utf-8')
#for i in file:
#    length = len(i)
#    count += 1
#    if i.endswith('\n'):
#        length -= 1
#    if length <= 3:
#        raise BaseException('В строке {} имя содержит меньше 3-х символов.'.format(count))
#    else:
#        summ_sym += length
#print('Количество символов:', summ_sym)

#Задача 2. Логирование

def check(word):
    counter = 0
    result = dict()
    for i in word:
        result[i] = result.get(i, 0) + 1
    print(result)
    for j in result.values():
        if j % 2 != 0:
            counter += 1
    return counter

file = open('words.txt', 'r', encoding='utf-8')
file_error = open('errors.log', 'w', encoding='utf-8')
count_check = 0
list = []
for i in file:
    try:
        clear_i = i.rstrip()
        #print(clear_i)
        if clear_i.isalpha():
            counter = check(clear_i.lower())
            #print(counter)
            if counter <= 1:
                count_check += 1
        else:
            raise ValueError('В слове также присутствуют цифры.')
    except ValueError:
        file_error.write(str(i))

print('Количество палиндромов:', count_check)
file.close()
file_error.close()