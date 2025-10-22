from typing import Any, List, Optional
from antlr4 import *

import ast
from .. import LinguisParser, EvaluationError

if "." in __name__:
    from .LinguisENUSLexer import LinguisENUSLexer
    from .LinguisENUSParser import LinguisENUSParser
    from .LinguisENUSVisitor import LinguisENUSVisitor
else:
    from LinguisENUSLexer import LinguisENUSLexer
    from LinguisENUSParser import LinguisENUSParser
    from LinguisENUSVisitor import LinguisENUSVisitor


