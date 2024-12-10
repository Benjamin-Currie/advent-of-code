"""
This is truly awful, it will take hours and hours to run!
"""

from aocd.models import Puzzle
from itertools import combinations_with_replacement


def parse(puzzle_input):
    """Parse input."""
    dict_of_nums = {}
    for line in puzzle_input.split("\n"):
        split_line = line.strip().split(": ")
        dict_of_nums[int(split_line[0])] = [int(i) for i in split_line[1].split(" ")]
    return dict_of_nums


def part_one(data):
    """Solve part 1."""
    total = CustomInt(0)
    for key, value in data.items():
        total += check_equation(key, value, ["+", "*"])
    return total


def part_two(data):
    """Solve part 2."""
    total = CustomInt(0)
    for key, value in data.items():
        print(value)
        total += check_equation(key, value, ["+", "*", "-"])
    return total


class CustomInt(int):
    """
    Class which inherits from int but overloads the sub method to
    concatentate two ints together.
    """

    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        if type(other) == int:
            other_num = other
        else:
            other_num = other.num
        return CustomInt(self.num * other_num)

    def __add__(self, other):
        if type(other) == int:
            other_num = other
        else:
            other_num = other.num
        return CustomInt(self.num + other_num)

    def __sub__(self, other):
        if type(other) == int:
            other_num = other
        else:
            other_num = other.num
        return CustomInt(int(str(self.num) + str(other_num)))


def create_equation(value, no_of_parens, combo):
    """Create the equation using parentheses to avoid the usual order of calculation"""
    calculation = "(" * no_of_parens
    calculation += f"CustomInt({value[0]}){combo[0]}CustomInt({value[1]})"
    for i in range(2, no_of_parens + 1):
        calculation += f"){combo[i-1]}CustomInt({value[i]})"
    calculation += ")"
    return calculation


def check_equation(desired_value, values_to_check, operators):
    no_of_parens = len(values_to_check) - 1
    if len(values_to_check) == 1:
        if desired_value == values_to_check[0]:
            return desired_value
        return 0
    for combo in {
        x
        for x in combinations_with_replacement(
            [i for i in operators * no_of_parens], no_of_parens
        )
    }:
        if desired_value == eval(create_equation(values_to_check, no_of_parens, combo)):
            return desired_value
    return 0


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=7)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
