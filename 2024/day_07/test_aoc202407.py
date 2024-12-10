import pathlib
import pytest
import aoc202407 as aoc

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
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20],
    }


def test_part_one_example_one(example_one):
    """Test part 1 on example input."""
    assert aoc.part_one(example_one) == 3749


def test_part_two_example_one(example_one):
    """Test part 2 on first example input."""
    assert aoc.part_two(example_one) == 11387


@pytest.mark.skip(reason="Not implemented")
def test_part_two_example_two(example_two):
    """Test part 2 on second example input."""
    assert aoc.part_two(example_two) == ...
