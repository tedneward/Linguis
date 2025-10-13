from typing import Any, List, Optional
from linguis.ast import *
from .. import LinguisParser, EvaluationError

if "." in __name__:
    from .LinguisENUSListener import LinguisENUSListener
    from .LinguisENUSParser import LinguisENUSParser
else:
    from LinguisENUSListener import LinguisENUSListener
    from LinguisENUSParser import LinguisENUSParser


class ENUSParser(LinguisParser):
    import linguis.parsers.en_us.LinguisENUSParser, linguis.parsers.en_us.LinguisENUSVisitor

    class Listener(LinguisENUSListener):
        def __init__(self) -> None:
            super().__init__()
        
        def enterBlock(self, ctx: Any) -> None:
            pass
        def exitBlock(self, ctx: Any) -> None:
            pass



    """ A parser for US English Linguis code. """
    def parse(self, code: List[str]) -> Block:
        from antlr4 import InputStream, CommonTokenStream

        # A real implementation would go here.
        incoming = InputStream(code.join("\n"))
        stream = CommonTokenStream(incoing)
        parser = HelloParser(stream)

        return Block([])

    def builtins(self) -> Dict[str, Any]:
        return {
            "println": lambda *args: print(*args),
            "print": lambda *args: print(*args, end=""),
            "size": lambda lst: len(lst) if isinstance(lst, list) else 0,
            "assert": lambda condition: condition or (_ for _ in ()).throw(EvaluationError("Assertion failed")),
            "input": lambda prompt=None: input(prompt) if prompt is not None else input()
        }
