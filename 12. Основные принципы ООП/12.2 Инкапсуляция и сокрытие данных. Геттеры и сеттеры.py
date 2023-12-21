#Задача 1. Координаты точки

class Point:
    __count = 0
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return 'Х: {}, Y: {}'.format(self.__x, self.__y)

    def get_x(self): # Геттер
        return self.__x

    def get_y(self): # Геттер
        return self.__y

    def check_value(self, value):
        if isinstance(value, (int, float)):
            return value
        else:
            raise Exception('Введено не число')

    def set_x(self, value): #Сеттер
        checker_value = self.check_value(value)
        if checker_value:
           self.__x = checker_value

    def set_y(self, value): #Сеттер
        checker_value = self.check_value(value)
        if checker_value:
            self.__y = checker_value

point_1 = Point(6, 58)
point_1.set_x(point_1.get_x())
point_1.set_y(point_1.get_y())
print(point_1.__str__())

#Задача 2. Человек

#class Human:
#    __count = 0
#    def __init__(self, name, age):
#        self.__name = name
#        self.__age = age
#        Human.__count += 1

#    def __str__(self):
#        return 'Имя: {}\tВозраст: {}'.format(self.__name, self.__age)

#    def get_name(self):
#        return self.__name

#    def get_age(self):
#        return self.__age

#    def get_count(self):
#        return self.__count

#    def set_name(self, word):
#        if not word.isalpha():
#            raise Exception('Имя состоит не только из букв.')
#        else:
#            return True

#    def set_age(self, value):
#        if value in range(0, 101):
#            return True
#        else:
#            raise Exception('Некорректно указано возраст.')

#misha = Human('Misha', 15)
#misha.set_name(misha.get_name())
#misha.set_age(misha.get_age())

#print(misha.__str__())
#print(misha.get_count())






