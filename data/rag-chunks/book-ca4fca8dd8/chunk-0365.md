---
chunk_id: "book-ca4fca8dd8-chunk-0365"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 365
confidence: "first-pass"
extraction_method: "structured-local"
---

224
Chapter 6
Adversarial Search and Games
has touched the edge of the truth of Go.” Lee Sedol retired from Go, lamenting, “Even if I
became the number one, there is an entity that cannot be defeated.”
In 2018, ALPHAZERO surpassed ALPHAGO at Go, and also defeated top programs in
chess and shogi, learning through self-play without any expert human knowledge and without
access to any past games. (It does, of course, rely on humans to deﬁne the basic architecture
as Monte Carlo tree search with deep neural networks and reinforcement learning, and to
encode the rules of the game.) The success of ALPHAZERO has led to increased interest in
reinforcement learning as a key component of general AI (see Chapter 23). Going one step
further, the MUZERO system operates without even being told the rules of the game it is
playing—it has to ﬁgure out the rules by making plays. MUZERO achieved state-of-the-art
results in Pacman, chess, Go, and 75 Atari games (Schrittwieser et al., 2019). It learns to
generalize; for example, it learns that in Pacman the “up” action moves the player up a square
(unless there is a wall there), even though it has only observed the result of the “up” action in
a small percentage of the locations on the board.
Othello, also called Reversi, has a smaller search space than chess, but deﬁning an eval-
uation function is difﬁcult, because material advantage is not as important as mobility. Pro-
grams have been at superhuman level since 1997 (Buro, 2002).
Backgammon, a game of chance, was analyzed mathematically by Gerolamo Cardano
(1663), and taken up for computer play with the BKG program (Berliner, 1980b), which used
a manually constructed evaluation function and searched only to depth 1. It was the ﬁrst pro-
gram to defeat a human world champion at a major game (Berliner, 1980a), although Berliner
readily acknowledged that BKG was very lucky with the dice.
Gerry Tesauro’s (1995)
TD-GAMMON learned its evaluation function using neural networks trained by self-play.
It consistently played at world champion level and caused human analysts to change their
opinion on the best opening move for several dice rolls.
Poker, like Go, has seen surprising advances in recent years. Bowling et al. (2015) used
game theory (see Section 17.2) to determine the exact optimal strategy for a version of poker
with just two players and a ﬁxed number of raises with ﬁxed bet sizes. In 2017, for the ﬁrst
time, champion poker players were beaten at heads-up (two player) no-limit Texas hold ’em
in two separate matches against the programs Libratus (Brown and Sandholm, 2017) and
DeepStack (Moravˇc´ık et al., 2017). In 2019, Pluribus (Brown and Sandholm, 2019) defeated
top-ranked professional human players in Texas hold ’em games with six players. Multiplayer
games introduce some strategic concerns that we will cover in Chapter 17. Petosa and Balch
(2019) implement a multiplayer version of ALPHAZERO.
Bridge: Smith et al. (1998) report on how BRIDGE BARON won the 1998 computer
bridge championship, using hierarchical plans (see Chapter 11) and high-level actions, such
as ﬁnessing and squeezing, that are familiar to bridge players. Ginsberg (2001) describes
how his GIB program, based on Monte Carlo simulation (ﬁrst proposed for bridge by Levy
(1989)), won the following computer championship and did surprisingly well against expert
human players. In the 21st century, the computer bridge championship has been dominated by
two commercial programs, JACK and WBRIDGE5. Neither has been described in published
articles, but both are believed to use Monte Carlo techniques. In general, bridge programs
are at human champion level when actually playing the hands, but lag behind in the bid-
ding phase, because they do not completely understand the conventions used by humans to
communicate with their partners. Bridge programmers have concentrated more on producing
