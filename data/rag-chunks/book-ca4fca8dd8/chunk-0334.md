---
chunk_id: "book-ca4fca8dd8-chunk-0334"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 334
confidence: "first-pass"
extraction_method: "structured-local"
---

206
Chapter 6
Adversarial Search and Games
v of a node and then using past experience to estimate how likely it is that a score of v at
depth d in the tree would be outside (α,β). Buro applied this technique to his Othello pro-
gram, LOGISTELLO, and found that a version of his program with PROBCUT beat the regular
version 64% of the time, even when the regular version was given twice as much time.
Another technique, late move reduction, works under the assumption that move ordering
Late move reduction
has been done well, and therefore moves that appear later in the list of possible moves are
less likely to be good moves. But rather than pruning them away completely, we just reduce
the depth to which we search these moves, thereby saving time. If the reduced search comes
back with a value above the current α value, we can re-run the search with the full depth.
Combining all the techniques described here results in a program that can play creditable
chess (or other games). Let us assume we have implemented an evaluation function for
chess, a reasonable cutoff test with a quiescence search. Let us also assume that, after months
of tedious bit-bashing, we can generate and evaluate around a million nodes per second on
the latest PC. The branching factor for chess is about 35, on average, and 355 is about 50
million, so if we used minimax search, we could look ahead only ﬁve ply in about a minute
of computation; the rules of competition would not give us enough time to search six ply.
Though not incompetent, such a program can be defeated by an average human chess player,
who can occasionally plan six or eight ply ahead.
With alpha–beta search and a large transposition table we get to about 14 ply, which
results in an expert level of play. We could trade in our PC for a workstation with 8 GPUs,
getting us over a billion nodes per second, but to obtain grandmaster status we would still
need an extensively tuned evaluation function and a large database of endgame moves. Top
chess programs like STOCKFISH have all of these, often reaching depth 30 or more in the
search tree and far exceeding the ability of any human player.
6.3.4 Search versus lookup
Somehow it seems like overkill for a chess program to start a game by considering a tree of
a billion game states, only to conclude that it will play pawn to e4 (the most popular ﬁrst
move). Books describing good play in the opening and endgame in chess have been available
for more than a century (Tattersall, 1911). It is not surprising, therefore, that many game-
playing programs use table lookup rather than search for the opening and ending of games.
For the openings, the computer is mostly relying on the expertise of humans. The best
advice of human experts on how to play each opening can be copied from books and entered
into tables for the computer’s use. In addition, computers can gather statistics from a database
of previously played games to see which opening sequences most often lead to a win. For the
ﬁrst few moves there are few possibilities, and most positions will be in the table. Usually
after about 10 or 15 moves we end up in a rarely seen position, and the program must switch
from table lookup to search.
Near the end of the game there are again fewer possible positions, and thus it is easier to
do lookup. But here it is the computer that has the expertise: computer analysis of endgames
goes far beyond human abilities. Novice humans can win a king-and-rook-versus-king (KRK)
endgame by following a few simple rules. Other endings, such as king, bishop, and knight
versus king (KBNK), are difﬁcult to master and have no succinct strategy description.
A computer, on the other hand, can completely solve the endgame by producing a policy,
which is a mapping from every possible state to the best move in that state. Then the computer
