from orange import Orange


class Banana(Orange):

    def __init__(self, sort, vitamins, price, name, num_of_kalium):      #характеристику задаем через init
        super().__init__(sort=sort, vitamins=vitamins, price=price, name=name)   # метод super
        self.num_of_kalium = num_of_kalium

    def __repr__(self):
        return f'sort {self.sort}, vitamins {self.vitamins}, price {self.price}, {self.name} and {self.num_of_kalium} K'