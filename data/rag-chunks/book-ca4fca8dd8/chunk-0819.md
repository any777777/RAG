---
chunk_id: "book-ca4fca8dd8-chunk-0819"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 819
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.3
Hidden Markov Models
493
function FIXED-LAG-SMOOTHING(et,hmm,d) returns a distribution over Xt−d
inputs: et, the current evidence for time step t
hmm, a hidden Markov model with S× S transition matrix T
d, the length of the lag for smoothing
persistent: t, the current time, initially 1
f, the forward message P(Xt |e1:t), initially hmm.PRIOR
B, the d-step backward transformation matrix, initially the identity matrix
et−d:t, double-ended list of evidence from t −d to t, initially empty
local variables: Ot−d,Ot, diagonal matrices containing the sensor model information
add et to the end of et−d:t
Ot ←diagonal matrix containing P(et |Xt)
if t > d then
f←FORWARD(f,et−d)
remove et−d−1 from the beginning of et−d:t
Ot−d ←diagonal matrix containing P(et−d |Xt−d)
B←O−1
t−dT−1BTOt
else B←BTOt
t←t +1
if t > d +1 then return NORMALIZE(f × B1) else return null
Figure 14.6 An algorithm for smoothing with a ﬁxed time lag of d steps, implemented as an
online algorithm that outputs the new smoothed estimate given the observation for a new time
step. Notice that the ﬁnal output NORMALIZE(f×B1) is just αf×b, by Equation (14.14).
b and f together, using them to compute the smoothed estimate at each step. Since only one
copy of each message is needed, the storage requirements are constant (i.e., independent of
t, the length of the sequence). There are two signiﬁcant restrictions on this algorithm: it re-
quires that the transition matrix be invertible and that the sensor model have no zeroes—that
is, that every observation be possible in every state.
A second area in which the matrix formulation reveals an improvement is in online
smoothing with a ﬁxed lag. The fact that smoothing can be done in constant space sug-
gests that there should exist an efﬁcient recursive algorithm for online smoothing—that is,
an algorithm whose time complexity is independent of the length of the lag. Let us suppose
that the lag is d; that is, we are smoothing at time slice t −d, where the current time is t. By
Equation (14.8), we need to compute
αf1:t−d ×bt−d+1:t
for slice t −d. Then, when a new observation arrives, we need to compute
αf1:t−d+1 ×bt−d+2:t+1
for slice t −d +1. How can this be done incrementally? First, we can compute f1:t−d+1 from
f1:t−d, using the standard ﬁltering process, Equation (14.5).
Computing the backward message incrementally is trickier, because there is no simple
relationship between the old backward message bt−d+1:t and the new backward message
bt−d+2:t+1. Instead, we will examine the relationship between the old backward message
bt−d+1:t and the backward message at the front of the sequence, bt+1:t. To do this, we apply
