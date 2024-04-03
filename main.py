from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float = field(repr=False)

@dataclass
class Cart:
    res: dict = field(default_factory=dict)
    total: list = field(default_factory=list)
    result: int = field(default_factory=int)

    def add_product(self, data):
        self.res[data.name] = data.price
        return self.res

    def get_total(self):
        for i in self.res.values():
            self.total.append(i)
        return sum(self.total)

    def apply_discount(self, value):
        if 1 > value > 100:
            raise ValueError('Неправильное значение скидки')
        self.discount = sum(self.total) * value / 100
        return sum(self.total) - self.discount



product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)

print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

print(f"Стоимость товаров в корзине без скидки: {cart.get_total()}")
# Применение скидки 10%
cart.apply_discount(10)
print(f"Стоимость товаров в корзине со скидкой 10%: {cart.get_total()}")