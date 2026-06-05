---
chunk_id: "book-ca4fca8dd8-chunk-0896"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 896
confidence: "first-pass"
extraction_method: "structured-local"
---

542
Chapter 15
Making Simple Decisions
the cost) doesn’t depend on the context provided by w and z. We have
∆= [C(w)+F(w)C(xyz)]−[C(w)+F(w)C(yxz)]
(by Equation (15.3))
= F(w)[C(xyz)−C(yxz)]
= F(w)[(C(xy)+F(xy)C(z))−(C(yx)+F(yx)C(z))]
(by Equation (15.3))
= F(w)[C(xy)−C(yx)]
(since F(xy)=F(yx)).
So we have shown that the direction of the change in the cost of the whole sequence depends
only on the direction of the change in cost of the pair of elements being ﬂipped; the context
of the pair doesn’t matter. This gives us a way to sort the sequence by pairwise comparisons
to obtain an optimal solution. Speciﬁcally, we now have
∆= F(w)[(C(x)+F(x)C(y))−(C(y)+F(y)C(x))]
(by Equation (15.3))
= F(w)[C(x)(1−F(y))−C(y)(1−F(x))] = F(w)[C(x)P(y)−C(y)P(x)].
This holds for any sequences x and y, so it holds speciﬁcally when x and y are single ob-
servations of locations i and j, respectively. So we know that, for i and j to be adjacent
in an optimal sequence, we must have C(i)P(j) ≤C(j)P(i), or P(i)
C(i) ≥P(j)
C(j). In other words,
the optimal order ranks the locations according to the success probability per unit cost. Ex-
ercise 15.HUNT asks you to determine whether this is in fact the policy followed by the
algorithm in Figure 15.9 for this problem.
15.6.6 Sensitivity analysis and robust decisions
The practice of sensitivity analysis is widespread in technological disciplines: it means an-
Sensitivity analysis
alyzing how much the output of a process changes as the model parameters are tweaked.
Sensitivity analysis in probabilistic and decision-theoretic systems is particularly important
because the probabilities used are typically either learned from data or estimated by human
experts, which means that they are themselves subject to considerable uncertainty. Only in
rare cases, such as the dice rolls in backgammon, are the probabilities objectively known.
For a utility-driven decision-making process, you can think of the output as either the
actual decision made or the expected utility of that decision. Consider the latter ﬁrst: because
expectation depends on probabilities from the model, we can compute the derivative of the
expected utility of any given action with respect to each of those probability values. (For
example, if all the conditional probability distributions in the model are explicitly tabulated,
then computing the expectation involves computing a ratio of two sum-of-product expres-
sions; for more on this, see Chapter 21.) Thus, one can determine which parameters in the
model have the largest effect on the expected utility of the ﬁnal decision.
If, instead, we are concerned about the actual decision made, rather than its utility ac-
cording to the model, then we can simply vary the parameters systematically (perhaps using
binary search) to see whether the decision changes, and, if so, what is the smallest perturba-
tion that causes such a change. One might think it doesn’t matter that much which decision
is made, only what its utility is. That’s true, but in practice there may be a very substantial
difference between the real utility of a decision and the utility according to the model.
If all reasonable perturbations of the parameters leave the optimal decision unchanged,
then it is reasonable to assume the decision is a good one, even if the utility estimate for
that decision is substantially incorrect. If, on the other hand, the optimal decision changes
considerably as the parameters of the model change, then there is a good chance that the
