import random
from real_estate_banking.entities.board import Board


class AbstractPlayer:
    def __init__(self, turn_order: int):
        self._turn_order = turn_order
        self._financial_balance = 300
        self._position = -1

    @property
    def turn_order(self):
        return self._turn_order

    @property
    def financial_balance(self):
        return self._financial_balance

    @financial_balance.setter
    def financial_balance(self, new_value):
        self._financial_balance = new_value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_value):
        self._position = new_value

    def roll_dice(self):
        number = random.randint(1, 6)
        self.position += number

        # Jogador deu a volta no tabuleiro, então seu saldo incrementa em 100.
        if self.position > (Board.length() - 1):
            self.position -= Board.length()
            self.financial_balance += 100
