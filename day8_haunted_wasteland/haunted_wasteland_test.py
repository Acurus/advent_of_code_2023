import unittest


from day8_haunted_wasteland.haunted_wasteland import *


class TestDay8(unittest.TestCase):

    def test_part1_example_test1(self):
        # Arrange
        test_input = ["RL",
                      "AAA = (BBB, CCC)",
                      "BBB = (DDD, EEE)",
                      "CCC = (ZZZ, GGG)",
                      "DDD = (DDD, DDD)",
                      "EEE = (EEE, EEE)",
                      "GGG = (GGG, GGG)",
                      "ZZZ = (ZZZ, ZZZ)"]

        expected = 2

        # Act
        actual = solve_part1(test_input)

        # Assert
        self.assertEqual(expected, actual)

    def test_part1_example_test2(self):

        test_input = [
            "LLR",

            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)"]

        expected = 6

        # Act
        actual = solve_part1(test_input)

        # Assert
        self.assertEqual(expected, actual)

    def test_part2_example_test2(self):

        test_input = [
            "LR",

            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)"]

        expected = 6

        # Act
        actual = solve_part2(test_input)

        # Assert
        self.assertEqual(expected, actual)

# 20569 too low