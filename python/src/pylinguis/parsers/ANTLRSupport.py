import antlr4
import ast
from . import LinguisParserBase

class ANTLRParserBase(LinguisParserBase):
    """A base class for parsers for Linguis that use ANTLR for their implementation."""

    def __init__(self):
        super().__init__()

    def getLexer(self, input_stream : antlr4.InputStream) -> antlr4.Lexer:
        raise Exception("E_NOTIMPL")
    
    def getParser(self, stream : antlr4.CommonTokenStream) -> antlr4.Parser:
        raise Exception("E_NOTIMPL")

    def getVisitor(self) -> antlr4.ParseTreeVisitor:
        raise Exception("E_NOTIMPL")

    def parse_from_stream(self, input_stream : antlr4.InputStream) -> ast.Module:
        """Internal(ish) method that takes an ANTLR stream and parses it, then runs it"""

        lexer = self.getLexer(input_stream)
        stream = antlr4.CommonTokenStream(lexer)        
        parser = self.getParser(stream)

        # The simple way
        tree = parser.block()
        self.logger.info(f"Parse Tree:\n{tree.toStringTree(recog=parser)}")

        visitor = self.getVisitor()
        nodes = visitor.visit(tree)

        # Do I want to wrap the main body in a function call, so that we
        # can 'return' from it and hand the value back through here to the
        # driver, to hand back to someplace else? Does that even make sense
        # for Linguis?
        #

        module = ast.Module(body=nodes, type_ignores=[])
        ast.fix_missing_locations(module) 
            # The above is absolutely necessary, to fixup line numbers and locations
            # for the AST to be valid for compilation. Failure to fixup them yields errors.
        self.logger.info(f"Python is:\n{ast.unparse(module)}")

        return module

    def parse_file(self, filename : str) -> ast.Module:
        """Takes filename and dumps it into self.parse()"""

        filestream = antlr4.FileStream(filename)
        return self.parse_from_stream(filestream)

    def parse(self, code: str) -> ast.Module:
        """Parses the entire code into a Python Module node."""

        # TODO: Need to figure out if/how ANTLR4 supports Unicode

        code_stream = antlr4.InputStream(code)
        return self.parse_from_stream(code_stream)


