---
chunk_id: "book-ca4fca8dd8-chunk-0943"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 943
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.3
Bandit Problems
571
UCT seems better suited for Tetris, where the playouts go far enough into the future to
give the agent a sense of whether a potentially risky move will work out in the end or cause
a massive pile-up. Exercise 16.UCTT explores the application of UCT to Tetris. One partic-
ularly interesting question is how much a simple simulation policy can help—for example,
one that avoids creating overhangs and puts pieces as low as possible.
16.3 Bandit Problems
In Las Vegas, a one-armed bandit is a slot machine. A gambler can insert a coin, pull the
lever, and collect the winnings (if any). An n-armed bandit has n levers. Behind each
N-armed bandit
lever is a ﬁxed but unknown probability distribution of winnings; each pull samples from that
unknown distribution.
The gambler must choose which lever to play on each successive coin—the one that has
paid off best, or maybe one that has not been tried yet? This is an example of the ubiquitous
tradeoff between exploitation of the current best action to obtain rewards and exploration
of previously unknown states and actions to gain information, which can in some cases be
converted into a better policy and better long-term rewards. In the real world, one constantly
has to decide between continuing in a comfortable existence, versus striking out into the
unknown in the hopes of a better life.
The n-armed bandit problem is a formal model for real problems in many vitally im-
portant areas, such as deciding which of n possible new treatments to try to cure a disease,
which of n possible investments to put part of your savings into, which of n possible re-
search projects to fund, or which of n possible advertisements to show when the user visits a
particular web page.
Early work on the problem began in the U.S. during World War II; it proved so recalcitrant
that Allied scientists proposed that “the problem be dropped over Germany, as the ultimate
instrument of intellectual sabotage” (Whittle, 1979).
It turns out that the scientists, both during and after the war, were trying to prove “obvi-
ously true” facts about bandit problems that are, in fact, false. (As Bradt et al. (1956) put it,
“There are many nice properties which optimal strategies do not possess.”) For example, it
was generally assumed that an optimal policy would eventually settle on the best arm in the
long run; in fact, there is a ﬁnite probability that an optimal policy settles on a suboptimal
arm. We now have a solid theoretical understanding of bandit problems as well as useful
algorithms for solving them.
There are several different deﬁnitions of bandit problems; one of the cleanest and most
Bandit problems
general is as follows:
• Each arm Mi is a Markov reward process or MRP, that is, an MDP with only one
Markov reward
process
possible action ai. It has states Si, transition model Pi(s′ |s,ai), and reward Ri(s,ai,s′).
The arm deﬁnes a distribution over sequences of rewards Ri,0,Ri,1,Ri,2,..., where each
Ri,t is a random variable.
• The overall bandit problem is an MDP: the state space is given by the Cartesian product
S=S1 × ··· ×Sn; the actions are a1,...,an; the transition model updates the state of
whichever arm Mi is selected, according to its speciﬁc transition model, leaving the
other arms unchanged; and the discount factor is γ.
