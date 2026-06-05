---
chunk_id: "book-ca4fca8dd8-chunk-1530"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1530
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 25.5
Pretraining and Transfer Learning
923
problems with vector subtraction. This indicates that the word embeddings are capturing
substantial information about the words.
In this section we will dive into the details of how word embeddings are created using an
entirely unsupervised process over a large corpus of text. That is in contrast to the embeddings
from Section 25.1, which were built during the process of supervised part of speech tagging,
and thus required POS tags that come from expensive hand annotation.
We will concentrate on one speciﬁc model for word embeddings, the GloVe (Global
Vectors) model. The model starts by gathering counts of how many times each word appears
within a window of another word, similar to the skip-gram model. First choose window size
(perhaps 5 words) and let Xij be the number of times that words i and j co-occur within
a window, and let Xi be the number of times word i co-occurs with any other word. Let
Pij =Xi j/Xi be the probability that word j appears in the context of word i. As before, let Ei
be the word embedding for word i.
Part of the intuition of the GloVe model is that the relationship between two words can
best be captured by comparing them both to other words. Consider the words ice and steam.
Now consider the ratio of their probabilities of co-occurrence with another word, w, that is:
Pw,ice/Pw,steam .
When w is the word solid the ratio will be high (meaning solid applies more to ice) and when
w is the word gas it will be low (meaning gas applies more to steam). And when w is a
non-content word like the, a word like water that is equally relevant to both, or an equally
irrelevant word like fashion, the ratio will be close to 1.
The GloVe model starts with this intuition and goes through some mathematical reason-
ing (Pennington et al., 2014) that converts ratios of probabilities into vector differences and
dot products, eventually arriving at the constraint
Ei ·E′
k = log(Pij).
In other words, the dot product of two word vectors is equal to the log probability of their
co-occurrence. That makes intuitive sense: two nearly-orthogonal vectors have a dot product
close to 0, and two nearly-identical normalized vectors have a dot product close to 1. There
is a technical complication wherein the GloVe model creates two word embedding vectors
for each word, Ei and E′
i; computing the two and then adding them together at the end helps
limit overﬁtting.
Training a model like GloVe is typically much less expensive than training a standard
neural network: a new model can be trained from billions of words of text in a few hours
using a standard desktop CPU.
It is possible to train word embeddings on a speciﬁc domain, and recover knowledge in
that domain. For example, Tshitoyan et al. (2019) used 3.3 million scientiﬁc abstracts on the
subject of material science to train a word embedding model. They found that, just as we saw
that a generic word embedding model can answer “Athens is to Greece as Oslo is to what?”
with “Norway,” their material science model can answer “NiFe is to ferromagnetic as IrMn
is to what?” with “antiferromagnetic.”
Their model does not rely solely on co-occurrence of words; it seems to be capturing
more complex scientiﬁc knowledge. When asked what chemical compounds can be classiﬁed
as “thermoelectric” or “topological insulator,” their model is able to answer correctly. For
example, CsAgGa2Se4 never appears near “thermoelectric” in the corpus, but it does appear
