---
chunk_id: "book-ca4fca8dd8-chunk-0359"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 359
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
221
approximation can be obtained by averaging the value of an action over each possible
conﬁguration of missing information.
• Programs have soundly defeated champion human players at chess, checkers, Othello,
Go, poker, and many other games. Humans retain the edge in a few games of imper-
fect information, such as bridge and Kriegspiel. In video games such as StarCraft and
Dota 2, programs are competitive with human experts, but part of their success may be
due to their ability to perform many actions very quickly.
Bibliographical and Historical Notes
In 1846, Charles Babbage discussed the feasibility of computer chess and checkers (Morri-
son and Morrison, 1961). He did not understand the exponential complexity of search trees,
claiming “the combinations involved in the Analytical Engine enormously surpassed any re-
quired, even by the game of chess.” Babbage also designed, but did not build, a special-
purpose machine for playing tic-tac-toe. The ﬁrst game-playing machine was built around
1890 by the Spanish engineer Leonardo Torres y Quevedo. It specialized in the “KRK” (king
and rook versus king) chess endgame, guaranteeing a win when the side with the rook has the
move. The minimax algorithm is traced to a 1912 paper by Ernst Zermelo, the developer of
modern set theory.
Game playing was one of the ﬁrst tasks undertaken in AI, with early efforts by such pi-
oneers as Konrad Zuse (1945), Norbert Wiener in his book Cybernetics (1948), and Alan
Turing (1953). But it was Claude Shannon’s article Programming a Computer for Playing
Chess (1950) that laid out all the major ideas: a representation for board positions, an evalua-
tion function, quiescence search, and some ideas for selective game-tree search. Slater (1950)
had the idea of an evaluation function as a linear combination of features, and stressed the
mobility feature in chess.
John McCarthy conceived the idea of alpha–beta search in 1956, although the idea did
not appear in print until later (Hart and Edwards, 1961). Knuth and Moore (1975) proved
the correctness of alpha–beta and analysed its time complexity, while Pearl (1982b) showed
alpha–beta to be asymptotically optimal among all ﬁxed-depth game-tree search algorithms.
Berliner (1979) introduced B∗, a heuristic search algorithm that maintains interval bounds
on the possible value of a node in the game tree rather than giving it a single point-valued
estimate. David McAllester’s (1988) conspiracy number search expands leaf nodes that, by
changing their values, could cause the program to prefer a new move at the root of the tree.
MGSS∗(Russell and Wefald, 1989) uses the decision-theoretic techniques of Chapter 15 to
estimate the value of expanding each leaf in terms of the expected improvement in decision
quality at the root.
The SSS∗algorithm (Stockman, 1979) can be viewed as a two-player A∗that never ex-
pands more nodes than alpha–beta. The memory requirements make it impractical, but a
linear-space version has been developed from the RBFS algorithm (Korf and Chickering,
1996). Baum and Smith (1997) propose a probability-based replacement for minimax, show-
ing that it results in better choices in certain games. The expectiminimax algorithm was
proposed by Donald Michie (1966). Bruce Ballard (1983) extended alpha–beta pruning to
cover trees with chance nodes.
