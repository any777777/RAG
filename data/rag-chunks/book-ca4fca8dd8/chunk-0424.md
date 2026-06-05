---
chunk_id: "book-ca4fca8dd8-chunk-0424"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 424
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 260

260
Chapter 7
Logical Agents
function HYBRID-WUMPUS-AGENT(percept) returns an action
inputs: percept, a list, [stench,breeze,glitter,bump,scream]
persistent: KB, a knowledge base, initially the atemporal “wumpus physics”
t, a counter, initially 0, indicating time
plan, an action sequence, initially empty
TELL(KB, MAKE-PERCEPT-SENTENCE(percept,t))
TELL the KB the temporal “physics” sentences for time t
safe←{[x,y] : ASK(KB,OKt
x,y) = true}
if ASK(KB,Glittert) = true then
plan←[Grab] + PLAN-ROUTE(current,{[1,1]},safe) + [Climb]
if plan is empty then
unvisited←{[x,y] : ASK(KB,Lt′
x,y) = false for all t′ ≤t}
plan←PLAN-ROUTE(current,unvisited∩safe,safe)
if plan is empty and ASK(KB,HaveArrowt) = true then
possible wumpus←{[x,y] : ASK(KB,¬ Wx,y) = false}
plan←PLAN-SHOT(current,possible wumpus,safe)
if plan is empty then
// no choice but to take a risk
not unsafe←{[x,y] : ASK(KB,¬ OKt
x,y) = false}
plan←PLAN-ROUTE(current,unvisited∩not unsafe,safe)
if plan is empty then
plan←PLAN-ROUTE(current,{[1,1]},safe) + [Climb]
action←POP(plan)
TELL(KB, MAKE-ACTION-SENTENCE(action,t))
t←t + 1
return action
function PLAN-ROUTE(current,goals,allowed) returns an action sequence
inputs: current, the agent’s current position
goals, a set of squares; try to plan a route to one of them
allowed, a set of squares that can form part of the route
problem←ROUTE-PROBLEM(current,goals,allowed)
return SEARCH(problem)
// Any search algorithm from Chapter 3
Figure 7.20 A hybrid agent program for the wumpus world. It uses a propositional knowl-
edge base to infer the state of the world, and a combination of problem-solving search and
domain-speciﬁc code to choose actions. Each time HYBRID-WUMPUS-AGENT is called, it
adds the percept to the knowledge base, and then either relies on a previously-deﬁned plan or
creates a new plan, and pops off the ﬁrst step of the plan as the action to do next.
of the world.13 The process of updating the belief state as new percepts arrive is called state
estimation (see page 150). Whereas in Section 4.4 the belief state was an explicit list of
states, here we can use a logical sentence involving the proposition symbols associated with
the current time step, as well as the atemporal symbols. For example, the logical sentence
WumpusAlive1 ∧L1
2,1 ∧B2,1 ∧(P3,1 ∨P2,2)
(7.4)
13 We can think of the percept history itself as a representation of the belief state, but one that makes inference
increasingly expensive as the history gets longer.

## Page 261
