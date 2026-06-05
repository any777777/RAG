---
chunk_id: "book-ca4fca8dd8-chunk-0399"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 399
confidence: "first-pass"
extraction_method: "structured-local"
---

246
Chapter 7
Logical Agents
function PL-RESOLUTION(KB,α) returns true or false
inputs: KB, the knowledge base, a sentence in propositional logic
α, the query, a sentence in propositional logic
clauses←the set of clauses in the CNF representation of KB∧¬α
new←{}
while true do
for each pair of clauses Ci, Cj in clauses do
resolvents←PL-RESOLVE(Ci,Cj)
if resolvents contains the empty clause then return true
new←new∪resolvents
if new ⊆clauses then return false
clauses←clauses∪new
Figure 7.13 A simple resolution algorithm for propositional logic. PL-RESOLVE returns the
set of all possible clauses obtained by resolving its two inputs.
The empty clause—a disjunction of no disjuncts—is equivalent to False because a disjunction
is true only if at least one of its disjuncts is true. Moreover, the empty clause arises only from
resolving two contradictory unit clauses such as P and ¬P.
We can apply the resolution procedure to a very simple inference in the wumpus world.
When the agent is in [1,1], there is no breeze, so there can be no pits in neighboring squares.
The relevant knowledge base is
KB = R2 ∧R4 = (B1,1 ⇔(P1,2 ∨P2,1))∧¬B1,1
and we wish to prove α, which is, say, ¬P1,2. When we convert (KB ∧¬α) into CNF, we
obtain the clauses shown at the top of Figure 7.14. The second row of the ﬁgure shows
clauses obtained by resolving pairs in the ﬁrst row. Then, when P1,2 is resolved with ¬P1,2,
we obtain the empty clause, shown as a small square. Inspection of Figure 7.14 reveals that
many resolution steps are pointless. For example, the clause B1,1 ∨¬B1,1 ∨P1,2 is equivalent
to True ∨P1,2 which is equivalent to True. Deducing that True is true is not very helpful.
Therefore, any clause in which two complementary literals appear can be discarded.
Completeness of resolution
To conclude our discussion of resolution, we now show why PL-RESOLUTION is complete.
To do this, we introduce the resolution closure RC(S) of a set of clauses S, which is the set
Resolution closure
of all clauses derivable by repeated application of the resolution rule to clauses in S or their
derivatives. The resolution closure is what PL-RESOLUTION computes as the ﬁnal value
of the variable clauses. It is easy to see that RC(S) must be ﬁnite: thanks to the factoring
step, there are only ﬁnitely many distinct clauses that can be constructed out of the symbols
P1,...,Pk that appear in S. Hence, PL-RESOLUTION always terminates.
The completeness theorem for resolution in propositional logic is called the ground res-
olution theorem:
Ground resolution
theorem
If a set of clauses is unsatisﬁable, then the resolution closure of those clauses
contains the empty clause.
