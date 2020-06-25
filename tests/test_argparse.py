# coding: utf-8

from kyoho.argparse import parse_args


def test_argparse():
    actually = parse_args(["test.yaml"])

    assert actually.yaml_file[0] == "test.yaml"
