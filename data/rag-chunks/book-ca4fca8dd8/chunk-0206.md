---
chunk_id: "book-ca4fca8dd8-chunk-0206"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 206
confidence: "first-pass"
extraction_method: "structured-local"
---

124
Chapter 3
Solving Problems by Searching
– Beam search puts a limit on the size of the frontier; that makes it incomplete
and suboptimal, but it often ﬁnds reasonably good solutions and runs faster than
complete searches.
– Weighted A∗search focuses the search towards a goal, expanding fewer nodes,
but sacriﬁcing optimality.
• The performance of heuristic search algorithms depends on the quality of the heuristic
function. One can sometimes construct good heuristics by relaxing the problem deﬁni-
tion, by storing precomputed solution costs for subproblems in a pattern database, by
deﬁning landmarks, or by learning from experience with the problem class.
Bibliographical and Historical Notes
The topic of state-space search originated in the early years of AI. Newell and Simon’s work
on the Logic Theorist (1957) and GPS (1961) led to the establishment of search algorithms
as the primary tool for 1960s AI researchers and to the establishment of problem solving as
the canonical AI task. Work in operations research by Richard Bellman (1957) showed the
importance of additive path costs in simplifying optimization algorithms. The text by Nils
Nilsson (1971) established the area on a solid theoretical footing.
The 8-puzzle is a smaller cousin of the 15-puzzle, whose history is recounted at length
by Slocum and Sonneveld (2006). In 1880, the 15-puzzle attracted broad attention from
the public and mathematicians (Johnson and Story, 1879; Tait, 1880). The editors of the
American Journal of Mathematics stated, “The ‘15’ puzzle for the last few weeks has been
prominently before the American public, and may safely be said to have engaged the attention
of nine out of ten persons of both sexes and all ages and conditions of the community,” while
the Weekly News-Democrat of Emporia, Kansas wrote on March 12, 1880 that “It has become
literally an epidemic all over the country.”
The famous American game designer Sam Loyd falsely claimed to have invented the 15
puzzle (Loyd, 1959); actually it was invented by Noyes Chapman, a postmaster in Canastota,
New York, in the mid-1870s (although a generic patent covering sliding blocks was granted
to Ernest Kinsey in 1878). Ratner and Warmuth (1986) showed that the general n×n version
of the 15-puzzle belongs to the class of NP-complete problems.
Rubik’s Cube was of course invented in 1974 by Ern˝o Rubik, who also discovered an
algorithm for ﬁnding good, but not optimal solutions. Korf (1997) found optimal solutions
for some random problem instances using pattern databases and IDA∗search. Rokicki et al.
(2014) proved that any instance can be solved in 26 moves (if you consider a 180◦twist to be
two moves; 20 if it counts as one). The proof consumed 35 CPU years of computation; it does
not lead immediately to an efﬁcient algorithm. Agostinelli et al. (2019) used reinforcement
learning, deep learning networks, and Monte Carlo tree search to learn a much more efﬁcient
solver for Rubik’s cube. It is not guaranteed to ﬁnd a cost-optimal solution, but does so about
60% of the time, and typical solutions times are less than a second.
Each of the real-world search problems listed in the chapter has been the subject of a
good deal of research effort. Methods for selecting optimal airline ﬂights remain proprietary
for the most part, but Carl de Marcken has shown by a reduction to Diophantine decision
problems that airline ticket pricing and restrictions have become so convoluted that the prob-
