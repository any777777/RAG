---
chunk_id: "chapter6-reduced-1-e8f2336f2b-chunk-0005"
source_id: "chapter6-reduced-1-e8f2336f2b"
source_file: "Chapter6_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

function AC-3( csp) returns the CSP, possibly with reduced domains
inputs: csp, a binary CSP with variables {X1, X2, . . . , Xn}
local variables: queue, a queue of arcs, initially all the arcs in csp
while queue is not empty do
(Xi, Xj ) ← Remove-First(queue)
if Remove-Inconsistent-Values(Xi, Xj ) then for each Xk in Neighbors[Xi] do
add (Xk, Xi) to queue

function Remove-Inconsistent-Values( Xi, Xj) returns true iff succeeds
removed ← false
for each x in Domain[Xi] do
if no value y in Domain[Xj] allows (x,y) to satisfy the constraint Xi	↔	Xj
then delete x from Domain[Xi];	removed ← true
return removed

O(n2d3), can be reduced to O(n2d2) (but detecting all is NP-hard)

Arc consistency

33

## Slide 34

CSPs are a special kind of problem:
states defined by values of a fixed set of variables goal test defined by constraints on variable values
Backtracking = depth-first search with one variable assigned per node Variable ordering and value selection heuristics help significantly
 Forward checking prevents assignments that guarantee later failure
 Constraint propagation (e.g., arc consistency) does additional work
to constrain values and detect inconsistencies
The CSP representation allows analysis of problem structure Tree-structured CSPs can be solved in linear time
Iterative min-conflicts is usually effective in practice

Summary

34
