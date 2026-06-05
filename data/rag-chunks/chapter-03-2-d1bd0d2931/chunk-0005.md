---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0005"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

3.3.4 Measuring problem-solving performance
• We can evaluate an algorithm’s performance in four ways:
• Completeness: 
• Is the algorithm guaranteed to find a solution when there is one, 
• and to correctly report failure when there is not? 
• Cost optimality: 
• Does it find a solution with the lowest path cost of all solutions?
• Time complexity: 
• How long does it take to find a solution? 
• This can be measured in seconds, 
• or more abstractly by the number of states and actions considered.
• Space complexity: 
• How much memory is needed to perform the search?
• maximum number of nodes in memory 
27

## Page 26

• When the graph is an explicit data, such as the map of Romania,
• the typical measure is the size of the state-space graph, |V|+|E|, where |V| 
is the number of vertices (state nodes) of the graph and |E| is the number of 
edges
• But in many AI problems, the graph is represented only implicitly by 
the initial state, actions, and transition model. 
• For an implicit state space, complexity can be measured in terms 
of:
• d, the depth or number of actions/steps in an optimal solution; 
• m, the maximum number of actions in any path; 
• and b, the branching factor or number of successors of a node that need to be 
considered.
28
… Measuring problem-solving performance
Total cost = path cost + search cost

## Page 27

• An uninformed search algorithm is given no clue about how 
close a state is to the goal(s).
• For example, consider our agent in Arad with the goal of 
reaching Bucharest:
• An uninformed agent with no knowledge of Romanian geography has 
no clue whether going to Zerind or Sibiu is a better first step. 
• In contrast, an informed agent (Section 3.5) who knows the location 
of each city knows that Sibiu is much closer to Bucharest and thus 
more likely to be on the shortest path.
29

## Page 28

30
Uninformed Search Strategies
Uninformed strategies use only the information available in
the problem definition
• Breadth-first search (BFS)
• Uniform-cost search (UCS)
• Depth-first search 
(DFS)
• Depth-limited search (DLS)
• Iterative deepening search

## Page 29

3.4.1 Breadth-first search
31

## Page 30

32
… Breadth-first search

## Page 31

Breadth-First Search
S
a
b
d
p
a
c
e
p
h
f
r
q
q
c
G
a
q
e
p
h
f
r
q
q
c
G
a
S
G
d
b
p
q
c
e
h
a
f
r
Search
Tiers
Strategy: expand a 
shallowest node first
Implementation: Fringe 
is a FIFO queue
33

## Page 32
