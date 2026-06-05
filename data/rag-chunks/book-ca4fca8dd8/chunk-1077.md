---
chunk_id: "book-ca4fca8dd8-chunk-1077"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1077
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.1
Relational Probability Models
645
where RecCPT is a separately deﬁned conditional probability table with 2×5×5=50 rows,
each with 5 entries. For the purposes of illustration, we’ll assume that an honest recommen-
dation for a book of quality q from a person of kindness k is uniformly distributed in the range
[⌊q+k
2 ⌋,⌈q+k
2 ⌉].
The semantics of the RPM can be obtained by instantiating these dependencies for all
known constants, giving a Bayesian network (as in Figure 18.2(b)) that deﬁnes a joint distri-
bution over the RPM’s random variables.3
The set of possible worlds is the Cartesian product of the ranges of all the basic ran-
dom variables, and, as with Bayesian networks, the probability for each possible world is
the product of the relevant conditional probabilities from the model. With C customers and
B books, there are C Honest variables, C Kindness variables, B Quality variables, and BC
Recommendation variables, leading to 2C5C+B+BC possible worlds. With ten million books
and a billion customers, that’s about 107×1015 worlds. Thanks to the expressive power of
RPMs, the complete probability model still has only fewer than 300 parameters—most of
them in the RecCPT table.
We can reﬁne the model by asserting a context-speciﬁc independence (see page 438) to
reﬂect the fact that dishonest customers ignore quality when giving a recommendation; more-
over, kindness plays no role in their decisions. Thus, Recommendation(c,b) is independent
of Kindness(c) and Quality(b) when Honest(c)=false:
Recommendation(c,b) ∼
if Honest(c) then
HonestRecCPT(Kindness(c),Quality(b))
else ⟨0.4,0.1,0.0,0.1,0.4⟩.
This kind of dependency may look like an ordinary if–then–else statement in a programming
language, but there is a key difference: the inference engine doesn’t necessarily know the
value of the conditional test because Honest(c) is a random variable.
We can elaborate this model in endless ways to make it more realistic. For example,
suppose that an honest customer who is a fan of a book’s author always gives the book a 5,
regardless of quality:
Recommendation(c,b) ∼
if Honest(c) then
if Fan(c,Author(b)) then Exactly(5)
else HonestRecCPT(Kindness(c),Quality(b))
else ⟨0.4,0.1,0.0,0.1,0.4⟩
Again, the conditional test Fan(c,Author(b)) is unknown, but if a customer gives only 5s to a
particular author’s books and is not otherwise especially kind, then the posterior probability
that the customer is a fan of that author will be high. Furthermore, the posterior distribution
will tend to discount the customer’s 5s in evaluating the quality of that author’s books.
In this example, we implicitly assumed that the value of Author(b) is known for every
b, but this may not be the case. How can the system reason about whether, say, C1 is a fan
of Author(B2) when Author(B2) is unknown? The answer is that the system may have to
reason about all possible authors. Suppose (to keep things simple) that there are just two
3
Some technical conditions are required for an RPM to deﬁne a proper distribution. First, the dependencies must
be acyclic; otherwise the resulting Bayesian network will have cycles. Second, the dependencies must (usually)
be well-founded: there can be no inﬁnite ancestor chains, such as might arise from recursive dependencies. See
Exercise 18.HAMD for an exception to this rule.
