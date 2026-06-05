---
chunk_id: "book-ca4fca8dd8-chunk-0617"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 617
confidence: "first-pass"
extraction_method: "structured-local"
---

374
Chapter 11
Automated Planning
A key idea in deﬁning heuristics is decomposition: dividing a problem into parts, solving
Decomposition
each part independently, and then combining the parts. The subgoal independence assump-
Subgoal
independence
tion is that the cost of solving a conjunction of subgoals is approximated by the sum of
the costs of solving each subgoal independently. The subgoal independence assumption can
be optimistic or pessimistic. It is optimistic when there are negative interactions between
the subplans for each subgoal—for example, when an action in one subplan deletes a goal
achieved by another subplan. It is pessimistic, and therefore inadmissible, when subplans
contain redundant actions—for instance, two actions that could be replaced by a single action
in the merged plan.
Suppose the goal is a set of ﬂuents G, which we divide into disjoint subsets G1,...,Gn.
We then ﬁnd optimal plans P1,...,Pn that solve the respective subgoals. What is an estimate
of the cost of the plan for achieving all of G? We can think of each COST(Pi) as a heuristic
estimate, and we know that if we combine estimates by taking their maximum value, we
always get an admissible heuristic. So maxi COST(Pi) is admissible, and sometimes it is
exactly correct: it could be that P1 serendipitously achieves all the Gi. But usually the estimate
is too low. Could we sum the costs instead? For many problems that is a reasonable estimate,
but it is not admissible. The best case is when Gi and G j are independent, in the sense
that plans for one cannot reduce the cost of plans for the other. In that case, the estimate
COST(Pi)+ COST(Pj) is admissible, and more accurate than the max estimate.
It is clear that there is great potential for cutting down the search space by forming ab-
stractions. The trick is choosing the right abstractions and using them in a way that makes
the total cost—deﬁning an abstraction, doing an abstract search, and mapping the abstraction
back to the original problem—less than the cost of solving the original problem. The tech-
niques of pattern databases from Section 3.6.3 can be useful, because the cost of creating
the pattern database can be amortized over multiple problem instances.
A system that makes use of effective heuristics is FF, or FASTFORWARD (Hoffmann,
2005), a forward state-space searcher that uses the ignore-delete-lists heuristic, estimating
the heuristic with the help of a planning graph. FF then uses hill climbing search (modiﬁed
to keep track of the plan) with the heuristic to ﬁnd a solution. FF’s hill climbing algorithm is
nonstandard: it avoids local maxima by running a breadth-ﬁrst search from the current state
until a better one is found. If this fails, FF switches to a greedy best-ﬁrst search instead.
11.4 Hierarchical Planning
The problem-solving and planning methods of the preceding chapters all operate with a ﬁxed
set of atomic actions. Actions can be strung together, and state-of-the-art algorithms can
generate solutions containing thousands of actions. That’s ﬁne if we are planning a vacation
and the actions are at the level of “ﬂy from San Francisco to Honolulu,” but at the motor-
control level of “bend the left knee by 5 degrees” we would need to string together millions
or billions of actions, not thousands.
Bridging this gap requires planning at higher levels of abstraction. A high-level plan for
a Hawaii vacation might be “Go to San Francisco airport; take ﬂight HA 11 to Honolulu;
do vacation stuff for two weeks; take HA 12 back to San Francisco; go home.” Given such
a plan, the action “Go to San Francisco airport” can be viewed as a planning task in itself,
with a solution such as “Choose a ride-hailing service; order a car; ride to airport.” Each of
