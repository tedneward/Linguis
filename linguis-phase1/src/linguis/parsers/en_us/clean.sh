#!/bin/bash

# A simple script to delete the generated ANTLR4 parser code.

echo Removing....
rm *.interp
rm *.tokens
rm LinguisENUSLexer*.*
rm LinguisENUSParser.py
rm LinguisENUSListener.py
rm LinguisENUSVisitor.py

