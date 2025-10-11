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

def test_functiondecl() -> None:
    # Create root environment (builtins available)
    env = Environment()

    # Build AST:
    # def add(a, b) { return a + b }
    func = FunctionDecl("add", 
                        ["a", "b"], 
                        Block(
                            [Return(BinaryOp(Identifier("a"), "+", Identifier("b")))]))

    # x = 2;
    # y = 3;
    assign_x = Assignment("x", Number(2))
    assign_y = Assignment("y", Number(3))

    # z = add(x, y);
    call_add = Assignment("z", FunctionCall(Identifier("add"), [Identifier("x"), Identifier("y")]))

    # println("Result:", z)
    print_call = FunctionCall(Identifier("println"), [String("Result:"), Identifier("z")])

    program = Block([func, assign_x, assign_y, call_add, print_call])

    # Execute
    program.eval(env)

    # Verify
    assert env.get("z") == 5
    assert env.get("add") is not None
