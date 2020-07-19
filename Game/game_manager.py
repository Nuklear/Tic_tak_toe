import os

from Game.player import Player
from Game.tic_tac_toe_game import TicTacToeGame
from Game.Save.save_json import SaveJson
from Game.Save.save_text import SaveText

from Game.const import PATH_FOR_SAVE

WIN_POINTS = 2
LOSE_POINTS = 1


class GameManager(object):
    def __init__(self, player_one: Player, player_two: Player):
        self._player_one = player_one
        self._player_two = player_two
        self._count_games = 0

    def start_game_series(self):
        while True:
            self._count_games +=1
            game = TicTacToeGame(self._player_one, self._player_two)
            result = game.turn()
            self._write_game_result(result)
            is_play_again = input("Play another game?(Y/N)").lower()
            if is_play_again != "Y":
                self.show_result()
                self.save_result()
                break

    def _write_game_result(self, result):
        if result == self._player_one:
            self._player_one.add_points_to_score(WIN_POINTS)
            self._player_two.add_points_to_score(LOSE_POINTS)
        elif result is None:
            self._player_one.add_points_to_score(LOSE_POINTS)
            self._player_two.add_points_to_score(LOSE_POINTS)
        else:
            self._player_one.add_points_to_score(LOSE_POINTS)
            self._player_two.add_points_to_score(WIN_POINTS)

    def show_result(self):
        print("*"*100)
        print("Game played - {}".format(self._count_games))
        print(str(self._player_one))
        print(str(self._player_two))
        if self._player_one.get_player_score() > self._player_two.get_player_score():
            print("Player {} WIN!!!".format(self._player_one.get_player_name()))
        elif self._player_two.get_player_score() > self._player_one.get_player_score():
            print("Player {} WIN!!!".format(self._player_two.get_player_name()))
        else:
            print("DRAW!!!")
        print("*" * 100)

    def get_result(self):
        return {
            "games played": self._count_games,
            self._player_one.get_player_name(): self._player_one.get_player_score(),
            self._player_two.get_player_name(): self._player_two.get_player_score()
        }

    def save_result(self):
        select_format = input("Pls select format for save result:\n1 - JSON\n2 - TEXT (default)")
        try:
            select_format = int(select_format)
        except ValueError:
            select_format = 2

        path = os.path.normpath(PATH_FOR_SAVE)
        if select_format != 1:
            saver = SaveText(path)
            saver.save(self.get_result())
        else:
            saver = SaveJson(path)
            saver.save(self.get_result())
