---
chunk_id: "book-ca4fca8dd8-chunk-0140"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 140
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 82

82
Chapter 3
Solving Problems by Searching
Giurgiu
Urziceni
Hirsova
Eforie
Neamt
Oradea
Zerind
Arad
Timisoara
Lugoj
Mehadia
Drobeta
Craiova
Sibiu
Fagaras
Pitesti
Vaslui
Iasi
Rimnicu Vilcea
Bucharest
71
75
118
111
70
75
120
151
140
99
80
97
101
211
138
146
85
90
98
142
92
87
86
Figure 3.1 A simpliﬁed road map of part of Romania, with road distances in miles.
• Problem formulation: The agent devises a description of the states and actions nec-
Problem formulation
essary to reach the goal—an abstract model of the relevant part of the world. For our
agent, one good model is to consider the actions of traveling from one city to an adja-
cent city, and therefore the only fact about the state of the world that will change due to
an action is the current city.
• Search: Before taking any action in the real world, the agent simulates sequences of
Search
actions in its model, searching until it ﬁnds a sequence of actions that reaches the goal.
Such a sequence is called a solution. The agent might have to simulate multiple se-
Solution
quences that do not reach the goal, but eventually it will ﬁnd a solution (such as going
from Arad to Sibiu to Fagaras to Bucharest), or it will ﬁnd that no solution is possible.
• Execution: The agent can now execute the actions in the solution, one at a time.
Execution
It is an important property that in a fully observable, deterministic, known environment, the
▶
solution to any problem is a ﬁxed sequence of actions: drive to Sibiu, then Fagaras, then
Bucharest. If the model is correct, then once the agent has found a solution, it can ignore its
percepts while it is executing the actions—closing its eyes, so to speak—because the solution
is guaranteed to lead to the goal. Control theorists call this an open-loop system: ignoring the
Open-loop
percepts breaks the loop between agent and environment. If there is a chance that the model
is incorrect, or the environment is nondeterministic, then the agent would be safer using a
closed-loop approach that monitors the percepts (see Section 4.4).
Closed-loop
In partially observable or nondeterministic environments, a solution would be a branching
strategy that recommends different future actions depending on what percepts arrive. For
example, the agent might plan to drive from Arad to Sibiu but might need a contingency plan
in case it arrives in Zerind by accident or ﬁnds a sign saying “Drum ˆInchis” (Road Closed).

## Page 83
