---
chunk_id: "ch6-15ec9003b6-chunk-0004"
source_id: "ch6-15ec9003b6"
source_file: "CH6.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

Given a variable, choose the least constraining value (color):
the one that rules out the fewest values in the remaining variables
Allows 0 values for SA
Combining these heuristics (mrv, degree heuristic,LCV)  makes 1000
queens feasible : 
Backtracking alone can solve 8-Queens easily, 25-Queens with 
difficulty, but 1000-Queens is almost impossible without heuristics."
Least Constraint values
Allows 1 value for SA
23

## Page 24

Idea: Keep track of remaining legal values for unassigned variables 
Terminate search when any variable has no legal values
WA
NT
Q
NSW
V
SA
T
Forward Checking
24

## Page 25

Idea: Keep track of remaining legal values for unassigned variables 
Terminate search when any variable has no legal values
WA
NT
Q
NSW
V
SA
T
Forward Checking
25

## Page 26

Idea: Keep track of remaining legal values for unassigned variables 
Terminate search when any variable has no legal values
WA
NT
Q
NSW
V
SA
T
Forward Checking
26

## Page 27

Idea: Keep track of remaining legal values for unassigned variables 
Terminate search when any variable has no legal values
WA
NT
Q
NSW
V
SA
T
Forward Checking
27
It does not check for constraints  for variables that have not been 
assigned yet. It check constraints after assigning values!!!

## Page 28

Forward checking propagates information from assigned to unassigned vari-
ables, but doesn’t provide early detection for all failures:
WA
NT
Q
NSW
V
SA
T
N T and S A cannot both be blue!
Constraint propagation repeatedly enforces constraints locally
Constraint propagation
• A CSP algorithm can do a specific type of inference called constraint propagation: using the constraints to reduce the
number of legal values for a variable,
28

## Page 29

Simplest form of constraint propagation makes each arc consistent
X →Y is consistent iff
for every value x of X there is some allowed y
WA
NT
Q
NSW
V
SA
T
Arc consistency
•An arc X→Y is arc consistent if:
•For every value x in the domain of X, there exists at least one value y in the domain of Y
that satisfies the constraint between X and Y.
•If some x has no corresponding y, then x is removed from X’s domain.
29

## Page 30

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
Arc consistency
30

## Page 31
