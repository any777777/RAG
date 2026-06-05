---
chunk_id: "book-ca4fca8dd8-chunk-1081"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1081
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.1
Relational Probability Models
647
For team games, we’ll assume, as a ﬁrst approximation, that the overall performance of
team t in game g is the sum of the individual performances of the players on t:
TeamPerformance(t,g) = ∑i∈t Performance(i,g).
Even though the individual performances are not visible to the ratings engine, the players’
skill levels can still be estimated from the results of several games, as long as the team com-
positions vary across games. Microsoft’s TrueSkillTM ratings engine uses this model, along
with an efﬁcient approximate inference algorithm, to serve hundreds of millions of users
every day.
This model can be elaborated in numerous ways. For example, we might assume that
weaker players have higher variance in their performance; we might include the player’s role
on the team; and we might consider speciﬁc kinds of performance and skill—e.g., defending
and attacking—in order to improve team composition and predictive accuracy.
18.1.3 Inference in relational probability models
The most straightforward approach to inference in RPMs is simply to construct the equivalent
Bayesian network, given the known constant symbols belonging to each type. With B books
and C customers, the basic model given previously could be constructed with simple loops:4
for b = 1 to B do
add node Qualityb with no parents, prior ⟨0.05,0.2,0.4,0.2,0.15 ⟩
for c = 1 to C do
add node Honestc with no parents, prior ⟨0.99,0.01 ⟩
add node Kindnessc with no parents, prior ⟨0.1,0.1,0.2,0.3,0.3 ⟩
for b = 1 to B do
add node Recommendationc,b with parents Honestc,Kindnessc,Qualityb
and conditional distribution RecCPT(Honestc,Kindnessc,Qualityb)
This technique is called grounding or unrolling; it is the exact analog of propositionaliza-
Grounding
Unrolling
tion for ﬁrst-order logic (page 298). The obvious drawback is that the resulting Bayes net
may be very large. Furthermore, if there are many candidate objects for an unknown relation
or function—for example, the unknown author of B2—then some variables in the network
may have many parents.
Fortunately, it is often possible to avoid generating the entire implicit Bayes net. As we
saw in the discussion of the variable elimination algorithm on page 451, every variable that is
not an ancestor of a query variable or evidence variable is irrelevant to the query. Moreover, if
the query is conditionally independent of some variable given the evidence, then that variable
is also irrelevant. So, by chaining through the model starting from the query and evidence,
we can identify just the set of variables that are relevant to the query. These are the only ones
that need to be instantiated to create a potentially tiny fragment of the implicit Bayes net.
Inference in this fragment gives the same answer as inference in the entire implicit Bayes net.
Another avenue for improving the efﬁciency of inference comes from the presence of re-
peated substructure in the unrolled Bayes net. This means that many of the factors constructed
during variable elimination (and similar kinds of tables constructed by clustering algorithms)
4
Several statistical packages would view this code as deﬁning the RPM, rather than just constructing a Bayes
net to perform inference in the RPM. This view, however, misses an important role for RPM syntax: without a
syntax with clear semantics, there is no way the model structure can be learned from data.
