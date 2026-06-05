---
chunk_id: "book-ca4fca8dd8-chunk-0935"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 935
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 566

566
Chapter 16
Making Complex Decisions
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 2
 4
 6
 8
 10
 12
 14
Max error/Policy loss
Number of iterations
Max error
Policy loss
Figure 16.8 The maximum error ∥Ui −U∥of the utility estimates and the policy loss ∥U πi −
U∥, as a function of the number of iterations of value iteration on the 4×3 world.
executing πi instead of the optimal policy π∗. The policy loss of πi is connected to the error
in Ui by the following inequality:
if
∥Ui −U∥< ϵ
then
∥Uπi −U∥< 2ϵ.
(16.13)
In practice, it often occurs that πi becomes optimal long before Ui has converged. Figure 16.8
shows how the maximum error in Ui and the policy loss approach zero as the value iteration
process proceeds for the 4×3 environment with γ =0.9. The policy πi is optimal when i=5,
even though the maximum error in Ui is still 0.51.
Now we have everything we need to use value iteration in practice. We know that it
converges to the correct utilities, we can bound the error in the utility estimates if we stop
after a ﬁnite number of iterations, and we can bound the policy loss that results from executing
the corresponding MEU policy. As a ﬁnal note, all of the results in this section depend on
discounting with γ < 1. If γ =1 and the environment contains terminal states, then a similar
set of convergence results and error bounds can be derived.
16.2.2 Policy iteration
In the previous section, we observed that it is possible to get an optimal policy even when
the utility function estimate is inaccurate. If one action is clearly better than all others, then
the exact magnitude of the utilities on the states involved need not be precise. This insight
suggests an alternative way to ﬁnd optimal policies. The policy iteration algorithm alternates
Policy iteration
the following two steps, beginning from some initial policy π0:
• Policy evaluation: given a policy πi, calculate Ui =Uπi, the utility of each state if πi
Policy evaluation
were to be executed.
• Policy improvement: Calculate a new MEU policy πi+1, using one-step look-ahead
Policy improvement
based on Ui (as in Equation (16.4)).
The algorithm terminates when the policy improvement step yields no change in the utilities.
At this point, we know that the utility function Ui is a ﬁxed point of the Bellman update, so
it is a solution to the Bellman equations, and πi must be an optimal policy. Because there are
only ﬁnitely many policies for a ﬁnite state space, and each iteration can be shown to yield a

## Page 567
