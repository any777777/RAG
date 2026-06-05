---
chunk_id: "book-ca4fca8dd8-chunk-0313"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 313
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 6
ADVERSARIAL SEARCH AND GAMES
In which we explore environments where other agents are plotting against us.
In this chapter we cover competitive environments, in which two or more agents have con-
ﬂicting goals, giving rise to adversarial search problems. Rather than deal with the chaos
Adversarial search
of real-world skirmishes, we will concentrate on games, such as chess, Go, and poker. For
AI researchers, the simpliﬁed nature of these games is a plus: the state of a game is easy to
represent, and agents are usually restricted to a small number of actions whose effects are
deﬁned by precise rules. Physical games, such as croquet and ice hockey, have more com-
plicated descriptions, a larger range of possible actions, and rather imprecise rules deﬁning
the legality of actions. With the exception of robot soccer, these physical games have not
attracted much interest in the AI community.
6.1 Game Theory
There are at least three stances we can take towards multi-agent environments. The ﬁrst
stance, appropriate when there are a very large number of agents, is to consider them in the
aggregate as an economy, allowing us to do things like predict that increasing demand will
Economy
cause prices to rise, without having to predict the action of any individual agent.
Second, we could consider adversarial agents as just a part of the environment—a part
that makes the environment nondeterministic. But if we model the adversaries in the same
way that, say, rain sometimes falls and sometimes doesn’t, we miss the idea that our adver-
saries are actively trying to defeat us, whereas the rain supposedly has no such intention.
The third stance is to explicitly model the adversarial agents with the techniques of ad-
versarial game-tree search. That is what this chapter covers. We begin with a restricted class
of games and deﬁne the optimal move and an algorithm for ﬁnding it: minimax search, a gen-
eralization of AND–OR search (from Figure 4.11). We show that pruning makes the search
Pruning
more efﬁcient by ignoring portions of the search tree that make no difference to the optimal
move. For nontrivial games, we will usually not have enough time to be sure of ﬁnding the
optimal move (even with pruning); we will have to cut off the search at some point.
For each state where we choose to stop searching, we ask who is winning. To answer this
question we have a choice: we can apply a heuristic evaluation function to estimate who is
winning based on features of the state (Section 6.3), or we can average the outcomes of many
fast simulations of the game from that state all the way to the end (Section 6.4).
Section 6.5 discusses games that include an element of chance (through rolling dice or
shufﬂing cards) and Section 6.6 covers games of imperfect information (such as poker and
Imperfect
information
bridge, where not all cards are visible to all players).
