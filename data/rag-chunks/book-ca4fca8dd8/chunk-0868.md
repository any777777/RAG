---
chunk_id: "book-ca4fca8dd8-chunk-0868"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 868
confidence: "first-pass"
extraction_method: "structured-local"
---

526
Chapter 15
Making Simple Decisions
insurance premiums are positive. People would rather pay a small insurance premium than
gamble the price of their house against the chance of a ﬁre. From the insurance company’s
point of view, the price of the house is very small compared with the ﬁrm’s total reserves.
This means that the insurer’s utility curve is approximately linear over such a small region,
and the gamble costs the company almost nothing.
Notice that for small changes in wealth relative to the current wealth, almost any curve
will be approximately linear. An agent that has a linear curve is said to be risk-neutral. For
Risk-neutral
gambles with small sums, therefore, we expect risk neutrality. In a sense, this justiﬁes the
simpliﬁed procedure that proposed small gambles to assess probabilities and to justify the
axioms of probability in Section 12.2.3.
15.3.3 Expected utility and post-decision disappointment
The rational way to choose the best action, a∗, is to maximize expected utility:
a∗= argmax
a
EU(a).
If we have calculated the expected utility correctly according to our probability model, and if
the probability model correctly reﬂects the underlying stochastic processes that generate the
outcomes, then, on average, we will get the utility we expect if the whole process is repeated
many times.
In reality, however, our model usually oversimpliﬁes the real situation, either because we
don’t know enough (e.g., when making a complex investment decision) or because the com-
putation of the true expected utility is too difﬁcult (e.g., when making a move in backgammon,
needing to take into account all possible future dice rolls). In that case, we are really working
with estimates c
EU(a) of the true expected utility. We will assume, kindly perhaps, that the
estimates are unbiased—that is, the expected value of the error, E( c
EU(a)−EU(a)), is zero.
Unbiased
In that case, it still seems reasonable to choose the action with the highest estimated utility
and to expect to receive that utility, on average, when the action is executed.
Unfortunately, the real outcome will usually be signiﬁcantly worse than we estimated,
even though the estimate was unbiased! To see why, consider a decision problem in which
there are k choices, each of which has true estimated utility of 0. Suppose that the error in
each utility estimate is independent and has a unit normal distribution—that is, a Gaussian
with zero mean and standard deviation of 1, shown as the bold curve in Figure 15.3. Now, as
we actually start to generate the estimates, some of the errors will be negative (pessimistic)
and some will be positive (optimistic). Because we select the action with the highest utility
estimate, we are favoring the overly optimistic estimates, and that is the source of the bias.
It is a straightforward matter to calculate the distribution of the maximum of the k es-
timates and hence quantify the extent of our disappointment. (This calculation is a special
case of computing an order statistic, the distribution of any particular ranked element of a
Order statistic
sample.) Suppose that each estimate Xi has a probability density function f(x) and cumula-
tive distribution F(x). (As explained in Appendix A, the cumulative distribution F measures
the probability that the cost is less than or equal to any given amount—that is, it integrates
the original density f.) Now let X∗be the largest estimate, i.e., max{X1,...,Xk}. Then the
cumulative distribution for X∗is
P(max{X1,...,Xk} ≤x) = P(X1 ≤x,...,Xk ≤x)
= P(X1 ≤x)...P(Xk ≤x) = F(x)k .
