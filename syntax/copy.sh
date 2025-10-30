#!/bin/sh

# This script copies each of the lexers into their respective directories
# and renames them to fit what the LinguisParser.g4 file is expecting them
# to be called (e.g, "LinguisLexer").
#

echo Copying EN-US lexer....
cp LinguisENUSLexer.g4 ../python/src/pylinguis/parsers/enus/LinguisLexer.g4