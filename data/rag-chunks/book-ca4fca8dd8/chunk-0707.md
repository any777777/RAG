---
chunk_id: "book-ca4fca8dd8-chunk-0707"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 707
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
425
OK
 1,1
 2,1
 1,2
OK
OK
B
B
OK
 1,1
 2,1
 1,2
 2,2
OK
OK
B
B
OK
 1,1
 2,1
 3,1
 1,2
OK
OK
B
B
0.2 3 0.2 5 0.04
0.2 3 0.8 5 0.16
0.8 3 0.2 5 0.16
OK
 1,1
 2,1
 1,2
 1,3
OK
OK
B
B
OK
 1,1
 2,1
 3,1
 1,2
 1,3
OK
OK
B
B
0.2 3 0.2 5 0.04
0.2 3 0.8 5 0.16
(a)
(b)
 2,2
 1,3
 1,3
 2,2
 1,3
 3,1
 2,2
 2,2
 3,1
 3,1
Figure 12.6 Consistent models for the frontier variables, P2,2 and P3,1, showing P(frontier)
for each model: (a) three models with P1,3 =true showing two or three pits, and (b) two
models with P1,3 =false showing one or two pits.
can tell us that it is unknown whether there is a pit in [2, 2], but we need probability to tell us
how likely it is.
What this section has shown is that even seemingly complicated problems can be for-
mulated precisely in probability theory and solved with simple algorithms. To get efﬁcient
solutions, independence and conditional independence relationships can be used to simplify
the summations required. These relationships often correspond to our natural understanding
of how the problem should be decomposed. In the next chapter, we develop formal represen-
tations for such relationships as well as algorithms that operate on those representations to
perform probabilistic inference efﬁciently.
Summary
This chapter has suggested probability theory as a suitable foundation for uncertain reasoning
and provided a gentle introduction to its use.
• Uncertainty arises because of both laziness and ignorance. It is inescapable in complex,
nondeterministic, or partially observable environments.
• Probabilities express the agent’s inability to reach a deﬁnite decision regarding the
truth of a sentence. Probabilities summarize the agent’s beliefs relative to the evidence.
• Decision theory combines the agent’s beliefs and desires, deﬁning the best action as
the one that maximizes expected utility.
• Basic probability statements include prior or unconditional probabilities and poste-
rior or conditional probabilities over simple and complex propositions.
• The axioms of probability constrain the probabilities of logically related propositions.
An agent that violates the axioms must behave irrationally in some cases.
• The full joint probability distribution speciﬁes the probability of each complete as-
signment of values to random variables. It is usually too large to create or use in its
explicit form, but when it is available it can be used to answer queries simply by adding
up entries for the possible worlds corresponding to the query propositions.
• Absolute independence between subsets of random variables allows the full joint dis-
tribution to be factored into smaller joint distributions, greatly reducing its complexity.
