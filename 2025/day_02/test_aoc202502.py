import pathlib
import pytest
import aoc202502 as aoc

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
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]


def test_is_repeat():
    """Test is_repeat function returns correct value"""
    assert aoc.is_repeat("1212", 2) is True
    assert aoc.is_repeat("123123", 3) is True
    assert aoc.is_repeat("1234", 2) is False
    assert aoc.is_repeat("12345", 2) is False


def test_part_one_example_one(example_one):
    """Test part 1 on example input."""
    assert aoc.part_one(example_one) == 1227775554


def test_part_two_example_one(example_one):
    """Test part 2 on first example input."""
    assert aoc.part_two(example_one) == 4174379265


@pytest.mark.skip(reason="Not needed")
def test_part_two_example_two(example_two):
    """Test part 2 on second example input."""
    assert aoc.part_two(example_two) == ...
