---
chunk_id: "ch6-15ec9003b6-chunk-0005"
source_id: "ch6-15ec9003b6"
source_file: "CH6.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

Simplest form of propagation makes each arc consistent
X →Y is consistent iff
for every value x of X there is some allowed y
WA
NT
Q
NSW
V
SA
T
If X loses a value, neighbors of X need to be
rechecked
Arc consistency
31

## Page 32

Simplest form of propagation makes each arc consistent
X →Y is consistent iff
for every value x of X there is some allowed y
WA
NT
Q
NSW
V
SA
T
If X loses a value, neighbors of X need to be rechecked
Arc consistency detects failure earlier than forward checking 
Can be run as a preprocessor or after each assignment
Arc consistency
32

## Page 33

function AC-3(csp) returns the CSP, possibly with reduced domains
inputs: csp, a binary CSP with variables {X1, X2, . . . , Xn}
local variables: queue, a queue of arcs, initially all the arcs in csp
while queue is not empty do
(Xi, Xj )←REMOVE-FIRST(queue)
if REMOVE-INCONSISTENT-VALUES(Xi, Xj) then 
for each Xk in NEIGHBORS[Xi] do
add (Xk, Xi) to queue
function REMOVE-INCONSISTENT-VALUES(Xi, Xj) returns true iff succeeds
removed←false
for each x in DOMAIN[Xi] do
if no value y in DOMAIN[Xj] allows (x,y) to satisfy the constraint Xi
↔Xj
then delete x from DOMAIN[Xi]; removed←true
return removed
O(n2d3), can be reduced to O(n2d2) (but detecting all is NP-hard)
Arc consistency
33

## Page 34

CSPs are a special kind of problem:
states defined by values of a fixed set of variables goal test defined by
constraints on variable values
Backtracking = depth-first search with one variable assigned per node Variable
ordering and value selection heuristics help significantly
Forward checking prevents assignments that guarantee later failure
Constraint propagation (e.g., arc consistency) does additional work
to constrain values and detect inconsistencies
The CSP representation allows analysis of problem structure Tree-structured
CSPs can be solved in linear time
Iterative min-conflicts is usually effective in practice
Summary
34
