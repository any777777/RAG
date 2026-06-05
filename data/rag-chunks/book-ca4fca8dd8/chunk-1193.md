---
chunk_id: "book-ca4fca8dd8-chunk-1193"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1193
confidence: "first-pass"
extraction_method: "structured-local"
---

720
Chapter 19
Learning from Examples
function ADABOOST(examples,L,K) returns a hypothesis
inputs: examples, set of N labeled examples (x1,y1),...,(xN,yN)
L, a learning algorithm
K, the number of hypotheses in the ensemble
local variables: w, a vector of N example weights, initially all 1/N
h, a vector of K hypotheses
z, a vector of K hypothesis weights
ϵ←a small positive number, used to avoid division by zero
for k = 1 to K do
h[k]←L(examples,w)
error←0
for j = 1 to N do
// Compute the total error for h[k]
if h[k](xj) ̸= y j then error←error + w[j]
if error > 1/2 then break from loop
error←min(error, 1 −ϵ)
for j = 1 to N do
// Give more weight to the examples h[k] got wrong
if h[k](xj) = yj then w[j]←w[j]· error/(1−error)
w←NORMALIZE(w)
z[k]←1
2 log((1−error)/error)
// Give more weight to accurate h[k]
return Function(x) : ∑zi hi(x)
Figure 19.25 The ADABOOST variant of the boosting method for ensemble learning. The
algorithm generates hypotheses by successively reweighting the training examples. The func-
tion WEIGHTED-MAJORITY generates a hypothesis that returns the output value with the
highest vote from the hypotheses in h, with votes weighted by z. For regression problems, or
for binary classiﬁcation with two classes -1 and 1, this is ∑k h[k]z[k].
model, we are updating the parameters of the next tree—but we must do that in a way that
reduces the loss by moving in the right direction along the gradient.
As in the models we saw in Section 19.4.3, regularization can help prevent overﬁtting.
That can come in the form of limiting the number of trees or their size (in terms of their depth
or number of nodes). It can come from the learning rate, α, which says how far to move along
the direction of the gradient; values in the range 0.1 to 0.3 are common, and the smaller the
learning rate, the more trees we will need in the ensemble.
Gradient boosting is implemented in the popular XGBOOST (eXtreme Gradient Boost-
ing) package, which is routinely used for both large-scale applications in industry (for prob-
lems with billions of examples), and by the winners of data science competitions (in 2015, it
was used by every team in the top 10 of the KDDCup). XGBOOST does gradient boosting
with pruning and regularization, and takes care to be efﬁcient, carefully organizing memory
to avoid cache misses, and allowing for parallel computation on multiple machines.
19.8.6 Online learning
So far, everything we have done in this chapter has relied on the assumption that the data are
i.i.d. (independent and identically distributed). On the one hand, that is a sensible assumption:
if the future bears no resemblance to the past, then how can we predict anything? On the other
