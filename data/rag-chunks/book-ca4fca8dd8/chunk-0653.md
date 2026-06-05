---
chunk_id: "book-ca4fca8dd8-chunk-0653"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 653
confidence: "first-pass"
extraction_method: "structured-local"
---

394
Chapter 11
Automated Planning
are consumed as wheels are added to the car, whereas the other resources are “borrowed” at
the start of an action and released at the action’s end.
The representation of resources as numerical quantities, such as Inspectors(2), rather
than as named entities, such as Inspector(I1) and Inspector(I2), is an example of a technique
called aggregation: grouping individual objects into quantities when the objects are all in-
Aggregation
distinguishable. In our assembly problem, it does not matter which inspector inspects the car,
so there is no need to make the distinction. Aggregation is essential for reducing complexity.
Consider what happens when a proposed schedule has 10 concurrent Inspect actions but only
9 inspectors are available. With inspectors represented as quantities, a failure is detected im-
mediately and the algorithm backtracks to try another schedule. With inspectors represented
as individuals, the algorithm would try all 9! ways of assigning inspectors to actions before
noticing that none of them work.
11.6.2 Solving scheduling problems
We begin by considering just the temporal scheduling problem, ignoring resource constraints.
To minimize makespan (plan duration), we must ﬁnd the earliest start times for all the actions
consistent with the ordering constraints supplied with the problem. It is helpful to view these
ordering constraints as a directed graph relating the actions, as shown in Figure 11.14. We can
apply the critical path method (CPM) to this graph to determine the possible start and end
Critical path method
times of each action. A path through a graph representing a partial-order plan is a linearly
ordered sequence of actions beginning with Start and ending with Finish. (For example, there
are two paths in the partial-order plan in Figure 11.14.)
The critical path is that path whose total duration is longest; the path is “critical” because
Critical path
it determines the duration of the entire plan—shortening other paths doesn’t shorten the plan
as a whole, but delaying the start of any action on the critical path slows down the whole plan.
Actions that are off the critical path have a window of time in which they can be executed.
The window is speciﬁed in terms of an earliest possible start time, ES, and a latest possible
start time, LS. The quantity LS – ES is known as the slack of an action. We can see in
Slack
Figure 11.14 that the whole plan will take 85 minutes, that each action in the top job has
15 minutes of slack, and that each action on the critical path has no slack (by deﬁnition).
Together the ES and LS times for all the actions constitute a schedule for the problem.
Schedule
The following formulas deﬁne ES and LS and constitute a dynamic-programming algo-
rithm to compute them. A and B are actions, and A≺B means that A precedes B:
ES(Start) = 0
ES(B) = maxA≺B ES(A)+Duration(A)
LS(Finish) = ES(Finish)
LS(A) = minB≻A LS(B)−Duration(A).
The idea is that we start by assigning ES(Start) to be 0. Then, as soon as we get an action
B such that all the actions that come immediately before B have ES values assigned, we
set ES(B) to be the maximum of the earliest ﬁnish times of those immediately preceding
actions, where the earliest ﬁnish time of an action is deﬁned as the earliest start time plus
the duration. This process repeats until every action has been assigned an ES value. The LS
values are computed in a similar manner, working backward from the Finish action.
The complexity of the critical path algorithm is just O(Nb), where N is the number of
actions and b is the maximum branching factor into or out of an action. (To see this, note
