from argparse import ArgumentParser, Namespace
from typing import List


def parse_args(inputted_args: List[str]) -> Namespace:
    parser = ArgumentParser(
        description="Test library for building python package.")

    parser.add_argument(
        "yaml_file",
        nargs=1,
        help="Input YAML file"
    )

    args = parser.parse_args(inputted_args)

    return args
