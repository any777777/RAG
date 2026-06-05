---
chunk_id: "book-ca4fca8dd8-chunk-0884"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 884
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.5
Decision Networks
535
with additional node types for actions and utilities. We use the problem of picking an airport
site as an example.
15.5.1 Representing a decision problem with a decision network
In its most general form, a decision network represents information about the agent’s current
state, its possible actions, the state that will result from the agent’s action, and the utility of
that state. It therefore provides a substrate for implementing utility-based agents of the type
ﬁrst introduced in Section 2.4.5. Figure 15.6 shows a decision network for the airport-siting
problem. It illustrates the three types of nodes used:
• Chance nodes (ovals) represent random variables, just as they do in Bayesian networks.
Chance nodes
The agent could be uncertain about the construction cost, the level of air trafﬁc and the
potential for litigation, and the Safety, Quietness, and total Frugality variables, each
of which also depends on the site chosen. Each chance node has associated with it a
conditional distribution that is indexed by the state of the parent nodes. In decision
networks, the parent nodes can include decision nodes as well as chance nodes. Note
that each of the current-state chance nodes could be part of a large Bayesian network
for assessing construction costs, air trafﬁc levels, or litigation potentials.
• Decision nodes (rectangles) represent points where the decision maker has a choice of
Decision nodes
actions. In this case, the AirportSite action can take on a different value for each site
under consideration. The choice inﬂuences the safety, quietness, and frugality of the
solution. In this chapter, we assume that we are dealing with a single decision node.
Chapter 16 deals with cases in which more than one decision must be made.
• Utility nodes (diamonds) represent the agent’s utility function.7 The utility node has
Utility nodes
as parents all variables describing the outcomes that directly affect utility. Associated
with the utility node is a description of the agent’s utility as a function of the parent
attributes. The description could be just a tabulation of the function, or it might be
a parameterized additive or linear function of the attribute values. For now, we will
assume that the function is deterministic; that is, given the values of its parent variables,
the value of the utility node is fully determined.
A simpliﬁed form is also used in many cases. The notation remains identical, but the
chance nodes describing the outcome states are omitted. Instead, the utility node is connected
directly to the current-state nodes and the decision node. In this case, rather than representing
a utility function on outcome states, the utility node represents the expected utility associated
with each action, as deﬁned in Equation (15.1) on page 519; that is, the node is associated
with an action-utility function (also known as a Q-function in reinforcement learning, as
Action-utility
function
described in Chapter 23). Figure 15.7 shows the action-utility representation of the airport
siting problem.
Notice that, because the Quietness, Safety, and Frugality chance nodes in Figure 15.6
refer to future states, they can never have their values set as evidence variables. Thus, the
simpliﬁed version that omits these nodes can be used whenever the more general form can
be used. Although the simpliﬁed form contains fewer nodes, the omission of an explicit
description of the outcome of the siting decision means that it is less ﬂexible with respect to
changes in circumstances.
7
These nodes are also called value nodes in the literature.
