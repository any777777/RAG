---
chunk_id: "book-ca4fca8dd8-chunk-1526"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1526
confidence: "first-pass"
extraction_method: "structured-local"
---

920
Chapter 25
Deep Learning for Natural Language Processing
The most straightforward way of applying self-attention is where the attention matrix is
directly formed by the dot product of the input vectors. However, this is problematic. The dot
product between a vector and itself will always be high, so each hidden state will be biased
towards attending to itself. The transformer solves this by ﬁrst projecting the input into three
different representations using three different weight matrices:
• The query vector qi =Wqxi is the one being attended from, like the target in the stan-
Query vector
dard attention mechanism.
• The key vector ki =Wkxi is the one being attended to, like the source in the basic
Key vector
attention mechanism.
• The value vector vi =Wvxi is the context that is being generated.
Value vector
In the standard attention mechanism, the key and value networks are identical, but intuitively
it makes sense for these to be separate representations. The encoding results of the ith word,
ci, can be calculated by applying an attention mechanism to the projected vectors:
rij = (qi ·kj)/
√
d
aij = erij/(∑
k
erik)
ci = ∑
j
aij ·vj ,
where d is the dimension of k and q. Note that i and j are indexes in the same sentence, since
we are encoding the context using self-attention. In each transformer layer, self-attention uses
the hidden vectors from the previous layer, which initially is the embedding layer.
There are several details worth mentioning here. First of all, the self-attention mecha-
nism is asymmetric, as rij is different from rji. Second, the scale factor
√
d was added to
improve numerical stability. Third, the encoding for all words in a sentence can be calculated
simultaneously, as the above equations can be expressed using matrix operations that can be
computed efﬁciently in parallel on modern specialized hardware.
The choice of which context to use is completely learned from training examples, not
prespeciﬁed. The context-based summarization, ci, is a sum over all previous positions in the
sentence. In theory, any information from the sentence could appear in ci, but in practice,
sometimes important information gets lost, because it is essentially averaged out over the
whole sentence. One way to address that is called multiheaded attention. We divide the
Multiheaded
attention
sentence up into m equal pieces and apply the attention model to each of the m pieces. Each
piece has its own set of weights. Then the results are concatenated together to form ci. By
concatenating rather than summing, we make it easier for an important subpiece to stand out.
25.4.2 From self-attention to transformer
Self-attention is only one component of the transformer model. Each transformer layer con-
sists of several sub-layers. At each transformer layer, self-attention is applied ﬁrst. The out-
put of the attention module is fed through feedforward layers, where the same feedforward
weight matrices are applied independently at each position. A nonlinear activation function,
typically ReLU, is applied after the ﬁrst feedforward layer. In order to address the potential
vanishing gradient problem, two residual connections are added into the transformer layer.
A single-layer transformer in shown in Figure 25.9. In practice, transformer models usually
