import pathlib
import pytest
import aoc202408 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_one():
    puzzle_input = (PUZZLE_DIR / "example_one.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example_two():
    puzzle_input = (PUZZLE_DIR / "example_two.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example_one(example_one):
    """Test that input is parsed properly."""
    assert example_one == {
        "0": [(1, 8), (2, 5), (3, 7), (4, 4)],
        "A": [(5, 6), (8, 8), (9, 9)],
        "size": 11,
    }


def test_part_one_example_one(example_one):
    """Test part 1 on example input."""
    assert aoc.part_one(example_one) == 14


def test_part_two_example_one(example_one):
    """Test part 2 on first example input."""
    assert aoc.part_two(example_one) == 34


def test_part_two_example_two(example_two):
    """Test part 2 on second example input."""
    assert aoc.part_two(example_two) == 9
