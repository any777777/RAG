---
chunk_id: "book-ca4fca8dd8-chunk-0880"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 880
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.4
Multiattribute Utility Functions
533
15.4.2 Preference structure and multiattribute utility
Suppose we have n attributes, each of which has d distinct possible values. To specify the
complete utility function U(x1,...,xn), we need dn values in the worst case. Multiattribute
utility theory aims to identify additional structure in human preferences so that we don’t
need to specify all dn values individually. Having identiﬁed some regularity in preference
behavior, we then derive representation theorems to show that an agent with a certain kind
Representation
theorem
of preference structure has a utility function
U(x1,...,xn) = F[f1(x1),..., fn(xn)],
where F is (we hope) a simple function such as addition. Notice the similarity to the use of
Bayesian networks to decompose the joint probability of several random variables.
As an example, suppose each xi is the amount of money the agent has in a particular
currency: dollars, euros, marks, lira, etc. The fi functions could then convert each amount
into a common currency, and F would then be simply addition.
Preferences without uncertainty
Let us begin with the deterministic case. On page 522 we noted that for deterministic envi-
ronments, the agent has a value function, which we write here as V(x1,...,xn); the aim is to
represent this function concisely. The basic regularity that arises in deterministic preference
structures is called preference independence. Two attributes X1 and X2 are preferentially in-
Preference
independence
dependent of a third attribute X3 if the preference between outcomes ⟨x1,x2,x3⟩and ⟨x′
1,x′
2,x3⟩
does not depend on the particular value x3 for attribute X3.
Going back to the airport example, where we have (among other attributes) Quietness,
Frugality, and Safety to consider, one may propose that Quietness and Frugality are prefer-
entially independent of Safety. For example, if we prefer an outcome with 20,000 people
residing in the ﬂight path and a construction cost of $4 billion over an outcome with 70,000
people residing in the ﬂight path and a cost of $3.7 billion when the safety level is 0.006
deaths per billion passenger miles in both cases, then we would have the same preference
when the safety level is 0.012 or 0.003; and the same independence would hold for pref-
erences between any other pair of values for Quietness and Frugality. It is also apparent
that Frugality and Safety are preferentially independent of Quietness and that Quietness and
Safety are preferentially independent of Frugality.
We say that the set of attributes {Quietness,Frugality,Safety} exhibits mutual preferen-
tial independence (MPI). MPI says that, whereas each attribute may be important, it does
Mutual preferential
independence (MPI)
not affect the way in which one trades off the other attributes against each other.
Mutual preferential independence is a complicated name, but it leads to a simple form for
the agent’s value function (Debreu, 1960): If attributes X1, ..., Xn are mutually preferentially ◀
independent, then the agent’s preferences can be represented by a value function
V(x1,...,xn) = ∑
i
Vi(xi),
where each Vi refers only to the attribute Xi. For example, it might well be the case that the
airport decision can be made using a value function
V(quietness,frugality,safety) = quietness×104 +frugality+safety×1012 .
A value function of this type is called an additive value function. Additive functions are an
Additive value
function
