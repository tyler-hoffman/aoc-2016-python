from dataclasses import dataclass
from enum import Enum
from typing import Sequence


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


@dataclass
class Instruction:
    directions: Sequence[Direction]
