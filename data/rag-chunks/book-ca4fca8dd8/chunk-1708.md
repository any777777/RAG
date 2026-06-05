---
chunk_id: "book-ca4fca8dd8-chunk-1708"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1708
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 28.3
The Ethics of AI
1043
D has ϵ–differential privacy if the log probability of the response y varies by less than ϵ when
we add the record r:
|logP(Q(D)=y)−logP(Q(D+r)=y)| ≤ϵ.
In other words, whether any one person decides to participate in the data base or not makes
no appreciable difference to the answers anyone can get, and therefore there is no privacy
disincentive to participate. Many databases are designed to guarantee differential privacy.
So far we have considered the issue of sharing de-identiﬁed data from a central database.
An approach called federated learning (Koneˇcn`y et al., 2016) has no central database; in-
Federated learning
stead, users maintain their own local databases that keep their data private. However, they
can share parameters of a machine learning model that is enhanced with their data, without
the risk of revealing any of the private data. Imagine a speech understanding application that
users can run locally on their phone. The application contains a baseline neural network,
which is then improved by local training on the words that are heard on the user’s phone.
Periodically, the owners of the application poll a subset of the users and ask them for the
parameter values of their improved local network, but not for any of their raw data. The
parameter values are combined together to form a new improved model which is then made
available to all users, so that they all get the beneﬁt of the training that is done by other users.
For this scheme to preserve privacy, we have to be able to guarantee that the model
parameters shared by each user cannot be reverse-engineered. If we sent the raw parameters,
there is a chance that an adversary inspecting them could deduce whether, say, a certain word
had been heard by the user’s phone. One way to eliminate this risk is with secure aggregation
Secure aggregation
(Bonawitz et al., 2017). The idea is that the central server doesn’t need to know the exact
parameter value from each distributed user; it only needs to know the average value for each
parameter, over all polled users. So each user can disguise their parameter values by adding
a unique mask to each value; as long as the sum of the masks is zero, the central server will
be able to compute the correct average. Details of the protocol make sure that it is efﬁcient
in terms of communication (less than half the bits transmitted correspond to masking), is
robust to individual users failing to respond, and is secure in the face of adversarial users,
eavesdroppers, or even an adversarial central server.
28.3.3 Fairness and bias
Machine learning is augmenting and sometimes replacing human decision-making in im-
portant situations: whose loan gets approved, to what neighborhoods police ofﬁcers are de-
ployed, who gets pretrial release or parole. But machine learning models can perpetuate
societal bias. Consider the example of an algorithm to predict whether criminal defendants
Societal bias
are likely to re-offend, and thus whether they should be released before trial. It could well be
that such a system picks up the racial or gender prejudices of human judges from the exam-
ples in the training set. Designers of machine learning systems have a moral responsibility to
ensure that their systems are in fact fair. In regulated domains such as credit, education, em-
ployment, and housing, they have a legal responsibility as well. But what is fairness? There
are multiple criteria; here are six of the most commonly-used concepts:
• Individual fairness: A requirement that individuals are treated similarly to other simi-
lar individuals, regardless of what class they are in.
