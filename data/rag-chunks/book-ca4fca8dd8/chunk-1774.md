---
chunk_id: "book-ca4fca8dd8-chunk-1774"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1774
confidence: "first-pass"
extraction_method: "structured-local"
---

1080
Appendix A
Mathematical Background
The root mean square (RMS) of a set of values (often samples of a random variable) is
the square root of the mean of the squares of the values,
RMS(x1,...,xn) =
s
x2
1 +...+x2n
n
.
The covariance of two random variables is the expectation of the product of their differences
Covariance
from their means:
cov(X,Y) = E((X −µX)(Y −µY)).
The covariance matrix, often denoted Σ, is a matrix of covariances between elements of a
Covariance matrix
vector of random variables. Given X = ⟨X1,...Xn⟩⊤, the entries of the covariance matrix are
as follows:
Σi,j = cov(Xi,Xj) = E((Xi −µi)(Xj −µj)).
We say we sample from a probability distribution, when we pick a value at random. We
Sampling
don’t know what any one pick will bring, but in the limit a large collection of samples will
approach the same probability density function as the distribution it is sampled from. The
uniform distribution is one where every element is equally (uniformly) probable. So when
Uniform distribution
we say we “sample uniformly (at random) from the integers 0 to 99” it means that we are
equally likely to pick any integer in that range.
Bibliographical and Historical Notes
The O() notation so widely used in computer science today was ﬁrst introduced in the con-
text of number theory by the mathematician P. G. H. Bachmann (1894). The concept of
NP-completeness was invented by Cook (1971), and the modern method for establishing a
reduction from one problem to another is due to Karp (1972). Cook and Karp have both won
the Turing award for their work.
Textbooks on the analysis and design of algorithms include Sedgewick and Wayne (2011)
and Cormen, Leiserson, Rivest and Stein (2009). These books place an emphasis on designing
and analyzing algorithms to solve tractable problems. For the theory of NP-completeness and
other forms of intractability, see Garey and Johnson (1979) or Papadimitriou (1994). Good
texts on probability include Chung (1979), Ross (2015), and Bertsekas and Tsitsiklis (2008).

## Page 1081
