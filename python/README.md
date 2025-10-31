# pylinguis

Linguis using Python's AST as the execution backbone.

This is the Python source root project, built and managed using the `uv` tool.

To run the tests: from this directory, run `uvx pytest`. 

* Use `-v` for verbose output. More verbosity? Use more "v"s (as in `-vv`, `-vvv`, ....). It's an interesting quirk of many Python packages.
* Use `-k `*{test_function_name}* to run just one of the elements of the test suite.
* Change the `log_cli_level` line in `pyproject.toml` to `"INFO"` to see INFO-level logging from the parser.

To run the interpreter: from this directory, run `uv run linguis --parser=`*parser* *sourcefile*

* the `ENUSParser` is the default parser if none is specified.
