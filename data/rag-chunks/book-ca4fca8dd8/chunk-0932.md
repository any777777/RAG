---
chunk_id: "book-ca4fca8dd8-chunk-0932"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 932
confidence: "first-pass"
extraction_method: "structured-local"
---

564
Chapter 16
Making Complex Decisions
-0.2
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 5
 10
 15
 20
 25
 30
 35
 40
(1,1)
(1,3)
(3,1)
(3,3)
(4,1)
Utility estimates
Number of iterations
 1
 10
 100
 1000
 10000
 100000
 1x106
 1x107
 0.5
 0.6
 0.7
 0.8
 0.9
 1
Iterations required
Discount factor γ
c = 0.0001
c = 0.001
c = 0.01
c = 0.1
(a)
(b)
Figure 16.7 (a) Graph showing the evolution of the utilities of selected states using value
iteration. (b) The number of value iterations required to guarantee an error of at most ϵ=c·
Rmax, for different values of c, as a function of the discount factor γ.
Convergence of value iteration
We said that value iteration eventually converges to a unique set of solutions of the Bellman
equations. In this section, we explain why this happens. We introduce some useful mathe-
matical ideas along the way, and we obtain some methods for assessing the error in the utility
function returned when the algorithm is terminated early; this is useful because it means that
we don’t have to run forever. This section is quite technical.
The basic concept used in showing that value iteration converges is the notion of a con-
traction. Roughly speaking, a contraction is a function of one argument that, when applied to
Contraction
two different inputs in turn, produces two output values that are “closer together,” by at least
some constant factor, than the original inputs. For example, the function “divide by two” is
a contraction, because, after we divide any two numbers by two, their difference is halved.
Notice that the “divide by two” function has a ﬁxed point, namely zero, that is unchanged by
the application of the function. From this example, we can discern two important properties
of contractions:
• A contraction has only one ﬁxed point; if there were two ﬁxed points they would not
get closer together when the function was applied, so it would not be a contraction.
• When the function is applied to any argument, the value must get closer to the ﬁxed
point (because the ﬁxed point does not move), so repeated application of a contraction
always reaches the ﬁxed point in the limit.
Now, suppose we view the Bellman update (Equation (16.10)) as an operator B that is ap-
plied simultaneously to update the utility of every state. Then the Bellman equation becomes
U =BU and the Bellman update equation can be written as
Ui+1 ←BUi .
Next, we need a way to measure distances between utility vectors. We will use the max norm,
Max norm
which measures the “length” of a vector by the absolute value of its biggest component:
∥U∥= max
s
|U(s)|.
