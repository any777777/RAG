---
chunk_id: "book-ca4fca8dd8-chunk-1540"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1540
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
929
There is certainly room for improvement: not only do NLP systems still lag human per-
formance on many tasks, but they do so after processing thousands of times more text than
any human could read in a lifetime. This suggests that there is plenty of scope for new insights
from linguists, psychologists, and NLP researchers.
Summary
The key points of this chapter are as follows:
• Continuous representations of words with word embeddings are more robust than dis-
crete atomic representations, and can be pretrained using unlabeled text data.
• Recurrent neural networks can effectively model local and long-distance context by
retaining relevant information in their hidden-state vectors.
• Sequence-to-sequence models can be used for machine translation and text generation
problems.
• Transformer models use self-attention and can model long-distance context as well as
local context. They can make effective use of hardware matrix multiplication.
• Transfer learning that includes pretrained contextual word embeddings allows models to
be developed from very large unlabeled corpora and applied to a range of tasks. Models
that are pretrained to predict missing words can handle other tasks such as question
answering and textual entailment, after ﬁne-tuning for the target domain.
Bibliographical and Historical Notes
The distribution of words and phrases in natural language follow Zipf’s Law (Zipf, 1935,
1949): the frequency of the nth most popular word is roughly inversely proportional to n.
That means we have a data sparsity problem: even with billions of words of training data, we
are constantly running into novel words and phrases that were not seen before.
Generalization to novel words and phrases is aided by representations that capture the
basic insight that words with similar meanings appear in similar contexts. Deerwester et al.
(1990) projected words into low-dimensional vectors by decomposing the co-occurrence ma-
trix formed by words and the documents the words appear in. Another possibility is to treat
the surrounding words—say, a 5-word window—as context. Brown et al. (1992) grouped
words into hierarchical clusters according to the bigram context of words; this has proven to
be effective for tasks such as named entity recognition (Turian et al., 2010). The WORD2VEC
system (Mikolov et al., 2013) was the ﬁrst signiﬁcant demonstration of the advantages of
word embeddings obtained from training neural networks. The GloVe word embedding vec-
tors (Pennington et al., 2014) were obtained by operating directly on a word co-occurrence
matrix obtained from billions of words of text. Levy and Goldberg (2014) explain why and
how these word embeddings are able to capture linguistic regularities.
Bengio et al. (2003) pioneered the use of neural networks for language models, proposing
to combine “(1) a distributed representation for each word along with (2) the probability func-
tion for word sequences, expressed in terms of these representations.” Mikolov et al. (2010)
demonstrated the use of RNNs for modeling local context in language models. Jozefowicz
