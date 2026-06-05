---
chunk_id: "book-ca4fca8dd8-chunk-0240"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 240
confidence: "first-pass"
extraction_method: "structured-local"
---

146
Chapter 4
Search in Complex Environments
2 
4 
1 
3 
2 
4 
1 
3 
1 
3 
(b)
(a)
Figure 4.13 (a) Predicting the next belief state for the sensorless vacuum world with the
deterministic action, Right. (b) Prediction for the same belief state and action in the slippery
version of the sensorless vacuum world.
several values. (This gives rise to a new class of problems, which we explore in Exer-
cise 4.MVAL.) For now we assume that the cost of an action is the same in all states and
so can be transferred directly from the underlying physical problem.
Figure 4.14 shows the reachable belief-state space for the deterministic, sensorless vac-
uum world. There are only 12 reachable belief states out of 28 =256 possible belief states.
The preceding deﬁnitions enable the automatic construction of the belief-state problem
formulation from the deﬁnition of the underlying physical problem. Once this is done, we
can solve sensorless problems with any of the ordinary search algorithms of Chapter 3.
In ordinary graph search, newly reached states are tested to see if they were previously
reached. This works for belief states, too; for example, in Figure 4.14, the action sequence
[Suck,Left,Suck] starting at the initial state reaches the same belief state as [Right,Left,Suck],
namely, {5,7}. Now, consider the belief state reached by [Left], namely, {1,3,5,7}. Obvi-
ously, this is not identical to {5,7}, but it is a superset. We can discard (prune) any such
superset belief state. Why? Because a solution from {1,3,5,7} must be a solution for each
of the individual states 1, 3, 5, and 7, and thus it is a solution for any combination of these
individual states, such as {5,7}; therefore we don’t need to try to solve {1,3,5,7}, we can
concentrate on trying to solve the strictly easier belief state {5,7}.
Conversely, if {1,3,5,7} has already been generated and found to be solvable, then any
subset, such as {5,7}, is guaranteed to be solvable. (If I have a solution that works when I’m
very confused about what state I’m in, it will still work when I’m less confused.) This extra
level of pruning may dramatically improve the efﬁciency of sensorless problem solving.
Even with this improvement, however, sensorless problem-solving as we have described
it is seldom feasible in practice. One issue is the vastness of the belief-state space—we saw in
the previous chapter that often a search space of size N is too large, and now we have search
spaces of size 2N. Furthermore, each element of the search space is a set of up to N elements.
For large N, we won’t be able to represent even a single belief state without running out of
memory space.
One solution is to represent the belief state by some more compact description. In En-
glish, we could say the agent knows “Nothing” in the initial state; after moving Left, we could
