import re
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [tuple(map(int, line.split("-"))) for line in puzzle_input.split(",")]


def is_repeat(y, half_length):
    return y[:half_length] == y[-half_length:]


def part_one(data):
    """Solve part 1."""
    total = 0
    codes = [x for start, end in data for x in range(start, end + 1)]
    for code in codes:
        y = str(code)
        q, r = divmod(len(y), 2)
        if r == 0 and is_repeat(y, q):
            total += code
    return total


def part_two(data):
    """Solve part 2."""
    total = 0
    codes = [x for start, end in data for x in range(start, end + 1)]
    for code in codes:
        y = str(code)
        q, r = divmod(len(y), 2)
        if (r == 0 and is_repeat(y, q)) or bool(re.fullmatch(r"(.+)\1+", y)):
            total += code
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2025, day=2)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
