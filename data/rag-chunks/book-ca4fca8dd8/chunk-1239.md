---
chunk_id: "book-ca4fca8dd8-chunk-1239"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1239
confidence: "first-pass"
extraction_method: "structured-local"
---

748
Chapter 20
Knowledge in Learning
Observations
Predictions
Hypotheses
Prior 
knowledge
Knowledge-based
inductive learning
Figure 20.6 A cumulative learning process uses, and adds to, its stock of background
knowledge over time.
This simple knowledge-free picture of inductive learning persisted until the early 1980s.
The modern approach is to design agents that already know something and are trying to learn
▶
some more. This may not sound like a terriﬁcally deep insight, but it makes quite a difference
to the way we design agents. It might also have some relevance to our theories about how
science itself works. The general idea is shown schematically in Figure 20.6.
An autonomous learning agent that uses background knowledge must somehow obtain
the background knowledge in the ﬁrst place, in order for it to be used in the new learning
episodes. This method must itself be a learning process. The agent’s life history will there-
fore be characterized by cumulative, or incremental, development. Presumably, the agent
could start out with nothing, performing inductions in vacuo like a good little pure induc-
tion program. But once it has eaten from the Tree of Knowledge, it can no longer pursue
such naive speculations and should use its background knowledge to learn more and more
effectively. The question is then how to actually do this.
20.2.1 Some simple examples
Let us consider some commonsense examples of learning with background knowledge. Many
apparently rational cases of inferential behavior in the face of observations clearly do not
follow the simple principles of pure induction.
• Sometimes one leaps to general conclusions after only one observation. Gary Larson
once drew a cartoon in which a bespectacled caveman, Zog, is roasting his lizard on
the end of a pointed stick. He is watched by an amazed crowd of his less intellectual
contemporaries, who have been using their bare hands to hold their victuals over the ﬁre.
This enlightening experience is enough to convince the watchers of a general principle
of painless cooking.
• Or consider the case of the traveler to Brazil meeting her ﬁrst Brazilian. On hearing him
speak Portuguese, she immediately concludes that Brazilians speak Portuguese, yet on
discovering that his name is Fernando, she does not conclude that all Brazilians are
called Fernando. Similar examples appear in science. For example, when a freshman
physics student measures the density and conductance of a sample of copper at a par-
ticular temperature, she is quite conﬁdent in generalizing those values to all pieces of
copper. Yet when she measures its mass, she does not even consider the hypothesis that
all pieces of copper have that mass. On the other hand, it would be quite reasonable to
make such a generalization over all pennies.
