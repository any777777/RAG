---
chunk_id: "book-ca4fca8dd8-chunk-0363"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 363
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
223
which solved all endgame positions with up to seven pieces—some require over 500 moves
without a capture. The 7-piece table consumes 140 terabytes; an 8-piece table would be 100
times larger.
In 2017, ALPHAZERO (Silver et al., 2018) defeated STOCKFISH (the 2017 TCEC com-
puter chess champion) in a 1000-game trial, with 155 wins and 6 losses. Additional matches
also resulted in decisive wins for ALPHAZERO, even when it was given only 1/10th the time
allotted to STOCKFISH.
Grandmaster Larry Kaufman was surprised at the sucess of this Monte Carlo program
and noted, “It may well be that the current dominance of minimax chess engines may be at an
end, but it’s too soon to say so.” Garry Kasparov commented “It’s a remarkable achievement,
even if we should have expected it after ALPHAGO. It approaches the Type B human-like
approach to machine chess dreamt of by Claude Shannon and Alan Turing instead of brute
force.” He went on to predict “Chess has been shaken to its roots by ALPHAZERO, but this is
only a tiny example of what is to come. Hidebound disciplines like education and medicine
will also be shaken” (Sadler and Regan, 2019).
Checkers was the ﬁrst of the classic games played by a computer (Strachey, 1952).
Arthur Samuel (1959, 1967) developed a checkers program that learned its own evaluation
function through self-play using a form of reinforcement learning. It is quite an achievement
that Samuel was able to create a program that played better than he did, on an IBM 704
computer with only 10,000 words of memory and a 0.000001 GHz processor. MENACE—the
Machine Educable Noughts And Crosses Engine (Michie, 1963)—also used reinforcement
learning to become competent at tic-tac-toe. Its processor was even slower: a collection of
304 matchboxes holding colored beads to represent the best learned move in each position.
In 1992, Jonathan Schaeffer’s CHINOOK checkers program challenged the legendary
Marion Tinsley, who had been world champion for over 20 years. Tinsley won the match,
but lost two games—the fourth and ﬁfth losses in his entire career. After Tinsley retired for
health reasons, CHINOOK took the crown. The saga was chronicled by Schaeffer (2008).
In 2007 Schaeffer and his team “solved” checkers (Schaeffer et al., 2007): the game
is a draw with perfect play. Richard Bellman (1965) had predicted this: “In checkers, the
number of possible moves in any given situation is so small that we can conﬁdently expect a
complete digital computer solution to the problem of optimal play in this game.” Bellman did
not anticipate the scale of the effort: the endgame table for 10 pieces has 39 trillion entries.
Given this table, it took 18 CPU-years of alpha–beta search to solve the game.
I. J. Good, who was taught the Game of Go by Alan Turing, wrote (1965a) “ I think it
will be even more difﬁcult to programme a computer to play a reasonable game of Go than of
chess.” He was right: through 2015, Go programs played only at an amateur level. The early
literature is summarized by Bouzy and Cazenave (2001) and M¨uller (2002).
Visual pattern recognition was proposed as a promising technique for Go by Zobrist
(1970), while Schraudolph et al. (1994) analyzed the use of reinforcement learning, Lubberts
and Miikkulainen (2001) recommended neural networks, and Br¨ugmann (1993) introduced
Monte Carlo tree search to Go. ALPHAGO (Silver et al., 2016) put those four ideas together
to defeat top-ranked professionals Lee Sedol (by a score of 4–1 in 2015) and Ke Jie (by 3–0
in 2016).
Ke Jie remarked “After humanity spent thousands of years improving our tactics, comput-
ers tell us that humans are completely wrong. I would go as far as to say not a single human
