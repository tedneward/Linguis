# Linguis
A procedural programming language with swappable syntax

## Intent
Programming languages have, almost since their inception, assumed a fixed syntax that is rooted in English for its keywords, with relatively few exceptions. Pascal has `PROGRAM`, `FUNCTION`, `VAR`, and so on. C has `if`/`else`, `for`, `while`. Even homoiconic languages like Lisp use English nouns for its forms.

When I was in college, though, I took a trip to visit some friends in Belgium, and they had a French computer there--complete with its own version of French BASIC, where all the keywords were in--you guessed it--French. It took me a hot second to map the keywords I knew to their French equivalents, and definitely made reading the code an extra level harder.

Now, in 2025, we still see most of our popular programming languages based on English keywords, which makes me wonder: Why? Don't get me wrong, as a native English speaker, I am happy that my native tongue is the default *lingua franca* for the programming industry, but in an era where we have literally gigs of RAM to throw at a problem, why are we continually enforcing English as a necessary prerequisite for programming?

Thus, Linguis: A programming language (procedural, since this is a POC) whose keywords are "pluggable" and in several sets, so that those of non-native English speaking descent can program in their mother tongue.

## Design
At its heart, Linguis is not going to be all that Earth-shattering in its implementation: A procedural language with some basic data types, the ability to define and call functions (taking zero to many parameters, returning a value), and so on. The emphasis will be on the parser side of the pipeline, where Linguis will use one of several possible lexers/parsers to parse the source code, based on either a command-line switch or possibly an in-file directive.

Beyond the flexible syntax, keep things simple: dynamically-typed, and fully procedural (no classes/objects, no metaprogramming, etc). Source-based interpreter, with a baked-in "standard library" and no mechanism to reference other files (no imports, no uses, etc).

Source files should be Unicode-based from the start, so that each language can operate using its own unique character sets. This should even open it up to languages like Hebrew or Arabic, though left-to-right/right-to-left/top-to-bottom representations could create some issues for me. (I may leave that to community contributions to figure out.)

### Technical
Since this isn't aiming to be production-quality, let's use a Python back-end, since Python has an AST baked right into the language/standard library (`import ast`), and is a dynamic language to boot (which saves from having to worry about type systems and type checking and all that).

Since I like it, I'll use ANTLR for generating the different language parsers; in fact, I think we can probably just define different lexers against a standard parser, but we'll see where that goes. In any event, I want the parser implementation to be hidden from the rest of the system, so the AST will be defined outside of ANTLR's reach, and encapsulated away from the rest of the system. ANTLR can then generate parsers for each syntax separately, or if somebody wanted to code one by hand, it should be possible.

### Open thoughts

* Supporting an in-file directive suggests that we could conceivably have more than one directive within a single source file, allowing for code in the same file to be written in two different syntaxes (yet refer to identifiers written in either). Supporting that could be interesting.

## Plan

- [x] Get the common procedural AST in place, with a number of tests to verify that once an AST instance tree is defined, it can execute. **Caveat:** First pass, I created my own AST; however, the goal was/is to use the Python AST, so see subsequent steps.

- [x] Set the parser abstraction in place (essentially a single source -> AST function).

- [x] Set up lots of tests in place to test each of the different parsers, of course.

- [x] Build the ANTLR g4 for an English (`en-us`) syntax and implement that. 

- [x] Migrate off of my AST and over to Python's AST.

- [ ] Since I know French (`fr`) reasonably well and German (`de`) passably so, target those two languages as second and third syntaxes. Should really be a copy of the `en-us` parser over and change just the keywords in the g4 parser grammar file.... emphasis on *should*. Oh heck, let's do Pig Latin (`en-pl`) as well, just for fun.

- [ ] Support an inline "keyword switch" pragma (a la `#parser en-us` or `#parser fr`, whatever's stored in the parsers dictionary) to allow us to switch mid-file to a different lexer. Already-established scopes would not change. I'm thinking the driver would just scan the whole file first, find each `#parser` line, and figuratively `split()` the whole thing before handing each segment off to its own parser, and then the whole would be collected into a single `ast.Module` for execution. (Maybe?)

Once I get to this point, I may put the idea on hold (though I'm always open to community contributions!) since the point will have been proven relatively well (or not!) by then.

Goal is to have this experiment "done" by the end of 2025.

-- Ted Neward (10 Oct 2025)

## Contents

* `antlrbox`: Rather than experiment with the ANTLR grammar in a subdirectory somewhere, I want to do it here where there's less overhead. Two experiments in particular: simplifying the grammar down some, and breaking it into lexer and parser g4 files (and then just swapping out the lexer files).

    **NOTES:**

    * Splitting the grammar is relatively easy; lexers must begin with `lexer grammar`, parsers must begin with `parser grammar`, and if the grammar is to be loaded and used from within `grun`/`TestRig`, the *filenames* must be precisely *language*`Lexer.g4` and *language*`Parser.g4`. You cannot do what I'd been doing, which is embed the internationalization codes in the lexer name (a la `LinguisENUSLexer`). `grun` doesn't really like that. *sigh*

    * There's not a lot of obvious places to simplify the grammar, I think. I could add actions, I suppose (once I spend more time figuring out how they work in ANTLR4), but all in all it seems pretty straightforward. I think I'm going to call that part of the experiment concluded with what's in v5. (I'm keeping this whole tree around, though, for easier `grun`-based exploration and validation.)

* `syntax`: Since I can't keep two different lexers in the same directory, I created this directory to be the repository for copies of the lexers and/or general descriptions of each input language's syntax. Moved the `SYNTAX.md` file here, too, just for easier reference. Each of the different lexers is in this directory, in case I want to make general changes to all of them, and the `copy.sh` script copies them over to their respective parser directory (and on top of the current files).

* `examples`: Some example Linguis programs.

* `linguis-phase1`: As its name implies, this was the "first pass" at building Linguis in Python. It had its own AST, which I now consider to be a mistake--I had actually imagined using the Python AST directly, then went ahead and built my own AST for some reason. I didn't delete it from the repo (or shove it off into a branch) because I want to keep it around for a while for reference purposes.

* `python`: Second pass, using Python AST as the result of the parser step. See the [README](python/README.md) for more details.

    * `parsers`: This directory contains the base-classes and shared code for all parsers. (There's not a lot, since I don't want to assume ANTLR for all of them.) **TODO:** At some point, I think I want to have one of the parsers built "by hand", just to make sure that there's nothing ANTLR-ish leaking out.

