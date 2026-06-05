---
chunk_id: "book-ca4fca8dd8-chunk-0419"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 419
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.7
Agents Based on Propositional Logic
257
First we need proposition symbols for the occurrences of actions. As with percepts, these
symbols are indexed by time; thus, Forward0 means that the agent executes the Forward
action at time 0. By convention, the percept for a given time step happens ﬁrst, followed by
the action for that time step, followed by a transition to the next time step.
To describe how the world changes, we can try writing effect axioms that specify the
Eﬀect axiom
outcome of an action at the next time step. For example, if the agent is at location [1,1]
facing east at time 0 and goes Forward, the result is that the agent is in square [2,1] and no
longer is in [1,1]:
L0
1,1 ∧FacingEast0 ∧Forward0 ⇒(L1
2,1 ∧¬L1
1,1).
(7.1)
We would need one such sentence for each possible time step, for each of the 16 squares,
and each of the four orientations. We would also need similar sentences for the other actions:
Grab, Shoot, Climb, TurnLeft, and TurnRight.
Let us suppose that the agent does decide to move Forward at time 0 and asserts this
fact into its knowledge base. Given the effect axiom in Equation (7.1), combined with the
initial assertions about the state at time 0, the agent can now deduce that it is in [2,1]. That
is, ASK(KB,L1
2,1)=true. So far, so good. Unfortunately, if we ASK(KB,HaveArrow1), the
answer is false, that is, the agent cannot prove it still has the arrow; nor can it prove it doesn’t
have it! The information has been lost because the effect axiom fails to state what remains
unchanged as the result of an action. The need to do this gives rise to the frame problem.12
Frame problem
One possible solution to the frame problem would be to add frame axioms explicitly asserting
Frame axiom
all the propositions that remain the same. For example, for each time t we would have
Forwardt ⇒(HaveArrowt ⇔HaveArrowt+1)
Forwardt ⇒(WumpusAlivet ⇔WumpusAlivet+1)
···
where we explicitly mention every proposition that stays unchanged from time t to time t +1
under the action Forward. Although the agent now knows that it still has the arrow after
moving forward and that the wumpus hasn’t died or come back to life, the proliferation of
frame axioms seems remarkably inefﬁcient. In a world with m different actions and n ﬂuents,
the set of frame axioms will be of size O(mn). This speciﬁc manifestation of the frame
problem is sometimes called the representational frame problem. The problem played a
Representational
frame problem
signiﬁcant role in the history of AI; we explore it further in the notes at the end of the chapter.
The representational frame problem is signiﬁcant because the real world has very many
ﬂuents, to put it mildly. Fortunately for us humans, each action typically changes no more
than some small number k of those ﬂuents—the world exhibits locality. Solving the repre-
Locality
sentational frame problem requires deﬁning the transition model with a set of axioms of size
O(mk) rather than size O(mn). There is also an inferential frame problem: the problem of
Inferential frame
problem
projecting forward the results of a t-step plan of action in time O(kt) rather than O(nt).
The solution to the problem involves changing one’s focus from writing axioms about
actions to writing axioms about ﬂuents. Thus for each ﬂuent F, we will have an axiom that
deﬁnes the truth value of Ft+1 in terms of ﬂuents (including F itself) at time t and the actions
that may have occurred at time t. Now, the truth value of Ft+1 can be set in one of two ways:
12 The name “frame problem” comes from “frame of reference” in physics—the assumed stationary background
with respect to which motion is measured. It also has an analogy to the frames of a movie, in which normally
most of the background stays constant while changes occur in the foreground.
