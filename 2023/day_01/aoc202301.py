from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()

def part_one(data):
    """Solve part 1."""
    return sum(
        int(f"{numbers[0]}{numbers[-1]}")
        for d in data
        if (numbers := [i for i in list(d) if i.isnumeric()])
    )


def part_two(data):
    """Solve part 2."""
    number_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    total = 0
    for word in data:
        numbers = []
        for letter_index, letter in enumerate(word):
            if letter.isnumeric():
                numbers.append(letter)
                continue
            for key in number_map.keys():
                if word[letter_index:].startswith(key):
                    numbers.append(number_map[key])
        total += int(f"{numbers[0]}{numbers[-1]}")
    return total

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two

if __name__ == "__main__":
    puzzle = Puzzle(year=2023, day=1)
    puzzle_input = puzzle.input_data
    with open('input.txt', 'w') as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
