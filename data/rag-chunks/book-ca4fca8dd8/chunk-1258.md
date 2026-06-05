---
chunk_id: "book-ca4fca8dd8-chunk-1258"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1258
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 762

762
Chapter 20
Knowledge in Learning
function FOIL(examples,target) returns a set of Horn clauses
inputs: examples, set of examples
target, a literal for the goal predicate
local variables: clauses, set of clauses, initially empty
while examples contains positive examples do
clause←NEW-CLAUSE(examples,target)
remove positive examples covered by clause from examples
add clause to clauses
return clauses
function NEW-CLAUSE(examples,target) returns a Horn clause
local variables: clause, a clause with target as head and an empty body
l, a literal to be added to the clause
extended examples, a set of examples with values for new variables
extended examples←examples
while extended examples contains negative examples do
l←CHOOSE-LITERAL(NEW-LITERALS(clause),extended examples)
append l to the body of clause
extended examples←set of examples created by applying EXTEND-EXAMPLE
to each example in extended examples
return clause
function EXTEND-EXAMPLE(example,literal) returns a set of examples
if example satisﬁes literal
then return the set of examples created by extending example with
each possible constant value for each new variable in literal
else return the empty set
Figure 20.12 Sketch of the FOIL algorithm for learning sets of ﬁrst-order Horn clauses from
examples. NEW-LITERALS and CHOOSE-LITERAL are explained in the text.
will incorrectly cover a negative example. In general FOIL will have to search through many
unsuccessful clauses before ﬁnding a correct solution.
This example is a very simple illustration of how FOIL operates. A sketch of the complete
algorithm is shown in Figure 20.12. Essentially, the algorithm repeatedly constructs a clause,
literal by literal, until it agrees with some subset of the positive examples and none of the
negative examples. Then the positive examples covered by the clause are removed from the
training set, and the process continues until no positive examples remain. The two main
subroutines to be explained are NEW-LITERALS, which constructs all possible new literals to
add to the clause, and CHOOSE-LITERAL, which selects a literal to add.
NEW-LITERALS takes a clause and constructs all possible “useful” literals that could be
added to the clause. Let us use as an example the clause
Father(x,z) ⇒Grandfather(x,y) .

## Page 763
