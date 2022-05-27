

class Property:
    def __init__(self, rent_value: float, purchase_price: float, board_position: int):
        self._rent_value = rent_value
        self._purchase_price = purchase_price
        self._board_position = board_position
        self._owner = None

    @property
    def purchase_price(self):
        return self._purchase_price

    @property
    def rent_value(self):
        return self._rent_value

    @property
    def board_position(self):
        return self._board_position

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_value):
        self._owner = new_value
