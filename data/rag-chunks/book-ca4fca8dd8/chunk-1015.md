---
chunk_id: "book-ca4fca8dd8-chunk-1015"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1015
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
611
corresponding to a raise, check, call, or fold, or, for Chance, the four possible deals (“AK”
means that player 1 gets an ace and player 2 a king). Terminal states are rectangles labeled
by their payoff to player 1 and player 2. Information sets are shown as labeled dashed boxes;
for example, I1,1 is the information set where it is player 1’s turn, and he knows he has an ace
(but does not know what player 2 has). In information set I2,1, it is player 2’s turn and she
knows that she has an ace and that player 1 has raised, but does not know what card player 1
has. (Due to the limits of two-dimensional paper, this information set is shown as two boxes
rather than one.)
One way to solve an extensive game is to convert it to a normal-form game. Recall that
the normal form is a matrix, each row of which is labeled with a pure strategy for player 1, and
each column by a pure strategy for player 2. In an extensive game a pure strategy for player i
corresponds to an action for each information set involving that player. So in Figure 17.5, one
pure strategy for player 1 is “raise when in I1,1 (that is, when I have an ace), and check when
in I1,2 (when I have a king).” In the payoff matrix below, this strategy is called rk. Similarly,
strategy cf for player 2 means “call when I have an ace and fold when I have a king.” Since
this is a zero-sum game, the matrix below gives only the payoff for player 1; player 2 always
has the opposite payoff:
2:cc
2:cf
2:ff
2:fc
1:rr
0
-1/6
1
7/6
1:kr
-1/3
-1/6
5/6
2/3
1:rk
1/3
0
1/6
1/2
1:kk
0
0
0
0
This game is so simple that it has two pure-strategy equilibria, shown in bold: cf for player
2 and rk or kk for player 1. But in general we can solve extensive games by converting
to normal form and then ﬁnding a solution (usually a mixed strategy) using standard linear
programming methods. That works in theory. But if a player has I information sets and
a actions per set, then that player will have aI pure strategies. In other words, the size of
the normal-form matrix is exponential in the number of information sets, so in practice the
approach works only for tiny game trees—a dozen states or so. A game like two-player Texas
hold ’em poker has about 1018 states, making this approach completely infeasible.
What are the alternatives? In Chapter 6 we saw how alpha–beta search could handle
games of perfect information with huge game trees by generating the tree incrementally, by
pruning some branches, and by heuristically evaluating nonterminal nodes. But that approach
does not work well for games with imperfect information, for two reasons: ﬁrst, it is harder
to prune, because we need to consider mixed strategies that combine multiple branches, not a
pure strategy that always chooses the best branch. Second, it is harder to heuristically evaluate
a nonterminal node, because we are dealing with information sets, not individual states.
Koller et al. (1996) came to the rescue with an alternative representation of extensive
games, called the sequence form, that is only linear in the size of the tree, rather than ex-
Sequence form
ponential. Rather than represent strategies, it represents paths through the tree; the number
of paths is equal to the number of terminal nodes. Standard linear programming methods
can again be applied to this representation. The resulting system can solve poker variants
with 25,000 states in a minute or two. This is an exponential speedup over the normal-form
approach, but still falls far short of handling, say, two-player Texas hold ’em, with 1018 states.
