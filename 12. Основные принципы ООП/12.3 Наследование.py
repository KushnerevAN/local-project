#Задача 1. Корабли

#class Ship:
#    def __init__(self, model):
#        self.__model = model

#    def __str__(self):
#        return 'Модель корабля: {model}'.format(model=self.__model)

#    def run(self):
#        print('Корабль начал ход.')

#class WarShip(Ship):
#    def __init__(self, model, gun):
#        super().__init__(model)
#        self.gun = gun

#    def attack(self):
#        print('Корабль атакует с помощью', self.gun)

#class CargoShip(Ship):
#    def __init__(self, model):
#        super().__init__(model)
#        self.workload_ship = 0

#    def loading(self):
#        print('Корабль загружается.')
#        self.workload_ship += 1
#        print('Уровень загрузки: ', self.workload_ship)

#    def discharge(self):
#        print('Корабль выгружается.')
#        self.workload_ship -= 1
#        print('Уровень загрузки: ', self.workload_ship)

#warship = WarShip('t1000', 'Пушка')
#warship.attack()
#cargo = CargoShip('аповап')
#cargo.loading()

#Задача 2. Роботы

#class Robots:
#    def __init__(self, model):
#        self.__model = model

#    def __str__(self):
#        return 'Модель корабля {model}'.format(model=self.__model)

#class Robot_cleaner(Robots):
#    def __init__(self, model):
#        super().__init__(model)
#        self.bag = 0

#    def operate(self):
#        print('\nРобот пылесосит пол')
#        self.bag += 1
#        print('Заполненность мешка', self.bag)

#class Robot_warrior(Robots):
#    def __init__(self, model, gun):
#        super().__init__(model)
#        self.gun = gun

#    def operate(self):
#        print('\nРобот защищает объект с помощью', self.gun)

#class Robot_submarine(Robots):
#    def __init__(self, model):
#        super().__init__(model)
#        self.depth = 0

#    def operate(self):
#        print('\nРобот ведет охрану под водой.')
#        self.depth -= 10
#        print('Глубина', self.depth)

#robot_1 = Robot_cleaner('Зина-5')
#robot_2 = Robot_warrior('Мишка-1', 'Пулемет')
#robot_3 = Robot_submarine('Лунтик-3')

#robot_1.operate()
#robot_2.operate()
#robot_3.operate()






