---
chunk_id: "book-ca4fca8dd8-chunk-0717"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 717
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.1
Representing Knowledge in an Uncertain Domain
431
Weather
Cavity
Toothache
Catch
Figure 13.1 A simple Bayesian network in which Weather is independent of the other three
variables and Toothache and Catch are conditionally independent, given Cavity.
The topology of the network—the set of nodes and links—speciﬁes the conditional indepen-
dence relationships that hold in the domain, in a way that will be made precise shortly. The
intuitive meaning of an arrow is typically that X has a direct inﬂuence on Y, which suggests
that causes should be parents of effects. It is usually easy for a domain expert to decide what
direct inﬂuences exist in the domain—much easier, in fact, than actually specifying the prob-
abilities themselves. Once the topology of the Bayes net is laid out, we need only specify the
local probability information for each variable, in the form of a conditional distribution given
its parents. The full joint distribution for all the variables is deﬁned by the topology and the
local probability information.
Recall the simple world described in Chapter 12, consisting of the variables Toothache,
Cavity, Catch, and Weather.
We argued that Weather is independent of the other vari-
ables; furthermore, we argued that Toothache and Catch are conditionally independent, given
Cavity. These relationships are represented by the Bayes net structure shown in Figure 13.1.
Formally, the conditional independence of Toothache and Catch, given Cavity, is indicated
by the absence of a link between Toothache and Catch. Intuitively, the network represents the
fact that Cavity is a direct cause of Toothache and Catch, whereas no direct causal relationship
exists between Toothache and Catch.
Now consider the following example, which is just a little more complex. You have a new
burglar alarm installed at home. It is fairly reliable at detecting a burglary, but is occasionally
set off by minor earthquakes. (This example is due to Judea Pearl, a resident of earthquake-
prone Los Angeles.) You also have two neighbors, John and Mary, who have promised to call
you at work when they hear the alarm. John nearly always calls when he hears the alarm, but
sometimes confuses the telephone ringing with the alarm and calls then, too. Mary, on the
other hand, likes rather loud music and often misses the alarm altogether. Given the evidence
of who has or has not called, we would like to estimate the probability of a burglary.
A Bayes net for this domain appears in Figure 13.2. The network structure shows that
burglary and earthquakes directly affect the probability of the alarm’s going off, but whether
John and Mary call depends only on the alarm. The network thus represents our assumptions
that they do not perceive burglaries directly, they do not notice minor earthquakes, and they
do not confer before calling.
The local probability information attached to each node in Figure 13.2 takes the form
of a conditional probability table (CPT). (CPTs can be used only for discrete variables;
Conditional
probability table
(CPT)
other representations, including those suitable for continuous variables, are described in Sec-
