---
chunk_id: "book-ca4fca8dd8-chunk-0244"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 244
confidence: "first-pass"
extraction_method: "structured-local"
---

150
Chapter 4
Search in Complex Environments
4.4.3 Solving partially observable problems
The preceding section showed how to derive the RESULTS function for a nondeterministic
belief-state problem from an underlying physical problem, given the PERCEPT function. With
this formulation, the AND–OR search algorithm of Figure 4.11 can be applied directly to
derive a solution. Figure 4.16 shows part of the search tree for the local-sensing vacuum
world, assuming an initial percept [L,Dirty]. The solution is the conditional plan
[Suck,Right,if Rstate={6} then Suck else []].
Notice that, because we supplied a belief-state problem to the AND–OR search algorithm, it
returned a conditional plan that tests the belief state rather than the actual state. This is as it
should be: in a partially observable environment the agent won’t know the actual state.
As in the case of standard search algorithms applied to sensorless problems, the AND–
OR search algorithm treats belief states as black boxes, just like any other states. One can
improve on this by checking for previously generated belief states that are subsets or supersets
of the current state, just as for sensorless problems. One can also derive incremental search
algorithms, analogous to those described for sensorless problems, that provide substantial
speedups over the black-box approach.
4.4.4 An agent for partially observable environments
An agent for partially observable environments formulates a problem, calls a search algo-
rithm (such as AND-OR-SEARCH) to solve it, and executes the solution. There are two main
differences between this agent and the one for fully observable deterministic environments.
First, the solution will be a conditional plan rather than a sequence; to execute an if–then–else
expression, the agent will need to test the condition and execute the appropriate branch of the
conditional. Second, the agent will need to maintain its belief state as it performs actions
and receives percepts. This process resembles the prediction–observation–update process in
Equation (4.5) but is actually simpler because the percept is given by the environment rather
than calculated by the agent. Given an initial belief state b, an action a, and a percept o, the
new belief state is:
b′ = UPDATE(PREDICT(b,a),o).
(4.6)
Consider a kindergarten vacuum world wherein agents sense only the state of their current
square, and any square may become dirty at any time unless the agent is actively cleaning it
at that moment.7 Figure 4.17 shows the belief state being maintained in this environment.
In partially observable environments—which include the vast majority of real-world
environments—maintaining one’s belief state is a core function of any intelligent system.
This function goes under various names, including monitoring, ﬁltering, and state estima-
Monitoring
Filtering
tion. Equation (4.6) is called a recursive state estimator because it computes the new belief
State estimation
state from the previous one rather than by examining the entire percept sequence. If the agent
is not to “fall behind,” the computation has to happen as fast as percepts are coming in. As
the environment becomes more complex, the agent will only have time to compute an ap-
proximate belief state, perhaps focusing on the implications of the percept for the aspects of
the environment that are of current interest. Most work on this problem has been done for
7
The usual apologies to those who are unfamiliar with the effect of small children on the environment.
