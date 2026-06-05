---
chunk_id: "book-ca4fca8dd8-chunk-0876"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 876
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.4
Multiattribute Utility Functions
531
(a) 
A
B
C
D
A
B
C
(b) 
This region
dominates A 
X2
X2
X1
X1
Figure 15.4 Strict dominance. (a) Deterministic: Option A is strictly dominated by B but
not by C or D. (b) Uncertain: A is strictly dominated by B but not by C.
Fortunately, there is a more useful generalization called stochastic dominance, which
Stochastic
dominance
occurs very frequently in real problems. Stochastic dominance is easiest to understand in
the context of a single attribute. Suppose we believe that the cost of placing the airport at
S1 is uniformly distributed between $2.8 billion and $4.8 billion and that the cost at S2 is
uniformly distributed between $3 billion and $5.2 billion. Deﬁne the Frugality attribute to
be the negative cost. Figure 15.5(a) shows the distributions for the frugality of sites S1 and
S2. Then, given only the information that the more frugal choice is better (all other things
being equal), we can say that S1 stochastically dominates S2 (i.e., S2 can be discarded). It is
important to note that this does not follow from comparing the expected costs. For example,
if we knew the cost of S1 to be exactly $3.8 billion, then we would be unable to make a
decision without additional information on the utility of money. (It might seem odd that
more information on the cost of S1 could make the agent less able to decide. The paradox
is resolved by noting that in the absence of exact cost information, the decision is easier to
make but is more likely to be wrong.)
The exact relationship between the attribute distributions needed to establish stochastic
dominance is best seen by examining the cumulative distributions, shown in Figure 15.5(b).
If the cumulative distribution for S1 is always to the right of the cumulative distribution for S2,
then, stochastically speaking, S1 is cheaper than S2. Formally, if two actions A1 and A2 lead
to probability distributions p1(x) and p2(x) on attribute X, then A1 stochastically dominates
A2 on X if
∀x
x
Z
−∞
p1(x′) dx′ ≤
x
Z
−∞
p2(x′) dx′ .
The relevance of this deﬁnition to the selection of optimal decisions comes from the following
property: if A1 stochastically dominates A2, then for any monotonically nondecreasing utility ◀
function U(x), the expected utility of A1 is at least as high as the expected utility of A2. To see
why this is true, consider the two expected utilities,
R p1(x)U(x)dx and
R p2(x)U(x)dx. Ini-
tially, it’s not obvious why the ﬁrst integral is bigger than the second, given that the stochastic
dominance condition has a p1-integral that is smaller than the p2-integral.
