---
chunk_id: "book-ca4fca8dd8-chunk-1279"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1279
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 777

Section 21.2
Learning with Complete Data
777
Flavor
P(F=cherry)
(a)
P(F=cherry)
Flavor
(b)
F
cherry
lime
P(W=red | F)
Wrapper


1
2
Figure 21.2 (a) Bayesian network model for the case of candies with an unknown proportion
of cherry and lime. (b) Model for the case where the wrapper color depends (probabilisti-
cally) on the candy ﬂavor.
each candy is selected probabilistically, according to some unknown conditional distribution,
depending on the ﬂavor. The corresponding probability model is shown in Figure 21.2(b).
Notice that it has three parameters: θ, θ1, and θ2. With these parameters, the likelihood of
seeing, say, a cherry candy in a green wrapper can be obtained from the standard semantics
for Bayesian networks (page 433):
P(Flavor=cherry,Wrapper=green|hθ,θ1,θ2)
= P(Flavor=cherry|hθ,θ1,θ2)P(Wrapper=green|Flavor=cherry,hθ,θ1,θ2)
= θ ·(1−θ1).
Now we unwrap N candies, of which c are cherry and ℓare lime. The wrapper counts are as
follows: rc of the cherry candies have red wrappers and gc have green, while rℓof the lime
candies have red and gℓhave green. The likelihood of the data is given by
P(d|hθ,θ1,θ2) = θc(1−θ)ℓ·θrc
1 (1−θ1)gc ·θrℓ
2 (1−θ2)gℓ.
This looks pretty horrible, but taking logarithms helps:
L = [clogθ +ℓlog(1−θ)]+[rc logθ1 +gc log(1−θ1)]+[rℓlogθ2 +gℓlog(1−θ2)].
The beneﬁt of taking logs is clear: the log likelihood is the sum of three terms, each of which
contains a single parameter. When we take derivatives with respect to each parameter and set
them to zero, we get three independent equations, each containing just one parameter:
∂L
∂θ =
c
θ −
ℓ
1−θ = 0
⇒
θ =
c
c+ℓ
∂L
∂θ1 =
rc
θ1 −
gc
1−θ1 = 0
⇒
θ1 =
rc
rc+gc
∂L
∂θ2 =
rℓ
θ2 −
gℓ
1−θ2 = 0
⇒
θ2 =
rℓ
rℓ+gℓ.
The solution for θ is the same as before. The solution for θ1, the probability that a cherry
candy has a red wrapper, is the observed fraction of cherry candies with red wrappers, and
similarly for θ2.
These results are very comforting, and it is easy to see that they can be extended to any
Bayesian network whose conditional probabilities are represented as tables. The most impor-

## Page 778
