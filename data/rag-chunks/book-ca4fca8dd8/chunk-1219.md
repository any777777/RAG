---
chunk_id: "book-ca4fca8dd8-chunk-1219"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1219
confidence: "first-pass"
extraction_method: "structured-local"
---

734
Chapter 19
Learning from Examples
be found in Quinlan (1993). An alternative industrial-strength software package, CART (for
Classiﬁcation and Regression Trees) was developed by the statistician Leo Breiman and his
colleagues (Breiman et al., 1984).
Hyaﬁl and Rivest (1976) proved that ﬁnding an optimal decision tree (rather than ﬁnding
a good tree through locally greedy selections) is NP-complete. But Bertsimas and Dunn
(2017) point out that in the last 25 years, advances in hardware design and in algorithms for
mixed-integer programming have resulted in an 800 billion-fold speedup, which means that
it is now feasible to solve this NP-hard problem at least for problems with not more than a
few thousand examples and a few dozen features.
Cross-validation was ﬁrst introduced by Larson (1931), and in a form close to what
we show by Stone (1974) and Golub et al. (1979). The regularization procedure is due to
Tikhonov (1963).
On the question of overﬁtting, John von Neumann was quoted (Dyson, 2004) as boast-
ing, “With four parameters I can ﬁt an elephant, and with ﬁve I can make him wiggle his
trunk,” meaning that a high-degree polynomial can be made to ﬁt almost any data, but at
the cost of potentially overﬁtting. Mayer et al. (2010) proved him right by demonstrating
a four-parameter elephant and ﬁve-parameter wiggle, and Bou´e (2019) went even further,
demonstrating an elephant and other animals with a one-parameter chaotic function.
Zhang et al. (2016) analyze under what conditions a model can memorize the training
data. They perform experiments using random data—surely an algorithm that gets zero error
on a training set with random labels must be memorizing the data set. However, they conclude
that the ﬁeld has yet to discover a precise measure of what it means for a model to be “simple”
in the sense of Ockham’s razor. Arpit et al. (2017) show that the conditions under which
memorization can occur depend on details of both the model and the data set.
Belkin et al. (2019) discuss the bias–variance tradeoff in machine learning and why some
model classes continue to improve after reaching the interpolation point, while other model
classes exhibit the U-shaped curve. Berrada et al. (2019) develop a new learning algorithm
based on gradient descent that exploits the ability of models to memorize to set good values
for the learning rate hyperparameter.
Theoretical analysis of learning algorithms began with the work of Gold (1967) on iden-
tiﬁcation in the limit. This approach was motivated in part by models of scientiﬁc discovery
from the philosophy of science (Popper, 1962), but has been applied mainly to the problem
of learning grammars from example sentences (Osherson et al., 1986).
Whereas the identiﬁcation-in-the-limit approach concentrates on eventual convergence,
the study of Kolmogorov complexity or algorithmic complexity, developed independently
Kolmogorov
complexity
by Solomonoff (1964, 2009) and Kolmogorov (1965), attempts to provide a formal deﬁnition
for the notion of simplicity used in Ockham’s razor. To escape the problem that simplicity
depends on the way in which information is represented, it is proposed that simplicity be
measured by the length of the shortest program for a universal Turing machine that correctly
reproduces the observed data. Although there are many possible universal Turing machines,
and hence many possible “shortest” programs, these programs differ in length by at most a
constant that is independent of the amount of data. This beautiful insight, which essentially
shows that any initial representation bias will eventually be overcome by the data, is marred
only by the undecidability of computing the length of the shortest program. Approximate
measures such as the minimum description length, or MDL (Rissanen, 1984, 2007) can be
