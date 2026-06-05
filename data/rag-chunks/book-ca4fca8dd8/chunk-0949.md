---
chunk_id: "book-ca4fca8dd8-chunk-0949"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 949
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.3
Bandit Problems
575
(1,1)
(2,1)
(3,1)
(4,1)
(3,2)
(1,2)
(2,2)
(1,3)
(2,3)
(1,4)
R=1
p=1/2
R=0
p=1/2
R=1
p=2/3
R=1
p=3/4
R=0
p=2/3
R=0
p=3/4
0
1/3
1
1/3
0
1/4
1
1/4
1
2/4
0
2/4
 0
 2
 4
 6
 8
 10
s
 0
 2
 4
 6
 8
 10
f
 0
 0.2
 0.4
 0.6
 0.8
 1
Gittins index
(a)
(b)
Figure 16.14 (a) States, rewards, and transition probabilities for the Bernoulli bandit. (b)
Gittins indices for the states of the Bernoulli bandit process.
We cannot quite apply the transformation of the preceding section to calculate the Gittins
index of the Bernoulli arm because it has inﬁnitely many states. We can, however, obtain
a very accurate approximation by solving the truncated MDP with states up to si + fi =100
and γ =0.9. The results are shown in Figure 16.14(b). The results are intuitively reasonable:
we see that, generally speaking, arms with higher payoff probabilities are preferred, but there
is also an exploration bonus associated with arms that have only been tried a few times.
Exploration bonus
For example, the index for the state (3,2) is higher than the index for the state (7,4) (0.7057
vs. 0.6922), even though the estimated value at (3,2) is lower (0.6 vs. 0.6364).
16.3.3 Approximately optimal bandit policies
Calculating Gittins indices for more realistic problems is rarely easy. Fortunately, the general
properties observed in the preceding section—namely, the desirability of some combination
of estimated value and uncertainty—lend themselves to the creation of simple policies that
turn out to be “nearly as good” as optimal policies.
The ﬁrst class of methods uses the upper conﬁdence bound or UCB heuristic, previously
Upper conﬁdence
bound
introduced for Monte Carlo tree search (Figure 6.11 on page 209). The basic idea is to use
the samples from each arm to establish a conﬁdence interval for the value of the arm, that is,
a range within which the value can be estimated to lie with high conﬁdence; then choose the
arm with the highest upper bound on its conﬁdence interval. The upper bound is the current
mean value estimate ˆµi plus some multiple of the standard deviation of the uncertainty in the
value. The standard deviation is proportional to
p
1/Ni, where Ni is the number of times arm
Mi has been sampled. So we have an approximate index value for arm Mi given by
UCB(Mi) = ˆµi +g(N)/√Ni ,
where g(N) is an appropriately chosen function of N, the total number of samples drawn
from all arms. A UCB policy simply picks the arm with the highest UCB value. Notice that
the UCB value is not strictly an index because it depends on N, the total number of samples
drawn across all arms, and not just on the arm itself.
The precise deﬁnition of g determines the regret relative to the clairvoyant policy, which
simply picks the best arm and yields average reward µ∗. A famous result due to Lai and
