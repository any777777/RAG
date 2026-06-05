---
chunk_id: "book-ca4fca8dd8-chunk-0983"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 983
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.1
Properties of Multiagent Environments
593
Actors(A,B)
Init(At(A,LeftBaseline) ∧At(B,RightNet) ∧
Approaching(Ball,RightBaseline) ∧Partner(A,B) ∧Partner(B,A)
Goal(Returned(Ball) ∧(At(x,RightNet) ∨At(x,LeftNet))
Action(Hit(actor,Ball),
PRECOND:Approaching(Ball,loc) ∧At(actor,loc)
EFFECT:Returned(Ball))
Action(Go(actor,to),
PRECOND:At(actor,loc) ∧to ̸= loc,
EFFECT:At(actor,to) ∧¬ At(actor,loc))
Figure 17.1 The doubles tennis problem. Two actors, A and B, are playing together and can
be in one of four locations: LeftBaseline, RightBaseline, LeftNet, and RightNet. The ball can
be returned only if a player is in the right place. The NoOp action is a dummy, which has no
effect. Note that each action must include the actor as an argument.
We begin with the transition model; for the single-agent deterministic case, this is the
function RESULT(s,a), which gives the state that results from performing the action a when
the environment is in state s. In the single-agent setting, there might be b different choices for
the action; b can be quite large, especially for ﬁrst-order representations with many objects
to act on, but action schemas provide a concise representation nonetheless.
In the multiactor setting with n actors, the single action a is replaced by a joint action
Joint action
⟨a1,...,an⟩, where ai is the action taken by the ith actor. Immediately, we see two problems:
ﬁrst, we have to describe the transition model for bn different joint actions; second, we have
a joint planning problem with a branching factor of bn.
Having put the actors together into a multiactor system with a huge branching factor,
the principal focus of research on multiactor planning has been to decouple the actors to the
extent possible, so that (ideally) the complexity of the problem grows linearly with n rather
than exponentially with bn.
If the actors have no interaction with one another—for example, n actors each playing a
game of solitaire—then we can simply solve n separate problems. If the actors are loosely
coupled, can we attain something close to this exponential improvement? This is, of course,
Loosely coupled
a central question in many areas of AI. We have seen successful solution methods for loosely
coupled systems in the context of CSPs, where “tree like” constraint graphs yielded efﬁcient
solution methods (see page 186), as well as in the context of disjoint pattern databases (page
119) and additive heuristics for planning (page 374).
The standard approach to loosely coupled problems is to pretend the problems are com-
pletely decoupled and then ﬁx up the interactions. For the transition model, this means writing
action schemas as if the actors acted independently.
Let’s see how this works for a game of doubles tennis. Here, we have two human tennis
players who form a doubles team with the common goal of winning the match against an
opponent team. Let’s suppose that at one point in the game, the team has the goal of returning
the ball that has been hit to them and ensuring that at least one of them is covering the net.
Figure 17.1 shows the initial conditions, goal, and action schemas for this problem. It is easy
to see that we can get from the initial conditions to the goal with a two-step joint plan that
Joint plan
