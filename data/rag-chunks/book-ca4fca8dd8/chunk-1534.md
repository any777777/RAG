---
chunk_id: "book-ca4fca8dd8-chunk-1534"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1534
confidence: "first-pass"
extraction_method: "structured-local"
---

926
Chapter 25
Deep Learning for Natural Language Processing
1. What will best separate a mixture of iron ﬁlings and black pepper?
(a) magnet
(b) ﬁlter paper
(c) triple beam balance
(d) voltmeter
2. Which form of energy is produced when a rubber band vibrates?
(a) chemical
(b) light
(c) electrical
(d) sound
3. Because copper is a metal, it is
(a) liquid at room temperature
(b) nonreactive with other substances
(c) a poor conductor of electricity (d) a good conductor of heat
4. Which process in an apple tree primarily results from cell division?
(a) growth
(b) photosynthesis
(c) gas exchange
(d) waste removal
Figure 25.13 Questions from an 8th grade science exam that the ARISTO system can an-
swer correctly using an ensemble of methods, with the most inﬂuential being a ROBERTA
language model. Answering these questions requires knowledge about natural language, the
structure of multiple-choice tests, commonsense, and science.
The ﬁnal hidden vectors that correspond to the masked tokens are then used to predict
the words that were masked—in this example, rose. During training a single sentence can
be used multiple times with different words masked out. The beauty of this approach is
that it requires no labeled data; the sentence provides its own label for the masked word. If
this model is trained on a large corpus of text, it generates pretrained representations that
perform well across a wide variety of NLP tasks (machine translation, question answering,
summarization, grammaticality judgments, and others).
25.6 State of the art
Deep learning and transfer learning have markedly advanced the state of the art for NLP—so
much so that one commentator in 2018 declared that “NLP’s ImageNet moment has arrived”
(Ruder, 2018). The implication is that just as a turning point occurred in 2012 for computer
vision when deep learning systems produced surprising good results in the ImageNet compe-
tition, a turning point occurred in 2018 for NLP. The principal impetus for this turning point
was the ﬁnding that transfer learning works well for natural language problems: a general
language model can be downloaded and ﬁne-tuned for a speciﬁc task.
It started with simple word embeddings from systems such as WORD2VEC in 2013 and
GloVe in 2014. Researchers can download such a model or train their own relatively quickly
without access to supercomputers. Pretrained contextual representations, on the other hand,
are orders of magnitude more expensive to train.
These models became feasible only after hardware advances (GPUs and TPUs) became
widespread, and in this case researchers were grateful to be able to download models rather
than having to spend the resources to train their own. The transformer model allowed for
efﬁcient training of much larger and deeper neural networks than was previously possible
(this time due to software advances, not hardware). Since 2018, new NLP projects typically
start with a pretrained transformer model.
Although these transformer models were trained to predict the next word in a text, they do
a surprisingly good job at other language tasks. A ROBERTA model with some ﬁne-tuning
