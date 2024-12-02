import pathlib
import pytest
import aoc202402 as aoc

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
    assert example_one == [
        ["7", "6", "4", "2", "1"],
        ["1", "2", "7", "8", "9"],
        ["9", "7", "6", "2", "1"],
        ["1", "3", "2", "4", "5"],
        ["8", "6", "4", "4", "1"],
        ["1", "3", "6", "7", "9"],
    ]


def test_part_one_example_one(example_one):
    """Test part 1 on example input."""
    assert aoc.part_one(example_one) == 2


def test_part_two_example_one(example_one):
    """Test part 2 on first example input."""
    assert aoc.part_two(example_one) == 4


@pytest.mark.skip(reason="Not needed")
def test_part_two_example_two(example_two):
    """Test part 2 on second example input."""
    assert aoc.part_two(example_two) == ...
