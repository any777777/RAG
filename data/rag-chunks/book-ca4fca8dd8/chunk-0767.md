---
chunk_id: "book-ca4fca8dd8-chunk-0767"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 767
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.4
Approximate Inference for Bayesian Networks
463
We can show that detailed balance implies stationarity simply by summing over x in
Equation (13.12). We have
∑
x
π(x)k(x →x′) = ∑
x
π(x′)k(x′ →x) = π(x′)∑
x
k(x′ →x) = π(x′)
where the last step follows because a transition from x′ is guaranteed to occur.
Why Gibbs sampling works
We will now show that Gibbs sampling returns consistent estimates for posterior probabil-
ities. The basic claim is straightforward: the stationary distribution of the Gibbs sampling ◀
process is exactly the posterior distribution for the nonevidence variables conditioned on
the evidence. This remarkable property follows from the speciﬁc way in which the Gibbs
sampling process moves from state to state.
The general deﬁnition of Gibbs sampling is that a variable Xi is chosen and then sam-
pled conditionally on the current values of all the other variables. (When applied specif-
ically to Bayes nets, we simply use the additional fact that sampling conditionally on all
variables is equivalent to sampling conditionally on the variable’s Markov blanket, as shown
on page 437.) We will use the notation Xi to refer to these other variables (except the evidence
variables); their values in the current state are xi.
To write down the transition kernel k(x →x′) for Gibbs sampling, there are three cases
to consider:
1. The states x and x′ differ in two or more variables. In that case, k(x →x′)=0 because
Gibbs sampling changes only a single variable.
2. The states differ in exactly one variable Xi that changes its value from xi to x′
i. The
probability of such an occurrence is
k(x →x′) = k((xi,xi) →(x′
i,xi)) = ρ(i)P(x′
i |xi).
(13.13)
3. The states are the same: x = x′. In that case, any variable could be chosen but then the
sampling process produces the same value the variable already has. The probability of
such an occurrence is
k(x →x) = ∑
i
ρ(i)k((xi,xi) →(xi,xi)) = ∑
i
ρ(i)P(xi |xi).
Now we show that this general deﬁnition of Gibbs sampling satisﬁes the detailed balance
equation with a stationary distribution equal to P(x|e), the true posterior distribution on
the nonevidence variables. That is, we show that π(x)k(x →x′)=π(x′)k(x′ →x) where
π(x)=P(x|e), for all states x and x′.
For the ﬁrst and third cases given above, detailed balance is always satisﬁed: if two states
differ in two or more variables, the transition probability in both directions is zero. If x ̸= x′
then from Equation (13.13), we have
π(x)k(x →x′) = P(x|e)ρ(i)P(x′
i |xi,e) = ρ(i)P(xi,xi |e)P(x′
i |xi,e)
= ρ(i)P(xi |xi,e)P(xi |e)P(x′
i |xi,e)
(using the chain rule on the ﬁrst term)
= ρ(i)P(xi |xi,e)P(x′
i,xi |e)
(reverse chain rule on last two terms)
= π(x′)k(x′ →x).
The ﬁnal piece of the puzzle is the ergodicity of the chain—that is, every state must be reach-
able from every other and there are no periodic cycles. Both conditions are satisﬁed provided
