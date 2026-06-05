---
chunk_id: "chapter6-reduced-1-e8f2336f2b-chunk-0002"
source_id: "chapter6-reduced-1-e8f2336f2b"
source_file: "Chapter6_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Constraints: adjacent regions must have   different colors 
      e.g., WA /= NT (if the language allows this), or
(WA, NT ) ∈ {(red, green), (red, blue), (green, red), (green, blue), . . .}

Solutions are assignments satisfying all constraints,
   e.g., {WA = red, NT = green, Q = red, NSW = green, V = red, SA = blue, T = green}

6

## Slide 7

Constraint graph

General-purpose CSP algorithms use the graph structure
to speed up search. E.g., Tasmania is an independent subproblem!

Binary CSP: each constraint relates at most two variables
Constraint graph: nodes are variables, arcs show constraints

7

## Slide 8

Discrete variables
finite domains; size d⇒O(dn) complete assignments
     e.g., Boolean CSPs, incl. Boolean satisfiability (NP-complete) 
infinite domains (integers, strings, etc.)
e.g., job scheduling, variables are start/end days for each job
need a constraint language, e.g., StartJob1 + 5 ≤ StartJob3
linear constraints solvable, nonlinear undecidable
Continuous variables
e.g., start/end times for Hubble Telescope observations
linear constraints solvable in poly time by LP methods

Varieties of CSP

8

## Slide 9

Unary constraints involve a single variable, e.g., SA /= green

Binary constraints involve pairs of variables, e.g., SA /= WA

Higher-order constraints involve 3 or more variables, e.g.,
 cryptarithmetic column constraints

Preferences (soft constraints), e.g., red is better than green
often representable by a cost for each variable assignment
→ constrained optimization problems

Varieties of CSP

9

## Slide 10

Variables: F T U W R O X1 X2 X3

Domains: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

Constraints:
alldiff(F, T, U, W, R, O)

O + O = R + 10 · X1, etc.

Example: Cryptarithmetic

10

## Slide 11

Example: Sudoku

Variables:  Each (open) square
Domains:   {1,2,…,9}
Constraints:

9-way alldiff for each row

9-way alldiff for each column

9-way alldiff for each region

(or can have a bunch of pairwise inequality constraints)

11

## Slide 12

Real-World CSPs

Assignment problems: e.g., who teaches what class
Timetabling problems: e.g., which class is offered when and where?
Hardware configuration
Transportation scheduling
Factory scheduling
Circuit layout
…

Many real-world problems involve real-valued variables

12

## Slide 13

How to Solve CSP?

Treat it as a search problem
Assign one variable at a time
State: A partial assignment 
Action: Assign value to an unassigned variable
Goal test: check whether all constraint are satisfied
