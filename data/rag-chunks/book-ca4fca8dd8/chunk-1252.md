---
chunk_id: "book-ca4fca8dd8-chunk-1252"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1252
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 756

756
Chapter 20
Knowledge in Learning
function MINIMAL-CONSISTENT-DET(E,A) returns a set of attributes
inputs: E, a set of examples
A, a set of attributes, of size n
for i = 0 to n do
for each subset Ai of A of size i do
if CONSISTENT-DET?(Ai,E) then return Ai
function CONSISTENT-DET?(A,E) returns a truth value
inputs: A, a set of attributes
E, a set of examples
local variables: H, a hash table
for each example e in E do
if some example in H has the same values as e for the attributes A
but a different classiﬁcation then return false
store the class of e in H, indexed by the values for attributes A of the example e
return true
Figure 20.8 An algorithm for ﬁnding a minimal consistent determination.
For example, suppose we have the following examples of conductance measurements on
material samples:
Sample Mass Temperature Material Size
Conductance
S1
12
26
Copper
3
0.59
S1
12
100
Copper
3
0.57
S2
24
26
Copper
6
0.59
S3
12
26
Lead
2
0.05
S3
12
100
Lead
2
0.04
S4
24
26
Lead
4
0.05
The minimal consistent determination is Material∧Temperature ≻Conductance. There is a
nonminimal but consistent determination, namely, Mass∧Size∧Temperature ≻Conductance.
This is consistent with the examples because mass and size determine density and, in our data
set, we do not have two different materials with the same density. As usual, we would need a
larger sample set in order to eliminate a nearly correct hypothesis.
There are several possible algorithms for ﬁnding minimal consistent determinations. The
most obvious approach is to conduct a search through the space of determinations, checking
all determinations with one predicate, two predicates, and so on, until a consistent determi-
nation is found. We will assume a simple attribute-based representation, like that used for
decision tree learning in Chapter 19. A determination d will be represented by the set of
attributes on the left-hand side, because the target predicate is assumed to be ﬁxed. The basic
algorithm is outlined in Figure 20.8.
The time complexity of this algorithm depends on the size of the smallest consistent
determination. Suppose this determination has p attributes out of the n total attributes. Then

## Page 757
