---
chunk_id: "book-ca4fca8dd8-chunk-0858"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 858
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.2
The Basis of Utility Theory
519
sense deﬁned on page 63. (This assumption is relaxed in Chapter 16.) The agent’s prefer-
ences are captured by a utility function, U(s), which assigns a single number to express the
Utility function
desirability of a state. The expected utility of an action given the evidence, EU(a), is just the
Expected utility
average utility value of the outcomes, weighted by the probability that the outcome occurs:
EU(a) = ∑
s′
P(RESULT(a)=s′)U(s′).
(15.1)
The principle of maximum expected utility (MEU) says that a rational agent should choose
the action that maximizes the agent’s expected utility:
action = argmax
a
EU(a).
In a sense, the MEU principle could be seen as a prescription for intelligent behavior. All an
intelligent agent has to do is calculate the various quantities, maximize utility over its actions,
and away it goes. But this does not mean that the AI problem is solved by the deﬁnition!
The MEU principle formalizes the general notion that an intelligent agent should “do the
right thing,” but does not operationalize that advice. Estimating the probability distribution
P(s) over possible states of the world, which folds into P(RESULT(a)=s′), requires percep-
tion, learning, knowledge representation, and inference. Computing P(RESULT(a)=s′) itself
requires a causal model of the world. There may be many actions to consider, and computing
the outcome utilities U(s′) may itself require further searching or planning because an agent
may not know how good a state is until it knows where it can get to from that state. An AI
system acting on behalf of a human may not know the human’s true utility function, so there
may be uncertainty about U. In summary, decision theory is not a panacea that solves the
AI problem—but it does provide the beginnings of a basic mathematical framework that is
general enough to deﬁne the AI problem.
The MEU principle has a clear relation to the idea of performance measures introduced
in Chapter 2. The basic idea is simple. Consider the environments that could lead to an agent
having a given percept history, and consider the different agents that we could design. If an ◀
agent acts so as to maximize a utility function that correctly reﬂects the performance measure,
then the agent will achieve the highest possible performance score (averaged over all the
possible environments). This is the central justiﬁcation for the MEU principle itself. While
the claim may seem tautological, it does in fact embody a very important transition from the
external performance measure to an internal utility function. The performance measure gives
a score for a history—a sequence of states. Thus it is applied retrospectively after an agent
completes a sequence of actions. The utility function applies to the very next state, so it can
be used to guide actions step by step.
15.2 The Basis of Utility Theory
Intuitively, the principle of Maximum Expected Utility (MEU) seems like a reasonable way
to make decisions, but it is by no means obvious that it is the only rational way. After all,
why should maximizing the average utility be so special? What’s wrong with an agent that
maximizes the weighted sum of the cubes of the possible utilities, or tries to minimize the
worst possible loss? Could an agent act rationally just by expressing preferences between
states, without giving them numeric values? Finally, why should a utility function with the
required properties exist at all? We shall see.
