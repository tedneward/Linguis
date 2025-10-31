import os
import sys

import pylinguis.parsers

def banner() -> str:
    vMajor, vMinor = version()
    return f"Linguis v{vMajor}.{vMinor}"

# v0.1 was basic parser infrastructure
# v0.2 is EN-US parser implementation
# v0.3 will be EN-PL parser implementation
# v0.4 will be FR parser
# v0.5 will be DE parser
def version() -> tuple[int, int]:
    return [0, 2]

def print_help() -> None:
    print("Usage: linguis [--parser=parsername] sourcefile")
    print("  --parser=parsername   Specifies which parser to use (default: en-us)")
    print("  --help, -h            Show this help message")
    sys.exit(0)

def main() -> None:
    print(f"{banner()}")

    parser = "en-us"
    incoming = []
    if len(sys.argv) < 2:
        print_help()
    for arg in sys.argv[1:]:
        if arg.startswith("--parser="):
            parser = arg[len("--parser="):]
        elif arg == "--help" or arg == "-h":
            print_help()
        else:
            incoming.append(arg)

    p = pylinguis.parsers.find_parser(parser)
    if not p:
        print(f"ERROR: Could not find parser named '{parser}'; exiting.")
        sys.exit(1)

    for fname in incoming:
        if not os.path.exists(fname):
            print(f"File '{fname}' does not exist!")
            sys.exit(1)
        else:
            print(f"Processing file '{fname}'...")

            # Get the code into a string!
            module = p.parse_file(fname)
            code = compile(module, filename=fname, mode="exec")
            localvars = {}
            globalvars = globals() # Later ask parser to fill in globals
            exec(code, globalvars, localvars)

if __name__ == "__main__":
    main()
