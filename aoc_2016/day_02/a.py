from dataclasses import dataclass
from typing import Optional, Sequence
from aoc_2016.day_02.parser import Parser
from aoc_2016.day_02.shared import Direction, Instruction


@dataclass
class Day02PartASolver:
    instructions: Sequence[Instruction]
    pad: dict[tuple[int, int], str]

    @property
    def solution(self) -> str:
        y, x = self.starting_pos
        output = ""
        for instruction in self.instructions:
            for d in instruction.directions:
                move: Optional[tuple[int, int]]
                match d:
                    case Direction.UP:
                        move = (-1, 0)
                    case Direction.RIGHT:
                        move = (0, 1)
                    case Direction.DOWN:
                        move = (1, 0)
                    case Direction.LEFT:
                        move = (0, -1)
                i, j = move
                next_pos = (y+i, x+j)
                if next_pos in self.pad:
                    y, x = next_pos
            output += self.pad[(x, y)]
        return output

    @property
    def starting_pos(self) -> tuple[int, int]:
        rows = max([row for row, _ in self.pad.keys()])
        cols = max([col for _, col in self.pad.keys()])
        return rows // 2, cols // 2


PAD = """
1 2 3
4 5 6
7 8 9
"""


def solve(input: str) -> int:
    instructions = Parser.parse(input)
    pad = Parser.parse_pad(PAD)
    solver = Day02PartASolver(instructions, pad)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2016/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
