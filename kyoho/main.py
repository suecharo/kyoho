#!/usr/bin/env python3
# coding: utf-8

from pathlib import Path
from sys import argv

from kyoho.argparse import parse_args

PWD = Path(__file__).resolve().parent
DATA_FILE_PATH = PWD.joinpath("data.txt")


def main() -> None:
    args = parse_args(argv[1:])
    print(f"Args: ${args}")
    with DATA_FILE_PATH.open(mode="r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
