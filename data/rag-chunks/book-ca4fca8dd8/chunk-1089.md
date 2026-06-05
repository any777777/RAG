---
chunk_id: "book-ca4fca8dd8-chunk-1089"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1089
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.2
Open-Universe Probability Models
651
Variable
Value
Probability
#Customer
2
0.3333
#Book
3
0.3333
Honest⟨Customer,,1⟩
true
0.99
Honest⟨Customer,,2⟩
false
0.01
Kindness⟨Customer,,1⟩
4
0.3
Kindness⟨Customer,,2⟩
1
0.1
Quality⟨Book,,1⟩
1
0.05
Quality⟨Book,,2⟩
3
0.4
Quality⟨Book,,3⟩
5
0.15
#LoginID⟨Owner,⟨Customer,,1⟩⟩
1
1.0
#LoginID⟨Owner,⟨Customer,,2⟩⟩
2
0.25
Recommendation⟨LoginID,⟨Owner,⟨Customer,,1⟩⟩,1⟩,⟨Book,,1⟩
2
0.5
Recommendation⟨LoginID,⟨Owner,⟨Customer,,1⟩⟩,1⟩,⟨Book,,2⟩
4
0.5
Recommendation⟨LoginID,⟨Owner,⟨Customer,,1⟩⟩,1⟩,⟨Book,,3⟩
5
0.5
Recommendation⟨LoginID,⟨Owner,⟨Customer,,2⟩⟩,1⟩,⟨Book,,1⟩
5
0.4
Recommendation⟨LoginID,⟨Owner,⟨Customer,,2⟩⟩,1⟩,⟨Book,,2⟩
5
0.4
Recommendation⟨LoginID,⟨Owner,⟨Customer,,2⟩⟩,1⟩,⟨Book,,3⟩
1
0.4
Recommendation⟨LoginID,⟨Owner,⟨Customer,,2⟩⟩,2⟩,⟨Book,,1⟩
5
0.4
Recommendation⟨LoginID,⟨Owner,⟨Customer,,2⟩⟩,2⟩,⟨Book,,2⟩
5
0.4
Recommendation⟨LoginID,⟨Owner,⟨Customer,,2⟩⟩,2⟩,⟨Book,,3⟩
1
0.4
Figure 18.4 One particular world for the book recommendation OUPM. The number vari-
ables and basic random variables are shown in topological order, along with their chosen
values and the probabilities for those values.
18.2.2 Inference in open-universe probability models
Because of the potentially huge and sometimes unbounded size of the implicit Bayes net that
corresponds to a typical OUPM, unrolling it fully and performing exact inference is quite
impractical. Instead, we must consider approximate inference algorithms such as MCMC
(see Section 13.4.2).
Roughly speaking, an MCMC algorithm for an OUPM is exploring the space of possible
worlds deﬁned by sets of objects and relations among them, as illustrated in Figure 18.1(top).
A move between adjacent states in this space can not only alter relations and functions but
also add or subtract objects and change the interpretations of constant symbols. Even though
each possible world may be huge, the probability computations required for each step—
whether in Gibbs sampling or Metropolis–Hastings—are entirely local and in most cases
take constant time. This is because the probability ratio between neighboring worlds depends
on a subgraph of constant size around the variables whose values are changed. Moreover, a
logical query can be evaluated incrementally in each world visited, usually in constant time
per world, rather than being recomputing from scratch.
Some special consideration needs to be given to the fact that a typical OUPM may have
possible worlds of inﬁnite size. As an example, consider the multitarget tracking model in
Figure 18.9: the function X(a,t), denoting the state of aircraft a at time t, corresponds to
an inﬁnite sequence of variables for an unbounded number of aircraft at each step. For this
reason, MCMC for OUPMs samples not completely speciﬁed possible worlds but partial
