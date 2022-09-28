import pytest

from aoc_2016.day_01.b import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("R8, R4, R4, R8", 4),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 79
