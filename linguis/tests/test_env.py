import pytest

from linguis.ast import (
    Environment, 
    EvaluationError,
)

def test_environment() -> None:
    """ Tests that setting and getting variables in the environment works correctly. """
    env = Environment()
    env.set("x", 42)
    assert env.get("x") == 42
    with pytest.raises(EvaluationError):
        env.get("y")

def test_scopes() -> None:
    """ Tests that pushing and popping scopes works correctly. """
    env = Environment()

    # Simple set
    env.set("x", 1)
    assert env.get("x") == 1

    # Now push a scope
    env.push()
    # Simple set
    env.set("y", 2)
    assert env.get("y") == 2
    # We should get this from the previous (outer) scope
    assert env.get("x") == 1
    env.set("x", 3)
    assert env.get("x") == 3

    # Toss the inner scope
    env.pop()
    # And the outer scope's value should still be there
    assert env.get("x") == 3
    # But the inner scope's value should be gone
    with pytest.raises(EvaluationError):
        env.get("y")

def test_parent_scopes() -> None:
    """ Tests that nested environments correctly reference parent scopes. """
    env = Environment(verbose=True)

    # Simple set
    env.set("a", 10)
    # Shouldn't find this in the current env
    with pytest.raises(EvaluationError):
        env.get("b")

    # Create a nested environment
    nested_env = Environment(parent=env, verbose=True)
    # We should find "a" in the parent env
    assert nested_env.get("a") == 10
    # Shouldn't find this in the current env
    with pytest.raises(EvaluationError):
        nested_env.get("b")
    # Now set it in the nested env
    nested_env.set("b", 20)
    # Should find it OK
    assert nested_env.get("b") == 20
    # But "b" shouldn't be in the parent env
    with pytest.raises(EvaluationError):
        print(env.get("b"))

    # Should still be able to modify "a" in the parent env
    nested_env.set("a", 30)
    assert nested_env.get("a") == 30
    assert env.get("a") == 30
