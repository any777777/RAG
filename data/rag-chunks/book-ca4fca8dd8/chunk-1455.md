---
chunk_id: "book-ca4fca8dd8-chunk-1455"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1455
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.1
Language Models
877
24.1.2 N-gram word models
The bag-of-words model has limitations. For example, the word “quarter” is common in
both the business and sports categories. But the four-word sequence “ﬁrst quarter earnings
report” is common only in business and “fourth quarter touchdown passes” is common only
in sports. We’d like our model to make that distinction. We could tweak the bag-of-words
model by treating special phrases like “ﬁrst-quarter earnings report” as if they were single
words, but a more principled approach is to introduce a new model, where each word is
dependent on previous words. We can start by making a word dependent on all previous
words in a sentence:
P(w1:N) =
N
∏
j=1
P(w j |w1: j−1).
This model is in a sense perfectly “correct” in that it captures all possible interactions between
words, but it is not practical: with a vocabulary of 100,000 words and a sentence length of
40, this model would have 10200 parameters to estimate. We can compromise with a Markov
chain model that considers only the dependence between n adjacent words. This is known
as an n-gram model (from the Greek root gramma meaning “written thing”): a sequence of
N-gram model
written symbols of length n is called an n-gram, with special cases “unigram” for 1-gram,
“bigram” for 2-gram, and “trigram” for 3-gram. In an n-gram model, the probability of each
word is dependent only on the n−1 previous words; that is:
P(w j |w1:j−1) = P(w j |w j−n+1:j−1)
P(w1:N) =
N
∏
j=1
P(w j |w j−n+1:j−1).
N-gram models work well for classifying newspaper sections, as well as for other classiﬁ-
cation tasks such as spam detection (distinguishing spam email from non-spam), sentiment
Spam detection
analysis (classifying a movie or product review as positive or negative) and author attribu-
Sentiment analysis
tion (Hemingway has a different style and vocabulary than Faulkner or Shakespeare).
Author attribution
24.1.3 Other n-gram models
An alternative to an n-gram word model is a character-level model in which the probability
Character-level
model
of each character is determined by the n −1 previous characters. This approach is helpful
for dealing with unknown words, and for languages that tend to run words together, as in the
Danish word “Speciallægepraksisplanlægningsstabiliseringsperiode.”
Character-level models are well suited for the task of language identiﬁcation: given a
Language
identiﬁcation
text, determine what language it is written in. Even with very short texts such as “Hello,
world” or “Wie geht’s dir,” n-gram letter models can identify the ﬁrst as English and the sec-
ond as German, generally achieving accuracy greater than 99%. (Closely related languages
such as Swedish and Norwegian are more difﬁcult to distinguish and require longer samples;
there, accuracy is in the 95% range.) Character models are good at certain classiﬁcation tasks,
such as deciding that “dextroamphetamine” is a drug name, “Kallenberger” is a person name,
and “Plattsburg” is a city name, even if we have never seen these words before.
Another possibility is the skip-gram model, in which we count words that are near each
Skip-gram
other, but skip a word (or more) between them. For example, given the French text “je
ne comprends pas” the 1-skip-bigrams are “je comprends,” and “ne pas.” Gathering these
