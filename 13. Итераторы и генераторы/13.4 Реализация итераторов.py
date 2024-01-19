#Задача 1. Бесконечный итератор

#class СountIterator:
#    counter = 0

#    def __iter__(self):
#        return self

#    def __next__(self):
#        СountIterator.counter += 1
#        return СountIterator.counter

#my_iter = СountIterator()
#for i_elem in my_iter:
#    print(i_elem)

#Задача 2. Случайная сумма

import random

#class ClassIterator:
#    def __init__(self, number):
#        self.count = 0
#        self.second_elem = 0
#        self.end_elem = number

#    def __iter__(self):
#        return self

#    def __next__(self):
#        self.count += 1
#        if self.count > self.end_elem:
#            raise StopIteration()
#        self.second_elem += random.random()
#        return self.second_elem

#resultat = ClassIterator(25)
#for i in resultat:
#    print(i)

#Задача 3. Простые числа

class Primes:

    def __init__(self, n):
        self.n = n
        self.i = 1
        self.prime_number = []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        while self.i <= self.n:
            self.i += 1
            for prime in self.prime_number:
                if self.i % prime == 0:
                    break
            else:
                self.prime_number.append(self.i)
                return self.i
        raise StopIteration

prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end=' ')





