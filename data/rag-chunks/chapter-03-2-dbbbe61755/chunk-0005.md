---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0005"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

A VLSI layout problem requires positioning millions of components and connections on a chip to minimize area, minimize circuit delays, minimize lost capacitances, and maximize manufacturing yield. 
Robot navigation is a generalization of the route-finding problem. 
Automatic assembly sequencing of complex objects (such as electric motors) by a robot has been standard industry practice since the 1970s.

23

… Real-world problems

## Slide 24

A search algorithm takes a search problem as input and returns a solution, 
or an indication of failure. 
In this chapter we consider algorithms that superimpose a search tree: 
forming various paths from the initial state, 
trying to find a path that reaches a goal state. 
Each node in the search tree corresponds to a state in the state space 
and the edges in the search tree correspond to actions. 
The root of the tree corresponds to the initial state of the problem.

24

## Slide 25

… Search Algorithms

25

## Slide 26

… Search Algorithms

26

## Slide 27

3.3.4 Measuring problem-solving performance

We can evaluate an algorithm’s performance in four ways:
Completeness: 
Is the algorithm guaranteed to find a solution when there is one, 
and to correctly report failure when there is not? 
Cost optimality: 
Does it find a solution with the lowest path cost of all solutions?
Time complexity: 
How long does it take to find a solution? 
This can be measured in seconds, 
or more abstractly by the number of states and actions considered.
Space complexity: 
How much memory is needed to perform the search?
maximum number of nodes in memory

27

## Slide 28

When the graph is an explicit data, such as the map of Romania,
the typical measure is the size of the state-space graph, |V|+|E|, where |V| is the number of vertices (state nodes) of the graph and |E| is the number of edges
But in many AI problems, the graph is represented only implicitly by the initial state, actions, and transition model. 
For an implicit state space, complexity can be measured in terms of:
d, the depth or number of actions/steps in an optimal solution; 
m, the maximum number of actions in any path; 
and b, the branching factor or number of successors of a node that need to be considered.

28

… Measuring problem-solving performance

Total cost = path cost + search cost

## Slide 29
