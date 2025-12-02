from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [(x[0], int(x[1:])) for x in puzzle_input.split("\n")]


def part_one(data):
    """Solve part 1."""
    safe_nums = [i for i in range(0, 100)]
    current_index = 50
    total = 0
    for direction, clicks in data:
        if direction == "R":
            new_index = safe_nums[(current_index+clicks)%len(safe_nums)]
        else:
            new_index = safe_nums[(current_index-clicks)%len(safe_nums)]
        total += 1 if new_index == 0 else 0
        current_index = new_index
    return total

def part_two(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2025, day=1)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
