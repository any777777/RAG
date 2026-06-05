---
chunk_id: "book-ca4fca8dd8-chunk-1383"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1383
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 23
REINFORCEMENT LEARNING
In which we see how experiencing rewards and punishments can teach an agent how to
maximize rewards in the future.
With supervised learning, an agent learns by passively observing example input/output
pairs provided by a “teacher.” In this chapter, we will see how agents can actively learn from
their own experience, without a teacher, by considering their own ultimate success or failure.
23.1 Learning from Rewards
Consider the problem of learning to play chess. Let’s imagine treating this as a supervised
learning problem using the methods of Chapters 19, 21, and 22. The chess-playing agent
function takes as input a board position and returns a move, so we train this function by sup-
plying examples of chess positions, each labeled with the correct move. Now, it so happens
that we have available databases of several million grandmaster games, each a sequence of
positions and moves. The moves made by the winner are, with few exceptions, assumed to be
good, if not always perfect. Thus, we have a promising training set. The problem is that there
are relatively few examples (about 108) compared to the space of all possible chess positions
(about 1040). In a new game, one soon encounters positions that are signiﬁcantly different
from those in the database, and the trained agent function is likely to fail miserably—not least
because it has no idea of what its moves are supposed to achieve (checkmate) or even what
effect the moves have on the positions of the pieces. And of course chess is a tiny part of the
real world. For more realistic problems, we would need much vaster grandmaster databases,
and they simply don’t exist.1
An alternative is reinforcement learning (RL), in which an agent interacts with the world
Reinforcement
learning
and periodically receives rewards (or, in the terminology of psychology, reinforcements)
that reﬂect how well it is doing. For example, in chess the reward is 1 for winning, 0 for
losing, and 1
2 for a draw. We have already seen the concept of rewards in Chapter 16 for
Markov decision processes (MDPs). Indeed, the goal is the same in reinforcement learning:
maximize the expected sum of rewards. Reinforcement learning differs from “just solving
an MDP” because the agent is not given the MDP as a problem to solve; the agent is in the
MDP. It may not know the transition model or the reward function, and it has to act in order
to learn more. Imagine playing a new game whose rules you don’t know; after a hundred or
so moves, the referee tells you “You lose.” That is reinforcement learning in a nutshell.
From our point of view as designers of AI systems, providing a reward signal to the agent
is usually much easier than providing labeled examples of how to behave. First, the reward
1
As Yann LeCun and Alyosha Efros have pointed out, “the AI revolution will not be supervised.”
