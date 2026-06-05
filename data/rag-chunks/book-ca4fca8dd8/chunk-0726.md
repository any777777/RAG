---
chunk_id: "book-ca4fca8dd8-chunk-0726"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 726
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 436

436
Chapter 13
Probabilistic Reasoning
JohnCalls
MaryCalls
Alarm
Burglary
Earthquake
MaryCalls
Alarm
Earthquake
Burglary
JohnCalls
(a)
(b)
1
2
4
2
4
1
2
4
8
16
Figure 13.3 Network structure and number of parameters depends on order of introduc-
tion. (a) The structure obtained with ordering M,J,A,B,E. (b) The structure obtained with
M,J,E,B,A. Each node is annotated with the number of parameters required; 13 in all for
(a) and 31 for (b). In Figure 13.2, only 10 parameters were required.
The resulting network has two more links than the original network in Figure 13.2 and re-
quires 13 conditional probabilities rather than 10. What’s worse, some of the links represent
tenuous relationships that require difﬁcult and unnatural probability judgments, such as as-
sessing the probability of Earthquake, given Burglary and Alarm. This phenomenon is quite
general and is related to the distinction between causal and diagnostic models introduced
in Section 12.5.1 (see also Exercise 13.WUMD). If we stick to a causal model, we end up
▶
having to specify fewer numbers, and the numbers will often be easier to come up with. For
example, in the domain of medicine, it has been shown by Tversky and Kahneman (1982)
that expert physicians prefer to give probability judgments for causal rules rather than for
diagnostic ones. Section 13.5 explores the idea of causal models in more depth.
Figure 13.3(b) shows a very bad node ordering: MaryCalls, JohnCalls, Earthquake,
Burglary, Alarm. This network requires 31 distinct probabilities to be speciﬁed—exactly
the same number as the full joint distribution. It is important to realize, however, that any
of the three networks can represent exactly the same joint distribution. The two versions in
Figure 13.3 simply fail to represent all the conditional independence relationships and hence
end up specifying a lot of unnecessary numbers instead.
13.2.1 Conditional independence relations in Bayesian networks
From the semantics of Bayes nets as deﬁned in Equation (13.2), we can derive a number of
conditional independence properties. We have already seen the property that a variable is
conditionally independent of its other predecessors, given its parents. It is also possible to
prove the more general “non-descendants” property that:
Each variable is conditionally independent of its non-descendants, given its parents.
Descendant

## Page 437
