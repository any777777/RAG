---
chunk_id: "book-ca4fca8dd8-chunk-1154"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1154
confidence: "first-pass"
extraction_method: "structured-local"
---

692
Chapter 19
Learning from Examples
Patrons(x, Some)
No
Yes
Yes
No
Patrons(x, Full)      Fri/Sat(x)
Yes
No
Yes
^
Figure 19.10 A decision list for the restaurant problem.
examples. Thus, with probability at least 1−δ, after seeing this many examples, the learning
algorithm will return a hypothesis that has error at most ϵ. In other words, it is probably
approximately correct. The number of required examples, as a function of ϵ and δ, is called
the sample complexity of the learning algorithm.
Sample complexity
As we saw earlier, if H is the set of all Boolean functions on n attributes, then |H| = 22n.
Thus, the sample complexity of the space grows as 2n. Because the number of possible
examples is also 2n, this suggests that PAC-learning in the class of all Boolean functions
requires seeing all, or nearly all, of the possible examples. A moment’s thought reveals the
reason for this: H contains enough hypotheses to classify any given set of examples in all
possible ways. In particular, for any set of N examples, the set of hypotheses consistent with
those examples contains equal numbers of hypotheses that predict xN+1 to be positive and
hypotheses that predict xN+1 to be negative.
To obtain real generalization to unseen examples, then, it seems we need to restrict the
hypothesis space H in some way; but of course, if we do restrict the space, we might eliminate
the true function altogether. There are three ways to escape this dilemma.
The ﬁrst is to bring prior knowledge to bear on the problem.
The second, which we introduced in Section 19.4.3, is to insist that the algorithm re-
turn not just any consistent hypothesis, but preferably a simple one (as is done in decision
tree learning). In cases where ﬁnding simple consistent hypotheses is tractable, the sample
complexity results are generally better than for analyses based only on consistency.
The third, which we pursue next, is to focus on learnable subsets of the entire hypoth-
esis space of Boolean functions. This approach relies on the assumption that the restricted
hypothesis space contains a hypothesis h that is close enough to the true function f; the bene-
ﬁts are that the restricted hypothesis space allows for effective generalization and is typically
easier to search. We now examine one such restricted hypothesis space in more detail.
19.5.1 PAC learning example: Learning decision lists
We now show how to apply PAC learning to a new hypothesis space: decision lists. A
Decision lists
decision list consists of a series of tests, each of which is a conjunction of literals. If a
test succeeds when applied to an example description, the decision list speciﬁes the value
to be returned. If the test fails, processing continues with the next test in the list. Decision
lists resemble decision trees, but their overall structure is simpler: they branch only in one
direction. In contrast, the individual tests are more complex. Figure 19.10 shows a decision
list that represents the following hypothesis:
WillWait ⇔(Patrons = Some)∨(Patrons = Full∧Fri/Sat).
If we allow tests of arbitrary size, then decision lists can represent any Boolean function
