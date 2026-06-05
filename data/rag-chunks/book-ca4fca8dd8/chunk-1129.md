---
chunk_id: "book-ca4fca8dd8-chunk-1129"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1129
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 678

678
Chapter 19
Learning from Examples
function LEARN-DECISION-TREE(examples,attributes,parent examples) returns a tree
if examples is empty then return PLURALITY-VALUE(parent examples)
else if all examples have the same classiﬁcation then return the classiﬁcation
else if attributes is empty then return PLURALITY-VALUE(examples)
else
A←argmaxa∈attributes IMPORTANCE(a,examples)
tree←a new decision tree with root test A
for each value v of A do
exs←{e : e∈examples and e.A = v}
subtree←LEARN-DECISION-TREE(exs,attributes−A,examples)
add a branch to tree with label (A = v) and subtree subtree
return tree
Figure 19.5 The decision tree learning algorithm. The function IMPORTANCE is described
in Section 19.3.3. The function PLURALITY-VALUE selects the most common output value
among a set of examples, breaking ties randomly.
None
Some
Full
Patrons?
No
Yes
No
 Yes
Hungry?
No
No
 Yes
Fri/Sat?
Yes
No
Yes
Type?
French
Italian
Thai
Burger
Yes
No
Figure 19.6 The decision tree induced from the 12-example training set.
ure 19.3. One might conclude that the learning algorithm is not doing a very good job of
learning the correct function. This would be the wrong conclusion to draw, however. The
learning algorithm looks at the examples, not at the correct function, and in fact, its hypothe-
sis (see Figure 19.6) not only is consistent with all the examples, but is considerably simpler
than the original tree! With slightly different examples the tree might be very different, but
the function it represents would be similar.
The learning algorithm has no reason to include tests for Raining and Reservation, be-
cause it can classify all the examples without them. It has also detected an interesting and
previously unsuspected pattern: SR will wait for Thai food on weekends. It is also bound to
make some mistakes for cases where it has seen no examples. For example, it has never seen

## Page 679
