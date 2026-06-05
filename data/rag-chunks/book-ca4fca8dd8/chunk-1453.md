---
chunk_id: "book-ca4fca8dd8-chunk-1453"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1453
confidence: "first-pass"
extraction_method: "structured-local"
---

876
Chapter 24
Natural Language Processing
a generative model that describes a process for generating a sentence: Imagine that for each
category (business, weather, etc.) we have a bag full of words (you can imagine each word
written on a slip of paper inside the bag; the more common the word, the more slips it is
duplicated on). To generate text, ﬁrst select one of the bags and discard the others. Reach
into that bag and pull out a word at random; this will be the ﬁrst word of the sentence. Then
put the word back and draw a second word. Repeat until an end-of-sentence indicator (e.g., a
period) is drawn.
This model is clearly wrong: it falsely assumes that each word is independent of the
others, and therefore it does not generate coherent English sentences. But it does allow us to
do classiﬁcation with good accuracy using the naive Bayes formula: the words “stocks” and
“earnings” are clear evidence for the business section, while “rain” and “cloudy” suggest the
weather section.
We can learn the prior probabilities needed for this model via supervised training on a
body or corpus of text, where each segment of text is labeled with a class. A corpus typically
Corpus
consists of at least a million words of text, and at least tens of thousands of distinct vocabulary
words. Recently we are seeing even larger corpuses being used, such as the 2.5 billion words
in Wikipedia or the 14 billion word iWeb corpus scraped from 22 million web pages.
From a corpus we can estimate the prior probability of each category, P(Class), by count-
ing how common each category is. We can also use counts to estimate the conditional prob-
ability of each word given the category, P(wj |Class). For example, if we’ve seen 3000 texts
and 300 of them were classiﬁed as business, then we can estimate P(Class = business) ≈
300/3000 = 0.1. And if within the business category we have seen 100,000 words and
the word “stocks” appeared 700 times, then we can estimate P(stocks|Class=business) ≈
700/100,000=0.007. Estimation by counting works well when we have high counts (and
low variance), but we will see in Section 24.1.4 a better way to estimate probabilities when
the counts are low.
Sometimes a different machine learning approach, such as logistic regression, neural
networks, or support vector machines, can work even better than naive Bayes. The features of
the machine learning model are the words in the vocabulary: “a,” “aardvark,” ..., “zyzzyva,”
and the values are the number of times each word appears in the text (or sometimes just a
Boolean value indicating whether the word appears or not). That makes the feature vector
large and sparse—we might have 100,000 words in the language model, and thus a feature
vector of length 100,000, but for a short text almost all the features will be zero.
As we have seen, some machine learning models work better when we do feature selec-
tion, limiting ourselves to a subset of the words as features. We could drop words that are
very rare (and thus have high variance in their predictive powers), as well as words that are
common to all classes (such as “the”) but don’t discriminate between classes. We can also
mix other features in with our word-based features; for example if we are classifying email
messages we could add features for the sender, the time the message was sent, the words
in the subject header, the presence of nonstandard punctuation, the percentage of uppercase
letters, whether there is an attachment, and so on.
Note it is not trivial to decide what a word is. Is “aren’t” one word, or should it be broken
up as “aren/’/t” or “are/n’t,” or something else? The process of dividing a text into a sequence
of words is called tokenization.
Tokenization
