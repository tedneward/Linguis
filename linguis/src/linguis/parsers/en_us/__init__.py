from typing import Any, List, Optional
from antlr4 import *

from linguis.ast import *
from .. import LinguisParser, EvaluationError

if "." in __name__:
    from .LinguisENUSLexer import LinguisENUSLexer
    from .LinguisENUSListener import LinguisENUSListener
    from .LinguisENUSParser import LinguisENUSParser
else:
    from LinguisENUSLexer import LinguisENUSLexer
    from LinguisENUSListener import LinguisENUSListener
    from LinguisENUSParser import LinguisENUSParser


class ENUSParser(LinguisParser):
    class Listener(LinguisENUSListener):
        def __init__(self) -> None:
            super().__init__()
        
        def enterBlock(self, ctx: Any) -> None:
            print("ENTER BLOCK")

        def exitBlock(self, ctx: Any) -> None:
            print("EXIT BLOCK")


    """ A parser for US English Linguis code. """
    def parse(self, fname: str) -> Block:

        # A real implementation would go here.
        incoming = FileStream(fname)
        lexer = LinguisENUSLexer(incoming)
        stream = CommonTokenStream(lexer)
        parser = LinguisENUSParser(stream)
        tree = parser.block()

        walker = ParseTreeWalker()
        walker.walk(ENUSParser.Listener(), tree)

        return Block([])

    def builtins(self) -> Dict[str, Any]:
        return {
            "assert": lambda condition: condition or (_ for _ in ()).throw(EvaluationError("Assertion failed")),
            "input": lambda prompt=None: input(prompt) if prompt is not None else input(),
            "println": lambda *args: print(*args),
            "print": lambda *args: print(*args, end=""),
            "size": lambda lst: len(lst) if isinstance(lst, list) else 0,
        }
