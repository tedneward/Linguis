import os
import sys
from linguis import ast
from linguis import parsers as parsers

def main(args : list[str] = []) -> None:
    print("Linguis v0.2; interpreter starting up...")
    parser = "en-us"
    for arg in sys.argv[1:]:
        print(f"  Arg: {arg}")
        if arg.startswith("--parser="):
            parser = arg[len("--parser="):]
    print(f"Using parser: {parser}")
    p = parsers.find_parser(parser)
    if not p:
        print(f"Could not find parser named '{parser}'")
        sys.exit(1)
    print(f"Parser class: {p.__class__.__name__}")

if __name__ == "__main__":
    main(sys.argv)
