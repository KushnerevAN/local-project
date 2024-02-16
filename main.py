from collections import defaultdict
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return (f'Пользователь {self.login}, баланс {self.balance}')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, value):
        self.balance += value

    def is_money_enough(self, sum):
        if sum >= self.balance:
            return False
        return True

    def payment(self, pay):
        if self.balance >= pay:
            self.balance -= pay
        else:
            print('Не хватает средств на балансе. Пополните счет')

class Cart:
    def __init__(self, User):
        self.user = User.login
        self.goods = defaultdict(dict)
        self.__total = 0

    @property
    def total(self):
        return self.__total

    def add(self, Product, num_products=1):
        self.goods[Product] = self.goods.get(Product, 0) + num_products
        self.__total += num_products * Product.price

    def remove(self, Product, num_products=1):
        self.goods[Product] = self.goods.get(Product, 0) - num_products
        self.__total -= num_products * Product.price

    def order(self):
        if self.user.payment(self.__total):
            print('Товар оплачен')
        else:
            print('Проблема с оплатой')

    def print_check(self):
        print(f'---Your check---')
        for k, v in sorted(self.goods.items(), key=lambda x: x[0].name):
            if v > 0:
                print(k.name, k.price, v, k.price * v)
            else:
                pass
        print(f'---Total: {self.__total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20













