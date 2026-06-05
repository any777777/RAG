---
chunk_id: "book-ca4fca8dd8-chunk-0357"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 357
confidence: "first-pass"
extraction_method: "structured-local"
---

220
Chapter 6
Adversarial Search and Games
Carlo search does attempt to do metareasoning to allocate resources to the most important
parts of the tree, but does not do so in an optimal way.
A third limitation is that both alpha-beta and Monte Carlo do all their reasoning at the
level of individual moves. Clearly, humans play games differently: they can reason at a more
abstract level, considering a higher-level goal—for example, trapping the opponent’s queen—
and using the goal to selectively generate plausible plans. In Chapter 11 we will study this
type of planning, and in Section 11.4 we will show how to plan with a hierarchy of abstract
to concrete representations.
A fourth issue is the ability to incorporate machine learning into the game search pro-
cess. Early game programs relied on human expertise to hand-craft evaluation functions,
opening books, search strategies, and efﬁciency tricks. We are just beginning to see programs
like ALPHAZERO (Silver et al., 2018), which relied on machine learning from self-play rather
than game-speciﬁc human-generated expertise. We cover machine learning in depth starting
with Chapter 19.
Summary
We have looked at a variety of games to understand what optimal play means, to understand
how to play well in practice, and to get a feel for how an agent should act in any type of
adversarial environment. The most important ideas are as follows:
• A game can be deﬁned by the initial state (how the board is set up), the legal actions
in each state, the result of each action, a terminal test (which says when the game is
over), and a utility function that applies to terminal states to say who won and what the
ﬁnal score is.
• In two-player, discrete, deterministic, turn-taking zero-sum games with perfect infor-
mation, the minimax algorithm can select optimal moves by a depth-ﬁrst enumeration
of the game tree.
• The alpha–beta search algorithm computes the same optimal move as minimax, but
achieves much greater efﬁciency by eliminating subtrees that are provably irrelevant.
• Usually, it is not feasible to consider the whole game tree (even with alpha–beta), so we
need to cut the search off at some point and apply a heuristic evaluation function that
estimates the utility of a state.
• An alternative called Monte Carlo tree search (MCTS) evaluates states not by apply-
ing a heuristic function, but by playing out the game all the way to the end and using
the rules of the game to see who won. Since the moves chosen during the playout may
not have been optimal moves, the process is repeated multiple times and the evaluation
is an average of the results.
• Many game programs precompute tables of best moves in the opening and endgame so
that they can look up a move rather than search.
• Games of chance can be handled by expectiminimax, an extension to the minimax
algorithm that evaluates a chance node by taking the average utility of all its children,
weighted by the probability of each child.
• In games of imperfect information, such as Kriegspiel and poker, optimal play re-
quires reasoning about the current and future belief states of each player. A simple
