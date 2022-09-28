from dataclasses import dataclass
from enum import Enum
from typing import Sequence


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
