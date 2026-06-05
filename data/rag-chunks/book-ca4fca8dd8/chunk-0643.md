---
chunk_id: "book-ca4fca8dd8-chunk-0643"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 643
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.5
Planning and Acting in Nondeterministic Domains
389
Variables in this plan should be considered existentially quantiﬁed; the second line says
that if there exists some color c that is the color of the table and the chair, then the agent
need not do anything to achieve the goal. When executing this plan, a contingent-planning
agent can maintain its belief state as a logical formula and evaluate each branch condition
by determining if the belief state entails the condition formula or its negation. (It is up to
the contingent-planning algorithm to make sure that the agent will never end up in a be-
lief state where the condition formula’s truth value is unknown.) Note that with ﬁrst-order
conditions, the formula may be satisﬁed in more than one way; for example, the condition
Color(Table,c)∧Color(can,c) might be satisﬁed by {can/Can1} and by {can/Can2} if both
cans are the same color as the table. In that case, the agent can choose any satisfying substi-
tution to apply to the rest of the plan.
As shown in Section 4.4.2, calculating the new belief state ˆb after an action a and subse-
quent percept is done in two stages. The ﬁrst stage calculates the belief state after the action,
just as for the sensorless agent:
ˆb = (b−DEL(a))∪ADD(a)
where, as before, we have assumed a belief state represented as a conjunction of literals. The
second stage is a little trickier. Suppose that percept literals p1,..., pk are received. One might
think that we simply need to add these into the belief state; in fact, we can also infer that the
preconditions for sensing are satisﬁed. Now, if a percept p has exactly one percept schema,
Percept(p,PRECOND:c), where c is a conjunction of literals, then those literals can be thrown
into the belief state along with p. On the other hand, if p has more than one percept schema
whose preconditions might hold according to the predicted belief state ˆb, then we have to add
in the disjunction of the preconditions. Obviously, this takes the belief state outside 1-CNF
and brings up the same complications as conditional effects, with much the same classes of
solutions.
Given a mechanism for computing exact or approximate belief states, we can generate
contingent plans with an extension of the AND–OR forward search over belief states used
in Section 4.4. Actions with nondeterministic effects—which are deﬁned simply by using a
disjunction in the EFFECT of the action schema—can be accommodated with minor changes
to the belief-state update calculation and no change to the search algorithm.3 For the heuristic
function, many of the methods suggested for sensorless planning are also applicable in the
partially observable, nondeterministic case.
11.5.3 Online planning
Imagine watching a spot-welding robot in a car plant. The robot’s fast, accurate motions are
repeated over and over again as each car passes down the line. Although technically im-
pressive, the robot probably does not seem at all intelligent because the motion is a ﬁxed,
preprogrammed sequence; the robot obviously doesn’t “know what it’s doing” in any mean-
ingful sense. Now suppose that a poorly attached door falls off the car just as the robot is
about to apply a spot-weld. The robot quickly replaces its welding actuator with a gripper,
picks up the door, checks it for scratches, reattaches it to the car, sends an email to the ﬂoor
supervisor, switches back to the welding actuator, and resumes its work. All of a sudden,
3
If cyclic solutions are required for a nondeterministic problem, AND–OR search must be generalized to a loopy
version such as LAO∗(Hansen and Zilberstein, 2001).
