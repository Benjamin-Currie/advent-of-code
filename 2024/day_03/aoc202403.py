import re
from aocd.models import Puzzle


def parse(puzzle_input, part_one=False):
    """Parse input."""
    output_part_one = re.findall("mul\([0-9]*,[0-9]*\)", puzzle_input)
    output_part_two = re.findall("mul\([0-9]*,[0-9]*\)|don't\(\)|do\(\)", puzzle_input)
    numbers = []
    pause = False
    if part_one:
        for item in output_part_one:
            numbers.append(item.replace("mul(", "").replace(")", "").split(","))
    else:
        for item in output_part_two:
            if item == "don't()":
                pause = True
                continue
            elif item == "do()":
                pause = False
                continue
            if not pause:
                numbers.append(item.replace("mul(", "").replace(")", "").split(","))

    return numbers


def part_one(data):
    """Solve part 1."""
    return sum(int(number_set[0]) * int(number_set[1]) for number_set in data)


def part_two(data):
    """Solve part 2."""
    return part_one(data)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    part_one_data = parse(puzzle_input, part_one=True)
    part_two_data = parse(puzzle_input)
    solution_one = part_one(part_one_data)
    solution_two = part_two(part_two_data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=3)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
