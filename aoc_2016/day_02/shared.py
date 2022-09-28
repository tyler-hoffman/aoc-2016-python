from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass
class Instruction:
    directions: Sequence[Direction]


@dataclass
class Day02Solver:
    instructions: Sequence[Instruction]
    pad: dict[tuple[int, int], str]

    @property
    def solution(self) -> str:
        x, y = self.starting_pos
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
                next_pos = (y + i, x + j)
                if next_pos in self.pad:
                    y, x = next_pos
            output += self.pad[(x, y)]
        return output

    @property
    def starting_pos(self) -> tuple[int, int]:
        for pos, value in self.pad.items():
            if value == "5":
                return pos
        assert False, "We can't get here"
