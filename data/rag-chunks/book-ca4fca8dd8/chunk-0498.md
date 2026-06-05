---
chunk_id: "book-ca4fca8dd8-chunk-0498"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 498
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.2
Uniﬁcation and First-Order Inference
303
function UNIFY(x,y,θ=empty) returns a substitution to make x and y identical, or failure
if θ = failure then return failure
else if x = y then return θ
else if VARIABLE?(x) then return UNIFY-VAR(x,y,θ)
else if VARIABLE?(y) then return UNIFY-VAR(y,x,θ)
else if COMPOUND?(x) and COMPOUND?(y) then
return UNIFY(ARGS(x), ARGS(y), UNIFY(OP(x), OP(y), θ))
else if LIST?(x) and LIST?(y) then
return UNIFY(REST(x), REST(y), UNIFY(FIRST(x), FIRST(y), θ))
else return failure
function UNIFY-VAR(var,x,θ) returns a substitution
if {var/val} ∈θ for some val then return UNIFY(val,x,θ)
else if {x/val} ∈θ for some val then return UNIFY(var,val,θ)
else if OCCUR-CHECK?(var,x) then return failure
else return add {var/x} to θ
Figure 9.1 The uniﬁcation algorithm. The arguments x and y can be any expression: a
constant or variable, or a compound expression such as a complex sentence or term, or a
list of expressions. The argument θ is a substitution, initially the empty substitution, but
with {var/val} pairs added to it as we recurse through the inputs, comparing the expressions
element by element. In a compound expression such as F(A,B), OP(x) ﬁeld picks out the
function symbol F and ARGS(x) ﬁeld picks out the argument list (A,B).
Knows facts in one bucket and all the Brother facts in another. The buckets can be stored in a
hash table for efﬁcient access.
Predicate indexing is useful when there are many predicate symbols but only a few
clauses for each symbol. Sometimes, however, a predicate has many clauses. For example,
suppose that the tax authorities want to keep track of who employs whom, using a predi-
cate Employs(x,y). This would be a very large bucket with perhaps millions of employers
and tens of millions of employees. Answering a query such as Employs(x,Richard) with
predicate indexing would require scanning the entire bucket.
For this particular query, it would help if facts were indexed both by predicate and by
second argument, perhaps using a combined hash table key. Then we could simply construct
the key from the query and retrieve exactly those facts that unify with the query. For other
queries, such as Employs(IBM,y), we would need to have indexed the facts by combining the
predicate with the ﬁrst argument. Therefore, facts can be stored under multiple index keys,
rendering them instantly accessible to various queries that they might unify with.
Given a sentence to be stored, it is possible to construct indices for all possible queries
that unify with it. For the fact Employs(IBM,Richard), the queries are
Employs(IBM,Richard)
Does IBM employ Richard?
Employs(x,Richard)
Who employs Richard?
Employs(IBM,y)
Whom does IBM employ?
Employs(x,y)
Who employs whom?
These queries form a subsumption lattice, as shown in Figure 9.2(a). The lattice has some
Subsumption lattice
