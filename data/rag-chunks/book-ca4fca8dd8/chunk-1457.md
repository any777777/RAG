---
chunk_id: "book-ca4fca8dd8-chunk-1457"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1457
confidence: "first-pass"
extraction_method: "structured-local"
---

878
Chapter 24
Natural Language Processing
helps create a better model of French, because it tells us about conjugation (“je” goes with
“comprends,” not “comprend”) and negation (“ne” goes with “pas”); we wouldn’t get that
from regular bigrams alone.
24.1.4 Smoothing n-gram models
High-frequency n-grams like “of the” have high counts in the training corpus, so their proba-
bility estimate is likely to be accurate: with a different training corpus we would get a similar
estimate. Low-frequency n-grams have low counts that are subject to random noise—they
have high variance. Our models will perform better if we can smooth out that variance.
Furthermore, there is always a chance that we will be asked to evaluate a text containing
an unknown or out-of-vocabulary word: one that never appeared in the training corpus. But
Out-of-vocabulary
it would be a mistake to assign such a word a probability of zero, because then the probability
of the whole sentence, P(w1:N), would be zero.
One way to model unknown words is to modify the training corpus by replacing infre-
quent words with a special symbol, traditionally <UNK>. We could decide in advance to
keep only, say, the 50,000 most common words, or all words with frequency greater than
0.0001%, and replace the others with <UNK>. Then compute n-gram counts for the corpus
as usual, treating <UNK> just like any other word. When an unknown word appears in a test
set, we look up its probability under <UNK>. Sometimes different unknown-word symbols
are used for different types. For example, a string of digits might be replaced with <NUM>, or
an email address with <EMAIL>. (We note that it is also advisable to have a special symbol,
such as <S>, to mark the start (and stop) of a text. That way, when the formula for bigram
probabilities asks for the word before the ﬁrst word, the answer is <S>, not an error.)
Even after we’ve handled unknown words, we have the problem of unseen n-grams. For
example, a test text might contain the phrase “colorless aquamarine ideas,” three words that
we may have seen individually in the training corpus, but never in that exact order. The prob-
lem is that some low-probability n-grams appear in the training corpus, while other equally
low-probability n-grams happen to not appear at all. We don’t want some of them to have a
zero probability while others have a small positive probability; we want to apply smoothing
Smoothing
to all the similar n-grams—reserving some of the probability mass of the model for never-
seen n-grams, to reduce the variance of the model.
The simplest type of smoothing was suggested by Pierre-Simon Laplace in the 18th
century to estimate the probability of rare events, such as the sun failing to rise tomorrow.
Laplace’s (incorrect) theory of the solar system suggested it was about N = 2 million days
old. Going by the data, there were zero out of two million days when the sun failed to rise, yet
we don’t want to say that the probability is exactly zero. Laplace showed that if we adopt a
uniform prior, and combine that with the evidence so far, we get a best estimate of 1/(N +2)
for the probability of the sun’s failure to rise tomorrow—either it will or it won’t (that’s the 2
in the denominator) and a uniform prior says it is as likely as not (that’s the 1 in the numera-
tor). Laplace smoothing (also called add-one smoothing) is a step in the right direction, but
for many natural language applications it performs poorly.
Another choice is a backoff model, in which we start by estimating n-gram counts, but
Backoﬀmodel
for any particular sequence that has a low (or zero) count, we back off to (n −1)-grams.
Linear interpolation smoothing is a backoff model that combines trigram, bigram, and
Linear interpolation
smoothing
