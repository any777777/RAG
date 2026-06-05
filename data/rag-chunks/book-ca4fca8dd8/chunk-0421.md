---
chunk_id: "book-ca4fca8dd8-chunk-0421"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 421
confidence: "first-pass"
extraction_method: "structured-local"
---

258
Chapter 7
Logical Agents
either the action at time t causes F to be true at t +1, or F was already true at time t and the
action at time t does not cause it to be false. An axiom of this form is called a successor-state
axiom and has this form:
Successor-state
axiom
Ft+1 ⇔ActionCausesFt ∨(Ft ∧¬ActionCausesNotFt).
One of the simplest successor-state axioms is the one for HaveArrow. Because there is no
action for reloading, the ActionCausesFt part goes away and we are left with
HaveArrowt+1 ⇔(HaveArrowt ∧¬Shoott).
(7.2)
For the agent’s location, the successor-state axioms are more elaborate. For example, Lt+1
1,1
is true if either (a) the agent moved Forward from [1,2] when facing south, or from [2,1]
when facing west; or (b) Lt
1,1 was already true and the action did not cause movement (either
because the action was not Forward or because the action bumped into a wall). Written out
in propositional logic, this becomes
Lt+1
1,1
⇔
(Lt
1,1 ∧(¬Forwardt ∨Bumpt+1))
∨(Lt
1,2 ∧(FacingSoutht ∧Forwardt))
(7.3)
∨(Lt
2,1 ∧(FacingWestt ∧Forwardt)).
Exercise 7.SSAX asks you to write out axioms for the remaining wumpus world ﬂuents.
Given a complete set of successor-state axioms and the other axioms listed at the begin-
ning of this section, the agent will be able to ASK and answer any answerable question about
the current state of the world. For example, in Section 7.2 the initial sequence of percepts and
actions is
¬Stench0 ∧¬Breeze0 ∧¬Glitter0 ∧¬Bump0 ∧¬Scream0 ; Forward0
¬Stench1 ∧Breeze1 ∧¬Glitter1 ∧¬Bump1 ∧¬Scream1 ; TurnRight1
¬Stench2 ∧Breeze2 ∧¬Glitter2 ∧¬Bump2 ∧¬Scream2 ; TurnRight2
¬Stench3 ∧Breeze3 ∧¬Glitter3 ∧¬Bump3 ∧¬Scream3 ; Forward3
¬Stench4 ∧¬Breeze4 ∧¬Glitter4 ∧¬Bump4 ∧¬Scream4 ; TurnRight4
¬Stench5 ∧¬Breeze5 ∧¬Glitter5 ∧¬Bump5 ∧¬Scream5 ; Forward5
Stench6 ∧¬Breeze6 ∧¬Glitter6 ∧¬Bump6 ∧¬Scream6
At this point, we have ASK(KB,L6
1,2)=true, so the agent knows where it is. Moreover,
ASK(KB,W1,3)=true and ASK(KB,P3,1)=true, so the agent has found the wumpus and one
of the pits. The most important question for the agent is whether a square is OK to move
into—that is, whether the square is free of a pit or live wumpus. It’s convenient to add
axioms for this, having the form
OKt
x,y ⇔¬Px,y ∧¬(Wx,y ∧WumpusAlivet).
Finally, ASK(KB,OK6
2,2)=true, so the square [2,2] is OK to move into. In fact, given a
sound and complete inference algorithm such as DPLL, the agent can answer any answerable
question about which squares are OK—and can do so in just a few milliseconds for small-to-
medium wumpus worlds.
Solving the representational and inferential frame problems is a big step forward, but a
pernicious problem remains: we need to conﬁrm that all the necessary preconditions of an
action hold for it to have its intended effect. We said that the Forward action moves the agent
