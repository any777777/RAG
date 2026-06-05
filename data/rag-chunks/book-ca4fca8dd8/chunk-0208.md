---
chunk_id: "book-ca4fca8dd8-chunk-0208"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 208
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
125
lem of selecting an optimal ﬂight is formally undecidable (Robinson, 2002). The traveling
salesperson problem (TSP) is a standard combinatorial problem in theoretical computer sci-
ence (Lawler et al., 1992). Karp (1972) proved the TSP decision problem to be NP-hard, but
effective heuristic approximation methods were developed (Lin and Kernighan, 1973). Arora
(1998) devised a fully polynomial approximation scheme for Euclidean TSPs. VLSI layout
methods are surveyed by LaPaugh (2010), and many layout optimization papers appear in
VLSI journals. Robotic navigation is discussed in Chapter 26. Automatic assembly sequenc-
ing was ﬁrst demonstrated by FREDDY (Michie, 1972); a comprehensive review is given by
(Bahubalendruni and Biswal, 2016).
Uninformed search algorithms are a central topic of computer science (Cormen et al.,
2009) and operations research (Dreyfus, 1969). Breadth-ﬁrst search was formulated for solv-
ing mazes by Moore (1959). The method of dynamic programming (Bellman, 1957; Bellman
and Dreyfus, 1962), which systematically records solutions for all subproblems of increasing
lengths, can be seen as a form of breadth-ﬁrst search.
Dijkstra’s algorithm in the form it is usually presented in (Dijkstra, 1959) is applicable
to explicit ﬁnite graphs. Nilsson (1971) introduced a version of Dijkstra’s algorithm that he
called uniform-cost search (because the algorithm “spreads out along contours of equal path
cost”) that allows for implicitly deﬁned, inﬁnite graphs. Nilsson’s work also introduced the
idea of closed and open lists, and the term “graph search.” The name BEST-FIRST-SEARCH
was introduced in the Handbook of AI (Barr and Feigenbaum, 1981). The Floyd–Warshall
(Floyd, 1962) and Bellman-Ford (Bellman, 1958; Ford, 1956) algorithms allow negative step
costs (as long as there are no negative cycles).
A version of iterative deepening designed to make efﬁcient use of the chess clock was ﬁrst
used by Slate and Atkin (1977) in the CHESS 4.5 game-playing program. Martelli’s algorithm
B (1977) also includes an iterative deepening aspect. The iterative deepening technique was
introduced by Bertram Raphael (1976) and came to the fore in work by Korf (1985a).
The use of heuristic information in problem solving appears in an early paper by Simon
and Newell (1958), but the phrase “heuristic search” and the use of heuristic functions that
estimate the distance to the goal came somewhat later (Newell and Ernst, 1965; Lin, 1965).
Doran and Michie (1966) conducted extensive experimental studies of heuristic search. Al-
though they analyzed path length and “penetrance” (the ratio of path length to the total num-
ber of nodes examined so far), they appear to have ignored the information provided by the
path cost g(n). The A∗algorithm, incorporating the current path cost into heuristic search,
was developed by Hart, Nilsson, and Raphael (1968). Dechter and Pearl (1985) studied the
conditions under which A∗is optimally efﬁcient (in number of nodes expanded).
The original A∗paper (Hart et al., 1968) introduced the consistency condition on heuristic
functions. The monotone condition was introduced by Pohl (1977) as a simpler replacement,
but Pearl (1984) showed that the two were equivalent.
Pohl (1977) pioneered the study of the relationship between the error in heuristic func-
tions and the time complexity of A∗. Basic results were obtained for tree-like search with unit
action costs and a single goal state (Pohl, 1977; Gaschnig, 1979; Huyn et al., 1980; Pearl,
1984) and with multiple goal states (Dinh et al., 2007). Korf and Reid (1998) showed how
to predict the exact number of nodes expanded (not just an asymptotic approximation) on a
variety of actual problem domains. The “effective branching factor” was proposed by Nils-
son (1971) as an empirical measure of efﬁciency. For graph search, Helmert and R¨oger (2008)
