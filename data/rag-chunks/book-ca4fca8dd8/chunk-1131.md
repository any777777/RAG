---
chunk_id: "book-ca4fca8dd8-chunk-1131"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1131
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 680

680
Chapter 19
Learning from Examples
P(vk) is deﬁned as
Entropy:
H(V) = ∑
k
P(vk)log2
1
P(vk) = −∑
k
P(vk)log2 P(vk).
We can check that the entropy of a fair coin ﬂip is indeed 1 bit:
H(Fair) = −(0.5log2 0.5+0.5log2 0.5) = 1 .
And of a four-sided die is 2 bits:
H(Die4) = −(0.25log2 0.25+0.25log2 0.25+0.25log2 0.25+0.25log2 0.25) = 2
For the loaded coin with 99% heads, we get
H(Loaded) = −(0.99log2 0.99+0.01log2 0.01) ≈0.08 bits.
It will help to deﬁne B(q) as the entropy of a Boolean random variable that is true with
probability q:
B(q)=−(qlog2 q+(1−q)log2(1−q)).
Thus, H(Loaded)=B(0.99) ≈0.08. Now let’s get back to decision tree learning. If a training
set contains p positive examples and n negative examples, then the entropy of the output
variable on the whole set is
H(Output) = B

p
p+n

.
The restaurant training set in Figure 19.2 has p = n = 6, so the corresponding entropy is
B(0.5) or exactly 1 bit. The result of a test on an attribute A will give us some information,
thus reducing the overall entropy by some amount. We can measure this reduction by looking
at the entropy remaining after the attribute test.
An attribute A with d distinct values divides the training set E into subsets E1,...,Ed.
Each subset Ek has pk positive examples and nk negative examples, so if we go along that
branch, we will need an additional B(pk/(pk +nk)) bits of information to answer the question.
A randomly chosen example from the training set has the kth value for the attribute (i.e., is
in Ek with probability (pk + nk)/(p + n)), so the expected entropy remaining after testing
attribute A is
Remainder(A) =
d
∑
k=1
pk+nk
p+n B(
pk
pk+nk ).
The information gain from the attribute test on A is the expected reduction in entropy:
Information gain
Gain(A) = B(
p
p+n)−Remainder(A).
In fact Gain(A) is just what we need to implement the IMPORTANCE function. Returning to
the attributes considered in Figure 19.4, we have
Gain(Patrons) = 1−
 2
12B(0
2)+ 4
12B(4
4)+ 6
12B(2
6)

≈0.541 bits,
Gain(Type) = 1−
 2
12B(1
2)+ 2
12B(1
2)+ 4
12B(2
4)+ 4
12B(2
4)

= 0 bits,
conﬁrming our intuition that Patrons is a better attribute to split on ﬁrst. In fact, Patrons
has the maximum information gain of any of the attributes and thus would be chosen by the
decision tree learning algorithm as the root.

## Page 681
