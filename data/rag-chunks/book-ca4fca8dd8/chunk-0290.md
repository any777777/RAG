---
chunk_id: "book-ca4fca8dd8-chunk-0290"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 290
confidence: "first-pass"
extraction_method: "structured-local"
---

178
Chapter 5
Constraint Satisfaction Problems
graph. For example, suppose that in Figure 5.1 we have generated the partial assignment
with WA=red and NT =green and that our next choice is for Q. Blue would be a bad choice
because it eliminates the last legal value left for Q’s neighbor, SA. The least-constraining-
value heuristic therefore prefers red to blue. In general, the heuristic is trying to leave the
maximum ﬂexibility for subsequent variable assignments.
Why should variable selection be fail-ﬁrst, but value selection be fail-last? Every variable
has to be assigned eventually, so by choosing the ones that are likely to fail ﬁrst, we will on
average have fewer successful assignments to backtrack over. For value ordering, the trick
is that we only need one solution; therefore it makes sense to look for the most likely values
ﬁrst. If we wanted to enumerate all solutions rather than just ﬁnd one, then value ordering
would be irrelevant.
5.3.2 Interleaving search and inference
We saw how AC-3 can reduce the domains of variables before we begin the search. But
inference can be even more powerful during the course of a search: every time we make
a choice of a value for a variable, we have a brand-new opportunity to infer new domain
reductions on the neighboring variables.
One of the simplest forms of inference is called forward checking. Whenever a variable
Forward checking
X is assigned, the forward-checking process establishes arc consistency for it: for each unas-
signed variable Y that is connected to X by a constraint, delete from Y’s domain any value
that is inconsistent with the value chosen for X.
Figure 5.7 shows the progress of backtracking search on the Australia CSP with forward
checking. There are two important points to notice about this example. First, notice that after
WA=red and Q=green are assigned, the domains of NT and SA are reduced to a single value;
we have eliminated branching on these variables altogether by propagating information from
WA and Q. A second point to notice is that after V =blue, the domain of SA is empty. Hence,
forward checking has detected that the partial assignment {WA=red,Q=green,V =blue} is
inconsistent with the constraints of the problem, and the algorithm backtracks immediately.
For many problems the search will be more effective if we combine the MRV heuristic
with forward checking. Consider Figure 5.7 after assigning {WA=red}. Intuitively, it seems
that that assignment constrains its neighbors, NT and SA, so we should handle those variables
next, and then all the other variables will fall into place. That’s exactly what happens with
MRV: NT and SA each have two values, so one of them is chosen ﬁrst, then the other, then
Q, NSW, and V in order. Finally T still has three values, and any one of them works. We can
view forward checking as an efﬁcient way to incrementally compute the information that the
MRV heuristic needs to do its job.
Although forward checking detects many inconsistencies, it does not detect all of them.
The problem is that it doesn’t look ahead far enough. For example, consider the Q=green
row of Figure 5.7. We’ve made WA and Q arc-consistent, but we’ve left both NT and SA with
blue as their only possible value, which is an inconsistency, since they are neighbors.
The algorithm called MAC (for Maintaining Arc Consistency) detects inconsistencies
Maintaining Arc
Consistency
like this. After a variable Xi is assigned a value, the INFERENCE procedure calls AC-3, but
instead of a queue of all arcs in the CSP, we start with only the arcs (Xj,Xi) for all Xj that are
unassigned variables that are neighbors of Xi. From there, AC-3 does constraint propagation
in the usual way, and if any variable has its domain reduced to the empty set, the call to AC-3
