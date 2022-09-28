import pytest

from aoc_2016.day_01.a import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 226
