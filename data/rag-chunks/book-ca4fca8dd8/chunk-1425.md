---
chunk_id: "book-ca4fca8dd8-chunk-1425"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1425
confidence: "first-pass"
extraction_method: "structured-local"
---

862
Chapter 23
Reinforcement Learning
continuously, which makes gradient-based search difﬁcult. For this reason, policy search
methods often use a stochastic policy representation πθ(s,a), which speciﬁes the probability
Stochastic policy
of selecting action a in state s. One popular representation is the softmax function:
πθ(s,a) =
eβ ˆQθ(s,a)
∑a′ eβ ˆQθ(s,a′) .
(23.14)
The parameter β > 0 modulates the softness of the softmax: for values of β that are large
compared to the separations between Q-values, the softmax approaches a hard max, whereas
for values of β close to zero the softmax approaches a uniform random choice among the
actions. For all ﬁnite values of β, the softmax provides a differentiable function of θ; hence,
the value of the policy (which depends continuously on the action-selection probabilities) is
a differentiable function of θ.
Now let us look at methods for improving the policy. We start with the simplest case: a
deterministic policy and a deterministic environment. Let ρ(θ) be the policy value, that is, the
Policy value
expected reward-to-go when πθ is executed. If we can derive an expression for ρ(θ) in closed
form, then we have a standard optimization problem, as described in Chapter 4. We can
follow the policy gradient vector ∇θρ(θ), provided ρ(θ) is differentiable. Alternatively, if
Policy gradient
ρ(θ) is not available in closed form, we can evaluate πθ simply by executing it and observing
the accumulated reward. We can follow the empirical gradient by hill climbing—that is,
evaluating the change in policy value for small increments in each parameter. With the usual
caveats, this process will converge to a local optimum in policy space.
When the environment (or the policy) is nondeterministic, things get more difﬁcult. Sup-
pose we are trying to do hill climbing, which requires comparing ρ(θ) and ρ(θ+∆θ) for some
small ∆θ. The problem is that the total reward for each trial may vary widely, so estimates
of the policy value from a small number of trials will be quite unreliable; trying to compare
two such estimates will be even more unreliable. One solution is simply to run lots of trials,
measuring the sample variance and using it to determine that enough trials have been run
to get a reliable indication of the direction of improvement for ρ(θ). Unfortunately, this is
impractical for many real problems in which trials may be expensive, time-consuming, and
perhaps even dangerous.
For the case of a nondeterministic policy πθ(s,a), it is possible to obtain an unbiased
estimate of the gradient at θ, ∇θρ(θ), directly from the results of trials executed at θ. For
simplicity, we will derive this estimate for the simple case of an episodic environment in
which each action a obtains reward R(s0,a,s0) and the environment restarts in s0. In this
case, the policy value is just the expected value of the reward, and we have
∇θρ(θ) = ∇θ∑
a
R(s0,a,s0)πθ(s0,a) = ∑
a
R(s0,a,s0)∇θπθ(s0,a).
Now we perform a simple trick so that this summation can be approximated by samples
generated from the probability distribution deﬁned by πθ(s0,a). Suppose that we have N
trials in all, and the action taken on the jth trial is aj. Then
∇θρ(θ) = ∑
a
πθ(s0,a)· R(s0,a,s0)∇θπθ(s0,a)
πθ(s0,a)
= ≈1
N
N
∑
j=1
R(s0,a j,s0)∇θπθ(s0,aj)
πθ(s0,aj)
.
