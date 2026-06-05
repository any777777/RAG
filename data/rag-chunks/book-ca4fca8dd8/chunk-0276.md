---
chunk_id: "book-ca4fca8dd8-chunk-0276"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 276
confidence: "first-pass"
extraction_method: "structured-local"
---

170
Chapter 5
Constraint Satisfaction Problems
in turn can reduce the legal values for another variable, and so on. The idea is that this will
leave fewer choices to consider when we make the next choice of a variable assignment.
Constraint propagation may be intertwined with search, or it may be done as a preprocessing
step, before search starts. Sometimes this preprocessing can solve the whole problem, so no
search is required at all.
The key idea is local consistency. If we treat each variable as a node in a graph (see
Local consistency
Figure 5.1(b)) and each binary constraint as an edge, then the process of enforcing local
consistency in each part of the graph causes inconsistent values to be eliminated throughout
the graph. There are different types of local consistency, which we now cover in turn.
5.2.1 Node consistency
A single variable (corresponding to a node in the CSP graph) is node-consistent if all the
Node consistency
values in the variable’s domain satisfy the variable’s unary constraints. For example, in the
variant of the Australia map-coloring problem (Figure 5.1) where South Australians dislike
green, the variable SA starts with domain {red,green,blue}, and we can make it node con-
sistent by eliminating green, leaving SA with the reduced domain {red,blue}. We say that a
graph is node-consistent if every variable in the graph is node-consistent.
It is easy to eliminate all the unary constraints in a CSP by reducing the domain of vari-
ables with unary constraints at the start of the solving process. As mentioned earlier, it is also
possible to transform all n-ary constraints into binary ones. Because of this, some CSP solvers
work with only binary constraints, expecting the user to eliminate the other constraints ahead
of time. We make that assumption for the rest of this chapter, except where noted.
5.2.2 Arc consistency
A variable in a CSP is arc-consistent1 if every value in its domain satisﬁes the variable’s
Arc consistency
binary constraints. More formally, Xi is arc-consistent with respect to another variable Xj if
for every value in the current domain Di there is some value in the domain D j that satisﬁes
the binary constraint on the arc (Xi,Xj). A graph is arc-consistent if every variable is arc-
consistent with every other variable. For example, consider the constraint Y = X2 where the
domain of both X and Y is the set of decimal digits. We can write this constraint explicitly as
⟨(X,Y),{(0,0),(1,1),(2,4),(3,9)}⟩.
To make X arc-consistent with respect to Y, we reduce X’s domain to {0,1,2,3}. If we also
make Y arc-consistent with respect to X, then Y’s domain becomes {0,1,4,9}, and the whole
CSP is arc-consistent. On the other hand, arc consistency can do nothing for the Australia
map-coloring problem. Consider the following inequality constraint on (SA,WA):
{(red,green),(red,blue),(green,red),(green,blue),(blue,red),(blue,green)}.
No matter what value you choose for SA (or for WA), there is a valid value for the other
variable. So applying arc consistency has no effect on the domains of either variable.
The most popular algorithm for enforcing arc consistency is called AC-3 (see Figure 5.3).
To make every variable arc-consistent, the AC-3 algorithm maintains a queue of arcs to con-
sider. Initially, the queue contains all the arcs in the CSP. (Each binary constraint becomes
two arcs, one in each direction.) AC-3 then pops off an arbitrary arc (Xi,Xj) from the queue
1
We have been using the term “edge” rather than “arc,” so it would make more sense to call this “edge-
consistent,” but the name “arc-consistent” is historical.
