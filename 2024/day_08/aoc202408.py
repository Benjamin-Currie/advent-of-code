from collections import defaultdict
from aocd.models import Puzzle
from itertools import product


def parse(puzzle_input):
    """Parse input."""
    map_dict = defaultdict(list)
    split_puzzle = puzzle_input.split()
    for ri, row in enumerate(split_puzzle):
        for ci, col in enumerate(row):
            if col != ".":
                map_dict[col].append((ri, ci))
    map_dict["size"] = len(split_puzzle) - 1
    return map_dict


def part_one(data):
    """Solve part 1."""
    antinode_coords = set()
    for k, v in data.items():
        if k != "size":
            for i, coord in enumerate(v):
                if i == len(v) - 1:
                    break
                other_coords = [[j[0], j[1]] for j in v[i + 1 :]]
                difference = [
                    (abs(coord[0] - x[0]), abs(coord[1] - x[1]))
                    for x in [[j[0], j[1]] for j in v[i + 1 :]]
                ]
                for di, diff in enumerate(difference):
                    new_coord_one, new_coord_two = calculate_antinode_coords(
                        coord, other_coords, diff, di
                    )
                    update_antinodes(new_coord_one, antinode_coords, data)
                    update_antinodes(new_coord_two, antinode_coords, data)
    return len(antinode_coords)


def part_two(data):
    """Solve part 2."""
    antinode_coords = set()
    for k, v in data.items():
        if k != "size":
            for i, coord in enumerate(v):
                if len(v) >= 2:
                    antinode_coords.add(coord)
                if i == len(v) - 1:
                    break
                other_coords = [[j[0], j[1]] for j in v[i + 1 :]]
                difference = [
                    (abs(coord[0] - x[0]), abs(coord[1] - x[1]))
                    for x in [[j[0], j[1]] for j in v[i + 1 :]]
                ]
                for di, diff in enumerate(difference):
                    original_diff = diff
                    while data["size"] >= diff[0] >= 0 and data["size"] >= diff[1] >= 0:
                        new_coord_one, new_coord_two = calculate_antinode_coords(
                            coord, other_coords, diff, di
                        )
                        update_antinodes(new_coord_one, antinode_coords, data)
                        update_antinodes(new_coord_two, antinode_coords, data)
                        diff = (diff[0] + original_diff[0], diff[1] + original_diff[1])
    return len(antinode_coords)


def update_antinodes(coord, antinodes, data):
    if (
        data["size"] >= coord[0] >= 0
        and data["size"] >= coord[1] >= 0
        and coord not in antinodes
    ):
        antinodes.add(coord)


def calculate_antinode_coords(coord, other_coords, diff, di):
    diagonal_right = coord[1] < other_coords[di][1]
    vertical = coord[1] == other_coords[di][1]
    horizontal = coord[0] == other_coords[di][0]
    if diagonal_right:
        new_coord_one = (coord[0] - diff[0], coord[1] - diff[1])
        new_coord_two = (
            other_coords[di][0] + diff[0],
            other_coords[di][1] + diff[1],
        )
    elif vertical:
        new_coord_one = (coord[0] - diff[0], coord[1])
        new_coord_two = (other_coords[di][0] + diff[0], coord[1])
    elif horizontal:
        new_coord_one = (coord[0], coord[1] - diff[1])
        new_coord_two = (coord[0], coord[1] + diff[1])
    else:
        new_coord_one = (coord[0] - diff[0], coord[1] + diff[1])
        new_coord_two = (
            other_coords[di][0] + diff[0],
            other_coords[di][1] - diff[1],
        )
    return new_coord_one, new_coord_two


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=8)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
