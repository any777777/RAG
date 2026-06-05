---
chunk_id: "book-ca4fca8dd8-chunk-0723"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 723
confidence: "first-pass"
extraction_method: "structured-local"
---

434
Chapter 13
Probabilistic Reasoning
constructing the topology of the network. First, we rewrite the entries in the joint distribution
in terms of conditional probability, using the product rule (see page 408):
P(x1,...,xn) = P(xn |xn−1,...,x1)P(xn−1,...,x1).
Then we repeat the process, reducing each joint probability to a conditional probability and a
joint probability on a smaller set of variables. We end up with one big product:
P(x1,...,xn) = P(xn |xn−1,...,x1)P(xn−1 |xn−2,...,x1) ··· P(x2 |x1)P(x1)
=
n
∏
i=1
P(xi |xi−1,...,x1).
This identity is called the chain rule. It holds for any set of random variables. Comparing it
Chain rule
with Equation (13.2), we see that the speciﬁcation of the joint distribution is equivalent to the
general assertion that, for every variable Xi in the network,
P(Xi |Xi−1,...,X1) = P(Xi |Parents(Xi)),
(13.3)
provided that Parents(Xi) ⊆{Xi−1,...,X1}. This last condition is satisﬁed by numbering the
nodes in topological order—that is, in any order consistent with the directed graph structure.
Topological ordering
For example, the nodes in Figure 13.2 could be ordered B,E,A,J,M; E,B,A,M,J; and so on.
What Equation (13.3) says is that the Bayesian network is a correct representation of the
domain only if each node is conditionally independent of its other predecessors in the node
ordering, given its parents. We can satisfy this condition with this methodology:
1. Nodes: First determine the set of variables that are required to model the domain. Now
order them, {X1,...,Xn}. Any order will work, but the resulting network will be more
compact if the variables are ordered such that causes precede effects.
2. Links: For i = 1 to n do:
• Choose a minimal set of parents for Xi from X1,...,Xi−1, such that Equation (13.3)
is satisﬁed.
• For each parent insert a link from the parent to Xi.
• CPTs: Write down the conditional probability table, P(Xi|Parents(Xi)).
Intuitively, the parents of node Xi should contain all those nodes in X1, ..., Xi−1 that directly
▶
inﬂuence Xi. For example, suppose we have completed the network in Figure 13.2 except for
the choice of parents for MaryCalls. MaryCalls is certainly inﬂuenced by whether there is
a Burglary or an Earthquake, but not directly inﬂuenced. Intuitively, our knowledge of the
domain tells us that these events inﬂuence Mary’s calling behavior only through their effect
on the alarm. Also, given the state of the alarm, whether John calls has no inﬂuence on
Mary’s calling. Formally speaking, we believe that the following conditional independence
statement holds:
P(MaryCalls|JohnCalls,Alarm,Earthquake,Burglary) = P(MaryCalls|Alarm).
Thus, Alarm will be the only parent node for MaryCalls.
Because each node is connected only to earlier nodes, this construction method guaran-
tees that the network is acyclic. Another important property of Bayes nets is that they contain
no redundant probability values. If there is no redundancy, then there is no chance for incon-
sistency: it is impossible for the knowledge engineer or domain expert to create a Bayesian
▶
network that violates the axioms of probability.
