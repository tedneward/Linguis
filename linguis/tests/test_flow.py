import pytest

from linguis.ast import (
    Environment, 
    Block, Identifier, 
    UnaryOp, BinaryOp, 
    Assignment, Number, Bool, Null, String,
    FunctionDecl, Return, FunctionCall, 
    ListLiteral, Index, 
    IfStatement, WhileStatement, ForStatement,
    EvaluationError,
)

def test_if() -> None:
    env = Environment()
    # if/else
    Assignment("a", Number(0)).eval(env)
    ifstmt = IfStatement(Bool(True), Block([Assignment("a", Number(7))]), Block([Assignment("a", Number(8))]))
    ifstmt.eval(env)
    assert env.get("a") == 7

def test_while() -> None:
    env = Environment()

    # while: i starts at 0 and increments to 3
    Assignment("i", Number(0)).eval(env)
    loop = WhileStatement(BinaryOp(Identifier("i"), "<", Number(3)), Block([Assignment("i", BinaryOp(Identifier("i"), "+", Number(1)))]))
    loop.eval(env)
    assert env.get("i") == 3

def test_for() -> None:
    env = Environment()
    
    # for: sum 1..3 -> 6
    Assignment("sum", Number(0)).eval(env)
    assert env.get("sum") == 0
    forstmt = ForStatement("k", Number(1), Number(3), 
                           Block([
                               Assignment("sum", BinaryOp(Identifier("sum"), "+", Identifier("k"))),
                               FunctionCall(Identifier("println"), [String("In loop, k="), Identifier("k"), String(" sum="), Identifier("sum")])
                               ]))
    forstmt.eval(env)
    assert env.get("sum") == 6

def test_builtin_assert() -> None:
    env = Environment()

    # assert builtin should raise on false
    with pytest.raises(EvaluationError):
        FunctionCall(Identifier("assert"), [Bool(False)]).eval(env)
