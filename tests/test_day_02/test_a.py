from aoc_2016.day_02.a import get_solution, solve

SAMPLE_INPUT = """
ULL
RRDDD
LURDL
UUUUD
"""


def test_solve():
    assert solve(SAMPLE_INPUT) == "1985"


def test_my_solution():
    assert get_solution() == "98575"
