---
chunk_id: "book-ca4fca8dd8-chunk-0975"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 975
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 17
MULTIAGENT DECISION MAKING
In which we examine what to do when more than one agent inhabits the environment.
17.1 Properties of Multiagent Environments
So far, we have largely assumed that only one agent has been doing the sensing, planning, and
acting. But this represents a huge simplifying assumption, which fails to capture many real-
world AI settings. In this chapter, therefore, we will consider the issues that arise when an
agent must make decisions in environments that contain multiple actors. Such environments
are called multiagent systems, and agents in such a system face a multiagent planning
Multiagent systems
problem. However, as we will see, the precise nature of the multiagent planning problem—
Multiagent planning
problem
and the techniques that are appropriate for solving it—will depend on the relationships among
the agents in the environment.
17.1.1 One decision maker
The ﬁrst possibility is that while the environment contains multiple actors, it contains only
one decision maker. In such a case, the decision maker develops plans for the other agents,
and tells them what to do. The assumption that agents will simply do what they are told
is called the benevolent agent assumption. However, even in this setting, plans involving
Benevolent agent
assumption
multiple actors will require actors to synchronize their actions. Actors A and B will have to
act at the same time for joint actions (such as singing a duet), at different times for mutually
exclusive actions (such as recharging batteries when there is only one plug), and sequentially
when one establishes a precondition for the other (such as A washing the dishes and then B
drying them).
One special case is where we have a single decision maker with multiple effectors that
can operate concurrently—for example, a human who can walk and talk at the same time.
Such an agent needs to do multieffector planning to manage each effector while handling
Multieﬀector
planning
positive and negative interactions among the effectors. When the effectors are physically
decoupled into detached units—as in a ﬂeet of delivery robots in a factory—multieffector
planning becomes multibody planning.
Multibody planning
A multibody problem is still a “standard” single-agent problem as long as the relevant
sensor information collected by each body can be pooled—either centrally or within each
body—to form a common estimate of the world state that then informs the execution of
the overall plan; in this case, the multiple bodies can be thought of as acting as a single
body. When communication constraints make this impossible, we have what is sometimes
called a decentralized planning problem; this is perhaps a misnomer, because the planning
Decentralized
planning
phase is centralized but the execution phase is at least partially decoupled. In this case, the
