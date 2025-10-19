import ast
import os
import sys

import parsers

def main() -> None:
    print("Linguis v0.2; interpreter starting up...")
    parser = "en-us"
    incoming = []
    for arg in sys.argv[1:]:
        if arg.startswith("--parser="):
            parser = arg[len("--parser="):]
        elif arg == "--help" or arg == "-h":
            print("Usage: linguis [--parser=parsername] sourcefile1 [sourcefile2 ...]")
            print("  --parser=parsername   Specifies which parser to use (default: en-us)")
            print("  --help, -h           Show this help message")
            sys.exit(0)
        else:
            incoming.append(arg)

    p = parsers.find_parser(parser)
    if not p:
        print(f"ERROR: Could not find parser named '{parser}'; exiting.")
        sys.exit(1)

    for fname in incoming:
        if not os.path.exists(fname):
            print(f"File '{fname}' does not exist!")
            sys.exit(1)
        else:
            print(f"Processing file '{fname}'...")
            module = p.parse(fname)
            code = compile(module, filename=fname, mode="exec")
            local_vars = {}
            globalvars = globals() # Later ask parser to fill in globals
            exec(code, globalvars, local_vars)

if __name__ == "__main__":
    main()
