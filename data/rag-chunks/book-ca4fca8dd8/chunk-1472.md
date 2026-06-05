---
chunk_id: "book-ca4fca8dd8-chunk-1472"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1472
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 888

888
Chapter 24
Natural Language Processing
function CYK-PARSE(words,grammar) returns a table of parse trees
inputs: words, a list of words
grammar, a structure with LEXICALRULES and GRAMMARRULES
T ←a table
// T[X, i, k] is most probable X tree spanning wordsi:k
P←a table, initially all 0
// P[X, i, k] is probability of tree T[X, i, k]
// Insert lexical categories for each word.
for i = 1 to LEN(words) do
for each (X, p) in grammar.LEXICALRULES(wordsi) do
P[X, i, i]←p
T[X, i, i]←TREE(X, wordsi)
// Construct Xi:k from Yi:j + Zj+1:k, shortest spans ﬁrst.
for each (i, j, k) in SUBSPANS(LEN(words)) do
for each (X, Y, Z, p) in grammar.GRAMMARRULES do
PYZ ←P[Y, i, j] × P[Z, j+1, k] × p
if PYZ > P[X, i, k] do
P[X, i, k]←PYZ
T[X, i, k]←TREE(X, T[Y, i, j], T[Z, j + 1, k])
return T
function SUBSPANS(N) yields (i, j, k) tuples
for length = 2 to N do
for i = 1 to N + 1 −length do
k←i + length −1
for j = i to k −1 do
yield (i, j, k)
Figure 24.5 The CYK algorithm for parsing. Given a sequence of words, it ﬁnds the most
probable parse tree for the sequence and its subsequences. The table P[X,i,k] gives the prob-
ability of the most probable tree of category X spanning wordsi:k. The output table T[X, i, k]
contains the most probable tree of category X spanning positions i to k inclusive. The func-
tion SUBSPANS returns all tuples (i,j,k) covering a span of wordsi:k, with i ≤j < k, listing the
tuples by increasing length of the i : k span, so that when we go to combine two shorter spans
into a longer one, the shorter spans are already in the table. LEXICALRULES(word) returns a
collection of (X, p) pairs, one for each rule of the form X →word [p], and GRAMMARRULES
gives (X,Y,Z,p) tuples, one for each grammar rule of the form X →Y Z [p].
Article
Noun
wumpus
Verb
NP
VP
S
Every
smells
0.25
0.90
 0.05
 0.15
 0.10
 0.40
Figure 24.6 Parse tree for the sentence “Every wumpus smells” according to the grammar
E0. Each interior node of the tree is labeled with its probability. The probability of the tree as
a whole is 0.9×0.25×0.05×0.15×0.40×0.10=0.0000675. The tree can also be written
in linear form as [S [NP [Article every][Noun wumpus]][VP [Verb smells]]].

## Page 889
