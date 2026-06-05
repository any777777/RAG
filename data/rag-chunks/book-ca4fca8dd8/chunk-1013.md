---
chunk_id: "book-ca4fca8dd8-chunk-1013"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1013
confidence: "first-pass"
extraction_method: "structured-local"
---

610
Chapter 17
Multiagent Decision Making
Unfortunately, backward induction does not work with games of imperfect information, and
in general, they are considerably more complex to solve than games of perfect information.
We saw in Section 6.6 that a player in a partially observable game such as Kriegspiel
can create a game tree over the space of belief states. With that tree, we saw that in some
cases a player can ﬁnd a sequence of moves (a strategy) that leads to a forced checkmate
regardless of what actual state we started in, and regardless of what strategy the opponent
uses. However, the techniques of Chapter 6 could not tell a player what to do when there is
no guaranteed checkmate. If the player’s best strategy depends on the opponent’s strategy and
vice versa, then minimax (or alpha–beta) by itself cannot ﬁnd a solution. The extensive form
does allow us to ﬁnd solutions because it represents the belief states (game theorists call them
information sets) of all players at once. From that representation we can ﬁnd equilibrium
Information set
solutions, just as we did with normal-form games.
As a simple example of a sequential game, place two agents in the 4×3 world of Fig-
ure 16.1 and have them move simultaneously until one agent reaches an exit square and gets
the payoff for that square. If we specify that no movement occurs when the two agents try
to move into the same square simultaneously (a common problem at many trafﬁc intersec-
tions), then certain pure strategies can get stuck forever. Thus, agents need a mixed strategy
to perform well in this game: randomly choose between moving ahead and staying put. This
is exactly what is done to resolve packet collisions in Ethernet networks.
Next we’ll consider a very simple variant of poker. The deck has only four cards, two
aces and two kings. One card is dealt to each player. The ﬁrst player then has the option to
raise the stakes of the game from 1 point to 2, or to check. If player 1 checks, the game is
over. If player 1 raises, then player 2 has the option to call, accepting that the game is worth
2 points, or fold, conceding the 1 point. If the game does not end with a fold, then the payoff
depends on the cards: it is zero for both players if they have the same card; otherwise the
player with the king pays the stakes to the player with the ace.
The extensive-form tree for this game is shown in Figure 17.5. Player 0 is Chance;
players 1 and 2 are depicted by triangles. Each action is depicted as an arrow with a label,
0 
0,0!
+1,-1!
0,0!
-1,+1!
1/6: AA
r 
k 
r 
k 
r 
k 
r 
k 
+1,-1!
+1,-1!
+1,-1!
+1,-1!
0,0!
+2,-2!
0,0!
-2,+2!
c 
f 
c 
f 
c 
f 
c 
f 
1/3: KA
1/3: AK 
1/6: KK 
I1,1 
I1,2 
I2,1 
I2,2 
I2,1 
1
1
1
1
2 
2 
2 
2 
Figure 17.5 Extensive form of a simpliﬁed version of poker with two players and only four
cards. The moves are r (raise), f (fold), c (call), and k (check).
