from typing import Sequence
from .shared import Instruction, Turn


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[Instruction]:
        chunks = input.strip().split(", ")
        output: list[Instruction] = []
        for chunk in chunks:
            turn = Parser.parse_turn(chunk[0])
            count = int(chunk[1:])
            output.append(Instruction(turn, count))
        return output

    @staticmethod
    def parse_turn(char: str) -> Turn:
        match char:
            case "L":
                return Turn.LEFT
            case "R":
                return Turn.RIGHT
            case _:
                raise Exception(f"Unknown direction {char}")