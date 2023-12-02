import unittest


from day2_cube_conundrum.cube_conundrum import *


class TestDay2(unittest.TestCase):

    def test_game_id_from_string_single_digit(self):
        # Arrange
        game1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

        # Act

        game = Game(game1)

        # Assert
        self.assertEqual(game.id, 1)

    def test_game_id_from_string_double_digit(self):
        # Arrange
        game1 = "Game 17: 14 green, 4 red; 1 green, 5 blue, 15 red; 5 green, 14 red, 5 blue"

        # Act
        game = Game(game1)

        # Assert
        self.assertEqual(game.id, 17)

    def test_game_sets_from_string(self):
        # Arrange
        game1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

        # Act

        game = Game(game1)

        # Assert
        self.assertEqual(len(game.sets), 3)
        self.assertEqual(game.sets[0].blue, 3)
        self.assertEqual(game.sets[0].red, 4)
        self.assertEqual(game.sets[0].green, 0)

    def test_play_game_part1(self):
        # Arrange
        input_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        bag = CubeCollection()
        bag.red = 12
        bag.green = 13
        bag.blue = 14
        # Act
        sum = play_game_part1(input_data, bag)

        # Assert
        self.assertEqual(sum, 8)

    def test_play_game_part2(self):
        # Arrange
        input_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                      "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                      "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                      "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                      "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        bag = CubeCollection()
        bag.red = 12
        bag.green = 13
        bag.blue = 14
        # Act
        sum = play_game_part2(input_data)

        # Assert
        self.assertEqual(sum, 2286)


if __name__ == '__main__':
    unittest.main()
