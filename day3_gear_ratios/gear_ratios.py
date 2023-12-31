import string


class Part:
    def __init__(self):
        self.start_position = None
        self.end_position = None
        self.part_number_string = ''
        self.is_valid = False

    @property
    def part_number(self):
        try:
            number = int(self.part_number_string)
        except Exception as e:
            print(e)
            number = 0
        return number


class Gear:
    def __init__(self, parts: list[Part]):
        self.gear_ratio = self.calculate_gear_ratio(parts)

    def calculate_gear_ratio(self, parts: list[Part]):
        return parts[0].part_number * parts[1].part_number


class Engine:
    def __init__(self, input_data: list[str]):
        self.symbols = [*string.printable[62:-5].replace(".", "")]
        self.input_data = input_data
        self.parts = self.find_parts()
        self.gears = self.find_gears()

    def sum_part_numbers(self):
        valid_parts = [x for x in self.parts if x.is_valid]
        return sum([x.part_number for x in valid_parts])

    def sum_gear_ratios(self):
        return sum([x.gear_ratio for x in self.gears])

    def find_parts(self) -> list[Part]:
        possible_parts = []
        reading_part_number = False
        for i, row in enumerate(self.input_data):
            for j, char in enumerate(row):
                if char.isnumeric() and reading_part_number is False:
                    part = Part()
                    part.start_position = (i, j)
                    part.part_number_string += char
                    reading_part_number = True
                elif char.isnumeric() and reading_part_number:
                    part.part_number_string += char
                elif char.isnumeric() == False and reading_part_number:
                    part.end_position = (i, j-1)
                    self._validate_part(part)
                    possible_parts.append(part)
                    reading_part_number = False
                else:
                    continue
        return possible_parts

    def _validate_part(self, part: Part) -> None:
        row = part.start_position[0]
        min_row = max(part.start_position[0]-1, 0)
        min_col = max(part.start_position[1]-1, 0)
        max_row = min(part.end_position[0]+1, len(self.input_data)-1)
        max_col = min(part.end_position[1]+1, len(self.input_data[0])-1)

        try:
            if self._check_for_symbol(self.input_data[row][max_col]):
                part.is_valid = True
                return
            elif self._check_for_symbol(self.input_data[row][min_col]):
                part.is_valid = True
                return
            elif self._check_for_symbol(self.input_data[min_row][min_col:max_col+1]):
                part.is_valid = True
                return
            elif self._check_for_symbol(self.input_data[max_row][min_col:max_col+1]):
                part.is_valid = True
                return
        except IndexError:
            print(f"Index Error: {max_col, max_row}")

    def _check_for_symbol(self, s: str):
        return any([char in self.symbols for char in s])

    def find_gears(self) -> list[Gear]:
        gears = []
        for i, row in enumerate(self.input_data):
            for j, char in enumerate(row):
                if char == '*':
                    gear = self._find_gear(i, j)
                    if gear:
                        gears.append(gear)
        return gears

    def _find_gear(self, row, col):
        parts = []
        for part in self.parts:
            is_adjecent = self._position_is_adjecent(row, col, part)
            if is_adjecent:
                parts.append(part)
        if len(parts) == 2:
            return Gear(parts)
        else:
            return None

    def _position_is_adjecent(self, row, col, part: Part) -> bool:

        row_above = max(part.start_position[0]-1, 0)
        row_below = min(part.start_position[0]+1, len(self.input_data)-1)
        
        col_before_min = max(part.start_position[1]-1, 0)
        col_after_max  = min(part.end_position[1]+1, len(self.input_data[0])-1)

        if part.start_position[0] == row and (col_before_min == col
                                              or col_after_max == col):
            return True
        elif row_above == row and (col >= col_before_min
                                       and col <= col_after_max):
            return True
        elif row_below == row and (col >= col_before_min
                                       and col <= col_after_max):
            return True
        return False


if __name__ == '__main__':
    with open("day3_gear_ratios/input.txt", "r") as f:
        engine = Engine(f.readlines())
        print(engine.sum_part_numbers())
        print(engine.sum_gear_ratios())
