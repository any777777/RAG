---
chunk_id: "book-ca4fca8dd8-chunk-0141"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 141
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.1
Problem-Solving Agents
83
3.1.1 Search problems and solutions
A search problem can be deﬁned formally as follows:
Problem
• A set of possible states that the environment can be in. We call this the state space.
States
State space
• The initial state that the agent starts in. For example: Arad.
Initial state
• A set of one or more goal states. Sometimes there is one goal state (e.g., Bucharest),
Goal states
sometimes there is a small set of alternative goal states, and sometimes the goal is
deﬁned by a property that applies to many states (potentially an inﬁnite number). For
example, in a vacuum-cleaner world, the goal might be to have no dirt in any location,
regardless of any other facts about the state. We can account for all three of these
possibilities by specifying an IS-GOAL method for a problem. In this chapter we will
sometimes say “the goal” for simplicity, but what we say also applies to “any one of the
possible goal states.”
• The actions available to the agent. Given a state s, ACTIONS(s) returns a ﬁnite2 set of
Action
actions that can be executed in s. We say that each of these actions is applicable in s.
Applicable
An example:
ACTIONS(Arad) = {ToSibiu,ToTimisoara,ToZerind}.
• A transition model, which describes what each action does. RESULT(s,a) returns the
Transition model
state that results from doing action a in state s. For example,
RESULT(Arad,ToZerind) = Zerind.
• An action cost function, denoted by ACTION-COST(s,a,s′) when we are programming
Action cost function
or c(s,a,s′) when we are doing math, that gives the numeric cost of applying action a
in state s to reach state s′. A problem-solving agent should use a cost function that
reﬂects its own performance measure; for example, for route-ﬁnding agents, the cost of
an action might be the length in miles (as seen in Figure 3.1), or it might be the time it
takes to complete the action.
A sequence of actions forms a path, and a solution is a path from the initial state to a goal
Path
state. We assume that action costs are additive; that is, the total cost of a path is the sum of the
individual action costs. An optimal solution has the lowest path cost among all solutions. In
Optimal solution
this chapter, we assume that all action costs will be positive, to avoid certain complications.3
The state space can be represented as a graph in which the vertices are states and the
Graph
directed edges between them are actions. The map of Romania shown in Figure 3.1 is such a
graph, where each road indicates two actions, one in each direction.
2
For problems with an inﬁnite number of actions we would need techniques that go beyond this chapter.
3
In any problem with a cycle of net negative cost, the cost-optimal solution is to go around that cycle an inﬁnite
number of times. The Bellman–Ford and Floyd–Warshall algorithms (not covered here) handle negative-cost
actions, as long as there are no negative cycles. It is easy to accommodate zero-cost actions, as long as the
number of consecutive zero-cost actions is bounded. For example, we might have a robot where there is a cost
to move, but zero cost to rotate 90o; the algorithms in this chapter can handle this as long as no more than three
consecutive 90o turns are allowed. There is also a complication with problems that have an inﬁnite number of
arbitrarily small action costs. Consider a version of Zeno’s paradox where there is an action to move half way to
the goal, at a cost of half of the previous move. This problem has no solution with a ﬁnite number of actions, but
to prevent a search from taking an unbounded number of actions without quite reaching the goal, we can require
that all action costs be at least ϵ, for some small positive value ϵ.
