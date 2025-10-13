import os
import sys
from linguis import ast

def main(args : list[str] = []) -> None:
    print("Hello from linguis!")
    for arg in sys.argv[1:]:
        print(f"  Arg: {arg}")

if __name__ == "__main__":
    main(sys.argv)
