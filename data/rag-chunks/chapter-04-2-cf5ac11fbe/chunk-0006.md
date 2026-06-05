---
chunk_id: "chapter-04-2-cf5ac11fbe-chunk-0006"
source_id: "chapter-04-2-cf5ac11fbe"
source_file: "Chapter 04 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 6
confidence: "first-pass"
extraction_method: "structured-local"
---

4.5.3 Online local search
• Hill-climbing search is already an online search algorithm 
• but Instead of random restarts, one might consider using a random walk to explore 
the environment.
• It keeps one current state in memory
• It can get stuck in a local minimum
• Random restart does not work here (Why?)
• The agent cannot transport itself to a new state
• A random walk simply selects at random one of the available actions from the current 
state; 
• A random walk will eventually find a goal or complete its exploration, 
• provided that the space is finite.
• On the other hand, the process can be very slow.
33

## Page 33

34
… Online local search

## Page 34

35
• Augmenting hill climbing with memory rather than randomness 
turns out to be a more effective approach. 
• The basic idea is to store a “current best estimate” H(s) of the 
cost to reach the goal from each state that has been visited. 
• H(s) starts out being just the heuristic estimate h(s) and is 
updated as the agent gains experience in the state space.
• This scheme is called learning real-time A∗(LRTA∗)
• Optimism under uncertainty encourages the agent to explore 
new, possibly promising paths.
… Online local search

## Page 35

36
… Online local search

## Page 36

37
… Online local search

## Page 37

The initial ignorance of online search agents provides several
opportunities for learning.
If we anticipate that we will be called upon to solve multiple similar 
problems in the future, then it makes sense to invest time (and
memory) to make those future searches easier.
There are several ways to do this, all falling under the heading of 
incremental search:
We could keep the search tree in memory and reuse the parts of it that are 
unchanged in the new problem.
We could keep the heuristic h values and update them as we gain new information—
either because the world has changed
or because we have computed a better estimate.
Or we could keep the best-path g values, using them to piece together a new 
solution, and updating them when the world changes.
38
4.5.4 Learning in online search
