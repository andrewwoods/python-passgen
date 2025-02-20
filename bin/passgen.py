#!/usr/bin/env python3

__version__ = "0.1.1"
__author__ = "Andrew Woods"

import argparse
import os
import sys
import string
import random


def main():
    DEFAULT_PASSWORD_LENGTH = 16
    DEFAULT_PIN_LENGTH = 6

    parser = argparse.ArgumentParser(
        prog="passgen.py",
        description="Generate a secure random value for your authentication system",
        epilog="by Andrew Woods",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )

    subparsers = parser.add_subparsers(title="command")

    pin_parser = subparsers.add_parser("pin")
    pin_parser.set_defaults(which="pin")
    pin_parser.add_argument(
        "--length",
        type=int,
        default=DEFAULT_PIN_LENGTH,
        action="store",
        help="The quantity of characters in your password",
    )

    random_parser = subparsers.add_parser("random")
    random_parser.set_defaults(which="random")
    random_parser.add_argument(
        "--numbers",
        action="store_true",
        help="Include numbers in your generated password",
    )
    random_parser.add_argument(
        "--symbols",
        action="store_true",
        help="Include symbols in your generated password",
    )
    random_parser.add_argument(
        "--length",
        type=int,
        default=DEFAULT_PASSWORD_LENGTH,
        action="store",
        help="Quantity of characters in your password",
    )
    args = parser.parse_args()

    result = ""
    if hasattr(args, "which"):
        if args.which == "random":
            gen = PasswordGenerator(args.numbers, args.symbols, args.length)
            result = gen.get()
        elif args.which == "pin":
            if args.length == DEFAULT_PASSWORD_LENGTH:
                args.length = DEFAULT_PIN_LENGTH

            gen = PinGenerator(args.length)
            result = gen.get()
    else:
        parser.print_help()

    print(f"\n{result}\n")


class PasswordGenerator:
    length = 16
    withNumbers = False
    withSymbols = False
    values = ""

    def __init__(self, withNumbers, withSymbols, length):
        self.withNumbers = withNumbers
        self.withSymbols = withSymbols
        self.length = length

    def get(self):
        self.values += string.ascii_letters
        if self.withNumbers == True:
            self.values += "0123456789"
        if self.withSymbols == True:
            self.values += "!@#$%^&*(),./<>?"

        output = ""
        i = 0
        while i < self.length:
            randomIndex = random.randint(0, len(self.values) - 1)
            letter = self.values[randomIndex]
            output += letter
            i += 1

        return output


class PinGenerator:
    length = 6
    values = ""

    def __init__(self, length):
        self.length = length

    def get(self):
        self.values += "0123456789"

        output = ""
        i = 0
        while i < self.length:
            randomIndex = random.randint(0, len(self.values) - 1)
            letter = self.values[randomIndex]
            output += letter
            i += 1

        return output


if not __package__:
    # Make CLI runnable from source tree with
    #    python src/package
    package_source_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, package_source_path)

if __name__ == "__main__":
    main()
