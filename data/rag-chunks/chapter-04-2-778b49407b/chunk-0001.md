---
chunk_id: "chapter-04-2-778b49407b-chunk-0001"
source_id: "chapter-04-2-778b49407b"
source_file: "New folder/Chapter 04 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Slide 1

Artificial intelligence

## Slide 2

Introduction

We begin with the problem of finding a good state without worrying about the path to get there, 
covering both discrete (Section 4.1) and continuous (Section 4.2) states. 
Then we relax the assumptions of determinism (Section 4.3) and observability (Section 4.4). 
Finally, Section 4.5 guides the agent through an unknown space that it must learn as it goes, using online search.

2

## Slide 3

For many important applications we care only about the final state, not the path to get there:
integrated-circuit design
factory floor layout
job shop scheduling
telecommunications network optimization
crop planning
portfolio management

3

## Slide 4

… Local Search and Optimization Problems

Local search algorithms operate by searching from a start state to neighboring states, 
without keeping track of the paths, 
nor the set of states that have been reached. 
That means they are not systematic—
they might never explore a portion of the search space where a solution actually resides. 
However, they have two key advantages: 
(1) they use very little memory; 
(2) they can often find reasonable solutions in large or infinite state spaces 
for which systematic algorithms are unsuitable.
Local search algorithms can also solve optimization problems, 
in which the aim is to find the best state according to an objective function.

4

## Slide 5

5

… Local Search and Optimization Problems

state-space
landscape

## Slide 6

If elevation corresponds to an objective function, then the aim is to find the highest peak—a global maximum—
and we call the process hill climbing. 
If elevation corresponds to cost, then the aim is to find the lowest valley—a global minimum—
and we call it gradient descent.

6

… Local Search and Optimization Problems

## Slide 7

4.1.1 Hill-climbing search

7

heads in the direction that
provides the steepest ascent

Hill-climbing algorithms typically choose randomly among the set of best successors if there is more than one

## Slide 8

8

… Hill-climbing search

## Slide 9
