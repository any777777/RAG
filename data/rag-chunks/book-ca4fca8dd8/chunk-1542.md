---
chunk_id: "book-ca4fca8dd8-chunk-1542"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1542
confidence: "first-pass"
extraction_method: "structured-local"
---

930
Chapter 25
Deep Learning for Natural Language Processing
et al. (2016) showed how an RNN trained on a billion words can outperform carefully hand-
crafted n-gram models. Contextual representations for words were emphasized by Peters
et al. (2018), who called them ELMO (Embeddings from Language Models) representations.
Note that some authors compare language models by measuring their perplexity. The
Perplexity
perplexity of a probability distribution is 2H, where H is the entropy of the distribution (see
Section 19.3.3). A language model with lower perplexity is, all other things being equal, a
better model. But in practice, all other things are rarely equal. Therefore it is more informa-
tive to measure performance on a real task rather than relying on perplexity.
Howard and Ruder (2018) describe the ULMFIT (Universal Language Model Fine-
tuning) framework, which makes it easier to ﬁne-tune a pretrained language model without
requiring a vast corpus of target-domain documents. Ruder et al. (2019) give a tutorial on
transfer learning for NLP.
Mikolov et al. (2010) introduced the idea of using RNNs for NLP, and Sutskever et al.
(2015) introduced the idea of sequence to sequence learning with deep networks. Zhu et al.
(2017) and (Liu et al., 2018b) showed that an unsupervised approach works, and makes
data collection much easier. It was soon found that these kinds of models could perform
surprisingly well at a variety of tasks, for example, image captioning (Karpathy and Fei-Fei,
2015; Vinyals et al., 2017b).
Devlin et al. (2018) showed that transformer models pretrained with the masked language
modeling objective can be directly used for multiple tasks. The model was called BERT
(Bidirectional Encoder Representations from Transformers). Pretrained BERT models can be
ﬁne-tuned for particular domains and particular tasks, including question answering, named
entity recognition, text classiﬁcation, sentiment analysis, and natural language inference.
The XLNET system (Yang et al., 2019) improves on BERT by eliminating a discrepancy
between the pretraining and ﬁne-tuning. The ERNIE 2.0 framework (Sun et al., 2019) extracts
more from the training data by considering sentence order and the presence of named entities,
rather than just co-occurrence of words, and was shown to outperform BERT and XLNET.
In response, researchers revisited and improved on BERT: the ROBERTA system (Liu et al.,
2019b) used more data and different hyperparameters and training procedures, and found that
it could match XLNET. The Reformer system (Kitaev et al., 2020) extends the range of the
context that can be considered all the way up to a million words. Meanwhile, ALBERT (A
Lite BERT) went in the other direction, reducing the number of parameters from 108 million
to 12 million (so as to ﬁt on mobile devices) while maintaining high accuracy.
The XLM system (Lample and Conneau, 2019) is a transformer model with training
data from multiple languages. This is useful for machine translation, but also provides more
robust representations for monolingual tasks. Two other important systems, GPT-2 (Radford
et al., 2019) and T5 (Raffel et al., 2019), were described in the chapter. The later paper also
introduced the 35 billion word Colossal Clean Crawled Corpus (C4).
Various promising improvements on pretraining algorithms have been proposed (Yang
et al., 2019; Liu et al., 2019b). Pretrained contextual models are described by Peters et al.
(2018) and Dai and Le (2016).
The GLUE (General Language Understanding Evaluation) benchmark, a collection of
tasks and tools for evaluating NLP systems, was introduced by Wang et al. (2018a). Tasks
include question answering, sentiment analysis, textual entailment, translation, and parsing.
Transformer models have so dominated the leaderboard (the human baseline is way down at
