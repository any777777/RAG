---
chunk_id: "book-ca4fca8dd8-chunk-1459"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1459
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.1
Language Models
879
unigram models by linear interpolation. It deﬁnes the probability estimate as
ˆP(ci|ci−2:i−1) = λ3P(ci|ci−2:i−1)+λ2P(ci|ci−1)+λ1P(ci),
where λ3 +λ2 +λ1 =1. The parameter values λi can be ﬁxed, or they can be trained with an
expectation–maximization algorithm. It is also possible to have the values of λi depend on
the counts: if we have a high count of trigrams, then we weigh them relatively more; if only
a low count, then we put more weight on the bigram and unigram models.
One camp of researchers has developed ever more sophisticated smoothing techniques
(such as Witten-Bell and Kneser-Ney), while another camp suggests gathering a larger corpus
so that even simple smoothing techniques work well (one such approach is called “stupid
backoff”). Both are getting at the same goal: reducing the variance in the language model.
24.1.5 Word representations
N-grams can give us a model that accurately predicts the probability of word sequences,
telling us that, for example, “a black cat” is a more likely English phrase than “cat black a”
because “a black cat” appears in about 0.000014% of the trigrams in a training corpus, while
“cat black a” does not appear at all. Everything that the n-gram word model knows, it learned
from counts of speciﬁc word sequences.
But a native speaker of English would tell a different story: “a black cat” is valid because
it follows a familiar pattern (article-adjective-noun), while “cat black a” does not.
Now consider the phrase “the fulvous kitten.” An English speaker could recognize this
as also following the article-adjective-noun pattern (even a speaker who does not know that
“fulvous” means “brownish yellow” could recognize that almost all words that end in “-ous”
are adjectives). Furthermore, the speaker would recognize the close syntactic connection
between “a” and “the,” as well as the close semantic relation between “cat” and “kitten.”
Thus, the appearance of “a black cat” in the data is evidence, through generalization, that
“the fulvous kitten” is also valid English.
The n-gram model misses this generalization because it is an atomic model: each word is
an atom, distinct from every other word, with no internal structure. We have seen throughout
this book that factored or structured models allow for more expressive power and better gen-
eralization. We will see in Section 25.1 that a factored model called word embeddings gives
a better ability to generalize.
One type of structured word model is a dictionary, usually constructed through man-
Dictionary
ual labor. For example, WordNet is an open-source, hand-curated dictionary in machine-
WordNet
readable format that has proven useful for many natural language applications1 Below is the
WordNet entry for “kitten:”
"kitten" <noun.animal> ("young domestic cat") IS A: young_mammal
"kitten" <verb.body> ("give birth to kittens")
EXAMPLE: "our cat kittened again this year"
WordNet will help you separate the nouns from the verbs, and get the basic categories (a
kitten is a young mammal, which is a mammal, which is an animal), but it won’t tell you the
details of what a kitten looks like or acts like. WordNet will tell you that two subclasses of
cat are Siamese cat and Manx cat, but won’t tell you any more about the breeds.
1
And even computer vision applications: WordNet provides the set of categories used by ImageNet.
