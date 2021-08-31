import re
import pathlib
from typing import List

from .user import User


class Parser:
    @staticmethod
    def parse_file(file: str) -> List[User]:
        Parser._validate_file(file)
        return [User(*line.split()) for line in Parser._get_clean_file_in_lines(file)]

    @staticmethod
    def _validate_file(file: str) -> None:
        if not pathlib.Path(file).is_file():
            raise FileNotFoundError(f"file {file} not found")

        if faulty_lines := [line for line in Parser._get_clean_file_in_lines(file) if line.count(" ") != 1]:
            lines = "\n".join(faulty_lines)
            raise ValueError(f"file not formatted correctly. see lines:\n{lines}")

    @staticmethod
    def _get_clean_file_in_lines(file: str) -> List[str]:
        return [
            re.sub(r"\s+", " ", line.strip())
            for line in pathlib.Path(file).read_text().splitlines()
            if not Parser._is_empty_or_comment(line)
        ]

    @staticmethod
    def _is_empty_or_comment(string: str) -> bool:
        return (not string) or string.isspace() or string.strip().startswith("#") or string.strip().startswith("//")
