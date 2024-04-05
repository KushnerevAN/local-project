from dataclasses import dataclass, field

ACTIVE_PROMO = list

@dataclass
class Promo:
    cod: str
    discount: int
    spisok_tovarov: list = field(default=False)

    def __post_init__(self):
        if self.discount > 100 or self.discount < 1:
            self.discount = 0

@dataclass
class Product:
    name: str
    price: float = field(repr=False)


@dataclass
class Cart:
    bag: dict = field(default_factory=dict)
    total_bag:  float = field(default=0)
    res_disc: float = field(default=0)
    quantity: dict = field(default_factory=dict)

    def add_product(self, data, num=1):
        self.bag[data.name] = data.price
        if data.name in self.quantity.keys():
            self.quantity[data.name] += num
        else:
            self.quantity[data.name] = num
        print(self.bag, self.quantity)

    def get_total(self):
        for i in self.bag.keys():
            self.total_bag += (self.bag[i] * self.quantity[i])
        print(self.total_bag, 'gbpltw')
        if self.apply_promo:
            #print(self.res_disc)
            return self.total_bag - self.res_disc
        return self.total_bag

    def apply_promo(self, promo):
        count = 0
        for i in ACTIVE_PROMO:
            if promo == i.cod and not i.spisok_tovarov:
                #print(promo, i)
                count += 1
                self.res_disc = self.total_bag * i.discount / 100
                print(f'Промокод {promo} успешно применился')
            if promo == i.cod and i.spisok_tovarov:
                for k in i.spisok_tovarov:
                   # print(self.bag[k.name])
                   # print(self.quantity[k.name])
                    #print(i.discount)
                    count += 1
                    self.res_disc = float(self.bag[k.name] * self.quantity[k.name]) * i.discount / 100
                    print(self.res_disc, 'fgfgdgfg')
                    print(f'Промокод {promo} успешно применился')
        if count == 0:
            print(f'Промокода {promo} не существует')


    #def apply_discount(self, value):
    #    if value > 100 or value < 1:
    #        raise ValueError('Неправильное значение скидки')
    #    #self.res_disc = self.total_bag * value / 100


book = Product('Книга', 100.0)
usb = Product('Флешка', 50.0)
pen = Product('Ручка', 10.0)

ACTIVE_PROMO = [
    Promo('new', 20, [pen]),
    Promo('all_goods', 30),
    Promo('only_book', 40, [book]),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print(cart.get_total())

# Применение промокода в 40% на книгу
cart.apply_promo('only_book')
print(cart.get_total())