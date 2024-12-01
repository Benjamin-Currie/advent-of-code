from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    list_of_ints = puzzle_input.split()
    left_list = []
    right_list = []
    for i in range(0, len(list_of_ints), 2):
        left_list.append(int(list_of_ints[i]))
        right_list.append(int(list_of_ints[i + 1]))
    return sorted(left_list), sorted(right_list)


def part_one(data):
    """Solve part 1."""
    total = 0
    for i in range(0, len(data[0])):
        sorted_data = sorted([data[0][i], data[1][i]])
        total += sorted_data[1] - sorted_data[0]
    return total


def part_two(data):
    """Solve part 2."""
    similarity_score = 0
    for i in range(0, len(data[0])):
        similarity_score += data[0][i] * data[1].count(data[0][i])
    return similarity_score


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=1)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
