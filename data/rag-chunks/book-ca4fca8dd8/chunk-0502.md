---
chunk_id: "book-ca4fca8dd8-chunk-0502"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 502
confidence: "first-pass"
extraction_method: "structured-local"
---

306
Chapter 9
Inference in First-Order Logic
function FOL-FC-ASK(KB,α) returns a substitution or false
inputs: KB, the knowledge base, a set of ﬁrst-order deﬁnite clauses
α, the query, an atomic sentence
while true do
new←{}
// The set of new sentences inferred on each iteration
for each rule in KB do
(p1 ∧...∧pn ⇒q)←STANDARDIZE-VARIABLES(rule)
for each θ such that SUBST(θ,p1 ∧... ∧pn) = SUBST(θ,p′
1 ∧... ∧p′
n)
for some p′
1,...,p′
n in KB
q′ ←SUBST(θ,q)
if q′ does not unify with some sentence already in KB or new then
add q′ to new
φ←UNIFY(q′,α)
if φ is not failure then return φ
if new = {} then return false
add new to KB
Figure 9.3 A conceptually straightforward, but inefﬁcient, forward-chaining algorithm. On
each iteration, it adds to KB all the atomic sentences that can be inferred in one step
from the implication sentences and the atomic sentences already in KB.
The function
STANDARDIZE-VARIABLES replaces all variables in its arguments with new ones that have
not been used before.
• On the ﬁrst iteration, rule (9.3) has unsatisﬁed premises.
Rule (9.6) is satisﬁed with {x/M1}, and Sells(West,M1,Nono) is added.
Rule (9.7) is satisﬁed with {x/M1}, and Weapon(M1) is added.
Rule (9.8) is satisﬁed with {x/Nono}, and Hostile(Nono) is added.
• On the second iteration, rule (9.3) is satisﬁed with {x/West,y/M1,z/Nono}, and the
inference Criminal(West) is added.
Figure 9.4 shows the proof tree that is generated. Notice that no new inferences are possible
at this point because every sentence that could be concluded by forward chaining is already
contained explicitly in the KB. Such a knowledge base is called a ﬁxed point of the inference
process. Fixed points reached by forward chaining with ﬁrst-order deﬁnite clauses are similar
to those for propositional forward chaining (page 249); the principal difference is that a ﬁrst-
order ﬁxed point can include universally quantiﬁed atomic sentences.
FOL-FC-ASK is easy to analyze. First, it is sound, because every inference is just an
application of Generalized Modus Ponens, which is sound. Second, it is complete for deﬁnite
clause knowledge bases; that is, it answers every query whose answers are entailed by any
knowledge base of deﬁnite clauses.
For Datalog knowledge bases, which contain no function symbols, the proof of com-
pleteness is fairly easy. We begin by counting the number of possible facts that can be added,
which determines the maximum number of iterations. Let k be the maximum arity (number
of arguments) of any predicate, p be the number of predicates, and n be the number of con-
stant symbols. Clearly, there can be no more than pnk distinct ground facts, so after this many
iterations the algorithm must have reached a ﬁxed point. Then we can make an argument very
