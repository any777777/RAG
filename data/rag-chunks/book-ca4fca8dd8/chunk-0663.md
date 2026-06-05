---
chunk_id: "book-ca4fca8dd8-chunk-0663"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 663
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
399
Bidirectional search (see Section 3.4.5) has also been known to suffer from a lack of
heuristics, but some success has been obtained by using backward search to create a perime-
ter around the goal, and then reﬁning a heuristic to search forward towards that perime-
ter (Torralba et al., 2016). The SYMBA* bidirectional search planner (Torralba et al., 2016)
won the 2016 competition.
Researchers turned to PDDL and the planning paradigm so that they could use domain
independent heuristics. Hoffmann (2005) analyzes the search space of the ignore-delete-
list heuristic. Edelkamp (2009) and Haslum et al. (2007) describe how to construct pattern
databases for planning heuristics. Felner et al. (2004) show encouraging results using pat-
tern databases for sliding-tile puzzles, which can be thought of as a planning domain, but
Hoffmann et al. (2006) show some limitations of abstraction for classical planning problems.
(Rintanen, 2012) discusses planning-speciﬁc variable-selection heuristics for SAT solving.
Helmert et al. (2011) describe the Fast Downward Stone Soup (FDSS) system, a portfolio
planner that, as in the fable of stone soup, invites us to throw in as many planning algorithms
as possible. The system maintains a set of training problems, and for each problem and each
algorithm records the run time and resulting plan cost of the problem’s solution. Then when
faced with a new problem, it uses the past experience to decide which algorithm(s) to try, with
what time limits, and takes the solution with minimal cost. FDSS was a winner in the 2018
International Planning Competition (Seipp and R¨oger, 2018). Seipp et al. (2015) describe
a machine learning approach to automatically learn a good portfolio, given a new problem.
Vallati et al. (2015) give an overview of portfolio planning. The idea of algorithm portfolios
for combinatorial search problems goes back to Gomes and Selman (2001).
Sistla and Godefroid (2004) cover symmetry reduction, and Godefroid (1990) covers
heuristics for partial ordering. Richter and Helmert (2009) demonstrate the efﬁciency gains
of forward pruning using preferred actions.
Blum and Furst (1997) revitalized the ﬁeld of planning with their Graphplan system,
which was orders of magnitude faster than the partial-order planners of the time. Bryce and
Kambhampati (2007) give an overview of planning graphs. The use of situation calculus for
planning was introduced by John McCarthy (1963) and reﬁned by Ray Reiter (2001).
Kautz et al. (1996) investigated various ways to propositionalize action schemas, ﬁnding
that the most compact forms did not necessarily lead to the fastest solution times. A system-
atic analysis was carried out by Ernst et al. (1997), who also developed an automatic “com-
piler” for generating propositional representations from PDDL problems. The BLACKBOX
planner, which combines ideas from Graphplan and SATPLAN, was developed by Kautz and
Selman (1998). Planners based on constraint satisfaction include CPLAN van Beek and Chen
(1999) and GP-CSP (Do and Kambhampati, 2003).
There has also been interest in the representation of a plan as a binary decision diagram
(BDD), a compact data structure for Boolean expressions widely studied in the hardware
Binary decision
diagram (BDD)
veriﬁcation community (Clarke and Grumberg, 1987; McMillan, 1993). There are techniques
for proving properties of binary decision diagrams, including the property of being a solution
to a planning problem. Cimatti et al. (1998) present a planner based on this approach. Other
representations have also been used, such as integer programming (Vossen et al., 2001).
There are some interesting comparisons of the various approaches to planning. Helmert
(2001) analyzes several classes of planning problems, and shows that constraint-based ap-
proaches such as Graphplan and SATPLAN are best for NP-hard domains, while search-based
