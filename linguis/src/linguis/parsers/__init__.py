from typing import Any, Dict, List, Optional, Sequence
from linguis.ast import *

class LinguisParser:
    """ A base class for parsers for Linguis. """
    def __init__(self) -> None:
        pass

    def builtins(self) -> Dict[str, Any]:
        """ Returns a dictionary of built-in functions available in this parser's environment. """
        return { }

    def parse(self, code: str) -> Block:
        """ Parses the entire code into a Block AST node. """

        # For simplicity, this is a stub implementation.
        # A real parser would tokenize and parse the input properly.
        return Block([])

parsers : Dict[str, LinguisParser] = {}

def register_parser(name: str, parser_cls: type[LinguisParser]) -> None:
    """ Registers a parser class under a given name/nationality. """
    parsers[name] = parser_cls

def find_parser(language: str) -> Optional[LinguisParser]:
    """ 
    Finds a parser by name/nationality. If found, instantiates an instance and returns it. 

    If not found, returns None.
    """
    parser_cls = parsers.get(language)
    if parser_cls:
        return parser_cls("")
    return None

from linguis.parsers.en_us import ENUSParser
register_parser("en-us", ENUSParser)
