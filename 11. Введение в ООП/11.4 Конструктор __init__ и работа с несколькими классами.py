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

class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def check_info(self):
        print(self.x, self.y)
point_1 = Point()
point_1.check_info(x = 6, y = 8)

