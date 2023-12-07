import unittest


from day7_camel_cards.camel_cards import *

TEST_INPUT = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483"]
SUM_PART1 = 6440
SUM_PART2 = 5905


class TestDay3(unittest.TestCase):

    def test_card_comparison(self):
        # Arrange
        card1 = Card("K")
        card2 = Card("9")

        # Act
        res = card1 > card2
        # Assert
        self.assertTrue(card1 > card2)
        self.assertFalse(card1 < card2)
        self.assertFalse(card1 == card2)

    def test_typeAssignment(self):
        # Arrange
        card_strings = [
            "1234Q",
            "11234",
            "11223",
            "11123",
            "11122",
            "11112",
            "11111",
            "1JJJJ",
            "JJ73Q"]

        bid = "0"

        # Act
        hands = []
        for card_string in card_strings:
            hands.append(Hand(card_string, bid))

        # Assert
        self.assertEqual(hands[0].type, "highCard")
        self.assertEqual(hands[1].type, "onePair")
        self.assertEqual(hands[2].type, "twoPair")
        self.assertEqual(hands[3].type, "threeOfAKind")
        self.assertEqual(hands[4].type, "fullHouse")
        self.assertEqual(hands[5].type, "fourOfAKind")
        self.assertEqual(hands[6].type, "fiveOfAKind")
        self.assertEqual(hands[7].type, "fiveOfAKind")
        self.assertEqual(hands[8].type, "threeOfAKind")

    def test_typecomparison(self):
        # Arrange
        hands = []
        for hand in TEST_INPUT:
            card_string, bid = hand.split(" ")
            hands.append(Hand(card_string, bid))

        # Assert
        self.assertLess(hands[0], hands[1])
        self.assertGreater(hands[2], hands[0])

    def test_part2(self):
        # Arrange
        lines = TEST_INPUT
        # Act
        res = solution(lines)
        # Assert
        self.assertEqual(res, SUM_PART2)
