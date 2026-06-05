---
chunk_id: "book-ca4fca8dd8-chunk-0729"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 729
confidence: "first-pass"
extraction_method: "structured-local"
---

438
Chapter 13
Probabilistic Reasoning
In brief, then, d-separation means separation in the undirected, moralized, ancestral subgraph.
Applying the deﬁnition to the burglary network in Figure 13.2, we can deduce that Burglary
and Earthquake are independent given the empty set (i.e., they are absolutely independent);
that they are not necessarily conditionally independent given Alarm; and that JohnCalls and
MaryCalls are conditionally independent given Alarm. Notice also that the Markov blanket
property follows directly from the d-separation property, since a variable’s Markov blanket
d-separates it from all other variables.
13.2.2 Eﬃcient Representation of Conditional Distributions
Even if the maximum number of parents k is smallish, ﬁlling in the CPT for a node requires
up to O(2k) numbers and perhaps a great deal of experience with all the possible conditioning
cases. In fact, this is a worst-case scenario in which the relationship between the parents and
the child is completely arbitrary. Usually, such relationships are describable by a canonical
distribution that ﬁts some standard pattern. In such cases, the complete table can be speciﬁed
Canonical
distribution
just by naming the pattern and perhaps supplying a few parameters.
The simplest example is provided by deterministic nodes. A deterministic node has its
Deterministic nodes
value speciﬁed exactly by the values of its parents, with no uncertainty. The relationship
can be a logical one: for example, the relationship between the parent nodes Canadian, US,
Mexican and the child node NorthAmerican is simply that the child is the disjunction of the
parents. The relationship can also be numerical: for example, the BestPrice for a car is the
minimum of the prices at each dealer in the area; and the WaterStored in a reservoir at year’s
end is the sum of the original amount, plus the inﬂows (rivers, runoff, precipitation) and
minus the outﬂows (releases, evaporation, seepage).
Many Bayes net systems allow the user to specify deterministic functions using a general-
purpose programming language; this makes it possible to include complex elements such as
global climate models or power-grid simulators within a probabilistic model.
Another important pattern that occurs often in practice is context-speciﬁc independence
Context-speciﬁc
independence
or CSI. A conditional distribution exhibits CSI if a variable is conditionally independent of
some of its parents given certain values of others. For example, let’s suppose that the Damage
to your car occurring during a given period of time depends on the Ruggedness of your car
and whether or not an Accident occurred in that period. Clearly, if Accident is false, then the
Damage, if any, doesn’t depend on the Ruggedness of your car. (There might be vandalism
damage to the car’s paintwork or windows, but we’ll assume all cars are equally subject to
such damage.) We say that Damage is context-speciﬁcally independent of Ruggedness given
Accident=false. Bayes net systems often implement CSI using an if-then-else syntax for
specifying conditional distributions; for example, one might write
P(Damage|Ruggedness,Accident) =
if (Accident=false) then d1 else d2(Ruggedness)
where d1 and d2 represent arbitrary distributions. As with determinism, the presence of CSI in
a network may facilitate efﬁcient inference. All of the exact inference algorithms mentioned
in Section 13.3 can be modiﬁed to take advantage of CSI to speed up computation.
Uncertain relationships can often be characterized by so-called noisy logical relation-
ships. The standard example is the noisy-OR relation, which is a generalization of the logical
Noisy-OR
OR. In propositional logic, we might say that Fever is true if and only if Cold, Flu, or Malaria
