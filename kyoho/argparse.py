from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description="Test library for building python package.")

    parser.add_argument(
        "yaml_file",
        nargs=1,
        help="Input YAML file"
    )

    args = parser.parse_args()

    return args
