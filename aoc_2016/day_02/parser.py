from typing import Optional, Sequence
from .shared import Direction, Instruction


class Parser(object):
    @staticmethod
    def parse(input: str) -> Sequence[Instruction]:
        lines = input.strip().splitlines()
        return [Parser.parse_instruction(line) for line in lines]

    @staticmethod
    def parse_instruction(line: str) -> Instruction:
        return Instruction([Parser.parse_direction(d) for d in line])

    @staticmethod
    def parse_direction(char: str) -> Direction:
        match char:
            case "U":
                return Direction.UP
            case "R":
                return Direction.RIGHT
            case "D":
                return Direction.DOWN
            case "L":
                return Direction.LEFT
            case _:
                raise Exception(f"Unknown direction {char}")

    @staticmethod
    def parse_pad(input: str) -> dict[tuple[int, int], str]:
        lines = input.strip().splitlines()
        line_chars = [Parser.parse_pad_line(line) for line in lines]
        output: dict[tuple[int, int], str] = {}
        for y, row in enumerate(line_chars):
            for x, char in enumerate(row):
                if char is not None:
                    output[(x, y)] = char
        return output

    @staticmethod
    def parse_pad_line(line: str) -> list[Optional[str]]:
        return [Parser.parse_pad_char(x) for i, x in enumerate(line) if i % 2 == 0]

    @staticmethod
    def parse_pad_char(ch: str) -> Optional[str]:
        return ch if ch != " " else None
