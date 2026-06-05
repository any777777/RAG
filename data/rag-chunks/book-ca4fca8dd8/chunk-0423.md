---
chunk_id: "book-ca4fca8dd8-chunk-0423"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 423
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.7
Agents Based on Propositional Logic
259
ahead unless there is a wall in the way, but there are many other unusual exceptions that could
cause the action to fail: the agent might trip and fall, be stricken with a heart attack, be carried
away by giant bats, etc. Specifying all these exceptions is called the qualiﬁcation problem.
Qualiﬁcation
problem
There is no complete solution within logic; system designers have to use good judgment in
deciding how detailed they want to be in specifying their model, and what details they want
to leave out. We will see in Chapter 12 that probability theory allows us to summarize all the
exceptions without explicitly naming them.
7.7.2 A hybrid agent
The ability to deduce various aspects of the state of the world can be combined fairly straight-
forwardly with condition–action rules (see Section 2.4.2) and with problem-solving algo-
rithms from Chapters 3 and 4 to produce a hybrid agent for the wumpus world. Figure 7.20
Hybrid agent
shows one possible way to do this. The agent program maintains and updates a knowledge
base as well as a current plan. The initial knowledge base contains the atemporal axioms—
those that don’t depend on t, such as the axiom relating the breeziness of squares to the
presence of pits. At each time step, the new percept sentence is added along with all the
axioms that depend on t, such as the successor-state axioms. (The next section explains why
the agent doesn’t need axioms for future time steps.) Then, the agent uses logical inference,
by ASKing questions of the knowledge base, to work out which squares are safe and which
have yet to be visited.
The main body of the agent program constructs a plan based on a decreasing priority of
goals. First, if there is a glitter, the program constructs a plan to grab the gold, follow a route
back to the initial location, and climb out of the cave. Otherwise, if there is no current plan,
the program plans a route to the closest safe square that it has not visited yet, making sure the
route goes through only safe squares.
Route planning is done with A∗search, not with ASK. If there are no safe squares to
explore, the next step—if the agent still has an arrow—is to try to make a safe square by
shooting at one of the possible wumpus locations. These are determined by asking where
ASK(KB,¬Wx,y) is false—that is, where it is not known that there is not a wumpus. The
function PLAN-SHOT (not shown) uses PLAN-ROUTE to plan a sequence of actions that will
line up this shot. If this fails, the program looks for a square to explore that is not provably
unsafe—that is, a square for which ASK(KB,¬OKt
x,y) returns false. If there is no such square,
then the mission is impossible and the agent retreats to [1,1] and climbs out of the cave.
7.7.3 Logical state estimation
The agent program in Figure 7.20 works quite well, but it has one major weakness: as time
goes by, the computational expense involved in the calls to ASK goes up and up. This happens
mainly because the required inferences have to go back further and further in time and involve
more and more proposition symbols. Obviously, this is unsustainable—we cannot have an
agent whose time to process each percept grows in proportion to the length of its life! What
we really need is a constant update time—that is, independent of t. The obvious answer is to
save, or cache, the results of inference, so that the inference process at the next time step can
Caching
build on the results of earlier steps instead of having to start again from scratch.
As we saw in Section 4.4, the history of percepts and all their ramiﬁcations can be re-
placed by the belief state—that is, some representation of the set of all possible current states
