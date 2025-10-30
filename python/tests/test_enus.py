# Tests for the en-us parser/lexer
#

#import pytest  # Don't think I need this, but let's keep it here just the same for now

from pylinguis.parsers import find_parser

import ast

########################################
## TODO:
##
## * Strings: indexes on strings (to substring)
## * Lists: assignments, indexing, comparisons, whatever other operations 
##   should be supported (like `in`), size
## * Null: lots of operator tests (and determining what semantics 
##   above/beyond what Python does)
## * Functions: function decls and invocation
## * Builtins: invoking print(), println(), input(), etc. (This one will 
##   require pytest manipulation, to capture stdout and provide stdin)
##

########################################
## Utilities and setup
##

# Set up our parser once, so we don't have to keep finding it
#
parser = find_parser("en-us")
assert parser is not None

# Helper method to do the parse/compile/exec cycle 
#
def run(code, local_vars = None) -> dict:

    # Parse into the Python ast.Module
    module = parser.parse(code)
    assert module is not None
    print(f"Parse returned: {ast.dump(module, True, False, indent="  ", show_empty=True)}")

    # This little hack is necessary because if we assign to a function default,
    # and the default is a reference (not a value), we actually modify the default value!
    # In other words, if local_vars were defaulted to {} above, passing it through the
    # exec() will modify local_vars, which in turn is the defaulted parameter value,
    # which means subsequent calls to run() will get that modified default.
    # It's a weird quirk of Python.
    #
    if local_vars == None:
        local_vars = {}

    # Compile it into bytecode
    code = compile(module, filename="<ast>", mode="exec")
    # Run it!
    exec(code, {}, local_vars)
    return local_vars

########################################
## Assignment and core types
##
def test_assignnull() -> None:
    code = """
a = null;
"""
    local_vars = run(code)
    assert local_vars['a'] == None

def test_assignint() -> None:
    code = """
a = 5;
"""
    local_vars = run(code)
    assert local_vars['a'] == 5

def test_assignstr() -> None:
    code = """
a = \"Fred\";
"""
    local_vars = run(code)
    assert local_vars['a'] == "Fred"
    
def test_assignbool() -> None:
    code = """
a = true;
"""
    local_vars = run(code)
    assert local_vars['a'] == True

def test_reassign() -> None:
    code = """
a = null;
a = \"Fred\";
a = true;
a = 5;
"""
    local_vars = run(code)
    assert local_vars['a'] == 5

########################################
## Operators
##
def test_addition() -> None:
    code = """
a = 1 + 2;
b = 1.0 + 2.0;
c = 1 + 2 + 3 + 4;
d = 1.1 + 2.2 + 3.3 + 4.4;
"""
    local_vars = run(code)
    assert local_vars['a'] == 3
    assert local_vars['b'] == 3.0
    assert local_vars['c'] == 10
    assert local_vars['d'] == 11.0

def test_subtraction() -> None:
    code = """
a = 2 - 1;
b = 2.0 - 1.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 1

def test_multiplication() -> None:
    code = """
a = 2 * 5;
b = 2.0 * 5.0;
c = 2 * 5 * 10;
d = 2.0 * 5.0 * 10.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 10
    assert local_vars['b'] == 10.0
    assert local_vars['c'] == 100.0

def test_division() -> None:
    code = """
a = 4 / 2;
b = 4.0 / 2.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 2
    assert local_vars['b'] == 2.0

def test_modulus() -> None:
    code = """
a = 5 % 2;
b = 5.0 % 2.0;
"""
    local_vars = run(code)
    assert local_vars['a'] == 1
    assert local_vars['b'] == 1.0

def test_numeric_comparison() -> None:
    code = """t1 = 1 < 2;
f1 = 1 > 2;
t2 = 1 <= 2;
f2 = 1 >= 2;
t3 = 1.0 < 2.0;
t4 = 1.0 <= 2.0;
f3 = 1.0 > 2.0;
f4 = 1.0 >= 2.0;
t5 = 1 < 2.0;
t6 = 2 > 1.0;
"""
    local_vars = run(code)
    assert local_vars['t1'] == True
    assert local_vars['t2'] == True
    assert local_vars['t3'] == True
    assert local_vars['t4'] == True
    assert local_vars['t5'] == True
    assert local_vars['t6'] == True
    assert local_vars['f1'] == False
    assert local_vars['f2'] == False
    assert local_vars['f3'] == False
    assert local_vars['f4'] == False

def test_numeric_equality_and_inequality() -> None:
    code = """
t1 = 1 == 1;
t2 = 1.0 == 1.0;
t3 = 1 != 2;
t4 = 1.0 != 2.0;
f1 = 1 == 2;
f2 = 1.0 == 2.0;
f3 = 1 != 1;
f4 = 1.0 != 1.0;
"""
    local_vars = run(code)
    assert local_vars['t1'] == True
    assert local_vars['t2'] == True
    assert local_vars['t3'] == True
    assert local_vars['t4'] == True
    assert local_vars['f1'] == False
    assert local_vars['f2'] == False
    assert local_vars['f3'] == False
    assert local_vars['f4'] == False

def test_string_equality_and_inequality() -> None:
    code = """
t1 = \"Hello\" == \"Hello\";
t2 = \"Hello\" != \"Goodbye\";
f1 = \"Hello\" == \"Goodbye\";
f2 = \"Hello\" != \"Hello\";
"""
    local_vars = run(code)
    assert local_vars['t1'] == True
    assert local_vars['t2'] == True
    assert local_vars['f1'] == False
    assert local_vars['f2'] == False


########################################
## Control flow
##
def test_iftrue() -> None:
    code = """
a = 5;
if a < 10 do
    a = 10;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 10

def test_iffalse() -> None:
    code = """
a = 10;
if a < 5 do
    a = 5;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 10

def test_iftrueelse() -> None:
    code = """
a = 5;
if a < 10 do
    a = 10;
else do
    a = 20;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 10

def test_iffalseelse() -> None:
    code = """
a = 20;
if a < 5 do
    a = 5;
else do
    a = 10;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 10

def test_ifelseif() -> None:
    """Test parsing an if"""

    code = """
a = 5;
if a < 1 do
    a = 1;
else if a < 10 do
    a = 10;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 10


def test_ifelseifelse() -> None:
    """Test parsing an if"""

    code = """
a = 5;
if a < 1 do
    a = 1;
else if a < 10 do
    a = 10;
else do
    a = 20;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 10







def ttest_while() -> None:
    """Test parsing an while"""

    code = """
a = 0
while a < 3 do
    a = a + 1;
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 3

def ttest_for() -> None:
    """Test parsing an for"""

    code = """
b = 0
for a = 0 to 3 do
    b = b + 1
end
"""
    local_vars = run(code)
    assert local_vars['a'] == 3
    assert local_vars['b'] == 3
