import random
import math
import statistics
from real_estate_banking.entities.players import *
from collections import defaultdict
from real_estate_banking.match import Match
from typing import TextIO


class Simulation:
    def __init__(self, number_of_simulations: int = 300):
        self._number_of_simulations = number_of_simulations
        self._count_timeout = 0
        self._amount_of_turns_by_match = []
        self._victories_by_player_type = defaultdict(int)

    @property
    def number_of_simulations(self):
        return self._number_of_simulations

    @property
    def count_timeout(self):
        return self._count_timeout

    @property
    def amount_of_turns_by_match(self):
        return self._amount_of_turns_by_match

    @property
    def victories_by_player_type(self):
        return self._victories_by_player_type

    @staticmethod
    def generate_players():
        players = []
        players_types = [ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer]

        for player_type in players_types:
            amount_of_player_type = random.randint(1, 3)
            for x in range(amount_of_player_type):
                players.append(player_type())

        return players

    def save_match_result(self, match: Match, result_file: TextIO, match_number: int):
        if match.timeout:
            self._count_timeout += 1

        self._amount_of_turns_by_match.append(match.count_turn)
        self._victories_by_player_type[match.winner.type_name] += 1

        result_file.write(f'Partida {match_number}\nVencedor: {str(match.winner)}\n')
        result_file.write(f'{str(match)}\n\n')

    def calculate_statistics_of_all_simulations(self, result_file: TextIO):
        average_turn_for_match = math.ceil(statistics.mean(self.amount_of_turns_by_match))

        max_victories = max(self.victories_by_player_type.values())
        most_successful_player_type = ''

        # Calculada a porcentagem de vitórias por tipo de jogador e obtido o mais vitorioso. Se houver mais de um tipo
        # com o máximo de vitórias, considera-se ambos.
        victories_percent_by_player_type = {}
        for player_type, amount_of_victories in self.victories_by_player_type.items():
            player_victories_percent = (amount_of_victories/self.number_of_simulations) * 100
            victories_percent_by_player_type[player_type] = math.ceil(player_victories_percent)
            if amount_of_victories == max_victories:
                most_successful_player_type += f'{player_type}, '

        result_file.write("Estatísticas das Simulações\n")
        result_file.write(f'{self.count_timeout} partidas terminaram por time out.\n')
        result_file.write(f'Uma partida dura, em média, {average_turn_for_match} turnos.\n\n')

        result_file.write(f'Porcentagem de vitórias por comportamento dos jogadores:\n')
        for player_type, victories_percent in victories_percent_by_player_type.items():
            result_file.write(f'{player_type}: {victories_percent}%\n')

        result_file.write(f'\nO comportamento mais vitorioso é o do(s) jogador(es) {most_successful_player_type[:-2]}')

    def start_simulations(self):
        with open('simulations_result.txt', 'w', encoding='utf-8') as result_file:
            for x in range(self.number_of_simulations):
                players = self.generate_players()
                match = Match(players)

                match.start()
                self.save_match_result(match, result_file, x)

            self.calculate_statistics_of_all_simulations(result_file)


if __name__ == "__main__":
    Simulation().start_simulations()
