from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


class CubeCollection:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def add_cubes(self, color: Color, amount: int):
        if color == Color.red:
            self.red += amount
        elif color == Color.green:
            self.green += amount
        elif color == Color.blue:
            self.blue += amount

    def power(self) -> int:
        return self.red * self.green * self.blue

    def __gt__(self, other):
        return (self.red > other.red or
                self.green > other.green or
                self.blue > other.blue)

    def __lt__(self, other):
        return (self.red < other.red or
                self.green < other.green or
                self.blue < other.blue)

    def __eq__(self, other):
        return (self.red == other.red and
                self.green == other.green and
                self.blue == other.blue)


class Game:
    def __init__(self, game_string: str):
        self.game_string = game_string
        self.id = self._game_id_from_string()
        self.sets = self._game_sets_from_string()

    def fewest_number_of_cubes(self) -> CubeCollection:
        fewest_cubes = CubeCollection()
        fewest_cubes.add_cubes(Color.red, max(
            self.sets, key=lambda x: x.red).red)
        fewest_cubes.add_cubes(Color.green, max(
            self.sets, key=lambda x: x.green).green)
        fewest_cubes.add_cubes(Color.blue, max(
            self.sets, key=lambda x: x.blue).blue)
        return fewest_cubes

    def _game_id_from_string(self) -> int:
        id_string = self.game_string.split(":")
        id = id_string[0].split(" ")[-1]
        return int(id)

    def _game_sets_from_string(self) -> list[CubeCollection]:
        game_sets = []
        sets_string = self.game_string.split(":")[1:][0]
        for cube_collection_string in sets_string.split(";"):
            game_set = CubeCollection()
            for cube_string in cube_collection_string.split(","):
                amount, color = cube_string.strip().split(" ")
                game_set.add_cubes(Color[color], int(amount))
            game_sets.append(game_set)
        return game_sets


def game_is_possible(bag: CubeCollection, game: Game) -> bool:
    for game_set in game.sets:
        if game_set > bag:
            print(f"{game.id} is impossible")
            return False
    return True


def read_input(input_data: list[str]) -> list[Game]:
    games = []
    for game_string in input_data:
        games.append(Game(game_string))
    return games


def play_game_part1(input_data: list[str], bag: CubeCollection):
    games = read_input(input_data)
    sum = 0
    for game in games:
        if game_is_possible(bag, game):
            sum += game.id
    return sum


def play_game_part2(input_data: list[str]):
    games = read_input(input_data)
    sum = 0
    for game in games:
        sum += game.fewest_number_of_cubes().power()
    return sum


if __name__ == '__main__':
    bag = CubeCollection()
    bag.red = 12
    bag.green = 13
    bag.blue = 14
    with open("day2_cube_conundrum\input.txt", "r") as input:
        data = input.readlines()
        print(f"Part 1 sum: {play_game_part1(data, bag)}")
        print(f"Part 2 sum: {play_game_part2(data, bag)}")
