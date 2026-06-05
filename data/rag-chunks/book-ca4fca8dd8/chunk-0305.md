---
chunk_id: "book-ca4fca8dd8-chunk-0305"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 305
confidence: "first-pass"
extraction_method: "structured-local"
---

188
Chapter 5
Constraint Satisfaction Problems
• Local search using the min-conﬂicts heuristic has also been applied to constraint satis-
faction problems with great success.
• The complexity of solving a CSP is strongly related to the structure of its constraint
graph. Tree-structured problems can be solved in linear time. Cutset conditioning can
reduce a general CSP to a tree-structured one and is quite efﬁcient (requiring only lin-
ear memory) if a small cutset can be found. Tree decomposition techniques transform
the CSP into a tree of subproblems and are efﬁcient if the tree width of the constraint
graph is small; however they need memory exponential in the tree width of the con-
straint graph. Combining cutset conditioning with tree decomposition can allow a better
tradeoff of memory versus time.
Bibliographical and Historical Notes
The Greek mathematician Diophantus (c. 200–284) presented and solved problems involving
algebraic constraints on equations, although he didn’t develop a generalized methodology.
We now call equations over integer domains Diophantine equations. The Indian mathe-
Diophantine
equations
matician Brahmagupta (c. 650) was the ﬁrst to show a general solution over the domain of
integers for the equation ax+by = c. Systematic methods for solving linear equations by vari-
able elimination were studied by Gauss (1829); the solution of linear inequality constraints
goes back to Fourier (1827).
Finite-domain constraint satisfaction problems also have a long history. For example,
graph coloring (of which map coloring is a special case) is an old problem in mathematics.
The four-color conjecture (that every planar graph can be colored with four or fewer colors)
was ﬁrst made by Francis Guthrie, a student of De Morgan, in 1852. It resisted solution—
despite several published claims to the contrary—until a proof was devised by Appel and
Haken (1977) (see the book Four Colors Sufﬁce (Wilson, 2004)). Purists were disappointed
that part of the proof relied on a computer, so Georges Gonthier (2008), using the COQ
theorem prover, derived a formal proof that Appel and Haken’s proof program was correct.
Speciﬁc classes of constraint satisfaction problems occur throughout the history of com-
puter science. One of the most inﬂuential early examples was SKETCHPAD (Sutherland,
1963), which solved geometric constraints in diagrams and was the forerunner of modern
drawing programs and CAD tools. The identiﬁcation of CSPs as a general class is due to
Ugo Montanari (1974). The reduction of higher-order CSPs to purely binary CSPs with aux-
iliary variables (see Exercise 5.NARY) is due originally to the 19th-century logician Charles
Sanders Peirce. It was introduced into the CSP literature by Dechter (1990b) and was elabo-
rated by Bacchus and van Beek (1998). CSPs with preferences among solutions are studied
widely in the optimization literature; see Bistarelli et al. (1997) for a generalization of the
CSP framework to allow for preferences.
Constraint propagation methods were popularized by Waltz’s (1975) success on poly-
hedral line-labeling problems for computer vision. Waltz showed that in many problems,
propagation completely eliminates the need for backtracking. Montanari (1974) introduced
the notion of constraint graphs and propagation by path consistency. Alan Mackworth (1977)
proposed the AC-3 algorithm for enforcing arc consistency as well as the general idea of com-
bining backtracking with some degree of consistency enforcement. AC-4, a more efﬁcient
