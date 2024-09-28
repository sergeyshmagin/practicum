class Customer:
    def __init__(self, name):
        self.name = name
        self.__discount = 10
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        ...

    # Реализуйте методы get_price() и set_discount().

    def get_price(self, price):
        return (round(price - (price * (self.__discount / 100)), 2))

    def set_discount(self, new_discount):
        if new_discount >= 80:
            new_discount = 80
        self.__discount = new_discount
        return (self.__discount)


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)