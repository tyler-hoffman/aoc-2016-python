from dataclasses import dataclass
from typing import Sequence
from aoc_2016.day_01.parser import Parser
from aoc_2016.day_01.shared import DIRECTIONS, Instruction, Turn


@dataclass
class Day01PartASolver:
    instructions: Sequence[Instruction]

    @property
    def solution(self) -> int:
        direction_index = 0
        x, y = 0, 0
        for instruction in self.instructions:
            if instruction.turn == Turn.RIGHT:
                direction_index += 1
            else:
                direction_index -= 1
            direction = DIRECTIONS[direction_index % len(DIRECTIONS)]
            a, b = direction.angle
            x += a * instruction.count
            y += b * instruction.count
        return abs(x) + abs(y)


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
