import random
from real_estate_banking.entities.board import Board
from real_estate_banking.entities.property import Property
from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    def __init__(self, type_name: str):
        self._type_name = type_name
        self._financial_balance = 300
        self._position = -1

    @property
    def type_name(self):
        return self._type_name

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

    @abstractmethod
    def evaluate_purchase(self, target_property: Property):
        pass

    def __str__(self):
        return f'Jogador {self.type_name} - Saldo de {self.financial_balance}'
