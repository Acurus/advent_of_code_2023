import unittest


from day3_gear_ratios.gear_ratios import *

TEST_INPUT = [
                "467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598.."]
SUM_PART_NUMBERS = 4361
SUM_GEAR_RATIOS = 467835
    

class TestDay3(unittest.TestCase):

    def test_parse_engine_parts(self):
        # Arrange
        engine = Engine(["..467....."])
        
        # Act
        parts = engine.parts
        # Assert
        self.assertEqual(1, len(parts))
        self.assertEqual(467, parts[0].part_number)

    def test_sum_partnumbers(self):
        # Arrange
        engine = Engine(TEST_INPUT)
        # Act
        sum = engine.sum_part_numbers()
        # Assert
        self.assertEqual(SUM_PART_NUMBERS, sum)

    def test_sum_gear_ratios(self):
        # Arrange
        engine = Engine(TEST_INPUT)
        # Act
        sum = engine.sum_gear_ratios()
        # Assert
        self.assertEqual(SUM_GEAR_RATIOS, sum)