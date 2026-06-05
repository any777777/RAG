---
chunk_id: "book-ca4fca8dd8-chunk-0233"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 233
confidence: "first-pass"
extraction_method: "structured-local"
---

140
Chapter 4
Search in Complex Environments
forming a convex set4 and the objective function is also linear. The time complexity of linear
Convex set
programming is polynomial in the number of variables.
Linear programming is probably the most widely studied and broadly useful method for
optimization. It is a special case of the more general problem of convex optimization, which
Convex optimization
allows the constraint region to be any convex region and the objective to be any function that is
convex within the constraint region. Under certain conditions, convex optimization problems
are also polynomially solvable and may be feasible in practice with thousands of variables.
Several important problems in machine learning and control theory can be formulated as
convex optimization problems (see Chapter 21).
4.3 Search with Nondeterministic Actions
In Chapter 3, we assumed a fully observable, deterministic, known environment. Therefore,
an agent can observe the initial state, calculate a sequence of actions that reach the goal, and
execute the actions with its “eyes closed,” never having to use its percepts.
When the environment is partially observable, however, the agent doesn’t know for sure
what state it is in; and when the environment is nondeterministic, the agent doesn’t know
what state it transitions to after taking an action. That means that rather than thinking “I’m in
state s1 and if I do action a I’ll end up in state s2,” an agent will now be thinking “I’m either
in state s1 or s3, and if I do action a I’ll end up in state s2,s4 or s5.” We call a set of physical
states that the agent believes are possible a belief state.
Belief state
In partially observable and nondeterministic environments, the solution to a problem is
no longer a sequence, but rather a conditional plan (sometimes called a contingency plan or a
Conditional plan
strategy) that speciﬁes what to do depending on what percepts agent receives while executing
the plan. We examine nondeterminism in this section and partial observability in the next.
4.3.1 The erratic vacuum world
The vacuum world from Chapter 2 has eight states, as shown in Figure 4.9. There are three
actions—Right, Left, and Suck—and the goal is to clean up all the dirt (states 7 and 8). If the
environment is fully observable, deterministic, and completely known, then the problem is
easy to solve with any of the algorithms in Chapter 3, and the solution is an action sequence.
For example, if the initial state is 1, then the action sequence [Suck, Right, Suck] will reach a
goal state, 8.
Now suppose that we introduce nondeterminism in the form of a powerful but erratic
vacuum cleaner. In the erratic vacuum world, the Suck action works as follows:
• When applied to a dirty square the action cleans the square and sometimes cleans up
dirt in an adjacent square, too.
• When applied to a clean square the action sometimes deposits dirt on the carpet.5
To provide a precise formulation of this problem, we need to generalize the notion of a tran-
sition model from Chapter 3. Instead of deﬁning the transition model by a RESULT function
4
A set of points S is convex if the line joining any two points in S is also contained in S. A convex function is
one for which the space “above” it forms a convex set; by deﬁnition, convex functions have no local (as opposed
to global) minima.
5
We assume that most readers face similar problems and can sympathize with our agent. We apologize to
owners of modern, efﬁcient cleaning appliances who cannot take advantage of this pedagogical device.
