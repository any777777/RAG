---
chunk_id: "book-ca4fca8dd8-chunk-1126"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1126
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.3
Learning Decision Trees
675
Example
Input Attributes
Output
Alt
Bar
Fri
Hun
Pat
Price Rain
Res
Type
Est
WillWait
x1
Yes
No
No
Yes
Some
$$$
No
Yes
French
0–10
y1 = Yes
x2
Yes
No
No
Yes
Full
$
No
No
Thai
30–60
y2 = No
x3
No
Yes
No
No
Some
$
No
No
Burger
0–10
y3 = Yes
x4
Yes
No
Yes
Yes
Full
$
Yes
No
Thai
10–30
y4 = Yes
x5
Yes
No
Yes
No
Full
$$$
No
Yes
French
>60
y5 = No
x6
No
Yes
No
Yes
Some
$$
Yes
Yes
Italian
0–10
y6 = Yes
x7
No
Yes
No
No
None
$
Yes
No
Burger
0–10
y7 = No
x8
No
No
No
Yes
Some
$$
Yes
Yes
Thai
0–10
y8 = Yes
x9
No
Yes
Yes
No
Full
$
Yes
No
Burger
>60
y9 = No
x10
Yes
Yes
Yes
Yes
Full
$$$
No
Yes
Italian
10–30
y10 = No
x11
No
No
No
No
None
$
No
No
Thai
0–10
y11 = No
x12
Yes
Yes
Yes
Yes
Full
$
No
No
Burger
30–60
y12 = Yes
Figure 19.2 Examples for the restaurant domain.
19.3 Learning Decision Trees
A decision tree is a representation of a function that maps a vector of attribute values to
Decision tree
a single output value—a “decision.” A decision tree reaches its decision by performing a
sequence of tests, starting at the root and following the appropriate branch until a leaf is
reached. Each internal node in the tree corresponds to a test of the value of one of the input
attributes, the branches from the node are labeled with the possible values of the attribute,
and the leaf nodes specify what value is to be returned by the function.
In general, the input and output values can be discrete or continuous, but for now we will
consider only inputs consisting of discrete values and outputs that are either true (a positive
Positive
example) or false (a negative example). We call this Boolean classiﬁcation. We will use j
Negative
to index the examples (xj is the input vector for the jth example and yj is the output), and xj,i
for the ith attribute of the jth example.
The tree representing the decision function that SR uses for the restaurant problem is
shown in Figure 19.3. Following the branches, we see that an example with Patrons=Full
and WaitEstimate=0–10 will be classiﬁed as positive (i.e., yes, we will wait for a table).
19.3.1 Expressiveness of decision trees
A Boolean decision tree is equivalent to a logical statement of the form:
Output ⇔(Path1 ∨Path2 ∨···),
where each Pathi is a conjunction of the form (Am = vx ∧An = vy ∧···) of attribute-value
tests corresponding to a path from the root to a true leaf. Thus, the whole expression is
in disjunctive normal form, which means that any function in propositional logic can be
expressed as a decision tree.
For many problems, the decision tree format yields a nice, concise, understandable result.
Indeed, many “How To” manuals (e.g., for car repair) are written as decision trees. But some
functions cannot be represented concisely. For example, the majority function, which returns
