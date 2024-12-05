from collections import defaultdict
from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input into ordering rules and page numbers."""
    sections = puzzle_input.split("\n\n")
    rules = defaultdict(list)
    page_numbers = []

    for section in sections:
        if "|" in section:
            for line in section.split("\n"):
                key, value = line.split("|")
                rules[key].append(value)
        else:
            page_numbers.append([row.split(",") for row in section.split("\n")])

    return rules, page_numbers[0]


def part_one(data):
    """Solve part 1."""
    rules = data[0]
    pages = data[1]
    total = 0
    for page in pages:
        if all_rules_pass(page, rules):
            total += int(page[len(page) // 2])
    return total


def part_two(data):
    """Solve part 2."""
    rules = data[0]
    pages = data[1]
    total = 0
    for page in pages:
        if not all_rules_pass(page, rules):
            correctly_ordered_page = correct_ordering(page, rules)
            total += int(correctly_ordered_page[len(page) // 2])
    return total


def all_rules_pass(page, rules):
    all_rules_passed = True
    for index, page_number in enumerate(page):
        valid_pages_to_be_ahead = rules[page_number]
        if all_rules_passed:
            if not all(x in valid_pages_to_be_ahead for x in page[index + 1 :]):
                all_rules_passed = False
    return all_rules_passed


def correct_ordering(page, rules):
    """Swap the values over based on the rules until no more swaps are needed"""
    new_page = []
    correct_order = False
    while not correct_order:
        correct_order = True
        for number_index, number in enumerate(page):
            if number_index == len(page) - 1:
                continue
            if number in rules[page[number_index + 1]]:
                # swap the current number with the next one
                page[number_index + 1], page[number_index] = (
                    page[number_index],
                    page[number_index + 1],
                )
                correct_order = False
    return page


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution_one = part_one(data)
    solution_two = part_two(data)

    return solution_one, solution_two


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=5)
    puzzle_input = puzzle.input_data
    with open("input.txt", "w") as input_file:
        input_file.write(puzzle_input)
    solutions = solve(puzzle_input)
    print(f"Part One: {solutions[0]}\nPart Two: {solutions[1]}")
