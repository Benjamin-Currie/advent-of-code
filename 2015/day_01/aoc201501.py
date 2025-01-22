from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input


def part_one(data):
    """Solve part 1."""
    return data.count("(") - data.count(")")


def part_two(data):
    """Solve part 2."""
    target = -1
    current_floor = 0
    for index, i in enumerate(data):
        current_floor += 1 if i == "(" else -1
        if current_floor == target:
            return index + 1



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2015, day=1)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
