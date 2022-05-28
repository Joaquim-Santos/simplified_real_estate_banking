from real_estate_banking.entities.players.abstract_player import AbstractPlayer
from real_estate_banking.entities.property import Property


class CautiousPlayer(AbstractPlayer):
    def __init__(self):
        super().__init__("Cauteloso")

    def evaluate_purchase(self, target_property: Property):
        return (self.financial_balance - target_property.purchase_price) >= 80
