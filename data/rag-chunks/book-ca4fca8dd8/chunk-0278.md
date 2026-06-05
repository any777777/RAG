---
chunk_id: "book-ca4fca8dd8-chunk-0278"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 278
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.2
Constraint Propagation: Inference in CSPs
171
function AC-3(csp) returns false if an inconsistency is found and true otherwise
queue←a queue of arcs, initially all the arcs in csp
while queue is not empty do
(Xi, Xj)←POP(queue)
if REVISE(csp, Xi, Xj) then
if size of Di = 0 then return false
for each Xk in Xi.NEIGHBORS - {Xj} do
add (Xk, Xi) to queue
return true
function REVISE(csp, Xi, Xj) returns true iff we revise the domain of Xi
revised←false
for each x in Di do
if no value y in D j allows (x,y) to satisfy the constraint between Xi and Xj then
delete x from Di
revised←true
return revised
Figure 5.3 The arc-consistency algorithm AC-3. After applying AC-3, either every arc is
arc-consistent, or some variable has an empty domain, indicating that the CSP cannot be
solved. The name “AC-3” was used by the algorithm’s inventor (Mackworth, 1977) because
it was the third version developed in the paper.
and makes Xi arc-consistent with respect to Xj. If this leaves Di unchanged, the algorithm
just moves on to the next arc. But if this revises Di (makes the domain smaller), then we add
to the queue all arcs (Xk,Xi) where Xk is a neighbor of Xi. We need to do that because the
change in Di might enable further reductions in Dk, even if we have previously considered Xk.
If Di is revised down to nothing, then we know the whole CSP has no consistent solution, and
AC-3 can immediately return failure. Otherwise, we keep checking, trying to remove values
from the domains of variables until no more arcs are in the queue. At that point, we are left
with a CSP that is equivalent to the original CSP—they both have the same solutions—but
the arc-consistent CSP will be faster to search because its variables have smaller domains.
In some cases, it solves the problem completely (by reducing every domain to size 1) and in
others it proves that no solution exists (by reducing some domain to size 0).
The complexity of AC-3 can be analyzed as follows. Assume a CSP with n variables,
each with domain size at most d, and with c binary constraints (arcs). Each arc (Xk,Xi) can
be inserted in the queue only d times because Xi has at most d values to delete. Checking
consistency of an arc can be done in O(d2) time, so we get O(cd3) total worst-case time.
5.2.3 Path consistency
Suppose we are to color the map of Australia with just two colors, red and blue. Arc con-
sistency does nothing because every constraint can be satisﬁed individually with red at one
end and blue at the other. But clearly there is no solution to the problem: because Western
Australia, Northern Territory, and South Australia all touch each other, we need at least three
colors for them alone.
