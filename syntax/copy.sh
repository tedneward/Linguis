#!/bin/sh

# This script copies each of the lexers into their respective directories
# and renames them to fit what the LinguisParser.g4 file is expecting them
# to be called (e.g, "LinguisLexer"). Copy over all the supporting scripts
# too, while we're at it. (Single source of truth and all that.)
#

echo Copying EN-US files/scripts....
cp LinguisENUSLexer.g4 ../python/src/pylinguis/parsers/enus/LinguisLexer.g4
cp LinguisParser.g4 ../python/src/pylinguis/parsers/enus/LinguisParser.g4
cp antlrgen.sh ../python/src/pylinguis/parsers/enus/antlrgen.sh
cp clean.sh ../python/src/pylinguis/parsers/enus/clean.sh
cp gitignore ../python/src/pylinguis/parsers/enus/.gitignore

echo Copying EN-PL files/scripts....
cp LinguisENPLLexer.g4 ../python/src/pylinguis/parsers/enpl/LinguisLexer.g4
cp LinguisParser.g4 ../python/src/pylinguis/parsers/enpl/LinguisParser.g4
cp antlrgen.sh ../python/src/pylinguis/parsers/enpl/antlrgen.sh
cp clean.sh ../python/src/pylinguis/parsers/enpl/clean.sh
cp gitignore ../python/src/pylinguis/parsers/enpl/.gitignore

#echo Copying FR files/scripts....
#cp LinguisFRLexer.g4 ../python/src/pylinguis/parsers/fr/LinguisLexer.g4
#cp LinguisParser.g4 ../python/src/pylinguis/parsers/fr/LinguisParser.g4
#cp antlrgen.sh ../python/src/pylinguis/parsers/fr/antlrgen.sh
#cp clean.sh ../python/src/pylinguis/parsers/fr/clean.sh
#cp gitignore ../python/src/pylinguis/parsers/fr/.gitignore

#echo Copying DE files/scripts....
#cp LinguisDELexer.g4 ../python/src/pylinguis/parsers/de/LinguisLexer.g4
#cp LinguisParser.g4 ../python/src/pylinguis/parsers/de/LinguisParser.g4
#cp antlrgen.sh ../python/src/pylinguis/parsers/de/antlrgen.sh
#cp clean.sh ../python/src/pylinguis/parsers/de/clean.sh
#cp gitignore ../python/src/pylinguis/parsers/de/.gitignore

