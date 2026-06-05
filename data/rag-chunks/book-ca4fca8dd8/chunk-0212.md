---
chunk_id: "book-ca4fca8dd8-chunk-0212"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 212
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 4
SEARCH IN COMPLEX
ENVIRONMENTS
In which we relax the simplifying assumptions of the previous chapter, to get closer to the
real world.
Chapter 3 addressed problems in fully observable, deterministic, static, known environments
where the solution is a sequence of actions. In this chapter, we relax those constraints. We
begin with the problem of ﬁnding a good state without worrying about the path to get there,
covering both discrete (Section 4.1) and continuous (Section 4.2) states. Then we relax the
assumptions of determinism (Section 4.3) and observability (Section 4.4). In a nondetermin-
istic world, the agent will need a conditional plan and carry out different actions depending
on what it observes—for example, stopping if the light is red and going if it is green. With
partial observability, the agent will also need to keep track of the possible states it might be
in. Finally, Section 4.5 guides the agent through an unknown space that it must learn as it
goes, using online search.
4.1 Local Search and Optimization Problems
In the search problems of Chapter 3 we wanted to ﬁnd paths through the search space, such as
a path from Arad to Bucharest. But sometimes we care only about the ﬁnal state, not the path
to get there. For example, in the 8-queens problem (Figure 4.3), we care only about ﬁnding
a valid ﬁnal conﬁguration of 8 queens (because if you know the conﬁguration, it is trivial to
reconstruct the steps that created it). This is also true for many important applications such as
integrated-circuit design, factory ﬂoor layout, job shop scheduling, automatic programming,
telecommunications network optimization, crop planning, and portfolio management.
Local search algorithms operate by searching from a start state to neighboring states,
Local search
without keeping track of the paths, nor the set of states that have been reached. That means
they are not systematic—they might never explore a portion of the search space where a
solution actually resides. However, they have two key advantages: (1) they use very little
memory; and (2) they can often ﬁnd reasonable solutions in large or inﬁnite state spaces for
which systematic algorithms are unsuitable.
Local search algorithms can also solve optimization problems, in which the aim is to
Optimization
problem
ﬁnd the best state according to an objective function.
Objective function
To understand local search, consider the states of a problem laid out in a state-space
landscape, as shown in Figure 4.1. Each point (state) in the landscape has an “elevation,” de-
State-space
landscape
ﬁned by the value of the objective function. If elevation corresponds to an objective function,
