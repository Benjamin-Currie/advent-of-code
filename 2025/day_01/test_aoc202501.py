import pathlib
import pytest
import aoc202501 as aoc

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
        ("L", 68),
        ("L", 30),
        ("R", 48),
        ("L", 5),
        ("R", 60),
        ("L", 55),
        ("L", 1),
        ("L", 99),
        ("R", 14),
        ("L", 82),
    ]


def test_get_new_index():
    """Test get_new_index returns the correct index"""
    safe_nums = [i for i in range(0, 100)]
    assert aoc.get_new_index(50, "R", 10, safe_nums) == 60
    assert aoc.get_new_index(95, "R", 10, safe_nums) == 5
    assert aoc.get_new_index(50, "L", 10, safe_nums) == 40
    assert aoc.get_new_index(5, "L", 10, safe_nums) == 95


def test_part_one_example_one(example_one):
    """Test part 1 on example input."""
    assert aoc.part_one(example_one) == 3


def test_part_two_example_one(example_one):
    """Test part 2 on first example input."""
    assert aoc.part_two(example_one) == 6


@pytest.mark.skip(reason="Not needed")
def test_part_two_example_two(example_two):
    """Test part 2 on second example input."""
    assert aoc.part_two(example_two) == ...
