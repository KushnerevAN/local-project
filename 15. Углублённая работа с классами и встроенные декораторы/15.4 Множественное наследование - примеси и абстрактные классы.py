#Задача 1. Транспорт
#from abc import ABC, abstractmethod

#class MusicMixin:

#    def play_music(self):
#        print("""
#        I see trees of green
#        Red roses too
#        I see them bloom
#        For me and for you
#        And I think to myself
#        What a wonderful world
#        """)


#class Transport(ABC):

#    @abstractmethod
#    def ride_on_earth(self):
#        pass

#    @abstractmethod
#    def ride_on_water(self):
#        pass


#class Car(Transport):

#    def ride_on_earth(self):
#        print("Едем по земле")


#class Boat(Transport):

#    def ride_on_water(self):
#        print("Ходим по воде")


#class Amphibian(Car, Boat, MusicMixin):
#    pass

#amph_transport = Amphibian()
#amph_transport.ride_on_earth()
#amph_transport.ride_on_water()
#amph_transport.play_music()

# Задача 2. Фигуры

class Figure:

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizeAbleMixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figure, ResizeAbleMixin):
    pass


class Square(Figure, ResizeAbleMixin):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)
