#!/usr/bin/env python3
from argparse import ArgumentParser
from json import load
from pathlib import Path
from jsonschema import validate
from ruamel.yaml import YAML


def parse_args():
    parser = ArgumentParser(
        description='Validator for the Open Recipe Format',
    )

    parser.add_argument(
        'file_path',
        help='Path to file to validate'
    )

    return parser.parse_args()


def validate_recipe(file_path):
    this_dir = Path(__file__).parent.resolve()
    with Path(this_dir, 'schema.json').open() as schema_file:
        schema = load(schema_file)

    yaml = YAML(typ='safe')
    with open(file_path) as orf_file:
        recipe = yaml.load(orf_file)

    validate(
        instance=recipe,
        schema=schema,
    )


if __name__ == '__main__':
    args = parse_args()
    validate_recipe(args.file_path)
