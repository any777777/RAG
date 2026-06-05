---
chunk_id: "book-ca4fca8dd8-chunk-0028"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 28
confidence: "first-pass"
extraction_method: "structured-local"
---

22
Chapter 1
Introduction
change, and create and pursue goals. A rational agent is one that acts so as to achieve the
Rational agent
best outcome or, when there is uncertainty, the best expected outcome.
In the “laws of thought” approach to AI, the emphasis was on correct inferences. Mak-
ing correct inferences is sometimes part of being a rational agent, because one way to act
rationally is to deduce that a given action is best and then to act on that conclusion. On the
other hand, there are ways of acting rationally that cannot be said to involve inference. For
example, recoiling from a hot stove is a reﬂex action that is usually more successful than a
slower action taken after careful deliberation.
All the skills needed for the Turing test also allow an agent to act rationally. Knowledge
representation and reasoning enable agents to reach good decisions. We need to be able to
generate comprehensible sentences in natural language to get by in a complex society. We
need learning not only for erudition, but also because it improves our ability to generate
effective behavior, especially in circumstances that are new.
The rational-agent approach to AI has two advantages over the other approaches. First, it
is more general than the “laws of thought” approach because correct inference is just one of
several possible mechanisms for achieving rationality. Second, it is more amenable to scien-
tiﬁc development. The standard of rationality is mathematically well deﬁned and completely
general. We can often work back from this speciﬁcation to derive agent designs that provably
achieve it—something that is largely impossible if the goal is to imitate human behavior or
thought processes.
For these reasons, the rational-agent approach to AI has prevailed throughout most of
the ﬁeld’s history. In the early decades, rational agents were built on logical foundations
and formed deﬁnite plans to achieve speciﬁc goals. Later, methods based on probability
theory and machine learning allowed the creation of agents that could make decisions under
uncertainty to attain the best expected outcome. In a nutshell, AI has focused on the study
▶
and construction of agents that do the right thing. What counts as the right thing is deﬁned
Do the right thing
by the objective that we provide to the agent. This general paradigm is so pervasive that we
might call it the standard model. It prevails not only in AI, but also in control theory, where a
Standard model
controller minimizes a cost function; in operations research, where a policy maximizes a sum
of rewards; in statistics, where a decision rule minimizes a loss function; and in economics,
where a decision maker maximizes utility or some measure of social welfare.
We need to make one important reﬁnement to the standard model to account for the fact
that perfect rationality—always taking the exactly optimal action—is not feasible in complex
environments. The computational demands are just too high. Chapters 6 and 16 deal with the
issue of limited rationality—acting appropriately when there is not enough time to do all
Limited rationality
the computations one might like. However, perfect rationality often remains a good starting
point for theoretical analysis.
1.1.5 Beneﬁcial machines
The standard model has been a useful guide for AI research since its inception, but it is
probably not the right model in the long run. The reason is that the standard model assumes
that we will supply a fully speciﬁed objective to the machine.
For an artiﬁcially deﬁned task such as chess or shortest-path computation, the task comes
with an objective built in—so the standard model is applicable. As we move into the real
world, however, it becomes more and more difﬁcult to specify the objective completely and
