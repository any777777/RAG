---
chunk_id: "book-ca4fca8dd8-chunk-0435"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 435
confidence: "first-pass"
extraction_method: "structured-local"
---

266
Chapter 7
Logical Agents
propositional logic, other mathematicians soon ﬁlled in the missing pieces. Schr¨oder (1877)
described conjunctive normal form, while Horn form was introduced much later by Alfred
Horn (1951). The ﬁrst comprehensive exposition of modern propositional logic (and ﬁrst-
order logic) is found in Gottlob Frege’s (1879) Begriffschrift (“Concept Writing” or “Con-
ceptual Notation”).
The ﬁrst mechanical device to carry out logical inferences was the Stanhope Demonstra-
tor, constructed by the third Earl of Stanhope (1753–1816). William Stanley Jevons, one of
the mathematicians who extended Boole’s work, constructed his “logical piano” in 1869 to
do inferences in Boolean logic. An entertaining history of these early mechanical inference
devices is given by Martin Gardner (1968). The ﬁrst computer programs for logical inference
were Martin Davis’s 1954 program for proofs in Presburger arithmetic (Davis, 1957), and the
Logic Theorist of Newell, Shaw, and Simon (1957).
Emil Post (1921) and Ludwig Wittgenstein (1922) independently used truth tables as a
method of testing validity of propositional logic sentences. The Davis–Putnam algorithm
(Davis and Putnam, 1960) was the ﬁrst algorithm for propositional resolution, and the im-
proved DPLL backtracking algorithm (Davis et al., 1962) proved to be more efﬁcient. The
resolution rule and a proof of its completeness were developed in full generality for ﬁrst-order
logic by J. A. Robinson (1965).
Stephen Cook (1971) showed that deciding satisﬁability of a sentence in propositional
logic (the SAT problem) is NP-complete. Many subsets of propositional logic are known for
which the satisﬁability problem is polynomially solvable; Horn clauses are one such subset.
Early investigations showed that DPLL has polynomial average-case complexity for cer-
tain natural distributions of problems. Even better, Franco and Paull (1983) showed that the
same problems could be solved in constant time simply by guessing random assignments.
Motivated by the empirical success of local search, Koutsoupias and Papadimitriou (1992)
showed that a simple hill-climbing algorithm can solve almost all satisﬁability problem in-
stances very quickly, suggesting that hard problems are rare. Sch¨oning (1999) exhibited a
randomized hill-climbing algorithm whose worst-case expected run time on 3-SAT problems
is O(1.333n)—still exponential, but substantially faster than previous worst-case bounds. The
current record is O(1.32216n) (Rolf, 2006).
Efﬁciency gains in propositional solvers have been rapid. Given ten minutes of comput-
ing time, the original DPLL algorithm on 1962 hardware could solve only problems with 10
or 15 variables (on a 2019 laptop it would be about 30 variables). By 1995 the SATZ solver (Li
and Anbulagan, 1997) could handle 1,000 variables, thanks to optimized data structures for
indexing variables. Two crucial contributions were the watched literal indexing technique
Watched literal
of Zhang and Stickel (1996), which makes unit propagation very efﬁcient, and the introduc-
tion of clause (i.e., constraint) learning techniques from the CSP community by Bayardo and
Schrag (1997). Using these ideas, and spurred by the prospect of solving industrial-scale
circuit veriﬁcation problems, Moskewicz et al. (2001) developed the CHAFF solver, which
could handle problems with millions of variables. Beginning in 2002, annual SAT competi-
tions have been held; most of the winning entries have been variants of CHAFF. The landscape
of solvers is surveyed by Gomes et al. (2008).
Local search algorithms for satisﬁability were tried by various authors throughout the
1980s, based on the idea of minimizing the number of unsatisﬁed clauses (Hansen and Jau-
mard, 1990). A particularly effective algorithm was developed by Gu (1989) and indepen-
