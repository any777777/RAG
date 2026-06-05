---
chunk_id: "book-ca4fca8dd8-chunk-1538"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1538
confidence: "first-pass"
extraction_method: "structured-local"
---

928
Chapter 25
Deep Learning for Natural Language Processing
There are limitations of ARISTO. It deals only with multiple-choice questions, not essay
questions, and it can neither read nor generate diagrams.1
T5 (the Text-to-Text Transfer Transformer) is designed to produce textual responses to
various kinds of textual input. It includes a standard encoder–decoder transformer model,
pretrained on 35 billion words from the 750 GB Colossal Clean Crawled Corpus (C4). This
unlabeled training is designed to give the model generalizable linguistic knowledge that will
be useful for multiple speciﬁc tasks. T5 is then trained for each task with input consisting of
the task name, followed by a colon and some content. For example, when given “translate
English to German: That is good,” it produces as output “Das ist gut.” For some tasks, the
input is marked up; for example in the Winograd Schema Challenge, the input highlights a
pronoun with an ambiguous referent. Given the input “referent: The city councilmen refused
the demonstrators a permit because they feared violence,” the correct response is “The city
councilmen” (not “the demonstrators”).
Much work remains to be done to improve NLP systems. One issue is that transformer
models rely on only a narrow context, limited to a few hundred words. Some experimental
approaches are trying to extend that context; the Reformer system (Kitaev et al., 2020) can
handle context of up to a million words.
Recent results have shown that using more training data results in better models—for
example, ROBERTA achieved state-of-the-art results after training on 2.2 trillion words. If
using more textual data is better, what would happen if we included other types of data:
structured databases, numerical data, images, and video? We would need a breakthrough in
hardware processing speeds to train on a large corpus of video, and we may need several
breakthroughs in AI as well.
The curious reader may wonder why we learned about grammars, parsing, and semantic
interpretation in the previous chapter, only to discard those notions in favor of purely data-
driven models in this chapter? At present, the answer is simply that the data-driven models
are easier to develop and maintain, and score better on standard benchmarks, compared to
the hand-built systems that can be constructed using a reasonable amount of human effort
with the approaches described in Chapter 24. It may be that transformer models and their
relatives are learning latent representations that capture the same basic ideas as grammars
and semantic information, or it may be that something entirely different is happening within
these enormous models; we simply don’t know. We do know that a system that is trained with
textual data is easier to maintain and to adapt to new domains and new natural languages than
a system that relies on hand-crafted features.
It may also be the case that future breakthroughs in explicit grammatical and semantic
modeling will cause the pendulum to swing back. Perhaps more likely is the emergence of
hybrid approaches that combine the best concepts from both chapters. For example, Kitaev
and Klein (2018) used an attention mechanism to improve a traditional constituency parser,
achieving the best result ever recorded on the Penn Treebank test set. Similarly, Ringgaard
et al. (2017) demonstrate how a dependency parser can be improved with word embeddings
and a recurrent neural network. Their system, SLING, parses directly into a semantic frame
representation, mitigating the problem of errors building up in a traditional pipeline system.
1
It has been pointed out that in some multiple-choice exams, it is possible to get a good score even without
looking at the questions, because there are tell-tale signs in the incorrect answers (Gururangan et al., 2018). That
seems to be true for visual question answering as well (Chao et al., 2018) .
