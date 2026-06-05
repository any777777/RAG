---
chunk_id: "book-ca4fca8dd8-chunk-0621"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 621
confidence: "first-pass"
extraction_method: "structured-local"
---

376
Chapter 11
Automated Planning
Reﬁnement(Go(Home,SFO),
STEPS: [Drive(Home,SFOLongTermParking),
Shuttle(SFOLongTermParking,SFO)] )
Reﬁnement(Go(Home,SFO),
STEPS: [Taxi(Home,SFO)] )
Reﬁnement(Navigate([a,b],[x,y]),
PRECOND: a=x ∧b=y
STEPS: [] )
Reﬁnement(Navigate([a,b],[x,y]),
PRECOND:Connected([a,b],[a−1,b])
STEPS: [Left,Navigate([a−1,b],[x,y])] )
Reﬁnement(Navigate([a,b],[x,y]),
PRECOND:Connected([a,b],[a+1,b])
STEPS: [Right,Navigate([a+1,b],[x,y])] )
...
Figure 11.7 Deﬁnitions of possible reﬁnements for two high-level actions: going to San
Francisco airport and navigating in the vacuum world. In the latter case, note the recursive
nature of the reﬁnements and the use of preconditions.
can be shown that the right collection of HLAs can result in the time complexity of blind
search dropping from exponential in the solution depth to linear in the solution depth, al-
though devising such a collection of HLAs may be a nontrivial task in itself. When HLAs
have multiple possible implementations, there are two options: one is to search among the
implementations for one that works, as in Section 11.4.2; the other is to reason directly about
the HLAs—despite the multiplicity of implementations—as explained in Section 11.4.3. The
latter method enables the derivation of provably correct abstract plans, without the need to
consider their implementations.
11.4.2 Searching for primitive solutions
HTN planning is often formulated with a single “top level” action called Act, where the aim
is to ﬁnd an implementation of Act that achieves the goal. This approach is entirely general.
For example, classical planning problems can be deﬁned as follows: for each primitive action
ai, provide one reﬁnement of Act with steps [ai,Act]. That creates a recursive deﬁnition of Act
that lets us add actions. But we need some way to stop the recursion; we do that by providing
one more reﬁnement for Act, one with an empty list of steps and with a precondition equal
to the goal of the problem. This says that if the goal is already achieved, then the right
implementation is to do nothing.
The approach leads to a simple algorithm: repeatedly choose an HLA in the current plan
and replace it with one of its reﬁnements, until the plan achieves the goal. One possible im-
plementation based on breadth-ﬁrst tree search is shown in Figure 11.8. Plans are considered
in order of depth of nesting of the reﬁnements, rather than number of primitive steps. It is
straightforward to design a graph-search version of the algorithm as well as depth-ﬁrst and
iterative deepening versions.
