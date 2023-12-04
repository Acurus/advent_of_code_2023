
class ScratchCard:
    def __init__(self, line: str):
        self.line = line
        self.id = int(line.split(':')[0].split()[1])
        self.winning_numbers = self._get_winning_numbers()
        self.numbers_i_have = self._get_numbers_i_have()
        self.number_of_wins = 0
        self.points = self._calculate_points()

    def _get_winning_numbers(self):
        return [int(x) for x in self.line.split(':')[1].split('|')[0].split()]

    def _get_numbers_i_have(self):
        return [int(x) for x in self.line.split(':')[1].split('|')[1].split()]

    def _calculate_points(self):
        points = 0
        for number in self.numbers_i_have:
            if number in self.winning_numbers:
                self.number_of_wins += 1
                if points == 0:
                    points = 1
                else:
                    points = points + points
        return points


def parse_cards(input_data: list[str]):
    cards = []
    for line in input_data:
        cards.append(ScratchCard(line))
    return cards


def calculate_points(cards: list[ScratchCard]):
    points = 0
    for card in cards:
        points += card.points
    return points


def run_part_2(cards: list[ScratchCard]):
    cards_to_process = {x.id: [x] for x in cards}

    for card_id in cards_to_process.keys():
        for card in cards_to_process[card_id]:
            for i in range(1, card.number_of_wins+1):
                try:
                    cards_to_process[card_id+i].append(cards_to_process[card_id+i][0])
                except KeyError:
                    pass

    total = 0
    for card_id in cards_to_process.keys():
        total += len(cards_to_process[card_id])
    return total


if __name__ == '__main__':
    with open("day4_scratchcards/input.txt") as f:
        input_data = f.readlines()
        cards = parse_cards(input_data)
        print(calculate_points(cards))
        print(run_part_2(cards))
