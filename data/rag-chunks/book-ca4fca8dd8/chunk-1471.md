---
chunk_id: "book-ca4fca8dd8-chunk-1471"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1471
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.3
Parsing
887
List of items
Rule
S
NP VP
S →NP VP
NP VP Adjective
VP →VP Adjective
NP Verb Adjective
VP →Verb
NP Verb dead
Adjective →dead
NP is dead
Verb →is
Article Noun is dead
NP →Article Noun
Article wumpus is dead
Noun →wumpus
the wumpus is dead
Article →the
Figure 24.4 Parsing the string “The wumpus is dead” as a sentence, according to the gram-
mar E0. Viewed as a top-down parse, we start with S, and on each step match one nontermi-
nal X with a rule of the form (X →Y ...) and replace X in the list of items with Y ...; for
example replacing S with the sequence NP VP. Viewed as a bottom-up parse, we start with
the words “the wumpus is dead”, and on each step match a string of tokens such as (Y ...)
against a rule of the form (X →Y ...) and replace the tokens with X; for example replacing
“the” with Article or Article Noun with NP.
The CYK algorithm is shown in Figure 24.5. It requires a grammar with all rules in one
of two very speciﬁc formats: lexical rules of the form X →word [p], and syntactic rules of
the form X →Y Z [p], with exactly two categories on the right-hand side. This grammar
format, called Chomsky Normal Form, may seem restrictive, but it is not: any context-free
Chomsky Normal
Form
grammar can be automatically transformed into Chomsky Normal Form. Exercise 24.CNFX
leads you through the process.
The CYK algorithm uses space of O(n2m) for the P and T tables, where n is the number of
words in the sentence, and m is the number of nonterminal symbols in the grammar, and takes
time O(n3m). If we want an algorithm that is guaranteed to work for all possible context-
free grammars, then we can’t do any better than that. But actually we only want to parse
natural languages, not all possible grammars. Natural languages have evolved to be easy
to understand in real time, not to be as tricky as possible, so it seems that they should be
amenable to a faster parsing algorithm.
To try to get to O(n), we can apply A∗search in a fairly straightforward way: each state is
a list of items (words or categories), as shown in Figure 24.4. The start state is a list of words,
and a goal state is the single item S. The cost of a state is the inverse of its probability as
deﬁned by the rules applied so far, and there are various heuristics to estimate the remaining
distance to the goal; the best heuristics in current use come from machine learning applied to
a corpus of sentences.
With the A∗algorithm we don’t have to search the entire state space, and we are guaran-
teed that the ﬁrst parse found will be the most probable (assuming an admissible heuristic).
This will usually be faster than CYK, but (depending on the details of the grammar) still
slower than O(n). An example result of a parse is shown in Figure 24.6.
Just as with part-of-speech tagging, we can use a beam search for parsing, where at
any time we consider only the b most probable alternative parses. This means we are not
