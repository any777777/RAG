---
chunk_id: "book-ca4fca8dd8-chunk-0234"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 234
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 141

Section 4.3
Search with Nondeterministic Actions
141
1
2
8
7
5
6
3
4
Figure 4.9 The eight possible states of the vacuum world; states 7 and 8 are goal states.
that returns a single outcome state, we use a RESULTS function that returns a set of possible
outcome states. For example, in the erratic vacuum world, the Suck action in state 1 cleans
up either just the current location, or both locations:
RESULTS(1,Suck) = {5,7}
If we start in state 1, no single sequence of actions solves the problem, but the following
conditional plan does:
[Suck,if State=5 then [Right,Suck] else []].
(4.3)
Here we see that a conditional plan can contain if–then–else steps; this means that solutions
are trees rather than sequences. Here the conditional in the if statement tests to see what the
current state is; this is something the agent will be able to observe at runtime, but doesn’t
know at planning time. Alternatively, we could have had a formulation that tests the percept
rather than the state. Many problems in the real, physical world are contingency problems,
because exact prediction of the future is impossible. For this reason, many people keep their
eyes open while walking around.
4.3.2 AND–OR search trees
How do we ﬁnd these contingent solutions to nondeterministic problems? As in Chapter 3,
we begin by constructing search trees, but here the trees have a different character. In a de-
terministic environment, the only branching is introduced by the agent’s own choices in each
state: I can do this action or that action. We call these nodes OR nodes. In the vacuum world,
Or node
for example, at an OR node the agent chooses Left or Right or Suck. In a nondeterministic
environment, branching is also introduced by the environment’s choice of outcome for each
action. We call these nodes AND nodes. For example, the Suck action in state 1 results in the
And node
belief state {5,7}, so the agent would need to ﬁnd a plan for state 5 and for state 7. These
two kinds of nodes alternate, leading to an AND–OR tree as illustrated in Figure 4.10.
And–or tree

## Page 142
