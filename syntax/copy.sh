#!/bin/sh

# This script copies each of the lexers into their respective directories
# and renames them to fit what the LinguisParser.g4 file is expecting them
# to be called (e.g, "LinguisLexer").
#

echo Copying EN-US files....
cp LinguisParser.g4 ../python/src/pylinguis/parsers/enus/LinguisParser.g4
cp LinguisENUSLexer.g4 ../python/src/pylinguis/parsers/enus/LinguisLexer.g4

echo Copying EN-PL files....
cp LinguisParser.g4 ../python/src/pylinguis/parsers/enpl/LinguisParser.g4
cp LinguisENPLLexer.g4 ../python/src/pylinguis/parsers/enpl/LinguisLexer.g4

echo Copying FR files....
cp LinguisParser.g4 ../python/src/pylinguis/parsers/fr/LinguisParser.g4
cp LinguisFRLexer.g4 ../python/src/pylinguis/parsers/fr/LinguisLexer.g4

echo Copying DE files....
cp LinguisParser.g4 ../python/src/pylinguis/parsers/de/LinguisParser.g4
cp LinguisDELexer.g4 ../python/src/pylinguis/parsers/de/LinguisLexer.g4

