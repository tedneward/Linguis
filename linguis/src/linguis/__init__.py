import os
import sys
from linguis import ast

def main(args : list[str] = []) -> None:
    print("Hello from linguis!")
    for arg in args:
        print(f"  Arg: {arg}")
    ast.hello()

if __name__ == "__main__":
    main(sys.argv)
