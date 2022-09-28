from aoc_2016.day_02.b import get_solution, solve

SAMPLE_INPUT = """
ULL
RRDDD
LURDL
UUUUD
"""


def test_solve():
    assert solve(SAMPLE_INPUT) == "5DB3"


def test_my_solution():
    assert get_solution() == "CD8D4"
