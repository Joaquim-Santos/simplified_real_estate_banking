import operator
from real_estate_banking.entities.players.abstract_player import AbstractPlayer
from real_estate_banking.entities.board import Board
from real_estate_banking.entities.property import Property


class Match:
    def __init__(self, players: list[AbstractPlayer]):
        self._players = players
        self._board = Board()
        self._winner = None
        self._round = 0
        self._timeout = False
        self._count_turn = 0

    @property
    def players(self):
        return self._players

    @property
    def board(self):
        return self._board

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, new_value):
        self._winner = new_value

    @property
    def round(self):
        return self._round

    @round.setter
    def round(self, new_value):
        self._round = new_value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, new_value):
        self._timeout = new_value

    @property
    def count_turn(self):
        return self._count_turn

    @count_turn.setter
    def count_turn(self, new_value):
        self._count_turn = new_value

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

    def eliminate_player_by_balance(self, player: AbstractPlayer):
        if player.financial_balance < 0:
            for position in player.acquired_properties:
                self.board.properties[position].owner = None
            self.players.remove(player)

    def verify_victory_condition_1(self):
        return len(self.players) == 1

    def verify_victory_condition_2(self):
        return self.round == 1000

    def start(self):
        # Loop executa o jogo enquanto não for atribuído um vencedor. A iteração da lista de players é feita em cima de
        # uma cópia, assim um jogador pode ser removido durante  iteração e a ordem dos posteriores é mantida.
        while self.winner is None:
            if self.verify_victory_condition_2():
                # Quando há time out, o jogador de maior saldo vence. Em caso de empate, a função max retorna o 1º.
                self.winner = max(self.players, key=operator.attrgetter('financial_balance'))
                self.timeout = True
                break

            self.round += 1
            for player in list(self.players):  # Execução da rodada.
                player.roll_dice()
                self.evaluate_property(self.board.properties[player.position], player)

                self.eliminate_player_by_balance(player)
                self.count_turn += 1

                # Se durante a rodada, sobrou apenas um jogador na lista, esse é o vencedor e não precisa jogar sua vez.
                if self.verify_victory_condition_1():
                    self.winner = self.players[0]
                    break
