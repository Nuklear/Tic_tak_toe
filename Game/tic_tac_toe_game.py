from Game.Base.base_game import BaseGame
from Game.player import Player

WIN_COMBO = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
PLAYER_ONE_SYMBOL = "X"
PLAYER_TWO_SYMBOL = "O"


class TicTacToeGame(BaseGame):
    def __init__(self, player_one: Player, player_two: Player):
        super().__init__()
        self._player_one = player_one
        self._player_two = player_two
        self._current_player = self._player_one
        self._game_field = [i for i in range(1, 10)]
        self._game_symbol_for_each_player = {
            self._player_one: PLAYER_ONE_SYMBOL,
            self._player_two: PLAYER_TWO_SYMBOL
        }

    def turn(self):
        counter = 0
        while not self.is_win():
            players_select = self.show_turn_interface()
            if self._is_cell_already_entered(players_select):
                print("Cell already selected, pls select another cell")
                continue

            counter+=1
            self._game_field[players_select-1] = self._game_symbol_for_each_player[self._current_player]
            if self.is_win():
                print("Player - {} WIN".format(self._current_player.get_player_name()))
                return self._current_player
            elif counter >= len(self._game_field):
                print("DRAW")
                return None
            else:
                if self._current_player == self._player_one:
                    self._current_player = self._player_two
                else:
                    self._current_player = self._player_one

    def is_win(self):
        for each in WIN_COMBO:
            if self._game_field[each[0]] == self._game_field[each[1]] == self._game_field[each[2]]:
                return self._game_field[each[0]]
        return False

    def current_status(self):
        for i in range(3):
            print("|", self._game_field[0 + i * 3], "|", self._game_field[1 + i * 3], "|", self._game_field[2 + i * 3],"|")
            print("-------------")
        print("Current player = {}\n".format(self._current_player.get_player_name()))

    def current_player(self):
        return self._current_player

    def show_turn_interface(self)->int:
        self.current_status()
        while True:
            players_select = input("Pls select cell (1-9): ")
            try:
                players_select = int(players_select)
                if 0 < players_select < 10:
                    return players_select
                else:
                    print("Not correct input, pls try again")
            except ValueError:
                print("Not correct input, pls try again")

    def _is_cell_already_entered(self, players_select: int):
        if self._game_field[players_select-1] in [k for k in self._game_symbol_for_each_player.values()]:
            return True

        return False


