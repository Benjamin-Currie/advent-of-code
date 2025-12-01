import re
from aocd.models import Puzzle
from collections import defaultdict, Counter


def parse(puzzle_input):
    """Parse input."""
    file_id = 0
    file_blocks = []
    for i, char in enumerate(puzzle_input):
        # file
        if i % 2 == 0:
            for _ in range(int(puzzle_input[i])):
                file_blocks.append(file_id)
            file_id += 1
        # free space
        else:
            for _ in range(int(puzzle_input[i])):
                file_blocks.append(".")
    return file_blocks


def part_one(data):
    """Solve part 1."""
    all_digits = [x for x in data if x != "."]
    moves_to_make = len(all_digits)
    total = 0
    # Loop through each file block and multiply that by the current index
    for i, char in enumerate(data):
        if i == moves_to_make:
            break
        multiply_by = char
        # If the character is an X then pop the last number from the file data and use that
        if multiply_by == ".":
            multiply_by = all_digits.pop()
        total += i * int(multiply_by)
    return total


class OrderedCounter(Counter):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return f"{self.__class__.__name__} {dict(self)}"

    def __reduce__(self):
        return self.__class__, (dict(self))


def part_two(data):
    """Solve part 2."""
    all_digits = [x for x in data if x != "."]
    ordered_counter = OrderedCounter(all_digits)
    print(ordered_counter)
    new_string = ""
    total = 0
    no_of_spaces = 0
    print("data: ", data)
    for i, char in enumerate(data):
        moved_char = None
        if no_of_spaces > 0:
            no_of_spaces -= 1
            continue
        # If the character is a . then check how many more .'s there are and pop the last number from the list
        if char == ".":
            no_of_spaces += 1
            another_space = True
            while another_space:
                next_char = data[i+no_of_spaces]
                if next_char == ".":
                    no_of_spaces += 1
                else:
                    another_space = False
            print("No of spaces: ", no_of_spaces)
            # Loop through the options in reverse order and see if they will fit
            for k, v in sorted(list(ordered_counter.items()), reverse=True):
                if len(str(k)) * v <= no_of_spaces:
                    new_string += str(k) * v
                    new_string += char * (no_of_spaces - len(str(k) * v))
                    # Remove this option from the list
                    ordered_counter.pop(k)
                    moved_char = k
                    break
                else:
                    continue
        else:
            new_string += str(char)
        if moved_char:
            new_data = []
            for d in data:
                new_data.append(d) if d != k else "."
            data = new_data
    print(data)
    print(new_string)
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=9)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
