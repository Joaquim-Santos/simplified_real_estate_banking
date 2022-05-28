from real_estate_banking.entities.players.abstract_player import AbstractPlayer
from real_estate_banking.entities.property import Property


class ImpulsivePlayer(AbstractPlayer):
    def __init__(self, turn_order: int):
        super().__init__(turn_order)

    def evaluate_purchase(self, target_property: Property):
        return True
