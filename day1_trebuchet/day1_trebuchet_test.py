import unittest

from day1_trebuchet.trebuchet import get_calibration


class TestDay1Methods(unittest.TestCase):

    def test_get_calibration_part1(self):
        # Arrange
        input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        expected = [12, 38, 15, 77]
        # Act
        actual = get_calibration(input)
        # Assert
        self.assertEqual(actual, expected)
        self.assertEqual(sum(actual), 142)

    def test_get_calibration_part2(self):
        # Arrange
        input = ["jgb95ninetwonine", "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen", "eightwo"]
        expected = [99,29, 83, 13, 24, 42, 14, 76, 82]
        # Act
        actual = get_calibration(input)
        # Assert
        self.assertEqual(actual, expected)
        self.assertEqual(sum(actual), 281+82+99)


if __name__ == '__main__':
    unittest.main()
