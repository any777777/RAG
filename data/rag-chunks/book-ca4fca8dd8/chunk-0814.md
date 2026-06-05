---
chunk_id: "book-ca4fca8dd8-chunk-0814"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 814
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 490

490
Chapter 14
Probabilistic Reasoning over Time
Figure 14.5 (a) Possible state sequences for Raint can be viewed as paths through a graph of
the possible states at each time step. (States are shown as rectangles to avoid confusion with
nodes in a Bayes net.) (b) Operation of the Viterbi algorithm for the umbrella observation
sequence [true,true,false,true,true], where the evidence starts at time 1. For each t, we
have shown the values of the message m1:t, which gives the probability of the best sequence
reaching each state at time t. Also, for each state, the bold arrow leading into it indicates
its best predecessor as measured by the product of the preceding sequence probability and
the transition probability. Following the bold arrows back from the most likely state in m1:5
gives the most likely sequence, shown by the bold outlines and darker shading.
the forward message f1:t in the ﬁltering algorithm. The message is deﬁned as follows:5
m1:t = max
x1:t−1 P(x1:t−1,Xt,e1:t).
To obtain the recursive relationship between m1:t+1 and m1:t, we can repeat more or less the
same steps that we used for Equation (14.5):
m1:t+1 = max
x1:t P(x1:t,Xt+1,e1:t+1) = max
x1:t P(x1:t,Xt+1,e1:t,et+1)
= max
x1:t P(et+1 |x1:t,Xt+1,e1:t)P(x1:t,Xt+1,e1:t)
= P(et+1 |Xt+1)max
x1:t P(Xt+1, |xt)P(x1:t,e1:t)
= P(et+1 |Xt+1)max
xt P(Xt+1, |xt)max
x1:t−1 P(x1:t−1,xt,e1:t)
(14.11)
where the ﬁnal term maxx1:t−1 P(x1:t−1,xt,e1:t) is exactly the entry for the particular state xt
in the message vector m1:t. Equation (14.11) is essentially identical to the ﬁltering equa-
tion (14.5) except that the summation over xt in Equation (14.5) is replaced by the maximiza-
tion over xt in Equation (14.11), and there is no normalization constant α in Equation (14.11).
Thus, the algorithm for computing the most likely sequence is similar to ﬁltering: it starts at
time 0 with the prior m1:0 =P(X0) and then runs forward along the sequence, computing the
5
Notice that these are not quite the probabilities of the most likely paths to reach the states Xt given the evidence,
which would be the conditional probabilities maxx1:t−1 P(x1:t−1,Xt |e1:t); but the two vectors are related by a
constant factor P(e1:t). The difference is immaterial because the max operator doesn’t care about constant factors.
We get a slightly simpler recursion with m1:t deﬁned this way.

## Page 491
