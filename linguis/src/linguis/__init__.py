import os
import sys
from linguis import ast
from linguis import parsers as parsers

def main() -> None:
    print("Linguis v0.2; interpreter starting up...")
    parser = "en-us"
    incoming = []
    for arg in sys.argv[1:]:
        print(f"  Arg: {arg}")
        if arg.startswith("--parser="):
            parser = arg[len("--parser="):]
        else:
            incoming.append(arg)

    p = parsers.find_parser(parser)
    if not p:
        print(f"ERROR: Could not find parser named '{parser}'; exiting.")
        sys.exit(1)

    #print(f"Using parser: {parser} to parse {incoming}")

    for fname in incoming:
        if not os.path.exists(fname):
            print(f"File '{fname}' does not exist!")
            sys.exit(1)
        else:
            print(f"Processing file '{fname}'... from {os.getcwd()}")
            ast = p.parse(fname)
            #env = ast.Environment(bindings=p.builtins())
            #ast.eval(env)

if __name__ == "__main__":
    main()
