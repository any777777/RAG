---
chunk_id: "book-ca4fca8dd8-chunk-0981"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 981
confidence: "first-pass"
extraction_method: "structured-local"
---

592
Chapter 17
Multiagent Decision Making
be depleted by other agents; whether actions are mutually exclusive; and a helpfully inclined
agent could consider how its actions might facilitate the actions of others.
To answer these questions we need a model of concurrent action within which we can
properly formulate them. Models of concurrent action have been a major focus of research
in the mainstream computer science community for decades, but no deﬁnitive, universally
accepted model has prevailed. Nevertheless, the following three approaches have become
widely established.
The ﬁrst approach is to consider the interleaved execution of the actions in respective
Interleaved
execution
plans. For example, suppose we have two agents, A and B, with plans as follows:
A : [a1,a2]
B : [b1,b2].
The key idea of the interleaved execution model is that the only thing we can be certain about
in the execution of the two agents’ plans is that the order of actions in the respective plans
will be preserved. If we further assume that actions are atomic, then there are six different
ways in which the two plans above might be executed concurrently:
[a1,a2,b1,b2]
[b1,b2,a1,a2]
[a1,b1,a2,b2]
[b1,a1,b2,a2]
[a1,b1,b2,a2]
[b1,a1,a2,b2]
For a plan to be correct in the interleaved execution model, it must be correct with respect
▶
to all possible interleavings of the plans. The interleaved execution model has been widely
adopted within the concurrency community, because it is a reasonable model of the way
multiple threads take turns running on a single CPU. However, it does not model the case
where two actions actually happen at the same time. Furthermore, the number of interleaved
sequences will grow exponentially with the number of agents and actions: as a consequence,
checking the correctness of a plan, which is computationally straightforward in single-agent
settings, is computationally difﬁcult with the interleaved execution model.
The second approach is true concurrency, in which we do not attempt to create a full
True concurrency
serialized ordering of the actions, but leave them partially ordered: we know that a1 will
occur before a2, but with respect to the ordering of a1 and b1, for example, we can say nothing;
one may occur before the other, or they could occur concurrently. We can always “ﬂatten”
a partial-order model of concurrent plans into an interleaved model, but in doing so, we lose
the partial-order information. While partial-order models are arguably more satisfying than
interleaved models as a theoretical account of concurrent action, they have not been as widely
adopted in practice.
The third approach is to assume perfect synchronization: there is a global clock that each
Synchronization
agent has access to, each action takes the same amount of time, and actions at each point in
the joint plan are simultaneous. Thus, the actions of each agent are executed synchronously,
in lockstep with each other (it may be that some agents execute a no-op action when they are
waiting for other actions to complete). Synchronous execution is not a very complete model
of concurrency in the real world, but it has a simple semantics, and for this reason, it is the
model we will work with here.
