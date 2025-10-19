#!/bin/bash

# A simple script to regenerate the ANTLR4 parser code for Linguis.
# Requires that you have ANTLR4 installed and available on your PATH.
# See https://www.antlr.org/ for installation instructions.

# This only generates the ANTLR4 parser code for the g4 file in this
# directory. No other parsers are generated here.

echo Generating EN-US Linguis parser...
#antlr -Dlanguage=Python3 -visitor -o . LinguisENUS.g4

echo Generating parser for antlr GUI exploration
antlr -o . LinguisParser.g4 LinguisFRFRLexer.g4
javac -classpath /home/linuxbrew/.linuxbrew/Cellar/antlr/4.13.2/antlr-4.13.2-complete.jar:. *.java
