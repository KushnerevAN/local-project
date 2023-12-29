#Задача 1. Юниты

#class Unit:
#    def __init__(self, hitpoint):
#        self.hitpoint = hitpoint

#    def take_damage(self):
#        self.hitpoint -= 0

#    def __str__(self):
#        return 'Количество здоровья: {}'.format(self.hitpoint)

#class Solder(Unit):
#    def __init__(self, hitpoint):
#        super().__init__(hitpoint)

#    def take_damage(self):
#        self.hitpoint -= self.hitpoint

#    def __str__(self):
#        return 'Количество здоровья: {}'.format(self.hitpoint)

#class Human(Unit):
#    def __init__(self, hitpoint):
#        super().__init__(hitpoint)

#    def take_damage(self):
#        self.hitpoint -= (self.hitpoint * 2)

#    def __str__(self):
#        return 'Количество здоровья: {}'.format(self.hitpoint)

#unit = Unit(100)
#unit.take_damage()
#print(unit)

#solder = Solder(250)
#solder.take_damage()
#print(solder)

#human = Human(300)
#human.take_damage()
#print(human)

#Задача 2. Полёт

class Can_fly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def Take_off(self): # Взлететь
        pass

    def Fly(self): # Лететь
        pass

    def To_land(self): # Приземлиться
        self.height = 0
        self.speed = 0

    def __str__(self):
        return 'Высота {}\tСкорость {}'.format(self.height, self.speed)

class Butterfly(Can_fly):

    def Take_off(self):  # Взлететь
        self.height = 1

    def Fly(self): # Лететь
        self.speed = 0.5

    def __str__(self):
        return 'Высота {}\tСкорость {}'.format(self.height, float(self.speed))

class Rocket(Can_fly):

    def Take_off(self):  # Взлететь
        self.height = 500
        self.speed = 1000

    def To_land(self): # Приземлиться
        self.height = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун')

    def __str__(self):
        return 'Высота {}\tСкорость {}'.format(self.height, float(self.speed))

butterfly = Butterfly()
butterfly.Take_off()
butterfly.Fly()
print(butterfly)

rocket = Rocket()
rocket.Take_off()
rocket.To_land()

print(rocket)










