---
chunk_id: "book-ca4fca8dd8-chunk-0693"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 693
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.4
Independence
415
In other words, we can calculate P(Cavity|toothache) even if we don’t know the value of
P(toothache)! We temporarily forget about the factor 1/P(toothache) and add up the values
for cavity and ¬cavity, getting 0.12 and 0.08. Those are the correct relative proportions, but
they don’t sum to 1, so we normalize them by dividing each one by 0.12 + 0.08, getting
the true probabilities of 0.6 and 0.4. Normalization turns out to be a useful shortcut in many
probability calculations, both to make the computation easier and to allow us to proceed when
some probability assessment (such as P(toothache)) is not available.
From the example, we can extract a general inference procedure. We begin with the case
in which the query involves a single variable, X (Cavity in the example). Let E be the list
of evidence variables (just Toothache in the example), let e be the list of observed values for
them, and let Y be the remaining unobserved variables (just Catch in the example). The query
is P(X |e) and can be evaluated as
P(X |e) = αP(X,e) = α∑
y
P(X,e,y),
(12.9)
where the summation is over all possible ys (i.e., all possible combinations of values of the
unobserved variables Y). Notice that together the variables X, E, and Y constitute the com-
plete set of variables for the domain, so P(X,e,y) is simply a subset of probabilities from the
full joint distribution.
Given the full joint distribution to work with, Equation (12.9) can answer probabilistic
queries for discrete variables. It does not scale well, however: for a domain described by n
Boolean variables, it requires an input table of size O(2n) and takes O(2n) time to process
the table. In a realistic problem we could easily have n = 100, making O(2n) impractical—a
table with 2100 ≈1030 entries! The problem is not just memory and computation: the real
issue is that if each of the 1030 probabilities has to be estimated separately from examples,
the number of examples required will be astronomical.
For these reasons, the full joint distribution in tabular form is seldom a practical tool
for building reasoning systems. Instead, it should be viewed as the theoretical foundation
on which more effective approaches may be built, just as truth tables formed a theoretical
foundation for more practical algorithms like DPLL in Chapter 7. The remainder of this
chapter introduces some of the basic ideas required in preparation for the development of
realistic systems in Chapter 13.
12.4 Independence
Let us expand the full joint distribution in Figure 12.3 by adding a fourth variable, Weather.
The full joint distribution then becomes P(Toothache,Catch,Cavity,Weather), which has 2×
2 × 2 × 4 = 32 entries. It contains four “editions” of the table shown in Figure 12.3, one
for each kind of weather. What relationship do these editions have to each other and to the
original three-variable table? How is the value of P(toothache,catch,cavity,cloud) related to
the value of P(toothache,catch,cavity)? We can use the product rule (Equation (12.4)):
P(toothache,catch,cavity,cloud)
= P(cloud|toothache,catch,cavity)P(toothache,catch,cavity).
Now, unless one is in the deity business, one should not imagine that one’s dental problems
inﬂuence the weather. And for indoor dentistry, at least, it seems safe to say that the weather
