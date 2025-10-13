import pytest

from linguis.ast import (
    Environment,
    Assignment, Number, Bool, Null, String,
    ListLiteral, Index, 
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

def test_primitives() -> None:
    env = Environment()
    assert Number(3).eval(env) == 3
    assert Bool(True).eval(env) is True
    assert Null().eval(env) is None
    assert String("hi").eval(env) == "hi"

