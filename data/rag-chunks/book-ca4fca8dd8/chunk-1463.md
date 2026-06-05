---
chunk_id: "book-ca4fca8dd8-chunk-1463"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1463
confidence: "first-pass"
extraction_method: "structured-local"
---

882
Chapter 24
Natural Language Processing
The question then is what should the features be? POS taggers typically use binary-
valued features that encode information about the word being tagged, wi (and perhaps other
nearby words), as well as the category that was assigned to the previous word, ci−1 (and
perhaps the category of earlier words). Features can depend on the exact identity of a word,
some aspects of the way it is spelled, or some attribute from a dictionary entry. A set of POS
tagging features might include:
wi−1 =“I”
wi+1 =“for”
wi−1 =“you”
ci−1 =IN
wi ends with “ous”
wi contains a hyphen
wi ends with “ly”
wi contains a digit
wi starts with “un”
wi is all uppercase
wi−2 = “to” and ci−1 =VB
wi−2 has attribute PRESENT
wi−1 = “I” and wi+1 =“to”
wi−2 has attribute PAST
For example, the word “walk” can be a noun or a verb, but in “I walk to school,” the feature
in the last row, left column could be used to classify “walk” as a verb (VBP). As another
example, the word “cut” can be either a noun (NN), past tense verb (VBD), or present tense
verb (VBP). Given the sentence “Yesterday I cut the rope,” the feature in the last row, right
column could help tag “cut” as VBD, while in the sentence “Now I cut the rope,” the feature
above that one could help tag “cut” as VBP.
All together, there might be a million features, but for any given word, only a few dozen
will be nonzero. The features are usually hand-crafted by a human system designer who
thinks up interesting feature templates.
Logistic regression does not have the notion of a sequence of inputs—you give it a single
feature vector (information about a single word) and it produces an output (a tag). But we
can force logistic regression to handle a sequence with a greedy search: start by choosing
the most likely category for the ﬁrst word, and proceed to the rest of the words in left-to-right
order. At each step the category ci is assigned according to
ci =
argmax
c′∈Categories
P(c′ |w1:N,c1:i−1).
That is, the classiﬁer is allowed to look at any of the non-category features for any of the
words anywhere in the sentence (because these features are all ﬁxed), as well as any previ-
ously assigned categories.
Note that the greedy search makes a deﬁnitive category choice for each word, and then
moves on to the next word; if that choice is contradicted by evidence later in the sentence,
there is no possibility to go back and reverse the choice. That makes the algorithm fast. The
Viterbi algorithm, in contrast, keeps a table of all possible category choices at each step, and
always has the option of changing. That makes the algorithm more accurate, but slower.
For both algorithms, a compromise is a beam search, in which we consider every possible
category at each time step, but then only keep the b most likely tags, dropping the other
less-likely tags. Changing b trades off speed versus accuracy.
Naive Bayes and Hidden Markov models are generative models (see Section 21.2.3).
That is, they learn a joint probability distribution, P(W,C), and we can generate a random
sentence by sampling from that probability distribution to get a ﬁrst word (with category) of
the sentence, and then adding words one at a time.
