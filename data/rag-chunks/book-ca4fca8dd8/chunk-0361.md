---
chunk_id: "book-ca4fca8dd8-chunk-0361"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 361
confidence: "first-pass"
extraction_method: "structured-local"
---

222
Chapter 6
Adversarial Search and Games
Pearl’s book Heuristics (1984) thoroughly analyzes many game-playing algorithms.
Monte Carlo simulation was pioneered by Metropolis and Ulam (1949) for calculations
related to the development of the atomic bomb. Monte Carlo tree search (MCTS) was intro-
duced by Abramson (1987). Tesauro and Galperin (1997) showed how a Monte Carlo search
could be combined with an evaluation function for the game of backgammon. Early play-
out termination is studied by Lorentz (2015). ALPHAGO terminated playouts and applied an
evaluation function (Silver et al., 2016). Kocsis and Szepesvari (2006) reﬁned the approach
with the “Upper Conﬁdence Bounds applied to Trees” selection mechanism. Chaslot et al.
(2008) show how MCTS can be applied to a variety of games and Browne et al. (2012) give
a survey.
Koller and Pfeffer (1997) describe a system for completely solving partially observable
games. It handles larger games than previous systems, but not the full version of complex
games like poker and bridge. Frank et al. (1998) describe several variants of Monte Carlo
search for partially observable games, including one where MIN has complete information
but MAX does not. Schoﬁeld and Thielscher (2015) adapt a general game-playing system for
partially observable games.
Ferguson hand-derived randomized strategies for winning Kriegspiel with a bishop and
knight (1992) or two bishops (1995) against a king. The ﬁrst Kriegspiel programs con-
centrated on ﬁnding endgame checkmates and performed AND–OR search in belief-state
space (Sakuta and Iida, 2002; Bolognesi and Ciancarini, 2003). Incremental belief-state al-
gorithms enabled much more complex midgame checkmates to be found (Russell and Wolfe,
2005; Wolfe and Russell, 2007), but efﬁcient state estimation remains the primary obstacle
to effective general play (Parker et al., 2005). Ciancarini and Favini (2010) apply MCTS to
Kriegspiel, and Wang et al. (2018b) describe a belief-state version of MCTS for Phantom Go.
Chess milestones have been marked by successive winners of the Fredkin Prize: BELLE
(Condon and Thompson, 1982), the ﬁrst program to achieve master status; DEEP THOUGHT
(Hsu et al., 1990), the ﬁrst to reach international master status; and Deep Blue (Campbell
et al., 2002; Hsu, 2004), which defeated world champion Garry Kasparov in a 1997 exhibition
match. Deep Blue ran alpha–beta search at over 100 million positions per second, and could
generate singular extensions to occasionally reach a depth of 40 ply.
The top chess programs today (e.g., STOCKFISH, KOMODO, HOUDINI) far exceed any
human player. These programs have reduced the effective branching factor to less than 3
(compared with the actual branching factor of about 35), searching to about 20 ply at a speed
of about a million nodes per second on a standard 1-core computer. They use pruning tech-
niques such as the null move heuristic, which generates a good lower bound on the value of
Null move
a position, using a shallow search in which the opponent gets to move twice at the beginning.
Also important is futility pruning, which helps decide in advance which moves will cause
Futility pruning
a beta cutoff in the successor nodes. SUNFISH is a simpliﬁed chess program for teaching
purposes; the core is less than 200 lines of Python.
The idea of retrograde analysis for computing endgame tables is due to Bellman (1965).
Using this idea, Ken Thompson (1986, 1996) and Lewis Stiller (1992, 1996) solved all chess
endgames with up to ﬁve pieces. Stiller discovered one case where a forced mate existed
but required 262 moves; this caused some consternation because the rules of chess require
a capture or pawn move to occur within 50 moves, or else a draw is declared. In 2012
Vladimir Makhnychev and Victor Zakharov compiled the Lomonosov Endgame Tablebase,
