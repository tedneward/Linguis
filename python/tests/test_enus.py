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

# Helper method to do the parse/compile/exec cycle 
def run(code, local_vars = {}) -> dict:
    # Compile and execute the AST
    module = parser.parse(code)
    assert module is not None

    code = compile(module, filename="<ast>", mode="exec")
    exec(code, {}, local_vars)
    return local_vars

def test_assignint() -> None:
    """Test parsing simple integer assignment"""

    local_vars = run("a = 5;")
    assert local_vars['a'] == 5

def test_assignstr() -> None:
    """Test parsing string assignment"""

    local_vars = run("a = \"Fred\";")
    assert local_vars['a'] == "Fred"
    
def test_assignbool() -> None:
    """Test parsing boolean assignment"""

    code = """
a = true;
"""
    local_vars = run(code)
    assert local_vars['a'] == True

def test_additionexpr() -> None:
    """Test parsing a simple addition pair"""

    code = """
a = 1 + 2;
b = 1.0 + 2.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 3
    assert local_vars['b'] == 3.0

def test_subtractionexpr() -> None:
    """Test parsing a simple subtraction pair"""

    code = """
a = 2 - 1;
b = 2.0 - 1.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 1

def test_multiplicationexpr() -> None:
    """Test parsing a simple multiplication pair"""

    code = """
a = 2 * 5;
b = 2.0 * 5.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 10
    assert local_vars['b'] == 10.0

def test_divisionexpr() -> None:
    """Test parsing a simple division pair"""

    code = """
a = 4 / 2;
b = 4.0 / 2.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 2
    assert local_vars['b'] == 2.0

def test_modulusexpr() -> None:
    """Test parsing a simple modulus pair"""

    code = """
a = 5 % 2;
b = 5.0 % 2.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 1
    assert local_vars['b'] == 1.0

def test_intcomparison() -> None:
    """Test integer comparisons (and multiple statements in a single block too!)"""

    code = """t1 = 1 < 2;
f1 = 1 > 2;
t2 = 1 <= 2;
f2 = 1 >= 2;
"""
    local_vars = run(code)
    assert local_vars['t1'] == True
    assert local_vars['t2'] == True
    assert local_vars['f1'] == False
    assert local_vars['f2'] == False
