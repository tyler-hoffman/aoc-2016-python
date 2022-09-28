from dataclasses import dataclass

from aoc_2016.day_01.parser import Parser
from aoc_2016.day_01.shared import Day01Solver


@dataclass
class Day01PartASolver(Day01Solver):
    @property
    def solution(self) -> int:
        x, y = 0, 0
        for i, j in self.get_positions():
            x, y = i, j
        return self.position_to_dist(x, y)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2016/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
