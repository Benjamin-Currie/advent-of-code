from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    dict_of_nums = {}
    for line in puzzle_input.split("\n"):
        split_line = line.strip().split(": ")
        dict_of_nums[int(split_line[0])] = [int(i) for i in split_line[1].split(" ")]
    return dict_of_nums


def part_one(data):
    """Solve part 1."""
    for key, value in data.items():
        # Loop for enough times to test all possible values
        combinations = []
        for i in range((len(value) - 1) * 2):
            total = 0
            for ni, number in enumerate(value):






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
