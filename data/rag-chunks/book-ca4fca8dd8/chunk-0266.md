---
chunk_id: "book-ca4fca8dd8-chunk-0266"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 266
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 5
CONSTRAINT SATISFACTION
PROBLEMS
In which we see how treating states as more than just little black boxes leads to new search
methods and a deeper understanding of problem structure.
Chapters 3 and 4 explored the idea that problems can be solved by searching the state space:
a graph where the nodes are states and the edges between them are actions. We saw that
domain-speciﬁc heuristics could estimate the cost of reaching the goal from a given state,
but that from the point of view of the search algorithm, each state is atomic, or indivisible—
a black box with no internal structure. For each problem we need domain-speciﬁc code to
describe the transitions between states.
In this chapter we break open the black box by using a factored representation for each
state: a set of variables, each of which has a value. A problem is solved when each variable
has a value that satisﬁes all the constraints on the variable. A problem described this way is
called a constraint satisfaction problem, or CSP.
Constraint
satisfaction problem
CSP search algorithms take advantage of the structure of states and use general rather
than domain-speciﬁc heuristics to enable the solution of complex problems. The main idea
is to eliminate large portions of the search space all at once by identifying variable/value
combinations that violate the constraints. CSPs have the additional advantage that the actions
and transition model can be deduced from the problem description.
5.1 Deﬁning Constraint Satisfaction Problems
A constraint satisfaction problem consists of three components, X,D, and C:
X is a set of variables, {X1,...,Xn}.
D is a set of domains, {D1,...,Dn}, one for each variable.
C is a set of constraints that specify allowable combinations of values.
A domain, Di, consists of a set of allowable values, {v1,...,vk}, for variable Xi. For exam-
ple, a Boolean variable would have the domain {true,false}. Different variables can have
different domains of different sizes. Each constraint Cj consists of a pair ⟨scope,rel⟩, where
scope is a tuple of variables that participate in the constraint and rel is a relation that de-
Relation
ﬁnes the values that those variables can take on. A relation can be represented as an ex-
plicit set of all tuples of values that satisfy the constraint, or as a function that can compute
whether a tuple is a member of the relation. For example, if X1 and X2 both have the do-
main {1,2,3}, then the constraint saying that X1 must be greater than X2 can be written as
⟨(X1,X2),{(3,1),(3,2),(2,1)}⟩or as ⟨(X1,X2),X1 > X2⟩.
