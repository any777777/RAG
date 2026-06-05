---
chunk_id: "book-ca4fca8dd8-chunk-1148"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1148
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.4
Model Selection and Optimization
689
19.4.3 Regularization
In Section 19.4.1, we saw how to do model selection with cross-validation. An alternative
approach is to search for a hypothesis that directly minimizes the weighted sum of empirical
loss and the complexity of the hypothesis, which we will call the total cost:
Cost(h) = EmpLoss(h)+λComplexity(h)
ˆh∗= argmin
h∈H
Cost(h).
Here λ is a hyperparameter, a positive number that serves as a conversion rate between loss
and hypothesis complexity. If λ is chosen well, it nicely balances the empirical loss of a
simple function against a complicated function’s tendency to overﬁt.
This process of explicitly penalizing complex hypotheses is called regularization: we’re
Regularization
looking for functions that are more regular. Note that we are now making two choices: the
loss function (L1 or L2), and the complexity measure, which is called a regularization func-
tion. The choice of regularization function depends on the hypothesis space. For example,
Regularization
function
for polynomials, a good regularization function is the sum of the squares of the coefﬁcients—
keeping the sum small would guide us away from the wiggly degree-12 polynomial in Fig-
ure 19.1. We will show an example of this type of regularization in Section 19.6.3.
Another way to simplify models is to reduce the dimensions that the models work with. A
process of feature selection can be performed to discard attributes that appear to be irrelevant.
Feature selection
χ2 pruning is a kind of feature selection.
It is in fact possible to have the empirical loss and the complexity measured on the same
scale, without the conversion factor λ: they can both be measured in bits. First encode
the hypothesis as a Turing machine program, and count the number of bits. Then count
the number of bits required to encode the data, where a correctly predicted example costs
zero bits and the cost of an incorrectly predicted example depends on how large the error is.
The minimum description length or MDL hypothesis minimizes the total number of bits
Minimum
description length
required. This works well in the limit, but for smaller problems the choice of encoding for
the program—how best to encode a decision tree as a bit string—affects the outcome. In
Chapter 21 (page 775), we describe a probabilistic interpretation of the MDL approach.
19.4.4 Hyperparameter tuning
In Section 19.4.1 we showed how to select the best value of the hyperparameter size by
applying cross-validation to each possible value until the validation error rate increases. That
is a good approach when there is a single hyperparameter with a small number of possible
values. But when there are multiple hyperparameters, or when they have continuous values,
it is more difﬁcult to choose good values.
The simplest approach to hyperparameter tuning is hand-tuning: guess some parameter
Hand-tuning
values based on past experience, train a model, measure its performance on the validation
data, analyze the results, and use your intuition to suggest new parameter values. Repeat until
you have satisfactory performance (or you run out of time, computing budget, or patience).
If there are only a few hyperparameters, each with a small number of possible values,
then a more systematic approach called grid search is appropriate: try all combinations of
Grid search
values and see which performs best on the validation data. Different combinations can be
run in parallel on different machines, so if you have sufﬁcient computing resources, this need
