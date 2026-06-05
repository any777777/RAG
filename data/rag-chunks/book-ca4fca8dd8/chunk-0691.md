---
chunk_id: "book-ca4fca8dd8-chunk-0691"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 691
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.3
Inference Using Full Joint Distributions
413
set of axioms for reasoning with degrees of beliefs: no contradictions, correspondence with
ordinary logic (for example, if belief in A goes up, then belief in ¬A must go down), and so
on. The only controversial axiom is that degrees of belief must be numbers, or at least act
like numbers in that they must be transitive (if belief in A is greater than belief in B, which is
greater than belief in C, then belief in A must be greater than C) and comparable (the belief
in A must be one of equal to, greater than, or less than belief in B). It can then be proved that
probability is the only approach that satisﬁes these axioms.
The world being the way it is, however, practical demonstrations sometimes speak louder
than proofs. The success of reasoning systems based on probability theory has been much
more effective than philosophical arguments in making converts. We now look at how the
axioms can be deployed to make inferences.
12.3 Inference Using Full Joint Distributions
In this section we describe a simple method for probabilistic inference—that is, the compu-
Probabilistic
inference
tation of posterior probabilities for query propositions given observed evidence. We use the
Query
full joint distribution as the “knowledge base” from which answers to all questions may be de-
rived. Along the way we also introduce several useful techniques for manipulating equations
involving probabilities.
We begin with a simple example: a domain consisting of just the three Boolean variables
Toothache, Cavity, and Catch (the dentist’s nasty steel probe catches in my tooth). The full
joint distribution is a 2×2×2 table as shown in Figure 12.3.
toothache
¬toothache
catch
¬catch
catch
¬catch
cavity
0.108
0.012
0.072
0.008
¬cavity
0.016
0.064
0.144
0.576
Figure 12.3 A full joint distribution for the Toothache, Cavity, Catch world.
Notice that the probabilities in the joint distribution sum to 1, as required by the axioms of
probability. Notice also that Equation (12.2) gives us a direct way to calculate the probability
of any proposition, simple or complex: simply identify those possible worlds in which the
proposition is true and add up their probabilities. For example, there are six possible worlds
in which cavity∨toothache holds:
P(cavity∨toothache) = 0.108+0.012+0.072+0.008+0.016+0.064 = 0.28.
One particularly common task is to extract the distribution over some subset of variables or
a single variable. For example, adding the entries in the ﬁrst row gives the unconditional or
marginal probability6 of cavity:
Marginal probability
P(cavity) = 0.108+0.012+0.072+0.008 = 0.2.
6
So called because of a common practice among actuaries of writing the sums of observed frequencies in the
margins of insurance tables.
