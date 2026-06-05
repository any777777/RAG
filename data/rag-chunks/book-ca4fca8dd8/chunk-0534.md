---
chunk_id: "book-ca4fca8dd8-chunk-0534"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 534
confidence: "first-pass"
extraction_method: "structured-local"
---

326
Chapter 9
Inference in First-Order Logic
9.5.6 Resolution strategies
We know that repeated applications of the resolution inference rule will eventually ﬁnd a
proof if one exists. In this subsection, we examine strategies that help ﬁnd proofs efﬁciently.
Unit preference: This strategy prefers to do resolutions where one of the sentences is a single
Unit preference
literal (also known as a unit clause). The idea behind the strategy is that we are trying to
produce an empty clause, so it might be a good idea to prefer inferences that produce shorter
clauses. Resolving a unit sentence (such as P) with any other sentence (such as ¬P∨¬Q∨R)
always yields a clause (in this case, ¬Q ∨R) that is shorter than the other clause. When
the unit preference strategy was ﬁrst tried for propositional inference in 1964, it led to a
dramatic speedup, making it feasible to prove theorems that could not be handled without the
preference. Unit resolution is a restricted form of resolution in which every resolution step
must involve a unit clause. Unit resolution is incomplete in general, but complete for Horn
clauses. Unit resolution proofs on Horn clauses resemble forward chaining.
The OTTER theorem prover (McCune, 1990), uses a form of best-ﬁrst search. Its heuristic
function measures the “weight” of each clause, where lighter clauses are preferred. The exact
choice of heuristic is up to the user, but generally, the weight of a clause should be correlated
with its size or difﬁculty. Unit clauses are treated as light; the search can thus be seen as a
generalization of the unit preference strategy.
Set of support: Preferences that try certain resolutions ﬁrst are helpful, but in general it is
Set of support
more effective to try to eliminate some potential resolutions altogether. For example, we can
insist that every resolution step involve at least one element of a special set of clauses—the
set of support. The resolvent is then added into the set of support. If the set of support is
small relative to the whole knowledge base, the search space will be reduced dramatically.
To ensure completeness of this strategy, we can choose the set of support S so that the
remainder of the sentences are jointly satisﬁable. For example, one can use the negated query
as the set of support, on the assumption that the original knowledge base is consistent. (After
all, if it is not consistent, then the fact that the query follows from it is vacuous.) The set-of-
support strategy has the additional advantage of generating goal-directed proof trees that are
often easy for humans to understand.
Input resolution: In this strategy, every resolution combines one of the input sentences (from
Input resolution
the KB or the query) with some other sentence. The proof in Figure 9.10 on page 319 uses
only input resolutions and has the characteristic shape of a single “spine” with single sen-
tences combining onto the spine. Clearly, the space of proof trees of this shape is smaller
than the space of all proof graphs. In Horn knowledge bases, Modus Ponens is a kind of
input resolution strategy, because it combines an implication from the original KB with some
other sentences. Thus, it is no surprise that input resolution is complete for knowledge bases
that are in Horn form, but incomplete in the general case. The linear resolution strategy is a
Linear resolution
slight generalization that allows P and Q to be resolved together either if P is in the original
KB or if P is an ancestor of Q in the proof tree. Linear resolution is complete.
Subsumption: The subsumption method eliminates all sentences that are subsumed by (that
Subsumption
is, more speciﬁc than) an existing sentence in the KB. For example, if P(x) is in the KB, then
there is no sense in adding P(A) and even less sense in adding P(A) ∨Q(B). Subsumption
helps keep the KB small and thus helps keep the search space small.
