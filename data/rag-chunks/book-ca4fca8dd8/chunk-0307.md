---
chunk_id: "book-ca4fca8dd8-chunk-0307"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 307
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
189
arc-consistency algorithm developed by Mohr and Henderson (1986), runs in O(cd2) worst-
case time but can be slower than AC-3 on average cases. The PC-2 algorithm (Mackworth,
1977) achieves path consistency in much the same way that AC-3 achieves arc consistency.
Soon after Mackworth’s paper appeared, researchers began experimenting with the trade-
off between the cost of consistency enforcement and the beneﬁts in terms of search reduc-
tion. Haralick and Elliott (1980) favored the minimal forward-checking algorithm described
by McGregor (1979), whereas Gaschnig (1979) suggested full arc-consistency checking after
each variable assignment—an algorithm later called MAC by Sabin and Freuder (1994). The
latter paper provides somewhat convincing evidence that on harder CSPs, full arc-consistency
checking pays off. Freuder (1978, 1982) investigated the notion of k-consistency and its
relationship to the complexity of solving CSPs. Dechter and Dechter (1987) introduced
directional arc consistency. Apt (1999) describes a generic algorithmic framework within
which consistency propagation algorithms can be analyzed, and surveys are given by Bessi`ere
(2006) and Bart´ak et al. (2010).
Special methods for handling higher-order or global constraints were developed ﬁrst
within the context of constraint logic programming. Marriott and Stuckey (1998) pro-
Constraint logic
programming
vide excellent coverage of research in this area. The Alldiff constraint was studied by Regin
(1994), Stergiou and Walsh (1999), and van Hoeve (2001). There are more complex inference
algorithms for Alldiff (see van Hoeve and Katriel, 2006) that propagate more constraints but
are more computationally expensive to run. Bounds constraints were incorporated into con-
straint logic programming by Van Hentenryck et al. (1998). A survey of global constraints is
provided by van Hoeve and Katriel (2006).
Sudoku has become the most widely known CSP and was described as such by Simonis
(2005). Agerbeck and Hansen (2008) describe some of the strategies and show that Sudoku
on an n2 ×n2 board is in the class of NP-hard problems.
In 1850, C. F. Gauss described a recursive backtracking algorithm for solving the 8-
queens problem, which had been published in the German chess magazine Schachzeitung in
1848. Gauss called his method Tatonniren, derived from the French word tˆatonner—to grope
around, as if in the dark.
According to Donald Knuth (personal communication), R. J. Walker introduced the term
backtrack in the 1950s. Walker (1960) described the basic backtracking algorithm and used it
to ﬁnd all solutions to the 13-queens problem. Golomb and Baumert (1965) formulated, with
examples, the general class of combinatorial problems to which backtracking can be applied,
and introduced what we call the MRV heuristic. Bitner and Reingold (1975) provided an
inﬂuential survey of backtracking techniques. Brelaz (1979) used the degree heuristic as a
tiebreaker after applying the MRV heuristic. The resulting algorithm, despite its simplicity,
is still the best method for k-coloring arbitrary graphs. Haralick and Elliott (1980) proposed
the least-constraining-value heuristic.
The basic backjumping method is due to John Gaschnig (1977, 1979). Kondrak and
van Beek (1997) showed that this algorithm is essentially subsumed by forward checking.
Conﬂict-directed backjumping was devised by Prosser (1993). Dechter (1990a) introduced
graph-based backjumping, which bounds the complexity of backjumping-based algorithms
as a function of the constraint graph (Dechter and Frost, 2002).
A very general form of intelligent backtracking was developed early on by Stallman and
Sussman (1977). Their technique of dependency-directed backtracking combines back-
Dependency-directed
backtracking
