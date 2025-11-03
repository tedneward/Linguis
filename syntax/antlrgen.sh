#!/bin/bash

# A simple script to regenerate the ANTLR4 parser code for Linguis.
# Requires that you have ANTLR4 installed and available on your PATH.
# See https://www.antlr.org/ for installation instructions.

# This only generates the ANTLR4 parser code for the g4 file in this
# directory. No other parsers are generated here.

echo Generating parser for Linguis use
antlr -Dlanguage=Python3 -visitor -o . LinguisParser.g4 LinguisLexer.g4
