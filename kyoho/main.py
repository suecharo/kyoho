#!/usr/bin/env python3
# coding: utf-8

from kyoho.argparse import parse_args
from pathlib import Path


PWD = Path(__file__).resolve().parent
DATA_FILE_PATH = PWD.joinpath("data.txt")


def main():
    args = parse_args()
    print(f"Args: ${args}")
    with DATA_FILE_PATH.open(mode="r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
