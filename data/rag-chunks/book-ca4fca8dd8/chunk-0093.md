---
chunk_id: "book-ca4fca8dd8-chunk-0093"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 93
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 56

56
Chapter 2
Intelligent Agents
A
B
Figure 2.2 A vacuum-cleaner world with just two locations. Each location can be clean or
dirty, and the agent can move left or right and can clean the square that it occupies. Different
versions of the vacuum world allow for different rules about what the agent can perceive,
whether its actions always succeed, and so on.
Percept sequence
Action
[A,Clean]
Right
[A,Dirty]
Suck
[B,Clean]
Left
[B,Dirty]
Suck
[A,Clean], [A,Clean]
Right
[A,Clean], [A,Dirty]
Suck
...
...
[A,Clean], [A,Clean], [A,Clean]
Right
[A,Clean], [A,Clean], [A,Dirty]
Suck
...
...
Figure 2.3 Partial tabulation of a simple agent function for the vacuum-cleaner world shown
in Figure 2.2. The agent cleans the current square if it is dirty, otherwise it moves to the other
square. Note that the table is of unbounded size unless there is a restriction on the length of
possible percept sequences.
Before closing this section, we should emphasize that the notion of an agent is meant to
be a tool for analyzing systems, not an absolute characterization that divides the world into
agents and non-agents. One could view a hand-held calculator as an agent that chooses the
action of displaying “4” when given the percept sequence “2 + 2 =,” but such an analysis
would hardly aid our understanding of the calculator. In a sense, all areas of engineering can
be seen as designing artifacts that interact with the world; AI operates at (what the authors
consider to be) the most interesting end of the spectrum, where the artifacts have signiﬁcant
computational resources and the task environment requires nontrivial decision making.

## Page 57
