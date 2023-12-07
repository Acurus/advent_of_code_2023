import unittest


from day7_camel_cards.camel_cards import *

TEST_INPUT = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483" ]
SUM_PART1 = 6440
    

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
        card_string1= "1234Q"
        card_string2= "11234"
        card_string3= "11223"
        card_string4= "11123"
        card_string5= "11122"
        card_string6= "11112"           
        card_string7= "11111"


        bid = "0"

        # Act
        hand1 = Hand(card_string1, bid)
        hand2 = Hand(card_string2, bid)
        hand3 = Hand(card_string3, bid)
        hand4 = Hand(card_string4, bid)
        hand5 = Hand(card_string5, bid)
        hand6 = Hand(card_string6, bid)
        hand7 = Hand(card_string7, bid)

        
        # Assert
        self.assertEqual(hand1.type, "highCard")
        self.assertEqual(hand2.type, "onePair")
        self.assertEqual(hand3.type, "twoPair")
        self.assertEqual(hand4.type, "threeOfAKind")
        self.assertEqual(hand5.type, "fullHouse")
        self.assertEqual(hand6.type, "fourOfAKind")
        self.assertEqual(hand7.type, "fiveOfAKind")


    def test_typecomparison(self):
        # Arrange
        hands = []
        for hand in TEST_INPUT:
            card_string, bid = hand.split(" ")
            hands.append(Hand(card_string, bid))

        # Assert
        self.assertLess(hands[0], hands[1])
        self.assertGreater(hands[2], hands[0])

    def test_part1(self):
        # Arrange
        lines = TEST_INPUT
        # Act
        res = part1(lines)
        # Assert
        self.assertEqual(res, SUM_PART1)

    def test_highcard_sort(self):
        # Arrange
        hands = []
        input = ["2K975 0",
                 "2954J 0",
                 "T5QK4 0",]
        
        # Act
        for hand in input:
            card_string, bid = hand.split(" ")
            hands.append(Hand(card_string, bid))
        hands.sort(reverse=True)
        for i in hands:
            print(f"{i.type} - {[x.value for x in i.cards]}")
        # Assert
        self.assertEqual(hands[0].cards[0].value, "T")