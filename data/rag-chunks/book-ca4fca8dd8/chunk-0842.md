---
chunk_id: "book-ca4fca8dd8-chunk-0842"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 842
confidence: "first-pass"
extraction_method: "structured-local"
---

508
Chapter 14
Probabilistic Reasoning over Time
P(R1|R0)
R0
P(R1|R0)
P(R1|R0)
P(R1|R0)
P(R1|R0)
R0
P(R2|R1)
R1
P(R3|R2)
R2
P(R4|R3)
R3
R1 P(U1|R1)
R1 P(U1|R1)
R2 P(U2|R2)
R3 P(U3|R3)
R4 P(U4|R4)
Rain4
Rain0
Rain1
Rain0
Rain1
Rain2
Rain3
Umbrella1
Umbrella1
Umbrella2
Umbrella3
Umbrella4
Figure 14.16 Unrolling a dynamic Bayesian network: slices are replicated to accommodate
the observation sequence Umbrella1:3. Further slices have no effect on inferences within the
observation period.
resentation of a DBN by replicating slices until the network is large enough to accommodate
the observations, as in Figure 14.16. This technique is called unrolling. (Technically, the
DBN is equivalent to the semi-inﬁnite network obtained by unrolling forever. Slices added
beyond the last observation have no effect on inferences within the observation period and
can be omitted.) Once the DBN is unrolled, one can use any of the inference algorithms—
variable elimination, clustering methods, and so on—described in Chapter 13.
Unfortunately, a naive application of unrolling would not be particularly efﬁcient. If
we want to perform ﬁltering or smoothing with a long sequence of observations e1:t, the
unrolled network would require O(t) space and would thus grow without bound as more
observations were added. Moreover, if we simply run the inference algorithm anew each
time an observation is added, the inference time per update will also increase as O(t).
Looking back to Section 14.2.1, we see that constant time and space per ﬁltering update
can be achieved if the computation can be done recursively. Essentially, the ﬁltering update
in Equation (14.5) works by summing out the state variables of the previous time step to get
the distribution for the new time step. Summing out variables is exactly what the variable
elimination (Figure 13.13) algorithm does, and it turns out that running variable elimination
with the variables in temporal order exactly mimics the operation of the recursive ﬁltering
update in Equation (14.5). The modiﬁed algorithm keeps at most two slices in memory at
any one time: starting with slice 0, we add slice 1, then sum out slice 0, then add slice 2, then
sum out slice 1, and so on. In this way, we can achieve constant space and time per ﬁltering
update. (The same performance can be achieved by suitable modiﬁcations to the clustering
algorithm.) Exercise 14.DBNE asks you to verify this fact for the umbrella network.
So much for the good news; now for the bad news: It turns out that the “constant” for the
per-update time and space complexity is, in almost all cases, exponential in the number of
state variables. What happens is that, as the variable elimination proceeds, the factors grow
to include all the state variables (or, more precisely, all those state variables that have parents
in the previous time slice). The maximum factor size is O(dn+k) and the total update cost per
step is O(ndn+k), where d is the domain size of the variables and k is the maximum number
of parents of any state variable.
Of course, this is much less than the cost of HMM updating, which is O(d2n), but it is still
infeasible for large numbers of variables. This grim fact means is that even though we can use
▶
DBNs to represent very complex temporal processes with many sparsely connected variables,
