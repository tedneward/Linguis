import pytest

from linguis.ast import (
    Environment,
    UnaryOp, BinaryOp, 
    Number, Bool, Null, String,
    EvaluationError,
)

def test_unary_operators() -> None:
    env = Environment()

    assert UnaryOp("-", Number(5)).eval(env) == -5
    assert UnaryOp("!", Bool(False)).eval(env) is True

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

    assert BinaryOp(String("Hello, "), "+", String("world!")).eval(env) == "Hello, world!"

    with pytest.raises(EvaluationError):
        BinaryOp(Number(1), "unknown_op", Number(2)).eval(env)
