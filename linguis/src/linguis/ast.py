"""AST node classes and a tiny interpreter runtime for the Linguis language.

This module provides node classes with an `eval(env)` method so a parsed
AST can be executed. It's intentionally small but supports the features
described in SYNTAX.md enough to run simple programs and unit tests.

Note: this file focuses on runtime representation and evaluation semantics.
Parsers are expected to yield instances of these classes for execution.
"""
#from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence


class EvaluationError(Exception):
    pass


class ReturnSignal(Exception):
    """Internal control-flow exception used to implement `return`.

    The exception carries the returned value so it can unwind the
    interpreter call stack.
    """

    def __init__(self, value: Any) -> None:
        super().__init__("return")
        self.value = value


# Forward-declaration of Environment is necessary because it is used
# in the "parent" parameter of the Environment __init__ method.
# Or was, at least, I suppose we could periodically remove this
# two-line thing to see if it still is.
class Environment:
    pass

# Error messages should probably somehow be localized based on the parser
# being used, but for now we just hard-code English messages here.
class Environment:
    """
    A simple environment / scope stack for variables and functions.

    - Each scope is a dict mapping names -> value.
    - Each Environment may have a parent Environment.
    - Functions are stored as Python-callable values (Function objects).
    - Builtins must be passed in via the bindings parameter, and are installed in the "root" scope.
    """

    def __init__(self, bindings: Dict[str,Any] = {}, parent: Optional[Environment] = None, verbose = False) -> None:
        self.verbose = verbose
        self.scopes: List[Dict[str, Any]] = [{}]
        self.parent = parent
        for k, v in bindings.items():
            self.set(k, v)

    def _log(self, message: str) -> None:
        if self.verbose:
            print(message)

    def push(self) -> None:
        self.scopes.append({})

    def pop(self) -> None:
        if len(self.scopes) == 1:
            raise EvaluationError("cannot pop global scope")
        self.scopes.pop()

    def set(self, name: str, value: Any) -> None:
        # search from top scope down to global
        for scope in reversed(self.scopes):
            if name in scope:
                scope[name] = value
                return

        # if not found in current chain, try parent environment
        if self.parent is not None:
            try:
                self.parent.get(name)  # just to see if it exists
                self.parent.set(name, value) # if we're still here, it exists
                return
            except EvaluationError:
                pass

        # set in the nearest (top) scope
        self.scopes[-1][name] = value

    def get(self, name: str) -> Any:
        # search from top scope down to global
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]

        # if not found in current chain, try parent environment
        if self.parent is not None:
            return self.parent.get(name)

        raise EvaluationError(f"name '{name}' is not defined")
    
    def to_s(self) -> str:
        lines = []
        if self.parent is not None:
            lines.append("Parent Environment:")
            lines.append(self.parent.to_s())
        lines.append("Current Environment Scopes:")
        for i, scope in enumerate(self.scopes):
            lines.append(f" Scope {i}:")
            for k, v in scope.items():
                lines.append(f"  {k} = {v}")
        return "\n".join(lines)


class Node:
    """Base class for all AST nodes."""

    def eval(self, env: Environment) -> Any:  # pragma: no cover - overriden
        raise NotImplementedError()


class Block(Node):
    """A block of statements, with its own scope."""
    def __init__(self, statements: Sequence[Node]) -> None:
        self.statements = list(statements)

    def eval(self, env: Environment) -> Any:
        result = None
        env.push()
        for stmt in self.statements:
            result = stmt.eval(env)
        env.pop()
        return result


class Number(Node):
    """A numeric literal (float)."""
    def __init__(self, value: float) -> None:
        self.value = value

    def eval(self, env: Environment) -> float:
        return self.value


class Bool(Node):
    """A boolean literal."""
    def __init__(self, value: bool) -> None:
        self.value = value

    def eval(self, env: Environment) -> bool:
        return self.value


class Null(Node):
    """A null literal."""
    def eval(self, env: Environment) -> None:
        return None


class String(Node):
    """A string literal."""
    def __init__(self, value: str) -> None:
        self.value = value

    def eval(self, env: Environment) -> str:
        return self.value


class Identifier(Node):
    """An identifier (variable or function name)."""
    def __init__(self, name: str) -> None:
        self.name = name

    def eval(self, env: Environment) -> Any:
        return env.get(self.name)


class Assignment(Node):
    """An assignment expression."""
    def __init__(self, name: str, expr: Node) -> None:
        self.name = name
        self.expr = expr

    def eval(self, env: Environment) -> Any:
        value = self.expr.eval(env)
        env.set(self.name, value)
        return value


