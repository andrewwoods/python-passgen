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
        usage="bin/passgen.py <passtype>",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    parser.add_argument(
        "passtype",
        choices=["random", "pin"],
        help="The type of generated value can be: random, or pin",
    )
    parser.add_argument(
        "--length",
        type=int,
        default=DEFAULT_PASSWORD_LENGTH,
        help="The quantity of characters in your password",
    )
    parser.add_argument(
        "--numbers",
        action="store_true",
        help="Include numbers in your generated password",
    )
    parser.add_argument(
        "--symbols",
        action="store_true",
        help="Include symbols in your generated password",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Show debug information",
    )

    args = parser.parse_args()

    if len(vars(args)) == None:
        parser.print_help()
    else:

        if args.debug == True:
            print("Your code goes here")
            print("-------------------")
            print(f"Password Type: {args.passtype}")
            print(f"Has Numbers: {args.numbers}")
            print(f"Has Symbols: {args.symbols}")
            print(f"Length: {args.length}")

        result = ""
        if args.passtype == "random":
            gen = PasswordGenerator(args.numbers, args.symbols, args.length)
            result = gen.get()
        elif args.passtype == "pin":
            if args.length == DEFAULT_PASSWORD_LENGTH:
                args.length = DEFAULT_PIN_LENGTH

            gen = PinGenerator(args.length)
            result = gen.get()
        else:
            print("The type you've chosen is not valid")

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
