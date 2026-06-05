---
chunk_id: "book-ca4fca8dd8-chunk-0509"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 509
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 311

Section 9.4
Backward Chaining
311
The fact Magic(West) is also added to the KB. In this way, even if the knowledge base con-
tains facts about millions of Americans, only Colonel West will be considered during the
forward inference process. The complete process for deﬁning magic sets and rewriting the
knowledge base is too complex to go into here, but the basic idea is to perform a sort of
“generic” backward inference from the goal in order to work out which variable bindings
need to be constrained. The magic sets approach can therefore be thought of as a kind of
hybrid between forward inference and backward preprocessing.
9.4 Backward Chaining
The second major family of logical inference algorithms uses backward chaining over def-
inite clauses. These algorithms work backward from the goal, chaining through rules to ﬁnd
known facts that support the proof.
9.4.1 A backward-chaining algorithm
Figure 9.6 shows a backward-chaining algorithm for deﬁnite clauses. FOL-BC-ASK(KB,
goal) will be proved if the knowledge base contains a rule of the form lhs ⇒goal, where lhs
(left-hand side) is a list of conjuncts. An atomic fact like American(West) is considered as
a clause whose lhs is the empty list. Now a query that contains variables might be proved
in multiple ways. For example, the query Person(x) could be proved with the substitution
{x/John} as well as with {x/Richard}. So we implement FOL-BC-ASK as a generator—a
function that returns multiple times, each time giving one possible result (see Appendix B).
Backward chaining is a kind of AND/OR search—the OR part because the goal query can
be proved by any rule in the knowledge base, and the AND part because all the conjuncts in
the lhs of a clause must be proved. FOL-BC-OR works by fetching all clauses that might
function FOL-BC-ASK(KB,query) returns a generator of substitutions
return FOL-BC-OR(KB,query,{})
function FOL-BC-OR(KB,goal,θ) returns a substitution
for each rule in FETCH-RULES-FOR-GOAL(KB, goal) do
(lhs ⇒rhs)←STANDARDIZE-VARIABLES(rule)
for each θ′ in FOL-BC-AND(KB,lhs, UNIFY(rhs, goal, θ)) do
yield θ′
function FOL-BC-AND(KB,goals,θ) returns a substitution
if θ = failure then return
else if LENGTH(goals) = 0 then yield θ
else
ﬁrst,rest←FIRST(goals), REST(goals)
for each θ′ in FOL-BC-OR(KB, SUBST(θ, ﬁrst), θ) do
for each θ′′ in FOL-BC-AND(KB,rest,θ′) do
yield θ′′
Figure 9.6 A simple backward-chaining algorithm for ﬁrst-order knowledge bases.

## Page 312
