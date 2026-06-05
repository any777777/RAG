---
chunk_id: "book-ca4fca8dd8-chunk-1003"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1003
confidence: "first-pass"
extraction_method: "structured-local"
---

604
Chapter 17
Multiagent Decision Making
17.2.3 Repeated games
So far, we have looked only at games that last a single move. The simplest kind of multiple-
move game is the repeated game (also called an iterated game), in which players repeatedly
Repeated game
play rounds of a single-move game, called the stage game. A strategy in a repeated game
Stage game
speciﬁes an action choice for each player at each time step for every possible history of
previous choices of players.
First, let’s look at the case where the stage game is repeated a ﬁxed, ﬁnite, and mutually
known number of rounds—all of these conditions are required for the following analysis to
work. Let’s suppose Ali and Bo are playing a repeated version of the prisoner’s dilemma, and
that both they know that they must play exactly 100 rounds of the game. On each round, they
will be asked whether to testify or refuse, and will receive a payoff for that round according
to the rules of the prisoner’s dilemma that we saw above.
At the end of 100 rounds, we ﬁnd the overall payoff for each player by summing that
player’s payoffs in the 100 rounds. What strategies should Ali and Bo choose to play this
game? Consider the following argument. They both know that the 100th round will not be
a repeated game—that is, its outcome can have no effect on future rounds. So, on the 100th
round, they are in effect playing a single prisoner’s dilemma game.
As we saw above, the outcome of the 100th round will be (testify,testify), the dominant
equilibrium strategy for both players. But once the 100th round is determined, the 99th round
can have no effect on subsequent rounds, so it too will yield (testify,testify). By this inductive
argument, both players will choose testify on every round, earning a total jail sentence of 500
years each. This type of reasoning is known as backward induction, and plays a fundamental
Backward induction
role in game theory.
However, if we drop one of the three conditions—ﬁxed, ﬁnite, or mutually known—then
the inductive argument doesn’t hold. Suppose that the game is repeated an inﬁnite number of
times. Mathematically, a strategy for a player in an inﬁnitely repeated game is a function that
maps every possible ﬁnite history of the game to a choice in the stage game for that player
in the corresponding round. Thus, a strategy looks at what happened previously in the game,
and decides what choice to make in the current round. But we can’t store an inﬁnite table in a
ﬁnite computer. We need a ﬁnite model of strategies for games that will be played an inﬁnite
number of rounds. For this reason, it is standard to represent strategies for inﬁnitely repeated
games as ﬁnite state machines (FSMs) with output.
Figure 17.3 illustrates a number of FSM strategies for the iterated prisoner’s dilemma.
Consider the Tit-for-Tat strategy. Each oval is a state of the machine, and inside the oval
Tit-for-Tat
is the choice that would be made by the strategy if the machine was in that state. From
each state, we have one outgoing edge for every possible choice of the counterpart agent:
we follow the outgoing edge corresponding to the choice made by the other to ﬁnd the next
state of the machine. Finally, one state is labeled with an incoming arrow, indicating that
it is the initial state. Thus, with TIT-FOR-TAT, the machine starts in the refuse state; if the
counterpart agent plays refuse, then it stays in the refuse state, while if the counterpart plays
testify it transitions to the testify state. It will remain in the testify state as long its counterpart
plays testify, but if ever its counterpart plays refuse, it will transition back to the refuse state.
In sum, TIT-FOR-TAT will start by choosing refuse, and will then simply copy whatever its
counterpart did on the previous round.
