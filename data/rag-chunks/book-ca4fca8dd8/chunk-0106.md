---
chunk_id: "book-ca4fca8dd8-chunk-0106"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 106
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.3
The Nature of Environments
63
For example, in chess, the opponent entity B is trying to maximize its performance mea-
sure, which, by the rules of chess, minimizes agent A’s performance measure. Thus, chess is
a competitive multiagent environment. On the other hand, in the taxi-driving environment,
Competitive
avoiding collisions maximizes the performance measure of all agents, so it is a partially co-
operative multiagent environment. It is also partially competitive because, for example, only
Cooperative
one car can occupy a parking space.
The agent-design problems in multiagent environments are often quite different from
those in single-agent environments; for example, communication often emerges as a rational
behavior in multiagent environments; in some competitive environments, randomized behav-
ior is rational because it avoids the pitfalls of predictability.
Deterministic vs. nondeterministic. If the next state of the environment is completely
Deterministic
Nondeterministic
determined by the current state and the action executed by the agent(s), then we say the
environment is deterministic; otherwise, it is nondeterministic. In principle, an agent need not
worry about uncertainty in a fully observable, deterministic environment. If the environment
is partially observable, however, then it could appear to be nondeterministic.
Most real situations are so complex that it is impossible to keep track of all the unobserved
aspects; for practical purposes, they must be treated as nondeterministic. Taxi driving is
clearly nondeterministic in this sense, because one can never predict the behavior of trafﬁc
exactly; moreover, one’s tires may blow out unexpectedly and one’s engine may seize up
without warning. The vacuum world as we described it is deterministic, but variations can
include nondeterministic elements such as randomly appearing dirt and an unreliable suction
mechanism (Exercise 2.VFIN).
One ﬁnal note: the word stochastic is used by some as a synonym for “nondeterministic,”
Stochastic
but we make a distinction between the two terms; we say that a model of the environment
is stochastic if it explicitly deals with probabilities (e.g., “there’s a 25% chance of rain to-
morrow”) and “nondeterministic” if the possibilities are listed without being quantiﬁed (e.g.,
“there’s a chance of rain tomorrow”).
Episodic vs. sequential: In an episodic task environment, the agent’s experience is di-
Episodic
Sequential
vided into atomic episodes. In each episode the agent receives a percept and then performs
a single action. Crucially, the next episode does not depend on the actions taken in pre-
vious episodes. Many classiﬁcation tasks are episodic. For example, an agent that has to
spot defective parts on an assembly line bases each decision on the current part, regardless
of previous decisions; moreover, the current decision doesn’t affect whether the next part is
defective. In sequential environments, on the other hand, the current decision could affect
all future decisions.4 Chess and taxi driving are sequential: in both cases, short-term actions
can have long-term consequences. Episodic environments are much simpler than sequential
environments because the agent does not need to think ahead.
Static vs. dynamic: If the environment can change while an agent is deliberating, then
Static
Dynamic
we say the environment is dynamic for that agent; otherwise, it is static. Static environments
are easy to deal with because the agent need not keep looking at the world while it is deciding
on an action, nor need it worry about the passage of time. Dynamic environments, on the
other hand, are continuously asking the agent what it wants to do; if it hasn’t decided yet,
4
The word “sequential” is also used in computer science as the antonym of “parallel.” The two meanings are
largely unrelated.
