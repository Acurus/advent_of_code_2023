
CARD_VALUE_MAP = {"2": 1,
                  "3": 2,
                  "4": 3,
                  "5": 4,
                  "6": 5,
                  "7": 6,
                  "8": 7,
                  "9": 8,
                  "T": 9,
                  "J": 0,
                  "Q": 11,
                  "K": 12,
                  "A": 13}

HAND_VALUE_MAP = {"fiveOfAKind": 7,
                  "fourOfAKind": 6,
                  "fullHouse": 5,
                  "threeOfAKind": 4,
                  "twoPair": 3,
                  "onePair": 2,
                  "highCard": 1}


class Card:
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __lt__(self, other):
        # < operator
        return CARD_VALUE_MAP[self.value] < CARD_VALUE_MAP[other.value]

    def __gt__(self, other):
        # < operator
        return CARD_VALUE_MAP[self.value] > CARD_VALUE_MAP[other.value]


class Hand:
    def __init__(self, cardsString: list[str], bid: str):
        self.cards = []
        for card in cardsString:
            self.cards.append(Card(card))
        self.bid = int(bid)

    @property
    def type(self):
        value_counts = {}
        for card in self.cards:
            if card.value in value_counts:
                value_counts[card.value] += 1
            else:
                value_counts[card.value] = 1
        
        
        if value_counts.get("J") == 5:
            return "fiveOfAKind"
        
        if "J" in value_counts:
            value_counts[max(value_counts, key=lambda k: value_counts[k] if k != 'J' else float('-inf'))] += value_counts["J"]
            value_counts["J"] = 0
        
        if 5 in value_counts.values():
            return "fiveOfAKind"
        elif 4 in value_counts.values():
            return "fourOfAKind"
        elif 3 in value_counts.values() and 2 in value_counts.values():
            return "fullHouse"
        elif 3 in value_counts.values():
            return "threeOfAKind"
        elif list(value_counts.values()).count(2) == 2:
            return "twoPair"
        elif 2 in value_counts.values():
            return "onePair"
        else:
            return "highCard"
        
    def __lt__(self, other):
        # < operator
        if HAND_VALUE_MAP[self.type] == HAND_VALUE_MAP[other.type]:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                elif self.cards[i] < other.cards[i]:
                    return True
                elif self.cards[i] > other.cards[i]:
                    return False
        else:
            return HAND_VALUE_MAP[self.type] < HAND_VALUE_MAP[other.type]


def solution(lines: list[str]):
    hands = []
    for line in lines:
        line = line.split(" ")
        cardsString = line[0]
        bid = line[1]
        hands.append(Hand(cardsString, bid))
    hands.sort()
    for i in hands:
        print(f"{i.type} - {[x.value for x in i.cards]}")
    sum = 0
    for rank, hand in enumerate(hands, 1):
        sum += hand.bid*rank
    return sum


if __name__ == "__main__":
    with open("day7_camel_cards\input.txt", "r") as f:
        lines = f.readlines()
    print(solution(lines))
