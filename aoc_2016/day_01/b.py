from dataclasses import dataclass

from aoc_2016.day_01.parser import Parser
from aoc_2016.day_01.shared import Day01Solver


@dataclass
class Day01PartBSolver(Day01Solver):
    @property
    def solution(self) -> int:
        visited: set[tuple[int, int]] = set()
        for pos in self.get_positions():
            if pos in visited:
                x, y = pos
                return self.position_to_dist(x, y)
            else:
                visited.add(pos)
        assert False, "We can't get here!"


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2016/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
