---
chunk_id: "ch6-15ec9003b6-chunk-0003"
source_id: "ch6-15ec9003b6"
source_file: "CH6.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

How to Solve CSP? 
●Treat it as a search problem
●Assign one variable at a time
●State: A partial assignment 
●Action: Assign value to an unassigned variable
●Goal test: check whether all constraint are 
satisfied
●But there’s more structure to leverage
●Variable ordering doesn’t matter
●Variables are interdependent in a local way
●We will start from known search algorithms, 
and try to speed it up 
13

## Page 14

Variable assignments are commutative, i.e.,
[WA = red thenNT = green] sameas
[NT = green thenWA = red]
Only need to consider assignments to a single variableat each node
⇒b= d and there are dn leaves
Depth-first search for CSPs with single-variableassignments is
called backtracking search
Backtracking search is the basic uninformed algorithm for CSPs Can
Can solve n-queens for n ≈25
Backtracking search
14

## Page 15

function BACKTRACKING-SEARCH(csp) returns solution/failure
return RECURSIVE-BACKTRACKING({ },csp)
function RECURSIVE-BACKTRACKING(assignment,csp) returns soln/failure
if assignment is complete then return assignment
var ←SELECT-UNASSIGNED-VARIABLE(VARIABLES[csp], assignment, csp)
for each value in ORDER-DOMAIN-VALUES(var,assignment,csp) do
if value is consistent with assignment given CONSTRAINTS[csp] then
add {var = value} to assignment
result ←RECURSIVE-BACKTRACKING(assignment, csp)
if result /=failure then return result
remove {var = value} from assignment
return failure
Backtracking search
15

## Page 16

Backtracking example
16

## Page 17

Backtracking example
17

## Page 18

Backtracking example
18

## Page 19

Backtracking example
19

## Page 20

General-purpose methods can give huge gains in speed:
1.Which variable should be assigned next?
2.In what order should its values be tried?
3.Can we detect inevitable failure early?
4.Can we take advantage of problem structure?
Improving Backtracking efficiency
20

## Page 21

Minimum remaining values (MRV):
choose the variable with the fewest legal values
Minimum remaining values
21

## Page 22

Tie-breaker among MRV (Minimum Remaining Values) variables
Degree heuristic:
choose the variable with the most constraints on remaining variables
Degree heuristics 
22

## Page 23
