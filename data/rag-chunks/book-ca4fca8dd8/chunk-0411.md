---
chunk_id: "book-ca4fca8dd8-chunk-0411"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 411
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.6
Effective Propositional Model Checking
253
function WALKSAT(clauses,p,max ﬂips) returns a satisfying model or failure
inputs: clauses, a set of clauses in propositional logic
p, the probability of choosing to do a “random walk” move, typically around 0.5
max ﬂips, number of value ﬂips allowed before giving up
model←a random assignment of true/false to the symbols in clauses
for each i= 1 to max ﬂips do
if model satisﬁes clauses then return model
clause←a randomly selected clause from clauses that is false in model
if RANDOM(0, 1) ≤p then
ﬂip the value in model of a randomly selected symbol from clause
else ﬂip whichever symbol in clause maximizes the number of satisﬁed clauses
return failure
Figure 7.18 The WALKSAT algorithm for checking satisﬁability by randomly ﬂipping the
values of variables. Many versions of the algorithm exist.
as “the set of clauses in which variable Xi appears as a positive literal.” This task is
complicated by the fact that the algorithms are interested only in the clauses that have
not yet been satisﬁed by previous assignments to variables, so the indexing structures
must be updated dynamically as the computation proceeds.
With these enhancements, modern solvers can handle problems with tens of millions of vari-
ables. They have revolutionized areas such as hardware veriﬁcation and security protocol
veriﬁcation, which previously required laborious, hand-guided proofs.
7.6.2 Local search algorithms
We have seen several local search algorithms so far in this book, including HILL-CLIMBING
(page 129) and SIMULATED-ANNEALING (page 133). These algorithms can be applied di-
rectly to satisﬁability problems, provided that we choose the right evaluation function. Be-
cause the goal is to ﬁnd an assignment that satisﬁes every clause, an evaluation function that
counts the number of unsatisﬁed clauses will do the job. In fact, this is exactly the measure
used by the MIN-CONFLICTS algorithm for CSPs (page 182). All these algorithms take steps
in the space of complete assignments, ﬂipping the truth value of one symbol at a time. The
space usually contains many local minima, to escape from which various forms of random-
ness are required. In recent years, there has been a great deal of experimentation to ﬁnd a
good balance between greediness and randomness.
One of the simplest and most effective algorithms to emerge from all this work is called
WALKSAT (Figure 7.18). On every iteration, the algorithm picks an unsatisﬁed clause and
picks a symbol in the clause to ﬂip. It chooses randomly between two ways to pick which
symbol to ﬂip: (1) a “min-conﬂicts” step that minimizes the number of unsatisﬁed clauses in
the new state and (2) a “random walk” step that picks the symbol randomly.
When WALKSAT returns a model, the input sentence is indeed satisﬁable, but when it
returns failure, there are two possible causes: either the sentence is unsatisﬁable or we need to
give the algorithm more time. If we set max ﬂips=∞and p > 0, WALKSAT will eventually
return a model (if one exists), because the random-walk steps will eventually hit upon the
