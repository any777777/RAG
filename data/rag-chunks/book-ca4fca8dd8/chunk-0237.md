---
chunk_id: "book-ca4fca8dd8-chunk-0237"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 237
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 144

144
Chapter 4
Search in Complex Environments
Suck
Right
6 
1 
2 
5 
Right
Figure 4.12 Part of the search graph for a slippery vacuum world, where we have shown
(some) cycles explicitly. All solutions for this problem are cyclic plans because there is no
way to move reliably.
4.4 Search in Partially Observable Environments
We now turn to the problem of partial observability, where the agent’s percepts are not enough
to pin down the exact state. That means that some of the agent’s actions will be aimed at
reducing uncertainty about the current state.
4.4.1 Searching with no observation
When the agent’s percepts provide no information at all, we have what is called a sensorless
Sensorless
problem (or a conformant problem). At ﬁrst, you might think the sensorless agent has no
Conformant
hope of solving a problem if it has no idea what state it starts in, but sensorless solutions are
surprisingly common and useful, primarily because they don’t rely on sensors working prop-
erly. In manufacturing systems, for example, many ingenious methods have been developed
for orienting parts correctly from an unknown initial position by using a sequence of actions
with no sensing at all. Sometimes a sensorless plan is better even when a conditional plan
with sensing is available. For example, doctors often prescribe a broad-spectrum antibiotic
rather than using the conditional plan of doing a blood test, then waiting for the results to
come back, and then prescribing a more speciﬁc antibiotic. The sensorless plan saves time
and money, and avoids the risk of the infection worsening before the test results are available.
Consider a sensorless version of the (deterministic) vacuum world. Assume that the agent
knows the geography of its world, but not its own location or the distribution of dirt. In that
case, its initial belief state is {1,2,3,4,5,6,7,8} (see Figure 4.9). Now, if the agent moves
Right it will be in one of the states {2,4,6,8}—the agent has gained information without
perceiving anything! After [Right,Suck] the agent will always end up in one of the states
{4,8}. Finally, after [Right,Suck,Left,Suck] the agent is guaranteed to reach the goal state 7,
no matter what the start state. We say that the agent can coerce the world into state 7.
Coercion

## Page 145
