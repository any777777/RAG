---
chunk_id: "book-ca4fca8dd8-chunk-0241"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 241
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 147

Section 4.4
Search in Partially Observable Environments
147
L
R
S
L
R
S
L
R
S
L
R
S
L
R
S
L
R
S
L
R
S
1
1
3
5
7
2
4
6
8
2
3
4
5
6
7
8
4
5
7
8
5
3
7
6
4
8
4
8
5
7
6
8
8
7
3
7
Figure 4.14 The reachable portion of the belief-state space for the deterministic, sensorless
vacuum world. Each rectangular box corresponds to a single belief state. At any given point,
the agent has a belief state but does not know which physical state it is in. The initial belief
state (complete ignorance) is the top center box.
say, “Not in the rightmost column,” and so on. Chapter 7 explains how to do this in a formal
representation scheme.
Another approach is to avoid the standard search algorithms, which treat belief states as
black boxes just like any other problem state. Instead, we can look inside the belief states
and develop incremental belief-state search algorithms that build up the solution one phys-
Incremental
belief-state search
ical state at a time. For example, in the sensorless vacuum world, the initial belief state is
{1,2,3,4,5,6,7,8}, and we have to ﬁnd an action sequence that works in all 8 states. We can
do this by ﬁrst ﬁnding a solution that works for state 1; then we check if it works for state 2;
if not, go back and ﬁnd a different solution for state 1, and so on.
Just as an AND–OR search has to ﬁnd a solution for every branch at an AND node, this
algorithm has to ﬁnd a solution for every state in the belief state; the difference is that AND–
OR search can ﬁnd a different solution for each branch, whereas an incremental belief-state
search has to ﬁnd one solution that works for all the states.
The main advantage of the incremental approach is that it is typically able to detect failure
quickly—when a belief state is unsolvable, it is usually the case that a small subset of the

## Page 148
