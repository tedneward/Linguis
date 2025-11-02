# pylinguis

Linguis using Python's AST as the execution backbone.

This is the Python source root project, built and managed using the `uv` tool.

### Preparation
Before the code can be run or test, the ANTLR-based parsers must be generated from their ANTLR source. The `prep.sh` script does this--it `cd`s into the parser's directory, runs the `antlrgen` script, and returns. This is to minimize the opportunities for "drift" to creep in between the grammar files and their generated outputs. (Were this a Java project, we'd be generating them as part of the Gradle build.)

### Tests
To run the tests: from this directory, run `uvx pytest`. 

* Use `-v` for verbose output. More verbosity? Use more "v"s (as in `-vv`, `-vvv`, ....). It's an interesting quirk of many Python packages.
* Use `-k `*{test_function_name}* to run just one of the elements of the test suite.
* Change the `log_cli_level` line in `pyproject.toml` to `"INFO"` to see INFO-level logging from the parser.

### Execution
To run the interpreter: from this directory, run `uv run pylinguis --parser=`*parser* *sourcefile*. 

* the `ENUSParser` is the default parser if none is specified.
* `uv run pylinguis` or `uv run pylinguis --help` shows the help.

