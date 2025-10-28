# Tests for the en-us parser/lexer
#

import pytest

import ast
import typing

from pylinguis.parsers import find_parser

# Once we know the wiring is set up, try this, so as to spare
# us from having to find_parser() every single test
parser = find_parser("en-us")
assert parser is not None

def test_assign() -> None:
    """Test parsing simple integer assignment"""

    module = parser.parse("a = 5;")
    assert module is not None

    # Compile and execute the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)

    # The result of the expression should be in local_vars
    assert local_vars['a'] == 5

def test_boolexpr() -> None:
    """Test parsing simple boolean constant values"""

    module = parser.parse("a = true;\n")
    assert module is not None

    # Compile and execute the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)

    # The result of the expression should be in local_vars
    assert local_vars['a'] == True

def test_additionexpr() -> None:
    """Test parsing a simple addition pair"""

    module = parser.parse("a = 1 + 2;\n")
    assert module is not None

    # Compile and execute the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)

    # The result of the expression should be in local_vars
    assert local_vars['a'] == 3
