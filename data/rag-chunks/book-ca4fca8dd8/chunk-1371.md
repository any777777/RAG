---
chunk_id: "book-ca4fca8dd8-chunk-1371"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1371
confidence: "first-pass"
extraction_method: "structured-local"
---

834
Chapter 22
Deep Learning
22.8.2 Natural language processing
Deep learning has also had a huge impact on natural language processing (NLP) applications
such as machine translation and speech recognition. Some advantages of deep learning for
these applications include the possibility of end-to-end learning, the automatic generation
of internal representations for the meanings of words, and the interchangeability of learned
encoders and decoders.
End-to-end learning refers to the construction of entire systems as a single, learned func-
tion f. For example, an f for machine translation might take as input an English sentence
SE and produce an equivalent Japanese sentence SJ = f(SE). Such an f can be learned from
training data in the form of human-translated pairs of sentences (or even pairs of texts, where
the alignment of corresponding sentences or phrases is part of the problem to be solved). A
more classical pipeline approach might ﬁrst parse SE, then extract its meaning, then re-express
the meaning in Japanese as SJ, then post-edit SJ using a language model for Japanese. This
pipeline approach has two major drawbacks: ﬁrst, errors are compounded at each stage; and
second, humans have to determine what constitutes a “parse tree” and a “meaning represen-
tation,” but there is no easily accessible ground truth for these notions, and our theoretical
ideas about them are almost certainly incomplete.
At our present stage of understanding, then, the classical pipeline approach—which, at
least naively, seems to correspond to how a human translator works—is outperformed by the
end-to-end method made possible by deep learning. For example, Wu et al. (2016b) showed
that end-to-end translation using deep learning reduced translation errors by 60% relative to
a previous pipeline-based system. As of 2020, machine translation systems are approaching
human performance for language pairs such as French and English for which very large paired
data sets are available, and they are usable for other language pairs covering the majority of
Earth’s population. There is even some evidence that networks trained on multiple languages
do in fact learn an internal meaning representation: for example, after learning to translate
Portuguese to English and English to Spanish, it is possible to translate Portuguese directly
into Spanish without any Portuguese/Spanish sentence pairs in the training set.
One of the most signiﬁcant ﬁndings to emerge from the application of deep learning
to language tasks is that a great deal deal of mileage comes from re-representing individ-
ual words as vectors in a high-dimensional space—so-called word embeddings (see Sec-
tion 25.1). The vectors are usually extracted from the weights of the ﬁrst hidden layer of
a network trained on large quantities of text, and they capture the statistics of the lexical
contexts in which words are used. Because words with similar meanings are used in similar
contexts, they end up close to each other in the vector space. This allows the network to gen-
eralize effectively across categories of words, without the need for humans to predeﬁne those
categories. For example, a sentence beginning “John bought a watermelon and two pounds
of . . . ” is likely to continue with “apples” or “bananas” but not with “thorium” or “geog-
raphy.” Such a prediction is much easier to make if “apples” and “bananas” have similar
representations in the internal layer.
22.8.3 Reinforcement learning
In reinforcement learning (RL), a decision-making agent learns from a sequence of reward
signals that provide some indication of the quality of its behavior. The goal is to optimize the
sum of future rewards. This can be done in several ways: in the terminology of Chapter 16,
