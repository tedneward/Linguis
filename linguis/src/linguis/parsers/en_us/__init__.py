from typing import Any, List, Optional
from antlr4 import *

from linguis.ast import *
from .. import LinguisParser, EvaluationError

if "." in __name__:
    from .LinguisENUSLexer import LinguisENUSLexer
    from .LinguisENUSParser import LinguisENUSParser
    from .LinguisENUSVisitor import LinguisENUSVisitor
else:
    from LinguisENUSLexer import LinguisENUSLexer
    from LinguisENUSParser import LinguisENUSParser
    from LinguisENUSVisitor import LinguisENUSVisitor


class ENUSParser(LinguisParser):
    """ A parser for US English Linguis code. """

    class Visitor(LinguisENUSVisitor):
        def __init__(self) -> None:
            super().__init__()

        def visitBlock(self, ctx: LinguisENUSParser.BlockContext) -> Any:
            block = Block()
            for child in ctx.children:
                print("Visiting child:", child.getText(), type(child))
                result = self.visit(child)
                if result is None:
                    print("Warning: visit returned None for child:", child.getText())                
                block.append(result)
            return block
        
        def visitIdentifierFunctionCall(self, ctx:LinguisENUSParser.IdentifierFunctionCallContext) -> Any:
            name = ctx.getChild(0).getText()
            print(ctx.Identifier())
            args = []
            if ctx.exprList():
                for arg in ctx.exprList().getChildren():
                    args.append(self.visit(arg))
            print(f"IdentifierFunctionCall: {name} {args}")
            return FunctionCall(Identifier(name), args)

        def visitFunctionDecl(self, ctx: LinguisENUSParser.FunctionDeclContext) -> Any:
            name = ctx.getChild(0).getText()
            params = []
            if ctx.idList():
                for param in ctx.idList().getChildren():
                    params.append(param.getText())
            body = self.visit(ctx.block())
            print(f"FunctionDecl: {name}({params}) {{...}}")
            return FunctionDecl(name, params, body)

        def visitAssignment(self, ctx: LinguisENUSParser.AssignmentContext) -> Any:
            print("Assignment:", ctx.toStringTree())
            name = self.visit(ctx.getChild(0))
            expr = self.visit(ctx.expression())
            print(f"Assignment: {name} = '{expr}'")
            return Assignment(name, expr)

        def visitBoolExpression(self, ctx):
            return Bool(ctx.getText().lower() == "true")
        
        def visitListExpression(self, ctx):
            return ListLiteral([self.visit(expr) for expr in ctx.expression()])
        
        def visitNumberExpression(self, ctx):
            return Number(float(ctx.getText()))
        
        def visitNullExpression(self, ctx):
            return Null()
        
        def visitStringExpression(self, ctx):
            return String(ctx.getText()[1:-1])  # Strip quotes
        
        def visitIdentifierExpression(self, ctx):
            print("IdentifierExpression:", ctx.getText())
            return Identifier(ctx.getText())


    def parse(self, fname: str) -> Block:
        incoming = FileStream(fname)
        lexer = LinguisENUSLexer(incoming)
        stream = CommonTokenStream(lexer)
        parser = LinguisENUSParser(stream)

        tree = parser.block()
        print(tree.toStringTree(recog=parser))  # Debug print of parse tree
        visitor = ENUSParser.Visitor()
        return visitor.visit(tree)

    def builtins(self) -> Dict[str, Any]:
        return {
            "assert": lambda condition: condition or (_ for _ in ()).throw(EvaluationError("Assertion failed")),
            "input": lambda prompt=None: input(prompt) if prompt is not None else input(),
            "println": lambda *args: print(*args),
            "print": lambda *args: print(*args, end=""),
            "size": lambda lst: len(lst) if isinstance(lst, list) else 0,
        }
