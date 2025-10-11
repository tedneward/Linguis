import pytest

from linguis.ast import (
    Environment,
    UnaryOp, BinaryOp, Ternary,
    Assignment, Number, Bool, Null, String,
    ListLiteral, Index, 
    EvaluationError,
)

def test_number_assignment() -> None:
    env = Environment()
    assign = Assignment("x", Number(10))
    assign.eval(env)
    assert env.get("x") == 10

def test_string_assignment() -> None:
    env = Environment()
    assign = Assignment("greeting", String("Hello, world!"))
    assign.eval(env)
    assert env.get("greeting") == "Hello, world!"

def test_boolean_assignment() -> None:
    env = Environment()
    assign = Assignment("flag", Bool(True))
    assign.eval(env)
    assert env.get("flag") is True

def test_null_assignment() -> None:
    env = Environment()
    assign = Assignment("nothing", Null())
    assign.eval(env)
    assert env.get("nothing") is None

def test_list_and_index() -> None:
    env = Environment()
    lst = ListLiteral([Number(1), Number(2), Number(3)])
    evaluated = lst.eval(env)
    assert evaluated == [1, 2, 3]
    assert Index(lst, Number(1)).eval(env) == 2

def test_primitives_and_unary_ternary() -> None:
    env = Environment()
    assert Number(3).eval(env) == 3
    assert Bool(True).eval(env) is True
    assert Null().eval(env) is None
    assert String("hi").eval(env) == "hi"
    assert UnaryOp("-", Number(5)).eval(env) == -5
    assert UnaryOp("!", Bool(False)).eval(env) is True
    assert Ternary(Bool(True), Number(1), Number(2)).eval(env) == 1


def test_binary_operators() -> None:
    env = Environment()
    assert BinaryOp(Number(2), "+", Number(3)).eval(env) == 5
    assert BinaryOp(Number(5), "-", Number(2)).eval(env) == 3
    assert BinaryOp(Number(3), "*", Number(4)).eval(env) == 12
    assert BinaryOp(Number(6), "/", Number(3)).eval(env) == 2
    assert BinaryOp(Number(5), "%", Number(2)).eval(env) == 1
    assert BinaryOp(Number(2), "^", Number(3)).eval(env) == 8
    assert BinaryOp(Number(2), ">=", Number(2)).eval(env) is True
    assert BinaryOp(Number(1), "<", Number(2)).eval(env) is True
    assert BinaryOp(Number(2), "==", Number(2)).eval(env) is True
    assert BinaryOp(Number(2), "!=", Number(3)).eval(env) is True
    assert BinaryOp(Bool(True), "&&", Bool(False)).eval(env) is False
    assert BinaryOp(Bool(True), "||", Bool(False)).eval(env) is True

    with pytest.raises(ZeroDivisionError):
        BinaryOp(Number(1), "/", Number(0)).eval(env)
    with pytest.raises(ZeroDivisionError):
        BinaryOp(Number(1), "%", Number(0)).eval(env)
    with pytest.raises(EvaluationError):
        BinaryOp(Number(1), "unknown_op", Number(2)).eval(env)

