---
chunk_id: "book-ca4fca8dd8-chunk-0597"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 597
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 11
AUTOMATED PLANNING
In which we see how an agent can take advantage of the structure of a problem to efﬁciently
construct complex plans of action.
Planning a course of action is a key requirement for an intelligent agent. The right represen-
tation for actions and states and the right algorithms can make this easier. In Section 11.1
we introduce a general factored representation language for planning problems that can nat-
urally and succinctly represent a wide variety of domains, can efﬁciently scale up to large
problems, and does not require ad hoc heuristics for a new domain. Section 11.4 extends the
representation language to allow for hierarchical actions, allowing us to tackle more complex
problems. We cover efﬁcient algorithms for planning in Section 11.2, and heuristics for them
in Section 11.3. In Section 11.5 we account for partially observable and nondeterministic
domains, and in Section 11.6 we extend the language once again to cover scheduling prob-
lems with resource constraints. This gets us closer to planners that are used in the real world
for planning and scheduling the operations of spacecraft, factories, and military campaigns.
Section 11.7 analyzes the effectiveness of these techniques.
11.1 Deﬁnition of Classical Planning
Classical planning is deﬁned as the task of ﬁnding a sequence of actions to accomplish a
Classical planning
goal in a discrete, deterministic, static, fully observable environment. We have seen two ap-
proaches to this task: the problem-solving agent of Chapter 3 and the hybrid propositional
logical agent of Chapter 7. Both share two limitations. First, they both require ad hoc heuris-
tics for each new domain: a heuristic evaluation function for search, and hand-written code
for the hybrid wumpus agent. Second, they both need to explicitly represent an exponentially
large state space. For example, in the propositional logic model of the wumpus world, the
axiom for moving a step forward had to be repeated for all four agent orientations, T time
steps, and n2 current locations.
In response to these limitations, planning researchers have invested in a factored repre-
sentation using a family of languages called PDDL, the Planning Domain Deﬁnition Lan-
PDDL
guage (Ghallab et al., 1998), which allows us to express all 4Tn2 actions with a single action
schema, and does not need domain-speciﬁc knowledge. Basic PDDL can handle classical
planning domains, and extensions can handle non-classical domains that are continuous, par-
tially observable, concurrent, and multi-agent. The syntax of PDDL is based on Lisp, but we
will translate it into a form that matches the notation used in this book.
In PDDL, a state is represented as a conjunction of ground atomic ﬂuents. Recall that
State
“ground” means no variables, “ﬂuent” means an aspect of the world that changes over time,
