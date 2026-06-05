---
chunk_id: "book-ca4fca8dd8-chunk-0810"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 810
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 487

Section 14.2
Inference in Temporal Models
487
Figure 14.3 Smoothing computes P(Xk |e1:t), the posterior distribution of the state at some
past time k given a complete sequence of observations from 1 to t.
ward” message bk+1:t =P(ek+1:t |Xk), analogous to the forward message f1:k. The forward
message f1:k can be computed by ﬁltering forward from 1 to k, as given by Equation (14.5). It
turns out that the backward message bk+1:t can be computed by a recursive process that runs
backward from t:
P(ek+1:t |Xk) = ∑
xk+1
P(ek+1:t |Xk,xk+1)P(xk+1 |Xk)
(conditioning on Xk+1)
= ∑
xk+1
P(ek+1:t |xk+1)P(xk+1 |Xk)
(by conditional independence)
= ∑
xk+1
P(ek+1,ek+2:t |xk+1)P(xk+1 |Xk)
= ∑
xk+1
P(ek+1 |xk+1)
|
{z
}
sensor model
P(ek+2:t |xk+1)
|
{z
}
recursion
P(xk+1 |Xk)
|
{z
}
transition model
,
(14.9)
where the last step follows by the conditional independence of ek+1 and ek+2:t, given xk+1.
In this expression, all the terms come either from the model or from the previous backward
message. Hence, we have the desired recursive formulation. In message form, we have
bk+1:t = BACKWARD(bk+2:t,ek+1),
where BACKWARD implements the update described in Equation (14.9). As with the forward
recursion, the time and space needed for each update are constant and thus independent of t.
We can now see that the two terms in Equation (14.8) can both be computed by recursions
through time, one running forward from 1 to k and using the ﬁltering equation (14.5) and the
other running backward from t to k +1 and using Equation (14.9).
For the initialization of the backward phase, we have bt+1:t =P(et+1:t |Xt)=P( |Xt)=1,
where 1 is a vector of 1s. The reason for this is that et+1:t is an empty sequence, so the
probability of observing it is 1.
Let us now apply this algorithm to the umbrella example, computing the smoothed esti-
mate for the probability of rain at time k=1, given the umbrella observations on days 1 and
2. From Equation (14.8), this is given by
P(R1 |u1,u2) = αP(R1 |u1)P(u2 |R1).
(14.10)
The ﬁrst term we already know to be ⟨.818,.182⟩, from the forward ﬁltering process de-
scribed earlier. The second term can be computed by applying the backward recursion in
Equation (14.9):
P(u2 |R1) = ∑
r2
P(u2 |r2)P( |r2)P(r2 |R1)
= (0.9×1×⟨0.7,0.3⟩)+(0.2×1×⟨0.3,0.7⟩) = ⟨0.69,0.41⟩.

## Page 488
