from ast import *
from typing import Any, Dict, Optional

class LinguisParserBase:
    """ A base class for parsers for Linguis. """
    def __init__(self) -> None:
        pass

    def builtins(self) -> Dict[str, Any]:
        """ Returns a dictionary of built-in functions available in this parser's environment. """
        return { }

    def parse(self, code: str) -> Module:
        """ Parses the entire code into a Python Module node. """

        # For simplicity, this is a stub implementation.
        # A real parser would tokenize and parse the input properly.
        return Module()

class EvaluationError(Exception):
    def __init__(self, message):
        super.__init__(self)
        self.message = message

parsers : Dict[str, LinguisParserBase] = {}

def register_parser(name: str, parser_cls: type[LinguisParserBase]) -> None:
    """ Registers a parser class under a given name/nationality. """
    # TODO: Verify parser_cls is a class and inherits from LinguisParserBase

    parsers[name] = parser_cls

def find_parser(language: str) -> Optional[LinguisParserBase]:
    """ 
    Finds a parser by name/nationality. If found, instantiates an instance and returns it. 

    If not found, returns None.
    """
    parser_cls = parsers.get(language)
    if parser_cls:
        # Instantiate and return
        return parser_cls()
    return None

# Register parser *classes* here (not instances)
from pylinguis.parsers.enus import ENUSParser
register_parser("en-us", ENUSParser)
#from pylinguis.parsers.fr import FRParser
#register_parser("fr", FRParser)
#from pylinguis.parsers.de import DEParser
#register_parser("de", DEParser)
