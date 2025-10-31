import ast
from typing import Any, Dict, List

class LinguisParserBase:
    """ A base class for parsers for Linguis. """
    def __init__(self) -> None:
        pass

    def builtins(self) -> Dict[str, Any]:
        """ Returns a dictionary of built-in functions available in this parser's environment. """
        return { }

    def parse(self, code: str) -> ast.Module:
        """ Parses the entire code into a Python Module node. """

        # For simplicity, this is a stub implementation.
        # A real parser would tokenize and parse the input properly.
        raise Exception("E_NOTIMPL")
    
    def parse_file(self, filename: str) -> ast.Module:
        """ Takes  file and dumps its contents into self.parse()"""

        raise Exception("E_NOTIMPL")
