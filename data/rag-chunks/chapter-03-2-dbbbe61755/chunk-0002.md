---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0002"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

A search problem can be defined formally by the following components as follows:
A set of possible states that the environment can be in. 
We call this the state space.
The initial state that the agent starts in. 
For example: Arad.
A set of one or more goal states.
The actions available to the agent.
ACTIONS(Arad) = {ToSibiu, ToTimisoara, ToZerind}
A transition model: which describes what each action does. 
RESULT(s, a) returns the state that results from doing action a in state s.
RESULT(Arad, ToZerind) = Zerind
An action cost function, denoted by ACTION-COST(s, a, s’)
e.g., the length in miles or the time it takes to complete the action

7

## Slide 8

A sequence of actions forms a path, 
and a solution is a path from the initial state to a goal state. 
We assume that action costs are additive; 
that is, the total cost of a path is the sum of the individual action costs. 
An optimal solution has the lowest path cost among all solutions. 
The state space can be represented as a graph 
in which the vertices are states 
and the directed edges between them are actions.

8

… Search problems and solutions

## Slide 9

In a fully observable, deterministic, known environment, the solution to any problem is a fixed sequence of actions: 
drive to Sibiu, then Fagaras, then Bucharest.
If the model is correct, then once the agent has found a solution, it can ignore its percepts while it is executing the actions
Control theorists call this an open-loop system: ignoring the percepts breaks the loop between agent and environment. 
If there is a chance that the model is incorrect, or the environment is nondeterministic, then the agent would be safer using a closed-loop approach that monitors the percepts (see Section 4.4).

9

… Problem-Solving Agents

## Slide 10

3.1.2 Formulating problems

Our formulation of the problem of getting to Bucharest is a model—
an abstract mathematical description—and not the real thing.
The process of removing detail from a representation is called abstraction. 
A good problem formulation has the right level of detail.
Can we be more precise about the appropriate level of abstraction?
For example, we could drive with the radio on between Sibiu and Rimnicu Vilcea, and then switch it off for the rest of the trip.

10
