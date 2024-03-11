
class Player:
    def __init__(self, id) -> None:
        self._id = id

    def get_record(self):
        import json
        file = open('file.json', 'r')
        data = json.load(file)
        if str(self._id) not in data.keys():
            return 0
        return data[str(self._id)]

    @staticmethod
    def get_dict():
        import json
        file = open('file.json', 'r')
        dict = json.load(file)
        return dict

    def save_record(self, new_record):
        import json
        dict = Player.get_dict()
        dict[self._id] = new_record + self.get_record()
        file = open('file.json', 'w')
        json.dump(dict, file, indent=4)


class PlayGuessNumber:
    def __init__(self, min, max):
        self._min = min
        self._max = max
        self._count_attempt = 0

    def set_count_attempt(self):
        self._count_attempt += 1

    def get_count_attempt(self):
        return self._count_attempt

    def get_perfect_count_attempt(self):
        import math
        n = int(self._max) - int(self._min)
        perfect_count = round(math.log(n, 2))
        return perfect_count + 1

    def calculate_record(self):
        record = round((int(self._max) - int(self._min)) * self.get_perfect_count_attempt() / self.get_count_attempt())
        return record


class PlayGuessCity:
    def __init__(self):
        self._game_step = 1

    def set_game_step(self):
        self._game_step += 1

    def get_game_step(self):
        return self._game_step

    def calculate_record(self):
        return int(120 / self.get_game_step())
