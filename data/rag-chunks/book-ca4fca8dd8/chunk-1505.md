---
chunk_id: "book-ca4fca8dd8-chunk-1505"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1505
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 25
DEEP LEARNING FOR NATURAL
LANGUAGE PROCESSING
In which deep neural networks perform a variety of language tasks, capturing the structure
of natural language as well as its ﬂuidity.
Chapter 24 explained the key elements of natural language, including grammar and semantics.
Systems based on parsing and semantic analysis have demonstrated success on many tasks,
but their performance is limited by the endless complexity of linguistic phenomena in real
text. Given the vast amount of text available in machine-readable form, it makes sense to
consider whether approaches based on data-driven machine learning can be more effective.
We explore this hypothesis using the tools provided by deep learning systems (Chapter 22).
We begin in Section 25.1 by showing how learning can be improved by representing
words as points in a high-dimensional space, rather than as atomic values. Section 25.2
covers the use of recurrent neural networks to capture meaning and long-distance context as
text is processed sequentially. Section 25.3 focuses primarily on machine translation, one of
the major successes of deep learning applied to NLP. Sections 25.4 and 25.5 cover models
that can be trained from large amounts of unlabeled text and then applied to speciﬁc tasks,
often achieving state-of-the-art performance. Finally, Section 25.6 takes stock of where we
are and how the ﬁeld may progress.
25.1 Word Embeddings
We would like a representation of words that does not require manual feature engineering, but
allows for generalization between related words—words that are related syntactically (“col-
orless” and “ideal” are both adjectives), semantically (“cat” and “kitten” are both felines),
topically (“sunny” and “sleet” are both weather terms), in terms of sentiment (“awesome”
has opposite sentiment to “cringeworthy”), or otherwise.
How should we encode a word into an input vector x for use in a neural network? As
explained in Section 22.2.1 (page 807), we could use a one-hot vector—that is, we encode
the ith word in the dictionary with a 1 bit in the ith input position and a 0 in all the other
positions. But such a representation would not capture the similarity between words.
Following the linguist John R. Firth’s (1957) maxim, “You shall know a word by the com-
pany it keeps,” we could represent each word with a vector of n-gram counts of all the phrases
that the word appears in. However, raw n-gram counts are cumbersome. With a 100,000-word
vocabulary, there are 1025 5-grams to keep track of (although vectors in this 1025-dimensional
space would be quite sparse—most of the counts would be zero). We would get better gen-
