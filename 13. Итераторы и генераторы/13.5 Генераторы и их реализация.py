#Задача 1. Бесконечный генератор

def gen():
    count = 0
    while True:
       yield count
       count += 1

res = gen()
for i in res:
    print(i)

#Задача 2. Очень большой файл

#def clear(line):
#    return [int(number) for number in line.rstrip().split()]

#def line(open_file):
#    file = open(open_file, 'r', encoding='utf-8')
#    for line in file:
#        sum_clear_line = sum(clear(line))
#        yield sum_clear_line

#all_summ = 0
#for num in line('number.txt'):
#    all_summ += num
#print(all_summ)








