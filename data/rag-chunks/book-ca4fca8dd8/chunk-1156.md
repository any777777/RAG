---
chunk_id: "book-ca4fca8dd8-chunk-1156"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1156
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.5
The Theory of Learning
693
function DECISION-LIST-LEARNING(examples) returns a decision list, or failure
if examples is empty then return the trivial decision list No
t←a test that matches a nonempty subset examplest of examples
such that the members of examplest are all positive or all negative
if there is no such t then return failure
if the examples in examplest are positive then o←Yes else o←No
return a decision list with initial test t and outcome o and remaining tests given by
DECISION-LIST-LEARNING(examples −examplest)
Figure 19.11 An algorithm for learning decision lists.
(Exercise 19.DLEX). On the other hand, if we restrict the size of each test to at most k literals,
then it is possible for the learning algorithm to generalize successfully from a small number
of examples. We use the notation k-DL for a decision list with up to k conjunctions. The
example in Figure 19.10 is in 2-DL. It is easy to show (Exercise 19.DLEX) that k-DL includes
as a subset k-DT, the set of all decision trees of depth at most k. We will use the notation
K-DT
k-DL(n) to denote a k-DL using n Boolean attributes.
The ﬁrst task is to show that k-DL is learnable—that is, that any function in k-DL can be
approximated accurately after training on a reasonable number of examples. To do this, we
need to calculate the number of possible hypotheses. Let the set of conjunctions of at most k
literals using n attributes be Conj(n,k). Because a decision list is constructed from tests, and
because each test can be attached to either a Yes or a No outcome or can be absent from the
decision list, there are at most 3|Conj(n,k)| distinct sets of component tests. Each of these sets
of tests can be in any order, so
|k-DL(n)| ≤3cc! where c = |Conj(n,k)|.
The number of conjunctions of at most k literals from n attributes is given by
|Conj(n,k)| =
k
∑
i=0
2n
i

= O(nk).
Hence, after some work, we obtain
|k-DL(n)| = 2O(nk log2(nk)) .
We can plug this into Equation (19.1) to show that the number of examples needed for PAC-
learning a k-DL(n) function is polynomial in n:
N ≥1
ϵ

ln 1
δ +O(nk log2(nk))

.
Therefore, any algorithm that returns a consistent decision list will PAC-learn a k-DL function
in a reasonable number of examples, for small k.
The next task is to ﬁnd an efﬁcient algorithm that returns a consistent decision list. We
will use a greedy algorithm called DECISION-LIST-LEARNING that repeatedly ﬁnds a test
that agrees exactly with some subset of the training set. Once it ﬁnds such a test, it adds
it to the decision list under construction and removes the corresponding examples. It then
