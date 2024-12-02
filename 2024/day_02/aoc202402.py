from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [i.split() for i in puzzle_input.split("\n")]


def part_one(data):
    """Solve part 1."""
    total = 0
    for line in data:
        if validation_check(line):
            total += 1
    return total


def part_two(data):
    """Solve part 2."""
    total = 0
    for line in data:
        if validation_check(line):
            total += 1
        else:
            for i in range(0, len(line)):
                updated_line = line.copy()
                del updated_line[i]
                if validation_check(updated_line):
                    total += 1
                    break
    return total


def validation_check(line):
    validation_passes = True
    increasing = False
    decreasing = False
    # Check that the increase or decrease is within the acceptable range otherwise go to the next iteration
    if int(line[-1]) > (int(line[0]) + (len(line) - 1) * 3) or int(line[-1]) < (
        int(line[0]) - (len(line) - 1) * 3
    ):
        return False
    if int(line[0]) > int(line[-1]):
        decreasing = True
    elif int(line[0]) < int(line[-1]):
        increasing = True
    else:
        return False
    for index, number in enumerate(line):
        if index == len(line) - 1:
            if validation_passes == True:
                return True
        if increasing and int(line[index + 1]) not in [
            int(number) + x for x in range(1, 4)
        ]:
            return False
        if decreasing and int(line[index + 1]) not in [
            int(number) - x for x in range(1, 4)
        ]:
            return False
    return True


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=2)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
