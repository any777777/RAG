---
chunk_id: "book-ca4fca8dd8-chunk-0603"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 603
confidence: "first-pass"
extraction_method: "structured-local"
---

366
Chapter 11
Automated Planning
We use On(b,x) to indicate that block b is on x, where x is either another block or the
table. The action for moving block b from the top of x to the top of y will be Move(b,x,y).
Now, one of the preconditions on moving b is that no other block be on it. In ﬁrst-order logic,
this would be ¬∃x On(x,b) or, alternatively, ∀x ¬On(x,b). Basic PDDL does not allow
quantiﬁers, so instead we introduce a predicate Clear(x) that is true when nothing is on x.
(The complete problem description is in Figure 11.4.)
The action Move moves a block b from x to y if both b and y are clear. After the move is
made, b is still clear but y is not. A ﬁrst attempt at the Move schema is
Action(Move(b,x,y),
PRECOND:On(b,x)∧Clear(b)∧Clear(y),
EFFECT:On(b,y)∧Clear(x)∧¬On(b,x)∧¬Clear(y)).
Unfortunately, this does not maintain Clear properly when x or y is the table. When x is
the Table, this action has the effect Clear(Table), but the table should not become clear; and
when y=Table, it has the precondition Clear(Table), but the table does not have to be clear
for us to move a block onto it. To ﬁx this, we do two things. First, we introduce another
action to move a block b from x to the table:
Action(MoveToTable(b,x),
PRECOND:On(b,x)∧Clear(b),
EFFECT:On(b,Table)∧Clear(x)∧¬On(b,x)).
Second, we take the interpretation of Clear(x) to be “there is a clear space on x to hold a
block.” Under this interpretation, Clear(Table) will always be true. The only problem is that
nothing prevents the planner from using Move(b,x,Table) instead of MoveToTable(b,x). We
could live with this problem—it will lead to a larger-than-necessary search space, but will
not lead to incorrect answers—or we could introduce the predicate Block and add Block(b)∧
Block(y) to the precondition of Move, as shown in Figure 11.4.
11.2 Algorithms for Classical Planning
The description of a planning problem provides an obvious way to search from the initial
state through the space of states, looking for a goal. A nice advantage of the declarative
representation of action schemas is that we can also search backward from the goal, looking
for the initial state (Figure 11.5 compares forward and backward searches). A third possibility
is to translate the problem description into a set of logic sentences, to which we can apply a
logical inference algorithm to ﬁnd a solution.
11.2.1 Forward state-space search for planning
We can solve planning problems by applying any of the heuristic search algorithms from
Chapter 3 or Chapter 4. The states in this search state space are ground states, where every
ﬂuent is either true or not. The goal is a state that has all the positive ﬂuents in the prob-
lem’s goal and none of the negative ﬂuents. The applicable actions in a state, Actions(s), are
grounded instantiations of the action schemas—that is, actions where the variables have all
been replaced by constant values.
To determine the applicable actions we unify the current state against the preconditions
of each action schema. For each uniﬁcation that successfully results in a substitution, we
