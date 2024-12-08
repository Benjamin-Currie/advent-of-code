from aocd.models import Puzzle
import copy


PATROL_RULES = {
    "^": {
        (-1, 0): {
            ".": ("X", "^"),
            "X": ("X", "^"),
            "#": (">", "#"),
        }
    },
    ">": {
        (0, 1): {
            ".": ("X", ">"),
            "X": ("X", ">"),
            "#": ("v", "#"),
        }
    },
    "v": {
        (1, 0): {
            ".": ("X", "v"),
            "X": ("X", "v"),
            "#": ("<", "#"),
        }
    },
    "<": {
        (0, -1): {
            ".": ("X", "<"),
            "X": ("X", "<"),
            "#": ("^", "#"),
        }
    },
}

PATROL_RULES_PART_TWO = {
    "^": (-1, 0, ">"),
    ">": (0, 1, "v"),
    "v": (1, 0, "<"),
    "<": (0, -1, "^"),
}


def parse(puzzle_input):
    """Parse input."""
    return [[character for character in x] for x in puzzle_input.strip().split()]


def part_one(data):
    """Solve part 1."""
    total = 1
    finished = False
    while not finished:
        data, finished = next_move_part_one(data)
    total += sum(1 for row in data for column in row if column == "X")
    return total


def part_two(data):
    """Solve part 2."""
    total = 0
    map_copies = (
        (copy.deepcopy(data), ri, ci)
        for ri, row in enumerate(data)
        for ci, column in enumerate(row)
    )
    for index, copied_map in enumerate(map_copies):
        alt_map, edited = alter_map(copied_map[0], copied_map[1], copied_map[2])
        if not edited:
            continue
        finished = False
        moves = set()
        start_row, start_col = get_starting_point(data)
        next_location = (start_row, start_col)
        next_orientation = "^"
        while not finished:
            position = (*next_location, next_orientation)
            if position not in moves:
                moves.add(position)
                next_location, next_orientation, finished = next_move_part_two(
                    alt_map, next_location[0], next_location[1], next_orientation
                )
            else:
                finished = True
                total += 1
    return total


def next_move_part_two(data, start_row, start_col, current_orientation):
    instructions = PATROL_RULES_PART_TWO[current_orientation]
    new_row = start_row + instructions[0]
    new_col = start_col + instructions[1]
    next_orientation = instructions[2]

    # Check we're not at the edge of the map
    if len(data) > new_row >= 0 and len(data[0]) > new_col >= 0:
        next_location = data[new_row][new_col]
        if next_location in [".", "^"]:
            return (new_row, new_col), current_orientation, False
        else:
            return (start_row, start_col), next_orientation, False
    # The guard is at the edge and can leave
    else:
        return (start_row, start_col), current_orientation, True


def alter_map(copied_map, row_index, col_index):
    edited = False
    if copied_map[row_index][col_index] not in ["^", "#"]:
        copied_map[row_index][col_index] = "#"
        edited = True
    return copied_map, edited


def get_starting_point(data):
    for row_index, row in enumerate(data):
        for column_index, _ in enumerate(row):
            if data[row_index][column_index] in ["^", ">", "v", "<"]:
                return row_index, column_index


def next_move_part_one(data):
    start_row, start_col = get_starting_point(data)
    instructions = PATROL_RULES[data[start_row][start_col]]
    for key, value in instructions.items():
        new_row = start_row + key[0]
        new_col = start_col + key[1]

        if len(data) > new_row >= 0 and len(data[0]) > new_col >= 0:
            new_location = data[new_row][new_col]
            # Check what new location needs to be updated to
            for inner_key, inner_value in value.items():
                if new_location == inner_key:
                    data[start_row][start_col] = inner_value[0]
                    data[new_row][new_col] = inner_value[1]
        # The guard is at the edge and can leave
        else:
            return data, True
    return data, False


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    # The data gets manipulated in part one so take a copy
    # here before it's changed so part two is using the original data
    copied_data = copy.deepcopy(data)

    solution_one = part_one(data)
    solution_two = part_two(copied_data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=6)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
