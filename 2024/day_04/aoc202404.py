from aocd.models import Puzzle

CROSS_PATTERN = {
    "cross": {"column": [1, 0, -1, -1, 0, 1], "row": [1, 0, -1, 1, 0, -1]},
}

ALL_PATTERNS = {
    "vertical": {"column": [0, 0, 0, 0], "row": [0, 1, 2, 3]},
    "horizontal": {"column": [0, 1, 2, 3], "row": [0, 0, 0, 0]},
    "diagonal_right": {"column": [0, 1, 2, 3], "row": [0, 1, 2, 3]},
    "diagonal_left": {"column": [0, -1, -2, -3], "row": [0, 1, 2, 3]},
}


def parse(puzzle_input):
    """Parse input."""
    return [[letter for letter in row] for row in puzzle_input.split()]


def part_one(data):
    """Solve part 1."""
    total = 0
    for row_index, row in enumerate(data):
        for column_index, _ in enumerate(row):
            total += check_patterns(data, row_index, column_index)
    return total


def part_two(data):
    """Solve part 2."""
    total = 0
    for row_index, row in enumerate(data):
        for column_index, _ in enumerate(row):
            total += check_patterns(
                data,
                row_index,
                column_index,
                ["MASSAM", "SAMMAS", "MASMAS", "SAMSAM"],
            )
    return total


def check_patterns(data, row_index, column_index, matching_words=["XMAS", "SAMX"]):
    """Given a starting row and column check all available patterns for a match"""
    total = 0
    patterns_to_check = (
        ALL_PATTERNS if matching_words == ["XMAS", "SAMX"] else CROSS_PATTERN
    )
    for name, pattern in patterns_to_check.items():
        letters = []
        for i, _ in enumerate(pattern["row"]):
            # Wrap in a try except to not stress about IndexErrors at boundaries
            try:
                row_to_check = row_index + pattern["row"][i]
                col_to_check = column_index + pattern["column"][i]
                # Avoids looking up the last element in the list if the row_to_check equals -1
                if row_to_check >= 0 and col_to_check >= 0:
                    letters.append(data[row_to_check][col_to_check])
                    if "".join(letters) in matching_words:
                        total += 1
            except IndexError:
                continue
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=4)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
