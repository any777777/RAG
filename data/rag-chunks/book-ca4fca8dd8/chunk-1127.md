---
chunk_id: "book-ca4fca8dd8-chunk-1127"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1127
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 676

676
Chapter 19
Learning from Examples
true if and only if more than half of the inputs are true, requires an exponentially large decision
tree, as does the parity function, which returns true if and only if an even number of input
attributes are true. With real-valued attributes, the function y > A1 + A2 is hard to represent
with a decision tree because the decision boundary is a diagonal line, and all decision tree
tests divide the space up into rectangular, axis-aligned boxes. We would have to stack a lot
of boxes to closely approximate the diagonal line. In other words, decision trees are good for
some kinds of functions and bad for others.
Is there any kind of representation that is efﬁcient for all kinds of functions? Unfortu-
nately, the answer is no—there are just too many functions to be able to represent them all
with a small number of bits. Even just considering Boolean functions with n Boolean at-
tributes, the truth table will have 2n rows, and each row can output true or false, so there are
22n different functions. With 20 attributes there are 21,048,576 ≈10300,000 functions, so if we
limit ourselves to a million-bit representation, we can’t represent all these functions.
19.3.2 Learning decision trees from examples
We want to ﬁnd a tree that is consistent with the examples in Figure 19.2 and is as small as
possible. Unfortunately, it is intractable to ﬁnd a guaranteed smallest consistent tree. But
with some simple heuristics, we can efﬁciently ﬁnd one that is close to the smallest. The
LEARN-DECISION-TREE algorithm adopts a greedy divide-and-conquer strategy: always
test the most important attribute ﬁrst, then recursively solve the smaller subproblems that are
deﬁned by the possible results of the test. By “most important attribute,” we mean the one
that makes the most difference to the classiﬁcation of an example. That way, we hope to get
to the correct classiﬁcation with a small number of tests, meaning that all paths in the tree
will be short and the tree as a whole will be shallow.
Figure 19.4(a) shows that Type is a poor attribute, because it leaves us with four possible
No
 Yes
No
 Yes
No
 Yes
No
 Yes
None
Some
Full
>60
30-60
10-30
0-10
No
 Yes
Alternate?
Hungry?
Reservation?
Bar?
Raining?
Alternate?
Patrons?
Fri/Sat?
No
Yes
No
Yes
Yes
Yes
No
 Yes
No
Yes
Yes
No
Yes
No
 Yes
Yes
No
WaitEstimate?
Figure 19.3 A decision tree for deciding whether to wait for a table.

## Page 677
