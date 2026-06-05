---
chunk_id: "book-ca4fca8dd8-chunk-0878"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 878
confidence: "first-pass"
extraction_method: "structured-local"
---

532
Chapter 15
Making Simple Decisions
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
-6
-5.5
-5
-4.5
-4
-3.5
-3
-2.5
-2
S1
S2
Probability
Negative cost
 0
 0.2
 0.4
 0.6
 0.8
 1
 1.2
-6
-5.5
-5
-4.5
-4
-3.5
-3
-2.5
-2
S1
S2
Probability
Negative cost
(a)
(b)
Figure 15.5 Stochastic dominance. (a) S1 stochastically dominates S2 on frugality (negative
cost). (b) Cumulative distributions for the frugality of S1 and S2.
Instead of thinking about the integral over x, however, think about the integral over y, the
cumulative probability, as shown in Figure 15.5(b). For any value of y, the corresponding
value of x (and hence of U(x)) is bigger for S1 than for S2; so if we integrate a bigger quantity
over the whole range of y, we are bound to get a bigger result. Formally, it’s just a substitution
of y=P1(x) in the integral for S1’s expected value and y=P2(x) in the integral for S2’s. With
these substitutions, we have dy= d
dx(P1(x))dx= p1(x)dx for S1 and dy= p2(x)dx for S2, hence
∞
Z
−∞
p1(x)U(x)dx =
1
Z
0
U(P−1
1 (y))dy ≥
1
Z
0
U(P−1
2 (y))dy =
∞
Z
−∞
p2(x)U(x)dx.
This inequality allows us to prefer A1 to A2 in a single-attribute problem. More generally,
if an action is stochastically dominated by another action on all attributes in a multiattribute
problem, then it can be discarded.
The stochastic dominance condition might seem rather technical and perhaps not so easy
to evaluate without extensive probability calculations. In fact, it can be decided very easily in
many cases. For example, would you rather fall head-ﬁrst onto concrete from 3 millimeters
or 3 meters? Assuming you chose 3 millimeters—good choice! Why is it necessarily a better
decision? There is a good deal of uncertainty about the degree of damage you will incur in
both cases; but for any given level of damage, the probability that you’ll incur at least that
level of damage is higher when falling from 3 meters than from 3 millimeters. In other words,
3 millimeters stochastically dominates 3 meters on the Safety attribute.
This kind of reasoning comes as second nature to humans; it’s so obvious we don’t even
think about it. Stochastic domination abounds in the airport problem too. Suppose, for exam-
ple, that the construction transportation cost depends on the distance to the supplier. The cost
itself is uncertain, but the greater the distance, the greater the cost. If S1 is closer than S2, then
S1 will dominate S2 on frugality. Although we will not present them here, algorithms exist
for propagating this kind of qualitative information among uncertain variables in qualitative
probabilistic networks, enabling a system to make rational decisions based on stochastic
Qualitative
probabilistic
networks
dominance, without using any numeric values.
