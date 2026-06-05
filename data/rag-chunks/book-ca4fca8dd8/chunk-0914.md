---
chunk_id: "book-ca4fca8dd8-chunk-0914"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 914
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 16
MAKING COMPLEX DECISIONS
In which we examine methods for deciding what to do today, given that we may face another
decision tomorrow.
In this chapter, we address the computational issues involved in making decisions in a stochas-
tic environment. Whereas Chapter 15 was concerned with one-shot or episodic decision prob-
lems, in which the utility of each action’s outcome was well known, we are concerned here
with sequential decision problems, in which the agent’s utility depends on a sequence of
Sequential decision
problem
decisions. Sequential decision problems incorporate utilities, uncertainty, and sensing, and
include search and planning problems as special cases. Section 16.1 explains how sequential
decision problems are deﬁned, and Section 16.2 describes methods for solving them to pro-
duce behaviors that are appropriate for a stochastic environment. Section 16.3 covers multi-
armed bandit problems, a speciﬁc and fascinating class of sequential decision problems
that arise in many contexts. Section 16.4 explores decision problems in partially observable
environments and Section 16.5 describes how to solve them.
16.1 Sequential Decision Problems
Suppose that an agent is situated in the 4×3 environment shown in Figure 16.1(a). Beginning
in the start state, it must choose an action at each time step. The interaction with the environ-
ment terminates when the agent reaches one of the goal states, marked +1 or –1. Just as for
search problems, the actions available to the agent in each state are given by ACTIONS(s),
sometimes abbreviated to A(s); in the 4×3 environment, the actions in every state are Up,
Down, Left, and Right. We assume for now that the environment is fully observable, so that
the agent always knows where it is.
If the environment were deterministic, a solution would be easy: [Up, Up, Right, Right,
Right]. Unfortunately, the environment won’t always go along with this solution, because the
actions are unreliable. The particular model of stochastic motion that we adopt is illustrated
in Figure 16.1(b). Each action achieves the intended effect with probability 0.8, but the rest
of the time, the action moves the agent at right angles to the intended direction. Furthermore,
if the agent bumps into a wall, it stays in the same square. For example, from the start square
(1,1), the action Up moves the agent to (1,2) with probability 0.8, but with probability 0.1, it
moves right to (2,1), and with probability 0.1, it moves left, bumps into the wall, and stays
in (1,1). In such an environment, the sequence [Up,Up,Right,Right,Right] goes up around
the barrier and reaches the goal state at (4,3) with probability 0.85 =0.32768. There is also a
small chance of accidentally reaching the goal by going the other way around with probability
0.14 ×0.8, for a grand total of 0.32776. (See also Exercise 16.MDPX.)
