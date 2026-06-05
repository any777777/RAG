---
chunk_id: "chapter-04-2-778b49407b-chunk-0005"
source_id: "chapter-04-2-778b49407b"
source_file: "New folder/Chapter 04 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

Offline search – computing a complete solution before acting and then execute it.

Online search – interleaving computation and action 
Take an action, observe the environment, then compute the next action
Solving an exploration problem where the states and actions are unknown to the agent
Good for domains where there is a penalty for computing too long, or for stochastic domains
An example: A robot is placed in a new building and must explore it to build a map that it can use for getting from A to B

28

## Slide 29

4.5.1 Online search problems

29

## Slide 30

The cost is the total path cost that the agent incurs as it travels. 
It is common to compare this cost with the path cost the agent would incur if it knew the search space in advance—
that is, the optimal path in the known environment.
In the language of online algorithms, this comparison is called the competitive ratio; 
Competitive ratio: the true path cost over the path cost if it knew the search space in advance.
The best achievable competitive ratio can be 1
we would like it to be as small as possible.
Online explorers are vulnerable to dead ends: 
states from which no goal state is reachable.

Dead ends are a real difficulty for robot exploration—
some actions are irreversible—there is no way to return to the previous state.

30

… Online search problems

## Slide 31

31

… Online search problems

## Slide 32

4.5.2 Online search agents

32

It can expand only a node that it physically occupies, so it should expand nodes in a local order
Online Depth-First Search
Backtracking requires that actions are reversible – because the
agent has to backtrack physically.

## Slide 33

4.5.3 Online local search

Hill-climbing search is already an online search algorithm 
but Instead of random restarts, one might consider using a random walk to explore the environment.
It keeps one current state in memory
It can get stuck in a local minimum
Random restart does not work here (Why?)
The agent cannot transport itself to a new state
A random walk simply selects at random one of the available actions from the current state; 
A random walk will eventually find a goal or complete its exploration, 
provided that the space is finite.
On the other hand, the process can be very slow.

33

## Slide 34

34

… Online local search

## Slide 35

35
