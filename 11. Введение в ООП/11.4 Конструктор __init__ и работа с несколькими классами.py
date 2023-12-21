#Задача 1. Машина 3

#class Toyota:

#    def __init__(self, color='Красный', price=10000, max_speed=200, current_speed=0):
#        self.color = color
#        self.price = price
#        self.max_speed = max_speed
#        self.current_speed = current_speed

#    def print_info(self):
#        print('Цвет машины: {}\nСтоимость: {}\nМаксимальная скорость: {}\nТекущая скорость: {}'.format
#              (self.color, self.price, self.max_speed, self.current_speed))

#    def current_info(self, change_speed):
#        self.current_speed = change_speed
#        print('Текущая скорость автомобиля: {}'.format(self.current_speed))

#toyota_1 = Toyota()
#toyota_2 = Toyota()
#toyota_1.print_info()
#toyota_2.current_info(155)

#Задача 2. Координаты точки
#class Point:
#    count = 0
#    def __init__(self, x=0, y=0):
#        self.x = x
#        self.y = y
#        Point.count += 1

#    def check_info(self):
#        print(self.x, self.y)

#    def count_P(self):
#        print(self.count)

#point_1 = Point(8, 8)
#point_1.check_info()
#point_1.count_P()

#Задача 3. Весёлая ферма

class Potato:
    states = {0: 'Отсутствуют', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))

class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела.\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')

my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()