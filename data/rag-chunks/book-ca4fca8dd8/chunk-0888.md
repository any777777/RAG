---
chunk_id: "book-ca4fca8dd8-chunk-0888"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 888
confidence: "first-pass"
extraction_method: "structured-local"
---

538
Chapter 15
Making Simple Decisions
• With probability (n−1)/n, the survey will show that the block contains no oil, in which
case the company will buy a different block. Now the probability of ﬁnding oil in one
of the other blocks changes from 1/n to 1/(n−1), so the company makes an expected
proﬁt of C/(n−1)−C/n = C/n(n−1) dollars.
Now we can calculate the expected proﬁt, given access to the survey information:
1
n × (n−1)C
n
+ n−1
n
×
C
n(n−1) = C/n.
Thus, the information is worthC/n dollars to the company, and the company should be willing
to pay the seismologist some signiﬁcant fraction of this amount.
The value of information derives from the fact that with the information, one’s course
of action can be changed to suit the actual situation. One can discriminate according to the
situation, whereas without the information, one has to do what’s best on average over the
possible situations. In general, the value of a given piece of information is deﬁned to be the
difference in expected value between best actions before and after information is obtained.
15.6.2 A general formula for perfect information
It is simple to derive a general mathematical formula for the value of information. We assume
that exact evidence can be obtained about the value of some random variable E j (that is, we
learn E j = ej), so the phrase value of perfect information (VPI) is used.8
Value of perfect
information
In the agent’s initial information state, the value of the current best action α is, from
Equation (15.1),
EU(α) = max
a ∑
s′
P(RESULT(a)=s′)U(s′),
and the value of the new best action (after the new evidence E j = ej is obtained) will be
EU(αej|ej) = max
a ∑
s′
P(RESULT(a)=s′ |ej)U(s′).
But E j is a random variable whose value is currently unknown, so to determine the value of
discovering E j we must average over all possible values ej that we might discover for E j,
using our current beliefs about its value:
VPI(E j) =
 
∑
e j
P(E j =ej) EU(αej|E j =ej)
!
−EU(α).
To get some intuition for this formula, consider the simple case where there are only two
actions, a1 and a2, from which to choose. Their current expected utilities are U1 and U2.
The information E j = e j will yield some new expected utilities U′
1 and U′
2 for the actions, but
before we obtain Ej, we will have some probability distributions over the possible values of
U′
1 and U′
2 (which we assume are independent).
Suppose that a1 and a2 represent two different routes through a mountain range in winter:
a1 is a nice, straight highway through a tunnel, and a2 is a winding dirt road over the top. Just
8
There is no loss of expressiveness in requiring perfect information. Suppose we wanted to model the case
in which we become somewhat more certain about a variable. We can do that by introducing another variable
about which we learn perfect information. For example, suppose we initially have broad uncertainty about the
variable Temperature. Then we gain the perfect knowledge Thermometer = 37; this gives us imperfect informa-
tion about the true Temperature, and the uncertainty due to measurement error is encoded in the sensor model
P(Thermometer|Temperature). See Exercise 15.VPIX for another example.
