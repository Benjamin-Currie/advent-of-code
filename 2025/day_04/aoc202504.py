from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [[i for i in line] for line in puzzle_input.split("\n")]


def get_neighbors(start_x, start_y, grid):
    neighbors = []
    # Directions for all 8 possible movements (N, S, E, W, NE, NW, SE, SW)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        neighbour_x, neighbour_y = start_x + dx, start_y + dy
        # Check if the neighbor is within the grid bounds
        if 0 <= neighbour_x < len(grid) and 0 <= neighbour_y < len(grid[0]):
            neighbors.append((neighbour_x, neighbour_y))
    return neighbors


def part_one(data):
    """Solve part 1."""
    total = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            count = 0
            if data[x][y] == "@":
                neighbors = get_neighbors(x, y, data)
                for nx, ny in neighbors:
                    count += 1 if data[nx][ny] == "@" else 0
                if count < 4:
                    total += 1
    return total


def search_and_destroy(data):
    total = 0
    items_to_update = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            count = 0
            if data[x][y] == "@":
                neighbors = get_neighbors(x, y, data)
                for nx, ny in neighbors:
                    count += 1 if data[nx][ny] == "@" else 0
                if count < 4:
                    total += 1
                    items_to_update.append((x, y))
    return total, items_to_update


def part_two(data):
    """Solve part 2."""
    grand_total = 0
    changes_being_made = True
    while changes_being_made:
        total, items_to_update = search_and_destroy(data)
        grand_total += total
        for x, y in items_to_update:
            data[x][y] = "."
        if not items_to_update:
            changes_being_made = False
    return grand_total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2025, day=4)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
