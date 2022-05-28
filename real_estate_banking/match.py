from real_estate_banking.entities.players.abstract_player import AbstractPlayer
from real_estate_banking.entities.board import Board
from real_estate_banking.entities.property import Property


class Match:
    def __init__(self, players: list[AbstractPlayer]):
        self._players = players
        self._board = Board()
        self._winner = None

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    @property
    def winner(self):
        return self._winner

    @staticmethod
    def evaluate_property(target_property: Property, player: AbstractPlayer):
        # Se a propriedade não possui dono, é avaliado se o jogador possui saldo suficiente e se deseja comprá-la, com
        # base no comportamento do seu tipo. Caso já tenha dono, apenas é feito o pagamento do aluguel.
        if target_property.owner is None:
            if (player.financial_balance >= target_property.purchase_price) and \
               player.evaluate_purchase(target_property):
                target_property.owner = player
                player.financial_balance -= target_property.purchase_price
                player.acquired_properties = player.position  # Posição atual do jogador é onde está a propriedade.
        else:
            player.financial_balance -= target_property.rent_value
            target_property.owner.financial_balance += target_property.rent_value

    def start(self):
        # Loop executa o jogo enquanto não for atribuído um vencedor. A iteração da lista de players é feita em cima de
        # uma cópia, assim um jogador pode ser removido durante  iteração e a ordem dos posteriores é mantida.
        while self.winner is None:
            for player in list(self.players):
                player.roll_dice()
                self.evaluate_property(self.board.properties[player.position], player)
