---
chunk_id: "book-ca4fca8dd8-chunk-1087"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1087
confidence: "first-pass"
extraction_method: "structured-local"
---

650
Chapter 18
Probabilistic Programming
objects. The most commonly used distribution over the nonnegative integers is the Poisson
distribution. The Poisson has one parameter, λ, which is the expected number of objects,
Poisson distribution
and a variable X sampled from Poisson(λ) has the following distribution:
P(X =k) = λke−λ/k!.
The variance of the Poisson is also λ, so the standard deviation is
√
λ. This means that
for large values of λ, the distribution is narrow relative to the mean—for example, if the
number of ants in a nest is modeled by a Poisson with a mean of one million, the standard
deviation is only a thousand, or 0.1%. For large numbers, it often makes more sense to use
the discrete log-normal distribution, which is appropriate when the log of the number of
Discrete log-normal
distribution
objects is normally distributed. A particularly intuitive form, which we call the order-of-
magnitude distribution, uses logs to base 10: thus, a distribution OM(3,1) has a mean of
Order-of-magnitude
distribution
103 and a standard deviation of one order of magnitude, i.e., the bulk of the probability mass
falls between 102 and 104.
The formal semantics of OUPMs begins with a deﬁnition of the objects that populate
possible worlds. In the standard semantics of typed ﬁrst-order logic, objects are just num-
bered tokens with types. In OUPMs, each object is a generation history; for example, an
object might be “the fourth login ID of the seventh customer.” (The reason for this slightly
baroque construction will become clear shortly.) For types with no origin functions—e.g.,
the Customer and Book types in Equation (18.2)—the objects have an empty origin; for ex-
ample, ⟨Customer, ,2⟩refers to the second customer generated from that number statement.
For number statements with origin functions—e.g., Equation (18.3)—each object records its
origin; for example, the object ⟨LoginID,⟨Owner,⟨Customer, ,2⟩⟩,3⟩is the third login be-
longing to the second customer.
The number variables of an OUPM specify how many objects there are of each type with
Number variable
each possible origin in each possible world; thus #LoginID⟨Owner,⟨Customer,,2⟩⟩(ω)=4 means
that in world ω, customer 2 owns 4 login IDs. As in relational probability models, the basic
random variables determine the values of predicates and functions for all tuples of objects;
thus, Honest⟨Customer,,2⟩(ω)=true means that in world ω, customer 2 is honest. A possible
world is deﬁned by the values of all the number variables and basic random variables. A
world may be generated from the model by sampling in topological order; Figure 18.4 shows
an example. The probability of a world so constructed is the product of the probabilities
for all the sampled values; in this case, 1.2672×10−11. Now it becomes clear why each
object contains its origin: this property ensures that every world can be constructed by exactly
one generation sequence. If this were not the case, the probability of a world would be an
unwieldy combinatorial sum over all possible generation sequences that create it.
Open-universe models may have inﬁnitely many random variables, so the full theory in-
volves nontrivial measure-theoretic considerations. For example, number statements with
Poisson or order-of-magnitude distributions allow for unbounded numbers of objects, lead-
ing to unbounded numbers of random variables for the properties and relations of those ob-
jects. Moreover, OUPMs can have recursive dependencies and inﬁnite types (integers, strings,
etc.). Finally, well-formedness disallows cyclic dependencies and inﬁnitely receding ancestor
chains; these conditions are undecidable in general, but certain syntactic sufﬁcient conditions
can be checked easily.
