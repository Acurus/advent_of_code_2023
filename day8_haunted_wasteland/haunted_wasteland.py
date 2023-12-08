
from datetime import datetime

class GamePart1:
    def __init__(self, lines: list[str]) -> None:
        self.instructions = [x for x in lines[0] if x == "R" or x == "L"]
        self.nodes = self._build_nodes(lines[1:])
        self.current_pos = self.nodes['AAA']
        self.counter = 0

        self.number_of_instructions = len(self.instructions)

    def solve(self) -> int:
        instruction = 0
        while True:
            self.current_pos = self._next_pos(self.instructions[instruction])
            self.counter += 1
            instruction += 1
            if instruction == self.number_of_instructions:
                instruction = 0
            if self.current_pos == self.nodes['ZZZ']:
                return self.counter

    def _next_pos(self, direction: str) -> dict[str, tuple[str, str]]:
        if direction == 'R':
            return self.nodes[self.current_pos[1]]
        elif direction == 'L':
            return self.nodes[self.current_pos[0]]
        else:
            raise ValueError(f"Invalid direction: {direction}")

    def _build_nodes(self, lines: list[str]) -> dict[str, tuple[str, str]]:
        nodes = {}
        for line in lines:
            if line == "\n":
                continue
            pos = line[:3]
            left = line[7:10]
            right = line[12:15]
            if pos in nodes:
                print("WTF!? Node already exists!")
            nodes[pos] = (left, right)
        return nodes


class GamePart2:
    def __init__(self, lines: list[str]) -> None:
        self.instructions = [x for x in lines[0] if x == "R" or x == "L"]
        self.start_time = 0
        self.nodes = self._build_nodes(lines[1:])
        self.current_posistions = {x: self.nodes[x] for x in self.nodes.keys() if x.endswith('A')}
        self.counter = 0
        self.memoized = {}
        self.number_of_instructions = len(self.instructions)

    def solve(self) -> int:
        self.start_time = datetime.now()
        instruction = 0
        max_found = 0
        while True:
            self.current_posistions = self._next_pos(self.instructions[instruction])
            self.counter += 1
            instruction += 1
            if instruction == self.number_of_instructions:
                instruction = 0

            number_found = len([x for x in self.current_posistions if x.endswith('Z')])
            if number_found > max_found:
                print(f" Found {number_found} that ends with Z")
                print(self.current_posistions)
                print(f" after checking {self.counter} instructions in {(datetime.now() - self.start_time )} seconds\n")
                max_found = number_found
            if number_found == len(self.current_posistions):
                return self.counter

    def _next_pos(self, direction: str) -> list[dict[str, tuple[str, str]]]:
        new_positions = {}
        for _, item in self.current_posistions.items():
            new_postion = self.memoized.get((direction, _), None)
            if new_postion:
                new_positions[list(new_postion.keys())[0]] = list(new_postion.values())[0]
                continue
            if direction == 'R':
                new_positions[item[1]] = self.nodes[item[1]]
                self.memoized[(direction, _)] = {item[1]: self.nodes[item[1]]}
            elif direction == 'L':
                new_positions[item[0]] = self.nodes[item[0]]
                self.memoized[(direction, _)] = {item[0]: self.nodes[item[0]]}
            else:
                raise ValueError(f"Invalid direction: {direction}")
        return new_positions

    def _build_nodes(self, lines: list[str]) -> dict[str, tuple[str, str]]:
        nodes = {}
        for line in lines:
            if line == "\n":
                continue
            pos = line[:3]
            left = line[7:10]
            right = line[12:15]
            if pos in nodes:
                print("WTF!? Node already exists!")
            nodes[pos] = (left, right)
        return nodes


def solve_part1(lines: list[str]) -> int:
    game = GamePart1(lines)
    return game.solve()


def solve_part2(lines: list[str]) -> int:
    game = GamePart2(lines)
    return game.solve()


if __name__ == '__main__':
    with open('day8_haunted_wasteland/input.txt') as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))
