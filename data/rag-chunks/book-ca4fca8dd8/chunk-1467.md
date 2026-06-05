---
chunk_id: "book-ca4fca8dd8-chunk-1467"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1467
confidence: "first-pass"
extraction_method: "structured-local"
---

884
Chapter 24
Natural Language Processing
• These models can also do better if their samples are chosen at random, rather than by an
expert in the domain. However, as a general rule, n-gram and language models that include a
large number of features tend to produce text better, since these features contribute the most to
language learning. To measure the performance of a model, I’ve made some sample sentences
that I’d like to train to better understand speech and language models. You can read them to get
a grasp of how the model predicts.
We see that these passages are diverse and grammatically ﬂuent; moreover, they stick to top-
ics that are relevant to the prompt sentences. But the sentences do not build on each other to
advance a coherent thesis. The GPT-2 language model is known as a transformer model,
which will be covered in Section 25.4; further examples from GPT-2 are in Figure 25.14.
Another transformer model is the Conditional Transformer Language, CTRL. It can be con-
trolled more ﬂexibly; in the following samples CTRL was asked to generate text in the cate-
gory product reviews, with a rating of 1 and of 4 (out of 5): speciﬁed rating (out of 5):
• 1.0: I bought this for my son who is a huge fan of the show. He was so excited to get it and when
he opened it, we were all very disappointed. The quality of the product is terrible. It looks like
something you would buy at a dollar store.
• 4.0: I bought this for my husband and he loves it. He has a small wrist so it is hard to ﬁnd
watches that ﬁt him well. This one ﬁts perfectly.
24.2 Grammar
In Chapter 7 we used Backus–Naur Form (BNF) to write down a grammar for the language
of ﬁrst-order logic. A grammar is a set of rules that deﬁnes the tree structure of allowable
phrases, and a language is the set of sentences that follow those rules.
Natural languages do not work exactly like the formal language of ﬁrst-order logic—they
do not have a hard boundary between allowable and unallowable sentences, nor do they have a
single deﬁnitive tree structure for each sentence. However, hierarchical structure is important
in natural language. The word “Stocks” in “Stocks rallied on Monday” is not just a word,
nor is it just a noun; in this sentence it also comprises a noun phrase, which is the subject
of the following verb phrase. Syntactic categories such as noun phrase or verb phrase help
Syntactic category
to constrain the probable words at each point within a sentence, and the phrase structure
Phrase structure
provides a framework for the meaning or semantics of the sentence.
There are many competing language models based on the idea of hierarchical syntactic
structure; in this section we will describe a popular model called the probabilistic context-
free grammar, or PCFG. A probabilistic grammar assigns a probability to each string, and
Probabilistic
context-free
grammar
“context-free” means that any rule can be used in any context: the rules for a noun phrase at
the beginning of a sentence are the same as for another noun phrase later in the sentence, and
if the same phrase occurs in two locations, it must have the same probability each time. We
will deﬁne a PCFG grammar for a tiny fragment of English that is suitable for communication
between agents exploring the wumpus world. We call this language E0 (see Figure 24.2). A
grammar rule such as
Adjs →Adjective
[0.80]
|
Adjective Adjs [0.20]
means that the syntactic category Adjs can consist of either a single Adjective, with probability
0.80, or of an Adjective followed by a string that constitutes an Adjs, with probability 0.20.
