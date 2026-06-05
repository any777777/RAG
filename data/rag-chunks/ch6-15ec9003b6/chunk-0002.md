---
chunk_id: "ch6-15ec9003b6-chunk-0002"
source_id: "ch6-15ec9003b6"
source_file: "CH6.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Example: Map Coloring
●Variables WA, NT , Q, NSW , V , SA, T
●Domains D i = {red, green, blue}
●Constraints: adjacent regions must have
different
colors 
e.g., WA /= N T (if the language allows this), or
●(WA, N T ) ∈{(red, green), (red, blue), (green, red), (green,
blue), . . .}
●Solutions are assignments satisfying all constraints,
e.g., {WA = red, NT = green, Q = red, NSW = green, V
= red, SA = blue, T = green}
6

## Page 7

Constraint graph
General-purpose CSP algorithms use the graph structure
to speed up search. E.g., Tasmania is an independent subproblem!
Binary CSP: each constraint relates at most two variables
Constraint graph: nodes are variables, arcs show constraints
7

## Page 8

Discrete variables
finite domains; size d⇒O(dn) complete assignments
e.g., Boolean CSPs, incl. Boolean satisfiability (NP-complete) 
infinite domains (integers, strings, etc.)
e.g., job scheduling, variables are start/end days for each job
need a constraint language, e.g., StartJob1 + 5 ≤StartJob3
linear constraints solvable, nonlinear undecidable
Continuous variables
e.g., start/end times for Hubble Telescope observations
linear constraints solvable in poly time by LP methods
Varieties of CSP
8

## Page 9

Unary constraints involve a single variable, e.g., SA /= green
Binary constraints involve pairs of variables, e.g., SA /= WA
Higher-order constraints involve 3 or more variables, e.g.,
cryptarithmetic column constraints
Preferences (soft constraints), e.g., red is better than green
often representable by a cost for each variable assignment
→constrained optimization problems
Varieties of CSP
9

## Page 10

Variables: F T U W R O X 1 X 2 X 3
Domains: {0, 1,2, 3,4, 5,6, 7,8, 9}
Constraints:
alldiff(F, T, U, W, R, O)
O + O = R + 10 ·X1, etc.
Example: Cryptarithmetic
10

## Page 11

Example: Sudoku
●Variables:  Each (open) 
square
●Domains:   {1,2,…,9}
●Constraints:
9-way alldiff for each row
9-way alldiff for each column
9-way alldiff for each region
(or can have a bunch of 
pairwise inequality 
constraints)
11

## Page 12

Real-World CSPs
●Assignment problems: e.g., who teaches what class
●Timetabling problems: e.g., which class is offered when and where?
●Hardware configuration
●Transportation scheduling
●Factory scheduling
●Circuit layout
●…
●Many real-world problems involve real-valued variables
12

## Page 13
