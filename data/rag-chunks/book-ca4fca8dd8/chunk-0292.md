---
chunk_id: "book-ca4fca8dd8-chunk-0292"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 292
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.3
Backtracking Search for CSPs
179
Initial domains
After WA=red
After Q=green
After V=blue
WA
NT
Q
NSW
V
SA
T
Figure 5.7 The progress of a map-coloring search with forward checking. WA=red is as-
signed ﬁrst; then forward checking deletes red from the domains of the neighboring variables
NT and SA. After Q=green is assigned, green is deleted from the domains of NT, SA, and
NSW. After V =blue is assigned, blue is deleted from the domains of NSW and SA, leaving
SA with no legal values.
fails and we know to backtrack immediately. We can see that MAC is strictly more powerful
than forward checking because forward checking does the same thing as MAC on the initial
arcs in MAC’s queue; but unlike MAC, forward checking does not recursively propagate
constraints when changes are made to the domains of variables.
5.3.3 Intelligent backtracking: Looking backward
The BACKTRACKING-SEARCH algorithm in Figure 5.5 has a very simple policy for what to
do when a branch of the search fails: back up to the preceding variable and try a different
value for it. This is called chronological backtracking because the most recent decision
Chronological
backtracking
point is revisited. In this subsection, we consider better possibilities.
Consider what happens when we apply simple backtracking in Figure 5.1 with a ﬁxed
variable ordering Q, NSW, V, T, SA, WA, NT. Suppose we have generated the partial assign-
ment {Q=red,NSW =green,V =blue,T =red}. When we try the next variable, SA, we see
that every value violates a constraint. We back up to T and try a new color for Tasmania!
Obviously this is silly—recoloring Tasmania cannot possibly help in resolving the problem
with South Australia.
A more intelligent approach is to backtrack to a variable that might ﬁx the problem—a
variable that was responsible for making one of the possible values of SA impossible. To do
this, we will keep track of a set of assignments that are in conﬂict with some value for SA.
The set (in this case {Q=red,NSW =green,V =blue}), is called the conﬂict set for SA. The
Conﬂict set
backjumping method backtracks to the most recent assignment in the conﬂict set; in this
Backjumping
case, backjumping would jump over Tasmania and try a new value for V. This method is
easily implemented by a modiﬁcation to BACKTRACK such that it accumulates the conﬂict
set while checking for a legal value to assign. If no legal value is found, the algorithm should
return the most recent element of the conﬂict set along with the failure indicator.
The sharp-eyed reader may have noticed that forward checking can supply the conﬂict set
with no extra work: whenever forward checking based on an assignment X =x deletes a value
from Y’s domain, it should add X =x to Y’s conﬂict set. If the last value is deleted from Y’s
domain, then the assignments in the conﬂict set of Y are added to the conﬂict set of X. That
is, we now know that X =x leads to a contradiction (in Y), and thus a different assignment
should be tried for X.
