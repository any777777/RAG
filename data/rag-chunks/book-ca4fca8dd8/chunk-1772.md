---
chunk_id: "book-ca4fca8dd8-chunk-1772"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1772
confidence: "first-pass"
extraction_method: "structured-local"
---

1078
Appendix A
Mathematical Background
A.3 Probability Distributions
A probability is a measure over a set of events that satisﬁes three axioms:
1. The measure of each event is between 0 and 1. We write this as 0 ≤P(X =xi) ≤1,
where X is a random variable representing an event and xi are the possible values of
X. In general, random variables are denoted by uppercase letters and their values by
lowercase letters.
2. The measure of the whole set is 1; that is, ∑n
i=1 P(X =xi)=1.
3. The probability of a union of disjoint events is the sum of the probabilities of the indi-
vidual events; that is, P(X =x1 ∨X =x2)=P(X =x1)+P(X =x2), in the case where x1
and x2 are disjoint.
A probabilistic model consists of a sample space of mutually exclusive possible outcomes,
together with a probability measure for each outcome.
For example, in a model of the
weather tomorrow, the outcomes might be sun, cloud, rain, and snow. A subset of these
outcomes constitutes an event. For example, the event of precipitation is the subset consist-
ing of {rain, snow}.
We use P(X) to denote the vector of values ⟨P(X =x1),...,P(X =xn)⟩. We also use P(xi)
as an abbreviation for P(X =xi) and ∑x P(x) for ∑n
i=1 P(X =xi).
The conditional probability P(B|A) is deﬁned as P(B∩A)/P(A). A and B are condition-
ally independent if P(B|A)=P(B) (or equivalently, P(A|B)=P(A)).
For continuous variables, there are an inﬁnite number of values, and unless there are
point spikes, the probability of any one exact value is 0. So it makes more sense to talk
about the value being within a range. We do that with a probability density function, which
Probability density
function
has a slightly different meaning from the discrete probability function. Since P(X =x)—the
probability that X has the value x exactly—is zero, we instead measure how likely it is that X
falls into an interval around x, compared to the width of the interval, and take the limit as the
interval width goes to zero:
P(x)= lim
dx→0P(x ≤X ≤x+dx)/dx.
The density function must be nonnegative for all x and must have
Z ∞
−∞P(x)dx=1.
We can also deﬁne the cumulative distribution FX(x), which is the probability of a random
Cumulative
distribution
variable being less than x:
FX(x) = P(X ≤x) =
Z x
−∞P(u)du.
Note that the probability density function has units, whereas the discrete probability function
is unitless. For example, if values of X are measured in seconds, then the density is measured
in Hz (i.e., 1/sec). If values of X are points in three-dimensional space measured in meters,
then density is measured in 1/m3.
One of the most important probability distributions is the Gaussian distribution, also
Gaussian distribution
known as the normal distribution. We use the notation N(x;µ,σ2) for the normal distribu-
