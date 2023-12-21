#Задача 1. Юниты

class Unit:
    def __init__(self, hitpoint):
        self.__hitpoint = hitpoint


    def set_hp(self, damage):
        self.__hitpoint = damage

    def get_hp(self):
        return self.__hitpoint

    def take_damage(self, damage):
        self.__hitpoint -= 0

    def __str__(self):
        return 'Количество здоровья: {hitpoint}'.format(hitpoint=self.__hitpoint)

class Solder(Unit):

    def take_damage(self, damage):
        self.__hitpoint(self.get_hp() * 2)

    def __str__(self):
        return 'Количество здоровья: {hitpoint}'.format(hitpoint=self.__hitpoint)



unit = Unit(100)
unit.set_hp
unit.take_damage(0)
print(unit)

solder = Solder(Unit)
solder.take_damage(unit.set_hp)
print(solder)







