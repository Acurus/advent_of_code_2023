
from datetime import datetime
import math


class Game:
    def __init__(self,
                 instructions: list[str],
                 nodes: dict[str, tuple[str, str]],
                 start_node: tuple[str, str],
                 end_nodes: list[tuple[str, str]]) -> None:
        
        self.instructions = instructions
        self.number_of_instructions = len(self.instructions)
        self.nodes = nodes
        self.current_node = start_node
        self.end_nodes = end_nodes
        self.counter = 0
        

    def solve(self) -> int:
        instruction = 0
        while True:
            self.current_node = self._next_pos(self.instructions[instruction])
            self.counter += 1
            instruction += 1
            if instruction == self.number_of_instructions:
                instruction = 0
            if self.current_node in self.end_nodes:
                return self.counter

    def _next_pos(self, direction: str) -> dict[str, tuple[str, str]]:
        if direction == 'R':
            return self.nodes[self.current_node[1]]
        elif direction == 'L':
            return self.nodes[self.current_node[0]]
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

def parse_nodes(lines: list[str]) -> dict[str, tuple[str, str]]:
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
    instructions = [x for x in lines[0] if x == "R" or x == "L"]
    nodes = parse_nodes(lines[1:])
    start_node = nodes['AAA']
    end_requirement = [nodes['ZZZ']]
    game = Game(instructions, nodes, start_node, end_requirement)
    return game.solve()


def solve_part2(lines: list[str]) -> int:
    paths = []
    instructions = [x for x in lines[0] if x == "R" or x == "L"]
    nodes = parse_nodes(lines[1:])
    start_nodes = [nodes[x] for x in nodes if x.endswith('A')]
    end_nodes = [nodes[x] for x in nodes if x.endswith('Z')]
    for start_node in start_nodes:
        game = Game(instructions, nodes, start_node, end_nodes)
        paths.append(game.solve())
    return math.lcm(*paths) # Not my idea.
    


if __name__ == '__main__':
    with open('day8_haunted_wasteland/input.txt') as f:
        lines = f.readlines()
    print(solve_part1(lines))
    print(solve_part2(lines))
