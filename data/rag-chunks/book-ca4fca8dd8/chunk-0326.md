---
chunk_id: "book-ca4fca8dd8-chunk-0326"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 326
confidence: "first-pass"
extraction_method: "structured-local"
---

202
Chapter 6
Adversarial Search and Games
6.3 Heuristic Alpha–Beta Tree Search
To make use of our limited computation time, we can cut off the search early and apply a
heuristic evaluation function to states, effectively treating nonterminal nodes as if they were
terminal. In other words, we replace the UTILITY function with EVAL, which estimates a
state’s utility. We also replace the terminal test by a cutoff test, which must return true for
Cutoﬀtest
terminal states, but is otherwise free to decide when to cut off the search, based on the search
depth and any property of the state that it chooses to consider. That gives us the formula
H-MINIMAX(s, d) for the heuristic minimax value of state s at search depth d:
H-MINIMAX(s,d) =



EVAL(s, MAX)
if IS-CUTOFF(s,d)
maxa∈Actions(s) H-MINIMAX(RESULT(s,a),d +1) if TO-MOVE(s) = MAX
mina∈Actions(s) H-MINIMAX(RESULT(s,a),d +1)
if TO-MOVE(s) = MIN.
6.3.1 Evaluation functions
A heuristic evaluation function EVAL(s, p) returns an estimate of the expected utility of state
s to player p, just as the heuristic functions of Chapter 3 return an estimate of the distance to
the goal. For terminal states, it must be that EVAL(s, p)=UTILITY(s, p) and for nonterminal
states, the evaluation must be somewhere between a loss and a win: UTILITY(loss, p) ≤
EVAL(s, p) ≤UTILITY(win, p).
Beyond those requirements, what makes for a good evaluation function? First, the com-
putation must not take too long! (The whole point is to search faster.) Second, the evaluation
function should be strongly correlated with the actual chances of winning. One might well
wonder about the phrase “chances of winning.” After all, chess is not a game of chance: we
know the current state with certainty, and no dice are involved; if neither player makes a mis-
take, the outcome is predetermined. But if the search must be cut off at nonterminal states,
then the algorithm will necessarily be uncertain about the ﬁnal outcomes of those states (even
though that uncertainty could be resolved with inﬁnite computing resources).
Let us make this idea more concrete. Most evaluation functions work by calculating
various features of the state—for example, in chess, we would have features for the number
Features
of white pawns, black pawns, white queens, black queens, and so on. The features, taken
together, deﬁne various categories or equivalence classes of states: the states in each category
have the same values for all the features. For example, one category might contain all two-
pawn versus one-pawn endgames. Any given category will contain some states that lead (with
perfect play) to wins, some that lead to draws, and some that lead to losses.
The evaluation function does not know which states are which, but it can return a single
value that estimates the proportion of states with each outcome. For example, suppose our
experience suggests that 82% of the states encountered in the two-pawns versus one-pawn
category lead to a win (utility +1); 2% to a loss (0), and 16% to a draw (1/2). Then a reason-
able evaluation for states in the category is the expected value: (0.82 × +1) +(0.02 × 0) +
Expected value
(0.16×1/2) = 0.90. In principle, the expected value can be determined for each category of
states, resulting in an evaluation function that works for any state.
In practice, this kind of analysis requires too many categories and hence too much expe-
rience to estimate all the probabilities. Instead, most evaluation functions compute separate
numerical contributions from each feature and then combine them to ﬁnd the total value. For
