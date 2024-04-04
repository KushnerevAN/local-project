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
    bag: list = field(default_factory=list, repr=False)
    total_bag:  float = field(default=0)
    res_disc: int = field(default=0)

    def add_product(self, data, num=1):
        self.bag.append([data.name, data.price, num])



    def get_total(self):
        self.total_bag = sum(i[1] * i[2] for i in self.bag)
        if self.apply_promo:
            return self.total_bag - self.res_disc
        return self.total_bag

    def apply_promo(self, promo):
        count = 0
        print(self.bag)
        for i in ACTIVE_PROMO:
            if promo == i.cod and not i.spisok_tovarov:
                count += 1
                self.res_disc = self.total_bag * i.discount / 100
                print(f'Промокод {promo} успешно применился')
                break
            if promo == i.cod and i.spisok_tovarov:
                count += 1
                self.res_disc = sum(i[0] * i[1] for i in self.bag[]) * i.discount / 100
                print(f'Промокод {promo} успешно применился')
                break
        if count == 0:
            print(f'Промокода {promo} не существует')

    def apply_discount(self, value):
        if value > 100 or value < 1:
            raise ValueError('Неправильное значение скидки')
        self.res_disc = self.total_bag * value / 100


book = Product('Книга', 100.0)
usb = Product('Флешка', 50.0)
pen = Product('Ручка', 10.0)

ACTIVE_PROMO = [
    Promo('new', 20, [pen]),
    Promo('all_goods', 30),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
print(cart.get_total())

# Применение промокода в 20% на ручку
cart.apply_promo('new')
print(cart.get_total())
