---
chunk_id: "chapter6-reduced-1-e8f2336f2b-chunk-0003"
source_id: "chapter6-reduced-1-e8f2336f2b"
source_file: "Chapter6_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

But there’s more structure to leverage
Variable ordering doesn’t matter
Variables are interdependent in a local way

We will start from known search algorithms, and try to speed it up

13

## Slide 14

Variable assignments are commutative, i.e.,
[WA = red then NT = green] same as	[NT = green then WA = red]
Only need to consider assignments to a single variable at each node
⇒	b = d and there are dn leaves

Depth-first search for CSPs with single-variable assignments is called backtracking search
Backtracking search is the basic uninformed algorithm for CSPs Can Can solve n-queens for n ≈ 25

Backtracking search

14

## Slide 15

function Backtracking-Search(csp) returns solution/failure
return Recursive-Backtracking({ }, csp)
function Recursive-Backtracking(assignment, csp) returns soln/failure
if assignment is complete then return assignment
var ← Select-Unassigned-Variable(Variables[csp], assignment, csp)
for each value in Order-Domain-Values(var, assignment, csp) do
if value is consistent with assignment given Constraints[csp] then
add {var = value} to assignment
result ← Recursive-Backtracking(assignment, csp)
if result /= failure then return result
remove {var = value} from assignment
return failure

Backtracking search

15

## Slide 16

Backtracking example

16

## Slide 17

Backtracking example

17

## Slide 18

Backtracking example

18

## Slide 19

Backtracking example

19

## Slide 20

General-purpose methods can give huge gains in speed:
Which variable should be assigned next?

In what order should its values be tried?

Can we detect inevitable failure early?

Can we take advantage of problem structure?

Improving Backtracking efficiency

20

## Slide 21

Minimum remaining values (MRV):
choose the variable with the fewest legal values

Minimum remaining values

21

## Slide 22

Tie-breaker among MRV (Minimum Remaining Values) variables
Degree heuristic:
choose the variable with the most constraints on remaining variables

Degree heuristics

22

## Slide 23

Given a variable, choose the least constraining value (color):
the one that rules out the fewest values in the remaining variables

Allows 0 values for SA

Combining these heuristics  (mrv, degree heuristic,LCV)  makes 1000 queens feasible : 
	Backtracking alone can solve 8-Queens easily, 25-Queens with difficulty, but 1000-Queens is almost impossible without heuristics."

Least Constraint values

Allows 1 value for SA

23

## Slide 24

Idea: Keep track of remaining legal values for unassigned variables Terminate search when any variable has no legal values

WA

NT

Q

NSW

V

SA

T

Forward Checking
