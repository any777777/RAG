---
chunk_id: "book-ca4fca8dd8-chunk-0807"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 807
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.2
Inference in Temporal Models
485
conditioning on the current state Xt. The resulting equation for the new state estimate is the
central result in this chapter:
P(Xt+1 |e1:t+1) = αP(et+1 |Xt+1)∑
xt
P(Xt+1 |xt,e1:t)P(xt |e1:t)
= α P(et+1 |Xt+1)
|
{z
}
sensor model
∑
xt
P(Xt+1 |xt)
|
{z
}
transition model
P(xt |e1:t)
|
{z
}
recursion
(Markov assumption).
(14.5)
In this expression, all the terms come either from the model or from the previous state esti-
mate. Hence, we have the desired recursive formulation. We can think of the ﬁltered estimate
P(Xt |e1:t) as a “message” f1:t that is propagated forward along the sequence, modiﬁed by
each transition and updated by each new observation. The process is given by
f1:t+1 = FORWARD(f1:t,et+1),
where FORWARD implements the update described in Equation (14.5) and the process begins
with f1:0 = P(X0). When all the state variables are discrete, the time for each update is
constant (i.e., independent of t), and the space required is also constant. (The constants
depend, of course, on the size of the state space and the speciﬁc type of the temporal model
in question.) The time and space requirements for updating must be constant if a ﬁnite agent ◀
is to keep track of the current state distribution indeﬁnitely.
Let us illustrate the ﬁltering process for two steps in the basic umbrella example (Fig-
ure 14.2). That is, we will compute P(R2 |u1:2) as follows:
• On day 0, we have no observations, only the security guard’s prior beliefs; let’s assume
that consists of P(R0) = ⟨0.5,0.5⟩.
• On day 1, the umbrella appears, so U1 =true. The prediction from t =0 to t =1 is
P(R1) = ∑
r0
P(R1 |r0)P(r0)
= ⟨0.7,0.3⟩×0.5+⟨0.3,0.7⟩×0.5 = ⟨0.5,0.5⟩.
Then the update step simply multiplies by the probability of the evidence for t =1 and
normalizes, as shown in Equation (14.4):
P(R1 |u1) = αP(u1 |R1)P(R1) = α⟨0.9,0.2⟩⟨0.5,0.5⟩
= α⟨0.45,0.1⟩≈⟨0.818,0.182⟩.
• On day 2, the umbrella appears, so U2 =true. The prediction from t =1 to t =2 is
P(R2 |u1) = ∑
r1
P(R2 |r1)P(r1 |u1)
= ⟨0.7,0.3⟩×0.818+⟨0.3,0.7⟩×0.182 ≈⟨0.627,0.373⟩,
and updating it with the evidence for t =2 gives
P(R2 |u1,u2) = αP(u2 |R2)P(R2 |u1) = α⟨0.9,0.2⟩⟨0.627,0.373⟩
= α⟨0.565,0.075⟩≈⟨0.883,0.117⟩.
Intuitively, the probability of rain increases from day 1 to day 2 because rain persists. Exer-
cise 14.CONV(a) asks you to investigate this tendency further.
The task of prediction can be seen simply as ﬁltering without the addition of new evi-
dence. In fact, the ﬁltering process already incorporates a one-step prediction, and it is easy
