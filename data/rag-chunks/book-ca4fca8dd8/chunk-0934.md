---
chunk_id: "book-ca4fca8dd8-chunk-0934"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 934
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.2
Algorithms for MDPs
565
With this deﬁnition, the “distance” between two vectors, ∥U −U′∥, is the maximum dif-
ference between any two corresponding elements. The main result of this section is the
following: Let Ui and U′
i be any two utility vectors. Then we have
∥BUi −BU′
i ∥≤γ ∥Ui −U′
i ∥.
(16.11)
That is, the Bellman update is a contraction by a factor of γ on the space of utility vectors. ◀
(Exercise 16.VICT provides some guidance on proving this claim.) Hence, from the properties
of contractions in general, it follows that value iteration always converges to a unique solution
of the Bellman equations whenever γ < 1.
We can also use the contraction property to analyze the rate of convergence to a solu-
tion. In particular, we can replace U′
i in Equation (16.11) with the true utilities U, for which
BU =U. Then we obtain the inequality
∥BUi −U∥≤γ ∥Ui −U∥.
If we view ∥Ui −U∥as the error in the estimate Ui, we see that the error is reduced by a factor
of at least γ on each iteration. Thus, value iteration converges exponentially fast. We can
calculate the number of iterations required as follows: First, recall from Equation (16.1) that
the utilities of all states are bounded by ±Rmax/(1−γ). This means that the maximum initial
error ∥U0 −U∥≤2Rmax/(1−γ). Suppose we run for N iterations to reach an error of at most
ϵ. Then, because the error is reduced by at least γ each time, we require γN ·2Rmax/(1−γ) ≤
ϵ. Taking logs, we ﬁnd that
N =⌈log(2Rmax/ϵ(1−γ))/log(1/γ)⌉
iterations sufﬁce. Figure 16.7(b) shows how N varies with γ, for different values of the ratio
ϵ/Rmax. The good news is that, because of the exponentially fast convergence, N does not
depend much on the ratio ϵ/Rmax. The bad news is that N grows rapidly as γ becomes close
to 1. We can get fast convergence if we make γ small, but this effectively gives the agent a
short horizon and could miss the long-term effects of the agent’s actions.
The error bound in the preceding paragraph gives some idea of the factors inﬂuencing the
run time of the algorithm, but is sometimes overly conservative as a method of deciding when
to stop the iteration. For the latter purpose, we can use a bound relating the error to the size of
the Bellman update on any given iteration. From the contraction property (Equation (16.11)),
it can be shown that if the update is small (i.e., no state’s utility changes by much), then the
error, compared with the true utility function, also is small. More precisely,
if
∥Ui+1 −Ui∥< ϵ(1−γ)/γ
then
∥Ui+1 −U∥< ϵ.
(16.12)
This is the termination condition used in the VALUE-ITERATION algorithm of Figure 16.6.
So far, we have analyzed the error in the utility function returned by the value iteration
algorithm. What the agent really cares about, however, is how well it will do if it makes its ◀
decisions on the basis of this utility function. Suppose that after i iterations of value iteration,
the agent has an estimate Ui of the true utility U and obtains the maximum expected utility
(MEU) policy πi based on one-step look-ahead using Ui (as in Equation (16.4)). Will the
resulting behavior be nearly as good as the optimal behavior? This is a crucial question for
any real agent, and it turns out that the answer is yes. Uπi(s) is the utility obtained if πi
is executed starting in s, and the policy loss ∥Uπi −U∥is the most the agent can lose by
Policy loss
