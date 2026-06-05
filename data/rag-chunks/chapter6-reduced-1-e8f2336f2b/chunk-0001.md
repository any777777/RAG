---
chunk_id: "chapter6-reduced-1-e8f2336f2b-chunk-0001"
source_id: "chapter6-reduced-1-e8f2336f2b"
source_file: "Chapter6_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Slide 1

Artificial intelligence

1

## Slide 2

What is CSP?
    Problem is  defined by a set of variables.
    Each variable has a domain of possible values.
    A set of constraints specifies allowable combinations of values.
Goal:
    Find an assignment of values to variables that satisfies all constraints.

Why CSPs?
Provide a general framework for many AI problems.
Allow the use of powerful, domain-independent algorithms.
Can drastically reduce search space using constraints.

Examples:  Map coloring, Sudoku, Scheduling, Cryptarithmetic puzzles

Introduction

2

## Slide 3

CSP consists of three components, X, D, and C:
X is a set of variables, {X1, . . . , Xn}.
D is a set of domains, {D1, . . . , Dn}, one for each variable.
C is a set of constraints that specify allowable combinations of values.
A domain, Di, consists of a set of allowable values, {v1, . . . ,vk}, for variable Xi.
For example, a Boolean variable would have the domain {true, false}.
Different variables can have different domains of different sizes.

Constraint satisfaction problems (CSPs)

3

## Slide 4

Constraint satisfaction problems (CSPs)

Each constraint Cj consists of a pair〈scope, rel〉,
where scope is a tuple of variables that participate in the constraint
and rel is a relation that defines the values that those variables can take on.

A relation can be represented as an explicit set of all tuples of values that satisfy the constraint, or as a function that can compute whether 	a tuple is a member of the relation.
For example, if X1 and X2 both have the domain {1,2,3}, then the constraint saying that X1 must be greater than X2 can be written as
〈(X1,X2), {(3,1), (3,2), (2,1)} 〉
or as 〈(X1,X2), X1 > X2〉.

4

## Slide 5

Constraint satisfaction problems (CSPs)

CSPs deal with assignments of values to variables,
{Xi = vi, Xj = vj, . . .}.
An assignment that does not violate any constraints is called a consistent
or legal assignment.
A complete assignment is one in which every variable is assigned a value,
and a solution to a CSP is a consistent, complete assignment.
A partial assignment is one that leaves some variables unassigned,
and a partial solution is a partial assignment that is consistent.
Solving a CSP is an NP-complete problem in general,
although there are important subclasses of CSPs that can be solved very efficiently.

5

## Slide 6

Example: Map Coloring

Variables WA, NT , Q, NSW , V , SA, T

Domains Di = {red, green, blue}
