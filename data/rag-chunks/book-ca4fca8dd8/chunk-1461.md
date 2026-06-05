---
chunk_id: "book-ca4fca8dd8-chunk-1461"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1461
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.1
Language Models
881
tagging. Although not very interesting in its own right, it is a useful ﬁrst step in many other
Part-of-speech
tagging
NLP tasks, such as question answering or translation. Even for a simple task like text-to-
speech synthesis, it is important to know that the noun “record” is pronounced differently
from the verb “record.” In this section we will see how two familiar models can be applied to
the tagging task, and in Chapter 25 we will consider a third model.
One common model for POS tagging is the hidden Markov model (HMM). Recall from
Section 14.3 that a hidden Markov model takes in a temporal sequence of evidence observa-
tions and predicts the most likely hidden states that could have produced that sequence. In
the HMM example on page 491, the evidence consisted of observations of a person carrying
an umbrella (or not), and the hidden state was rain (or not) in the outside world. For POS
tagging, the evidence is the sequence of words, W1:N, and the hidden states are the lexical
categories, C1:N.
The HMM is a generative model that says that the way to produce language is to start in
one state, such as IN, the state for prepositions, and then make two choices: what word (such
as from) should be emitted, and what state (such as DT) should come next. The model does
not consider any context other than the current part-of-speech state, nor does it have any idea
of what the sentence is actually trying to convey. And yet it is a useful model—if we apply
the Viterbi algorithm (Section 14.2.3) to ﬁnd the most probable sequence of hidden states
Viterbi algorithm
(tags), we ﬁnd that the tagging achieves very high accuracy; usually around 97%.
To create a HMM for POS tagging, we need the transition model, which gives the prob-
ability of one part of speech following another, P(Ct |Ct−1), and the sensor model, P(Wt |Ct).
For example, P(Ct =VB|Ct−1 =MD)=0.8 means that given a modal verb (such as would),
we can expect the following word to be a verb (such as think) with probability 0.8. Where
does the 0.8 number come from? Just as with n-gram models, from counts in the corpus,
with appropriate smoothing. It turns out that there are 13124 instances of MD in the Penn
Treebank, and 10471 of them are followed by a VB.
For the sensor model, P(Wt =would|Ct =MD)=0.1 means that when we are choosing a
modal verb, we will choose would 10% of the time. These numbers also come from corpus
counts, with smoothing.
A weakness of HMM models is that everything we know about language has to be ex-
pressed in terms of the transition and sensor models. The part of speech for the current word
is determined solely by the probabilities in these two models and by the part of speech of
the previous word. There is no easy way for a system developer to say, for example, that
any word that ends in “ous” is likely an adjective, nor that in the phrase “attorney general,”
attorney is a noun, not an adjective.
Fortunately, logistic regression does have the ability to represent information like this.
Recall from Section 19.6.5 that in a logistic regression model, the input is a vector, x, of
feature values. We then take the dot product, w·x, of those features with a pretrained vector
of weights w, and transform that sum into a number between 0 and 1 that can be interpreted
as the probability that the input is a positive example of a category.
The weights in the logistic regression model correspond to how predictive each feature
is for each category; the weight values are learned by gradient descent. For POS tagging
we would build 45 different logistic regression models, one for each part of speech, and ask
each model how probable it is that the example word is a member of that category, given the
feature values for that word in its particular context.
