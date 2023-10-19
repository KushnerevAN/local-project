#Задача 1. Машина 2

#class Toyota:
#    color = 'Красный'
#    price = 1000000
#    max_speed = 200
#    current_spedd = 0

#    def info(self):
#        print('Цвет: {}\nЦена: {}\nМаксмиальная скорость: {}\nТекущая скорость: {}\n'
#              .format(self.color, self.price, self.max_speed, self.current_spedd))

#    def cur_speed(self, speed):
#        print('Текущая скорость машины: {}\n'.format(speed))

#toyota_1 = Toyota()
#print(toyota_1.info())
#print(toyota_1.cur_speed(652546))

#Задача 2. Семья

class Family:
    name = 'Common family'
    funds = 100000
    house = False

    def info(self):
        print('Family name: {}\nFamily funds: {}\nHaving a house: {}'.format(self.name, self.funds, self.house))

    def income(self, earnings):
        self.funds += earnings
        print('Заработок {} money. Current value: {}.'.format(earnings, self.funds))

    def buy_house(self, cost_house):
        if self.funds >= cost_house:
            self.funds -= cost_house
            self.house = True
            print('House purchased! Current money: {}'.format(self.funds))
        else:
            print('Not enough money!')

family_1 = Family()
family_1.info()
print()
print('Try to buy a house.')
family_1.buy_house(1000000)
print()
if not family_1.house:
    family_1.income(900000)
    print('Try to buy a house again.')
    family_1.buy_house(1000000)
print()
family_1.info()