class BinaryOp(Node):
    operations = {
        # Maths operations
        "+": lambda a, b: a + b, 
        "-": lambda a, b: a - b, 
        "*": lambda a, b: a * b, 
        "/": lambda a, b: a / b, 
        "%": lambda a, b: a % b, 
        "^": lambda a, b: a ** b,
        # Comparison and logical operations
        ">=": lambda a, b: a >= b, 
        "<=": lambda a, b: a <= b, 
        ">": lambda a, b: a > b,
        "<": lambda a, b: a < b,
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
        "&&": lambda a, b: bool(a) and bool(b),
        "||": lambda a, b: bool(a) or bool(b),
        # Membership operation
        # I kinda feel like "in" should be parser-sensitive, maybe?
        # This is simpler, tho
        "in": lambda a, b: a in b,
    }

    """A binary operation expression. Supports arithmetic, comparison, logical ops."""
    def __init__(self, left: Node, op: str, right: Node) -> None:
        self.left = left
        self.op = op
        self.right = right

    def eval(self, env: Environment) -> Any:
        a = self.left.eval(env)
        b = self.right.eval(env)

        operation = self.operations[self.op] if self.op in self.operations else None
        if operation is None:
            raise EvaluationError(f"unknown binary operator: {self.op}")
        else:
            return operation(a,b)


class UnaryOp(Node):
    """A unary operation expression. Supports negation and logical NOT."""
    def __init__(self, op: str, expr: Node) -> None:
        self.op = op
        self.expr = expr

    def eval(self, env: Environment) -> Any:
        v = self.expr.eval(env)
        if self.op == "-":
            return -v
        if self.op == "!":
            return not v
        raise EvaluationError(f"unknown unary operator: {self.op}")

class ListLiteral(Node):
    """A list literal."""
    def __init__(self, items: Sequence[Node]) -> None:
        self.items = list(items)

    def eval(self, env: Environment) -> list:
        return [it.eval(env) for it in self.items]


class Index(Node):
    """Indexing into a list or string."""
    def __init__(self, value: Node, index: Node) -> None:
        self.value = value
        self.index = index

    def eval(self, env: Environment) -> Any:
        container = self.value.eval(env)
        idx = self.index.eval(env)
        try:
            return container[idx]
        except Exception as e:
            raise EvaluationError(str(e))


class FunctionDecl(Node):
    """A function declaration."""
    def __init__(self, name: str, params: Sequence[str], body: Block) -> None:
        self.name = name
        self.params = list(params)
        self.body = body

    def eval(self, env: Environment) -> None:
        func = Function(self.params, self.body, env)
        env.set(self.name, func)
        return func


class Function:
    """A user-defined function object."""
    def __init__(self, params: Sequence[str], body: Block, defining_env: Environment) -> None:
        self.params = list(params)
        self.body = body
        # capture parent environment for closures
        self.defining_env = defining_env

    def call(self, args: Sequence[Any]) -> Any:
        env = Environment(parent=self.defining_env)
        env.push()
        # bind params
        for i, name in enumerate(self.params):
            env.set(name, args[i] if i < len(args) else None)
        try:
            result = self.body.eval(env)
        except ReturnSignal as r:
            return r.value
        finally:
            # ensure we drop the pushed scope (not strictly necessary here)
            try:
                env.pop()
            except Exception:
                pass
        return result


class FunctionCall(Node):
    """A function call expression."""
    def __init__(self, callee: Node, args: Sequence[Node]) -> None:
        # callee is often Identifier but we accept any expression
        self.callee = callee
        self.args = list(args)

    def eval(self, env: Environment) -> Any:
        fn = self.callee.eval(env)
        evaluated_args = [a.eval(env) for a in self.args]
        # builtin: python-callable
        if callable(fn):
            return fn(*evaluated_args)
        if isinstance(fn, Function):
            return fn.call(evaluated_args)
        raise EvaluationError("attempted to call a non-function")


class IfStatement(Node):
    """An if/else statement."""
    def __init__(self, cond: Node, then_block: Block, else_block: Optional[Block] = None) -> None:
        self.cond = cond
        self.then_block = then_block
        self.else_block = else_block

    def eval(self, env: Environment) -> Any:
        if self.cond.eval(env):
            return self.then_block.eval(env)
        if self.else_block is not None:
            return self.else_block.eval(env)
        return None


class WhileStatement(Node):
    """A while loop statement."""
    def __init__(self, cond: Node, body: Block) -> None:
        self.cond = cond
        self.body = body

    def eval(self, env: Environment) -> Any:
        result = None
        while self.cond.eval(env):
            result = self.body.eval(env)
        return result


class ForStatement(Node):
    """A for loop statement."""
    def __init__(self, name: str, start: Node, end: Node, body: Block) -> None:
        self.name = name
        self.start = start
        self.end = end
        self.body = body

    def eval(self, env: Environment) -> Any:
        s = int(self.start.eval(env))
        e = int(self.end.eval(env))
        result = None
        for i in range(s, e + 1):
            env.push()
            env.set(self.name, i)
            result = self.body.eval(env)
            env.pop()
        return result


class Return(Node):
    """A return statement."""
    def __init__(self, expr: Optional[Node]) -> None:
        self.expr = expr

    def eval(self, env: Environment) -> None:
        value = self.expr.eval(env) if self.expr is not None else None
        raise ReturnSignal(value)
