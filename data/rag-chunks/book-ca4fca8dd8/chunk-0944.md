---
chunk_id: "book-ca4fca8dd8-chunk-0944"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 944
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 572

572
Chapter 16
Making Complex Decisions
0, 2, 0, 7.2, 0, 0, 0, …
1, 1, 1, 1, 1, 1, 1, …
M
M1
R0, R1, R2, R3, R4, …
λ, λ, λ, λ, λ, λ, λ, …
M
Mλ
(a)
(b)
Figure 16.12 (a) A simple deterministic bandit problem with two arms. The arms can be
pulled in any order, and each yields the sequence of rewards shown. (b) A more general case
of the bandit in (a), where the ﬁrst arm gives an arbitrary sequence of rewards and the second
arm gives a ﬁxed reward λ.
This deﬁnition is very general, covering a wide range of cases. The key property is that the
arms are independent, coupled only by the fact that the agent can work on only one arm at
a time. It’s possible to deﬁne a still more general version in which fractional efforts can be
applied to all arms simultaneously, but the total effort across all arms is bounded; the basic
results described here carry over to this case.
We will see shortly how to formulate a typical bandit problem within this framework, but
let’s warm up with the simple special case of deterministic reward sequences. Let γ =0.5,
and suppose that there are two arms labeled M and M1. Pulling M multiple times yields the
sequence of rewards 0,2,0,7.2,0,0,..., while pulling M1 yields 1,1,1,... (Figure 16.12(a)).
If, at the beginning, one had to commit to one arm or the other and stick with it, the choice
would be made by computing the utility (total discounted reward) for each arm:
U(M) = (1.0×0)+(0.5×2)+(0.52 ×0)+(0.53 ×7.2) = 1.9
U(M1) =
∞
∑
t =0
0.5t = 2.0.
One might think the best choice is to go with M1, but a moment’s more thought shows
that starting with M and then switching to M1 after the fourth reward gives the sequence
S=0,2,0,7.2,1,1,1,..., for which
U(S) = (1.0×0)+(0.5×2)+(0.52 ×0)+(0.53 ×7.2)+
∞
∑
t =4
0.5t = 2.025.
Hence the strategy S that switches from M to M1 at the right time is better than either arm
individually. In fact, S is optimal for this problem: all other switching times give less reward.
Let’s generalize this case slightly, so that now the ﬁrst arm M yields an arbitrary sequence
R0,R1,R2,... (which may be known or unknown) and the second arm Mλ yields λ,λ,λ,...
for some known ﬁxed constant λ (see Figure 16.12(b)). This is called a one-armed bandit
One-armed bandit
in the literature, because it is formally equivalent to the case where there is one arm M that
produces rewards R0,R1,R2,... and costs λ for each pull. (Pulling arm M is equivalent to not

## Page 573
