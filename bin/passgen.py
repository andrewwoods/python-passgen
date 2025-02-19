#!/usr/bin/env python3

__version__ = "0.0.0"
__author__ = "Andrew Woods"

import argparse
import os
import sys


def main():
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
        choices=["random"],
        help="The type of generated value can be: random",
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

        result = ""
        if args.passtype == "random":
            gen = PasswordGenerator(args.numbers, args.symbols)
            result = gen.get()
        else:
            print("The type you've chosen is not valid")

        print(f"\n{result}\n")


class PasswordGenerator:
    length = 16
    withNumbers = False
    withSymbols = False

    def __init__(self, withNumbers, withSymbols):
        self.withNumbers = withNumbers
        self.withSymbols = withSymbols

    def get(self):
        return "asdf1234qwer4321"


if not __package__:
    # Make CLI runnable from source tree with
    #    python src/package
    package_source_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, package_source_path)

if __name__ == "__main__":
    main()
