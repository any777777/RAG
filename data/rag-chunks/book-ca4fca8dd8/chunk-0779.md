---
chunk_id: "book-ca4fca8dd8-chunk-0779"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 779
confidence: "first-pass"
extraction_method: "structured-local"
---

470
Chapter 13
Probabilistic Reasoning
For example, suppose we turn the sprinkler on—that is, if we (who are, by deﬁnition,
not part of the causal processes described by the model) intervene to impose the condition
Sprinkler=true. In the notation of the do-calculus, which is a key part of the theory of causal
Do-calculus
networks, this is written as do(Sprinkler=true). Once done, this means that the sprinkler
variable is no longer dependent on whether it’s a cloudy day. We therefore delete the equation
S= fS(C,US) from the system of structural equations and replace it with S=true, giving us
C = fC(UC)
R = fR(C,UR)
S = true
(13.16)
W = fW(R,S,UW)
G = fG(W,UG).
From these equations, we obtain the new joint distribution for the remaining variables condi-
tioned on do(Sprinkler=true):
P(c,r,w,g|do(S=true)) = P(c) P(r|c) P(w|r,s=true) P(g|w)
(13.17)
This corresponds to the “mutilated” network in Figure 13.23(b). From Equation (13.17), we
see that the only variables whose probabilities change are WetGrass and GreenerGrass, that
is, the descendants of the manipulated variable Sprinkler.
Note the difference between conditioning on the action do(Sprinkler=true) in the origi-
nal network and conditioning on the observation Sprinkler=true. The original network tells
us that the sprinkler is less likely to be on when the weather is cloudy, so if we observe
the sprinkler to be on, that reduces the probability that the weather is cloudy. But common
sense tells us that if we (operating from outside the world, so to speak) reach in and turn
on the sprinkler, that doesn’t affect the weather or provide new information about what the
weather is like that day. As shown in Figure 13.23(b), intervening breaks the normal causal
link between the weather and the sprinkler. This prevents any inﬂuence ﬂowing backward
from Sprinkler to Cloudy. Thus, conditioning on do(Sprinkler=true) in the original graph is
equivalent to conditioning on Sprinkler=true in the mutilated graph.
A similar approach can be taken to analyze the effect of do(Xj =xjk) in a general causal
network with variables X1,...,Xn. The network corresponds to a joint distribution deﬁned in
the usual way (see Equation (13.2)):
P(x1,...,xn) =
n
∏
i=1
P(xi | parents(Xi)).
(13.18)
After applying do(Xj =xjk), the new joint distribution Pxjk simply omits the factor for Xj:
Pxjk(x1,...,xn) =
(
∏i̸=j P(xi | parents(Xi)) =
P(x1,...,xn)
P(xj | parents(Xj))
if xj =x jk
0
if xj ̸= xjk
(13.19)
This follows from the fact that setting Xj to a particular value xjk corresponds to deleting
the equation Xj = f j(Parents(Xj),Uj) from the system of structural equations and replacing it
with Xj =xjk. With a bit more algebraic manipulation, one can derive a formula for the effect
of setting variable Xj on any other variable Xi:
P(Xi = xi |do(Xj =x jk)) = Pxjk(Xi =xi)
=
∑
parents(Xj)
P(xi |xjk, parents(Xj))P(parents(Xj)).
(13.20)
