#Задача 1. Бесконечный генератор

#def gen():
#    count = 0
#    while True:
#        for i in range(count):
#            yield i
#        count += 1

#res = gen()
#for i in res:
#    print(i)

#Задача 2. Очень большой файл
def gen():
    file = open('number.txt', 'w', encoding='utf-8')

    for i in file:
        yield ' ','n'.join(i)

res = gen()
summ = 0
for i in res:
   summ += res
   print(summ)
