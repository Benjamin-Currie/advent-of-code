from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [[int(i) for i in line] for line in puzzle_input.split("\n")]


def part_one(data):
    """Solve part 1."""
    total = 0
    for row in data:
        l = max(row)
        if row.index(l) == len(row) - 1:
            r = l
            l = max(row[:-1])
        else:
            r = max(row[row.index(l) + 1 :])
        total += int(f"{l}{r}")
    return total


def part_two(data):
    """Solve part 2."""
    total = 0
    for row in data:
        new_row = []
        start_index = 0
        end_index = -11
        for i in range(12):
            if i == 11:
                highest_number = max(row[start_index:])
            else:
                highest_number = max(row[start_index:end_index])

            # Trim the row to start after the latest highest number
            row = row[start_index:]
            new_row.append(highest_number)
            start_index = row.index(highest_number) + 1

            # Avoid setting end_index to 0 on the last iteration
            if end_index != -1:
                end_index += 1

        total += int("".join(str(i) for i in new_row))
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2025, day=3)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
