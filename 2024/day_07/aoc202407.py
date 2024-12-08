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
    total = 0
    for key, value in data.items():
        no_of_parens = (len(value) -1)
        for combo in {x for x in combinations_with_replacement([i for i in ["+", "*"]*no_of_parens], no_of_parens)}:
            if key == eval(create_equation(value, no_of_parens, combo)):
                total += key
                break
    return total


def create_equation(value, no_of_parens, combo):
    """Create the equation using parentheses to avoid the usual order of calculation"""
    calculation = "(" * no_of_parens
    calculation += f"{value[0]}{combo[0]}{value[1]}"
    for i in range(2, no_of_parens+1):
        calculation += f"){combo[i-1]}{value[i]}"
    calculation += ")"
    return calculation


def part_two(data):
    """Solve part 2."""


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
