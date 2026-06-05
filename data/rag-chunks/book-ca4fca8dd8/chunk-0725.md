---
chunk_id: "book-ca4fca8dd8-chunk-0725"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 725
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.2
The Semantics of Bayesian Networks
435
Compactness and node ordering
As well as being a complete and nonredundant representation of the domain, a Bayes net
can often be far more compact than the full joint distribution. This property is what makes
it feasible to handle domains with many variables. The compactness of Bayesian networks
is an example of a general property of locally structured (also called sparse) systems. In a
Locally structured
Sparse
locally structured system, each subcomponent interacts directly with only a bounded number
of other components, regardless of the total number of components. Local structure is usually
associated with linear rather than exponential growth in complexity.
In the case of Bayes nets, it is reasonable to suppose that in most domains each ran-
dom variable is directly inﬂuenced by at most k others, for some constant k. If we assume
n Boolean variables for simplicity, then the amount of information needed to specify each
conditional probability table will be at most 2k numbers, and the complete network can be
speciﬁed by 2k ·n numbers. In contrast, the joint distribution contains 2n numbers. To make
this concrete, suppose we have n=30 nodes, each with ﬁve parents (k=5). Then the Bayesian
network requires 960 numbers, but the full joint distribution requires over a billion.
Specifying the conditional probability tables for a fully connected network, in which
each variable has all of its predecessors as parents, requires the same amount of information
as specifying the joint distribution in tabular form. For this reason, we often leave out links
even though a slight dependency exists, because the slight gain in accuracy is not worth the
the additional complexity in the network. For example, one might object to our burglary
network on the grounds that if there is a large earthquake, then John and Mary would not call
even if they heard the alarm, because they assume that the earthquake is the cause. Whether
to add the link from Earthquake to JohnCalls and MaryCalls (and thus enlarge the tables)
depends on the importance of getting more accurate probabilities compared with the cost of
specifying the extra information.
Even in a locally structured domain, we will get a compact Bayes net only if we choose
the node ordering well. What happens if we happen to choose the wrong order? Consider
the burglary example again. Suppose we decide to add the nodes in the order MaryCalls,
JohnCalls, Alarm, Burglary, Earthquake. We then get the somewhat more complicated net-
work shown in Figure 13.3(a). The process goes as follows:
• Adding MaryCalls: No parents.
• Adding JohnCalls: If Mary calls, that probably means the alarm has gone off, which
makes it more likely that John calls. Therefore, JohnCalls needs MaryCalls as a parent.
• Adding Alarm: Clearly, if both call, it is more likely that the alarm has gone off than if
just one or neither calls, so we need both MaryCalls and JohnCalls as parents.
• Adding Burglary: If we know the alarm state, then the call from John or Mary might
give us information about our phone ringing or Mary’s music, but not about burglary:
P(Burglary|Alarm,JohnCalls,MaryCalls) = P(Burglary|Alarm).
Hence we need just Alarm as parent.
• Adding Earthquake: If the alarm is on, it is more likely that there has been an earth-
quake. (The alarm is an earthquake detector of sorts.) But if we know that there has
been a burglary, then that explains the alarm, and the probability of an earthquake would
be only slightly above normal. Hence, we need both Alarm and Burglary as parents.
