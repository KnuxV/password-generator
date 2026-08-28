"""Strong password generator.

Two kinds of password:
- memorable: random words from the EFF long wordlist ("Stubbed Congress Tiptop")
- random: mixed characters ("aB3$cD9#eF2@")

Command line:
    uv run strong_password.py -t memorable -l 5
    uv run strong_password.py -t random -l 16

From Python:
    >>> gen = StrongPassword(length=5, type_p=TypePassword.MEMORABLE)
    >>> password = gen.generate()
"""

import argparse
import secrets
from enum import StrEnum, auto
from pathlib import Path

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?"
CHAR_SETS = [LOWERCASE, UPPERCASE, DIGITS, SPECIAL]

# The wordlist sits next to this file, so the script works from any folder.
WORDLIST_FILE = Path(__file__).parent / "data" / "eff_large_wordlist.txt"
with open(WORDLIST_FILE, encoding="utf-8") as f:
    # each line is "11111<TAB>abacus": keep the word, capitalise it
    WORD_LIST = [line.split()[1].capitalize() for line in f]


class TypePassword(StrEnum):
    """The two kinds of password this tool can generate."""

    MEMORABLE = auto()  # "memorable": words from the EFF wordlist
    RANDOM = auto()  # "random": mixed characters


class StrongPassword:
    """A password generator.

    Attributes:
        length: number of words (memorable) or characters (random).
        type_p: which kind of password to generate.
    """

    def __init__(self, length: int, type_p: TypePassword):
        self.length = length
        self.type_p = type_p

    def generate(self) -> str:
        """Generate a password of the configured type."""
        match self.type_p:
            case TypePassword.MEMORABLE:
                return self.generate_memorable()
            case TypePassword.RANDOM:
                return self.generate_random()
            case _:
                raise ValueError(f"Unknown password type: {self.type_p}")

    def generate_memorable(self) -> str:
        """Pick `length` words from the EFF wordlist (7776 words), capitalised,
        separated by spaces: "Stubbed Congress Tiptop"."""
        words = [secrets.choice(WORD_LIST) for _ in range(self.length)]
        return " ".join(words)

    def generate_random(self) -> str:
        """Build `length` characters, cycling through the four character sets
        (lowercase, uppercase, digit, special) so that each kind is present
        when length >= 4, then shuffle: "aB3$cD9#eF2@"."""
        password = [secrets.choice(CHAR_SETS[i % 4]) for i in range(self.length)]
        secrets.SystemRandom().shuffle(password)
        return "".join(password)


def main() -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(
        prog="strong_password",
        description="Generate a strong password.",
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=[t.value for t in TypePassword],
        required=True,
        help="'memorable' (words) or 'random' (characters)",
    )
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="number of words (memorable) or characters (random); default: 12",
    )
    args = parser.parse_args()

    generator = StrongPassword(length=args.length, type_p=TypePassword(args.type))
    print(generator.generate())


if __name__ == "__main__":
    main()
