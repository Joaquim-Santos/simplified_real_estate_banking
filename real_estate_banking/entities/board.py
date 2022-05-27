from real_estate_banking.entities.property import Property


class Board:
    def __init__(self):
        self._properties = self.load_properties()

    @property
    def properties(self):
        return self._properties

    @staticmethod
    def length():
        return 20

    @staticmethod
    def load_properties():
        properties = []
        start_rent = 25
        start_price = 100
        position = 0

        # Cada grupo de 5 propriedades terá o mesmo valor de aluguel e compra, respectivamente variando de 25 a 100, e
        # 100 a 400, sendo o aluguel sempre 4 vezes maior do que o valor de compra.
        for x in range(1, 5):
            for y in range(5):
                properties.append(Property(start_rent*x, start_price*x, position))
                position += 1

        return properties
