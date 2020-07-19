
class Player(object):
    def __init__(self, name: str):
        self._name = name
        self._score = 0

    def get_player_score(self):
        return self._score

    def add_points_to_score(self, points: int):
        self._score += points

    def get_player_name(self):
        return self._name

    def __str__(self):
        return "Player: {}\tscore = {}".format(self._name, self._score)
