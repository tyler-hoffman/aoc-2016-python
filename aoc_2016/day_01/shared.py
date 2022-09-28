from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Sequence


class Turn(Enum):
    LEFT = 0
    RIGHT = 1


@dataclass
class Instruction:
    turn: Turn
    count: int


@dataclass
class Direction:
    angle: tuple[int, int]


DIRECTIONS: Sequence[Direction] = [
    Direction((0, 1)),
    Direction((1, 0)),
    Direction((0, -1)),
    Direction((-1, 0)),
]


@dataclass
class Day01Solver:
    instructions: Sequence[Instruction]

    def position_to_dist(self, x: int, y: int) -> int:
        return abs(x) + abs(y)

    def get_positions(self) -> Iterable[tuple[int, int]]:
        direction_index = 0
        x, y = 0, 0
        for instruction in self.instructions:
            if instruction.turn == Turn.RIGHT:
                direction_index += 1
            else:
                direction_index -= 1
            direction = DIRECTIONS[direction_index % len(DIRECTIONS)]
            a, b = direction.angle
            for _ in range(instruction.count):
                x += a
                y += b
                yield x, y
