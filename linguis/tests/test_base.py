import pytest

from linguis.ast import hello

def test_hello() -> None:
    assert hello() != None
    assert hello() == "Hello from linguis.ast!"
