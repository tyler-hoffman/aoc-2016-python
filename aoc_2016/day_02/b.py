from aoc_2016.day_02.parser import Parser
from aoc_2016.day_02.shared import Day02Solver

PAD = """
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""


def solve(input: str) -> str:
    instructions = Parser.parse(input)
    pad = Parser.parse_pad(PAD)
    solver = Day02Solver(instructions, pad)

    return solver.solution


def get_solution() -> str:
    with open("aoc_2016/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
