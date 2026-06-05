---
chunk_id: "book-ca4fca8dd8-chunk-0809"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 809
confidence: "first-pass"
extraction_method: "structured-local"
---

486
Chapter 14
Probabilistic Reasoning over Time
to derive the following recursive computation for predicting the state at t +k +1 from a pre-
diction for t +k:
P(Xt+k+1 |e1:t) = ∑
xt+k
P(Xt+k+1 |xt+k)
|
{z
}
transition model
P(xt+k |e1:t)
|
{z
}
recursion
.
(14.6)
Naturally, this computation involves only the transition model and not the sensor model.
It is interesting to consider what happens as we try to predict further and further into
the future. As Exercise 14.CONV(b) shows, the predicted distribution for rain converges to
a ﬁxed point ⟨0.5,0.5⟩, after which it remains constant for all time.4 This is the stationary
distribution of the Markov process deﬁned by the transition model. (See also page 462.) A
great deal is known about the properties of such distributions and about the mixing time—
Mixing time
roughly, the time taken to reach the ﬁxed point. In practical terms, this dooms to failure any
attempt to predict the actual state for a number of steps that is more than a small fraction of
the mixing time, unless the stationary distribution itself is strongly peaked in a small area of
the state space. The more uncertainty there is in the transition model, the shorter will be the
mixing time and the more the future is obscured.
In addition to ﬁltering and prediction, we can use a forward recursion to compute the
likelihood of the evidence sequence, P(e1:t). This is a useful quantity if we want to compare
different temporal models that might have produced the same evidence sequence (e.g., two
different models for the persistence of rain). For this recursion, we use a likelihood message
ℓ1:t(Xt)=P(Xt,e1:t). It is easy to show (Exercise 14.LIKL) that the message calculation is
identical to that for ﬁltering:
ℓ1:t+1 = FORWARD(ℓ1:t,et+1).
Having computed ℓ1:t, we obtain the actual likelihood by summing out Xt:
L1:t = P(e1:t) = ∑
xt
ℓ1:t(xt).
(14.7)
Notice that the likelihood message represents the probabilities of longer and longer evidence
sequences as time goes by and so becomes numerically smaller and smaller, leading to under-
ﬂow problems with ﬂoating-point arithmetic. This is an important problem in practice, but
we shall not go into solutions here.
14.2.2 Smoothing
As we said earlier, smoothing is the process of computing the distribution over past states
given evidence up to the present—that is, P(Xk |e1:t) for 0 ≤k < t. (See Figure 14.3.) In
anticipation of another recursive message-passing approach, we can split the computation
into two parts—the evidence up to k and the evidence from k +1 to t,
P(Xk |e1:t) = P(Xk |e1:k,ek+1:t)
= αP(Xk |e1:k)P(ek+1:t |Xk,e1:k)
(using Bayes’ rule, given e1:k)
= αP(Xk |e1:k)P(ek+1:t |Xk)
(using conditional independence)
= αf1:k ×bk+1:t .
(14.8)
where “×” represents pointwise multiplication of vectors. Here we have deﬁned a “back-
4
If one picks an arbitrary day to be t =0, then it makes sense to choose the prior P(Rain0) to match the stationary
distribution, which is why we picked ⟨0.5,0.5⟩as the prior. Had we picked a different prior, the stationary
distribution would still have worked out to ⟨0.5,0.5⟩.
