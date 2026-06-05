---
chunk_id: "book-ca4fca8dd8-chunk-0659"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 659
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
397
Unfortunately, we do not yet have a clear understanding of which techniques work best
on which kinds of problems. Quite possibly, new techniques will emerge, perhaps providing
a synthesis of highly expressive ﬁrst-order and hierarchical representations with the highly
efﬁcient factored and propositional representations that dominate today. We are seeing exam-
ples of portfolio planning systems, where a collection of algorithms are available to apply to
Portfolio
any given problem. This can be done selectively (the system classiﬁes each new problem to
choose the best algorithm for it), or in parallel (all the algorithms run concurrently, each on a
different CPU), or by interleaving the algorithms according to a schedule.
Summary
In this chapter, we described the PDDL representation for both classical and extended plan-
ning problems, and presented several algorithmic approaches for ﬁnding solutions. The points
to remember:
• Planning systems are problem-solving algorithms that operate on explicit factored rep-
resentations of states and actions. These representations make possible the derivation of
effective domain-independent heuristics and the development of powerful and ﬂexible
algorithms for solving problems.
• PDDL, the Planning Domain Deﬁnition Language, describes the initial and goal states
as conjunctions of literals, and actions in terms of their preconditions and effects. Ex-
tensions represent time, resources, percepts, contingent plans, and hierarchical plans.
• State-space search can operate in the forward direction (progression) or the backward
direction (regression). Effective heuristics can be derived by subgoal independence
assumptions and by various relaxations of the planning problem.
• Other approaches include encoding a planning problem as a Boolean satisﬁability prob-
lem or as a constraint satisfaction problem; and explicitly searching through the space
of partially ordered plans.
• Hierarchical task network (HTN) planning allows the agent to take advice from the
domain designer in the form of high-level actions (HLAs) that can be implemented in
various ways by lower-level action sequences. The effects of HLAs can be deﬁned with
angelic semantics, allowing provably correct high-level plans to be derived without
consideration of lower-level implementations. HTN methods can create the very large
plans required by many real-world applications.
• Contingent plans allow the agent to sense the world during execution to decide what
branch of the plan to follow. In some cases, sensorless or conformant planning can be
used to construct a plan that works without the need for perception. Both conformant
and contingent plans can be constructed by search in the space of belief states. Efﬁcient
representation or computation of belief states is a key problem.
• An online planning agent uses execution monitoring and splices in repairs as needed
to recover from unexpected situations, which can be due to nondeterministic actions,
exogenous events, or incorrect models of the environment.
• Many actions consume resources, such as money, gas, or raw materials. It is convenient
to treat these resources as numeric measures in a pool rather than try to reason about,
