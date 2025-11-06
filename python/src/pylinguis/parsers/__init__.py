from typing import Dict, Optional

from .LinguisParserBase import LinguisParserBase
from .ANTLRSupport import ANTLRParserBase # Used by other files importing this one; do not remove

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
from pylinguis.parsers.enpl import ENPLParser
register_parser("en-pl", ENPLParser)
#from pylinguis.parsers.fr import FRParser
#register_parser("fr", FRParser)
#from pylinguis.parsers.de import DEParser
#register_parser("de", DEParser)
