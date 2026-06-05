---
chunk_id: "book-ca4fca8dd8-chunk-0249"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 249
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 154

154
Chapter 4
Search in Complex Environments
G
S
1
2
3
1
2
3
Figure 4.19 A simple maze problem. The agent starts at S and must reach G but knows
nothing of the environment.
S
G
S
G
A
A
S
G
(a)
(b)
Figure 4.20 (a) Two state spaces that might lead an online search agent into a dead end.
Any given agent will fail in at least one of these spaces. (b) A two-dimensional environment
that can cause an online search agent to follow an arbitrarily inefﬁcient route to the goal.
Whichever choice the agent makes, the adversary blocks that route with another long, thin
wall, so that the path followed is much longer than the best possible path.
is no way it could know how to choose the correct action in both state spaces. This is an
example of an adversary argument—we can imagine an adversary constructing the state
Adversary argument
space while the agent explores it and putting the goals and dead ends wherever it chooses, as
in Figure 4.20(b).
Dead ends are a real difﬁculty for robot exploration—staircases, ramps, cliffs, one-way
streets, and even natural terrain all present states from which some actions are irreversible—
Irreversible action
there is no way to return to the previous state. The exploration algorithm we will present is
only guaranteed to work in state spaces that are safely explorable—that is, some goal state
Safely explorable
is reachable from every reachable state. State spaces with only reversible actions, such as

## Page 155
