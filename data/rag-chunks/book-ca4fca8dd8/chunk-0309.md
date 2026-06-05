---
chunk_id: "book-ca4fca8dd8-chunk-0309"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 309
confidence: "first-pass"
extraction_method: "structured-local"
---

190
Chapter 5
Constraint Satisfaction Problems
jumping with no-good learning (McAllester, 1990) and led to the development of truth main-
tenance systems (Doyle, 1979), which we discuss in Section 10.6.2. The connection between
the two areas is analyzed by de Kleer (1989).
The work of Stallman and Sussman also introduced the idea of constraint learning, in
Constraint learning
which partial results obtained by search can be saved and reused later in the search. The
idea was formalized by Dechter (1990a). Backmarking (Gaschnig, 1979) is a particularly
simple method in which consistent and inconsistent pairwise assignments are saved and used
to avoid rechecking constraints. Backmarking can be combined with conﬂict-directed back-
jumping; Kondrak and van Beek (1997) present a hybrid algorithm that provably subsumes
either method taken separately.
The method of dynamic backtracking (Ginsberg, 1993) retains successful partial as-
signments from later subsets of variables when backtracking over an earlier choice that does
not invalidate the later success. Moskewicz et al. (2001) show how these techniques and
others are used to create an efﬁcient SAT solver. Empirical studies of several randomized
backtracking methods were done by Gomes et al. (2000) and Gomes and Selman (2001).
Van Beek (2006) surveys backtracking.
Local search in constraint satisfaction problems was popularized by the work of Kirk-
patrick et al. (1983) on simulated annealing (see Chapter 4), which is widely used for VLSI
layout and scheduling problems. Beck et al. (2011) give an overview of recent work on job-
shop scheduling. The min-conﬂicts heuristic was ﬁrst proposed by Gu (1989) and was devel-
oped independently by Minton et al. (1992). Sosic and Gu (1994) showed how it could be
applied to solve the 3,000,000 queens problem in less than a minute. The astounding success
of local search using min-conﬂicts on the n-queens problem led to a reappraisal of the nature
and prevalence of “easy” and “hard” problems. Peter Cheeseman et al. (1991) explored the
difﬁculty of randomly generated CSPs and discovered that almost all such problems either
are trivially easy or have no solutions. Only if the parameters of the problem generator are
set in a certain narrow range, within which roughly half of the problems are solvable, do we
ﬁnd “hard” problem instances. We discuss this phenomenon further in Chapter 7.
Konolige (1994) showed that local search is inferior to backtracking search on problems
with a certain degree of local structure; this led to work that combined local search and
inference, such as that by Pinkas and Dechter (1995). Hoos and Tsang (2006) provide a
survey of local search techniques, and textbooks are offered by Hoos and St¨utzle (2004) and
Aarts and Lenstra (2003).
Work relating the structure and complexity of CSPs originates with Freuder (1985) and
Mackworth and Freuder (1985), who showed that search on arc-consistent trees works with-
out any backtracking. A similar result, with extensions to acyclic hypergraphs, was developed
in the database community (Beeri et al., 1983). Bayardo and Miranker (1994) present an al-
gorithm for tree-structured CSPs that runs in linear time without any preprocessing. Dechter
(1990a) describes the cycle-cutset approach.
Since those papers were published, there has been a great deal of progress in developing
more general results relating the complexity of solving a CSP to the structure of its constraint
graph. The notion of tree width was introduced by the graph theorists Robertson and Sey-
mour (1986). Dechter and Pearl (1987, 1989), building on the work of Freuder, applied a
related notion (which they called induced width but is identical to tree width) to constraint
satisfaction problems and developed the tree decomposition approach sketched in Section 5.5.
