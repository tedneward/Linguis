# A collection of exploration tests around building Python ASTs
# for direct execution using the `ast` module.
# 
# These tests are not part of the main test suite and are intended
# for experimental purposes only.
# 
# They may be removed or modified without notice.
# 

import pytest
import ast
import sys

def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"

def test_simple_expression() -> None:
    """ Test building and executing a simple expression AST. """
    # Build AST for the expression: a = 1 + 2
    print(ast.dump(ast.parse("a = 1 + 2")))

    body = [
        ast.Assign(targets=[ast.Name(id='a', ctx=ast.Store())], value=ast.BinOp(
                left=ast.Constant(value=1),
                op=ast.Add(),
                right=ast.Constant(value=2)),
        ),
        ast.Expr(
            value=ast.Call(
                func=ast.Name(id='print', ctx=ast.Load()),
                args=[
                    ast.BinOp(
                        left=ast.Constant(value="Hello, "),
                        op=ast.Add(),
                        right=ast.Constant(value="Fred")
                    )
                ],
                keywords=[]
            )
        )
    ]
    module = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(module) 
        # The above is absolutely necessary, to fixup line numbers and locations
        # for the AST to be valid for compilation. Failure to fix them yields errors.

    # Compile and execute the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)

    # The result of the expression should be in local_vars
    assert local_vars['a'] == 3  # The last expression result is stored in '_'

def test_function_definition() -> None:
    """ Test building and executing a function definition AST. """
    # Build AST for the function:
    # def add(a, b):
    #     return a + b
    print(ast.dump(ast.parse("""
def add(a, b):
    return a + b
                             """)))


    func_def = ast.FunctionDef(
        name='add',
        args=ast.arguments(
            posonlyargs=[],
            args=[
                ast.arg(arg='a'),
                ast.arg(arg='b')
            ],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[]
        ),
        body=[
            ast.Return(
                value=ast.BinOp(
                    left=ast.Name(id='a', ctx=ast.Load()),
                    op=ast.Add(),
                    right=ast.Name(id='b', ctx=ast.Load())
                )
            )
        ],
        decorator_list=[]
    )
    module = ast.Module(body=[func_def], type_ignores=[])
    ast.fix_missing_locations(module)

    # Compile and execute the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)

    # The function should be defined in local_vars
    assert 'add' in local_vars
    # And calling the function should return the correct result
    assert local_vars['add'](2, 3) == 5

def ttest_conditional_statement() -> None:
    """ Test building and executing a conditional statement AST. """
    # Build AST for the conditional:
    # if x > 0:
    #     y = 1
    # else:
    #     y = -1
    print(ast.dump(ast.parse("""
if x > 0:
    y = 1
else:
    y = -1
                             """)))


    if_stmt = ast.If(
        test=ast.Compare(
            left=ast.Name(id='x', ctx=ast.Load()),
            ops=[ast.Gt()],
            comparators=[ast.Constant(value=0)]
        ),
        body=[
            ast.Assign(
                targets=[ast.Name(id='y', ctx=ast.Store())],
                value=ast.Constant(value=1)
            )
        ],
        orelse=[
            ast.Assign(
                targets=[ast.Name(id='y', ctx=ast.Store())],
                value=ast.Constant(value=-1)
            )
        ]
    )
    module = ast.Module(body=[if_stmt], type_ignores=[])
    ast.fix_missing_locations(module)

    # Compile and execute the AST with x = 5
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {'x': 5}
    exec(code, {}, local_vars)
    assert local_vars['y'] == 1

    # Compile and execute the AST with x = -3
    local_vars = {'x': -3}
    exec(code, {}, local_vars)
    assert local_vars['y'] == -1

def ttest_loop_statement() -> None:
    """ Test building and executing a loop statement AST. """
    # Build AST for the loop:
    # total = 0
    # for i in range(5):
    #     total += i
    print(ast.dump(ast.parse("""
total = 0
for i in range(5):
    total += i
                             """)))


    assign_total = ast.Assign(
        targets=[ast.Name(id='total', ctx=ast.Store())],
        value=ast.Constant(value=0)
    )
    for_loop = ast.For(
        target=ast.Name(id='i', ctx=ast.Store()),
        iter=ast.Call(
            func=ast.Name(id='range', ctx=ast.Load()),
            args=[ast.Constant(value=5)],
            keywords=[]
        ),
        body=[
            ast.AugAssign(
                target=ast.Name(id='total', ctx=ast.Store()),
                op=ast.Add(),
                value=ast.Name(id='i', ctx=ast.Load())
            )
        ],
        orelse=[]
    )
    module = ast.Module(body=[assign_total, for_loop], type_ignores=[])
    ast.fix_missing_locations(module)

    # Compile and execute the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)

    # The total should be the sum of 0 to 4
    assert local_vars['total'] == 10

def ttest_input_and_println_statement() -> None:
    """ Test building and executing an input and print statement AST. """
    # Build AST for:
    # name = input("Enter your name: ")
    # print("Hello, " + name)
    print(ast.dump(ast.parse("""
name = input("Enter your name: ")
print("Hello, " + name)
                             """)))


    input_call = ast.Assign(
        targets=[ast.Name(id='name', ctx=ast.Store())],
        value=ast.Call(
            func=ast.Name(id='input', ctx=ast.Load()),
            args=[ast.Constant(value="Enter your name: ")],
            keywords=[]
        )
    )
    print_call = ast.Expr(
        value=ast.Call(
            func=ast.Name(id='print', ctx=ast.Load()),
            args=[
                ast.BinOp(
                    left=ast.Constant(value="Hello, "),
                    op=ast.Add(),
                    right=ast.Name(id='name', ctx=ast.Load())
                )
            ],
            keywords=[]
        )
    )
    module = ast.Module(body=[input_call, print_call], type_ignores=[])
    ast.fix_missing_locations(module)

    # Compile the AST
    code = compile(module, filename="<ast>", mode="exec")
    local_vars = {}
    exec(code, {}, local_vars)
    assert 'name' in local_vars  # Ensure that 'name' variable is set
    assert isinstance(local_vars['name'], str)  # 'name' should be a string
