---
chunk_id: "book-ca4fca8dd8-chunk-0427"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 427
confidence: "first-pass"
extraction_method: "structured-local"
---

262
Chapter 7
Logical Agents
function SATPLAN(init, transition, goal, T max) returns solution or failure
inputs: init, transition, goal, constitute a description of the problem
T max, an upper limit for plan length
for t = 0 to T max do
cnf ←TRANSLATE-TO-SAT(init, transition, goal,t)
model←SAT-SOLVER(cnf)
if model is not null then
return EXTRACT-SOLUTION(model)
return failure
Figure 7.22 The SATPLAN algorithm. The planning problem is translated into a CNF sen-
tence in which the goal is asserted to hold at a ﬁxed time step t and axioms are included for
each time step up to t. If the satisﬁability algorithm ﬁnds a model, then a plan is extracted by
looking at those proposition symbols that refer to actions and are assigned true in the model.
If no model exists, then the process is repeated with the goal moved one step later.
7.7.4 Making plans by propositional inference
The agent in Figure 7.20 uses logical inference to determine which squares are safe, but uses
A∗search to make plans. In this section, we show how to make plans by logical inference.
The basic idea is very simple:
1. Construct a sentence that includes
(a) Init0, a collection of assertions about the initial state;
(b) Transition1,...,Transitiont, the successor-state axioms for all possible actions at
each time up to some maximum time t;
(c) the assertion that the goal is achieved at time t: HaveGoldt ∧ClimbedOutt.
2. Present the whole sentence to a SAT solver. If the solver ﬁnds a satisfying model, then
the goal is achievable; if the sentence is unsatisﬁable, then the problem is unsolvable.
3. Assuming a model is found, extract from the model those variables that represent ac-
tions and are assigned true. Together they represent a plan to achieve the goals.
A propositional planning procedure, SATPLAN, is shown in Figure 7.22. It implements the
basic idea just given, with one twist. Because the agent does not know how many steps it
will take to reach the goal, the algorithm tries each possible number of steps t, up to some
maximum conceivable plan length Tmax. In this way, it is guaranteed to ﬁnd the shortest plan
if one exists. Because of the way SATPLAN searches for a solution, this approach cannot
be used in a partially observable environment; SATPLAN would just set the unobservable
variables to the values it needs to create a solution.
The key step in using SATPLAN is the construction of the knowledge base. It might
seem, on casual inspection, that the wumpus world axioms in Section 7.7.1 sufﬁce for steps
1(a) and 1(b) above. There is, however, a signiﬁcant difference between the requirements for
entailment (as tested by ASK) and those for satisﬁability.
Consider, for example, the agent’s location, initially [1,1], and suppose the agent’s unam-
bitious goal is to be in [2,1] at time 1. The initial knowledge base contains L0
1,1 and the goal
is L1
2,1. Using ASK, we can prove L1
2,1 if Forward0 is asserted, and, reassuringly, we cannot
