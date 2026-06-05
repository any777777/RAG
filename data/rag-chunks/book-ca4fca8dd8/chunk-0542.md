---
chunk_id: "book-ca4fca8dd8-chunk-0542"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 542
confidence: "first-pass"
extraction_method: "structured-local"
---

330
Chapter 9
Inference in First-Order Logic
Early work on constraint logic programming was done by Jaffar and Lassez (1987). Jaffar
et al. (1992) developed the CLP(R) system for handling real-valued constraints. There are
now commercial products for solving large-scale conﬁguration and optimization problems
with constraint programming; one of the best known is ILOG (Junker, 2003). Answer set
programming (Gelfond, 2008) extends Prolog, allowing disjunction and negation.
Texts on logic programming and Prolog include Shoham (1994), Bratko (2009), Clocksin
(2003), and Clocksin and Mellish (2003). Prior to 2000, the Journal of Logic Programming
was the journal of record; it has been replaced by Theory and Practice of Logic Programming.
Logic programming conferences include the International Conference on Logic Programming
(ICLP) and the International Logic Programming Symposium (ILPS).
Research into mathematical theorem proving began even before the ﬁrst complete ﬁrst-
order systems were developed. Herbert Gelernter’s Geometry Theorem Prover (Gelernter,
1959) used heuristic search methods combined with diagrams for pruning false subgoals and
was able to prove some quite intricate results in Euclidean geometry. The demodulation
and paramodulation rules for equality reasoning were introduced by Wos et al. (1967) and
Wos and Robinson (1968), respectively. These rules were also developed independently in
the context of term-rewriting systems (Knuth and Bendix, 1970). The incorporation of equal-
ity reasoning into the uniﬁcation algorithm is due to Gordon Plotkin (1972). Jouannaud
and Kirchner (1991) survey equational uniﬁcation from a term-rewriting perspective. An
overview of uniﬁcation is given by Baader and Snyder (2001).
A number of control strategies have been proposed for resolution, beginning with the
unit preference strategy (Wos et al., 1964). The set-of-support strategy was proposed by Wos
et al. (1965) to provide a degree of goal-directedness in resolution. Linear resolution ﬁrst
appeared in Loveland (1970). Genesereth and Nilsson (1987, Chapter 5) provide an analysis
of a wide variety of control strategies. Alemi et al. (2017) show how the DEEPMATH system
uses deep neural nets to select the axioms that are most likely to lead to a proof when handed
to a traditional theorem prover. In a sense, the neural net plays the role of the mathematician’s
intuition, and the theorem prover plays the role of the mathematician’s technical expertise.
(Loos et al., 2017) show that this approach can be extended to help guide the search, allowing
more theorems to be proved.
A Computational Logic (Boyer and Moore, 1979) is the basic reference on the Boyer-
Moore theorem prover. Stickel (1992) describes the Prolog Technology Theorem Prover
(PTTP), which combines Prolog compilation and model elimination. SETHEO (Letz et al.,
1992) is another widely used theorem prover based on this approach. LEANTAP (Beckert
and Posegga, 1995) is an efﬁcient theorem prover implemented in only 25 lines of Prolog.
Weidenbach (2001) describes SPASS, one of the strongest current theorem provers. The most
successful theorem prover in recent annual competitions has been VAMPIRE (Riazanov and
Voronkov, 2002). The COQ system (Bertot et al., 2004) and the E equational solver (Schulz,
2004) have also proven to be valuable tools for proving correctness.
Theorem provers have been used to automatically synthesize and verify software. Exam-
ples include the control software for NASA’s Orion capsule (Lowry, 2008) and other space-
craft (Denney et al., 2006). The design of the FM9001 32-bit microprocessor was proved
correct by the NQTHM theorem proving system (Hunt and Brock, 1992).
The Conference on Automated Deduction (CADE) runs an annual contest for automated
theorem provers. Sutcliffe (2016) describes the 2016 competition; top-scoring systems in-
