class Product:
    def __init__(self, title, count) -> None:
        self.title = title
        self.count = count

    def get_info(self):
        return (f'{self.title} (в наличии: {self.count})')
    # Опишите инициализатор класса и метод get_info()
    ...


class Kettlebell(Product):
    def __init__(self, title, count, weight) -> None:
        super().__init__(title, count)
        self.weight = weight

    def get_weight(self):
        return (f'{self.get_info()}. Вес: {self.weight} кг')
# Опишите инициализитор класса и метод get_weight()


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, title, count, size) -> None:
        super().__init__(title, count)
        self.size = size

    def get_size(self):
        return (f'{self.get_info()}. Размер: {self.size}')


# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:
small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
