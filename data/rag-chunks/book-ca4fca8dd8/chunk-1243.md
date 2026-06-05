---
chunk_id: "book-ca4fca8dd8-chunk-1243"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1243
confidence: "first-pass"
extraction_method: "structured-local"
---

750
Chapter 20
Knowledge in Learning
We call this kind of generalization relevance-based learning, or RBL (although the name is
Relevance-based
learning
not standard). Notice that whereas RBL does make use of the content of the observations, it
does not produce hypotheses that go beyond the logical content of the background knowledge
and the observations. It is a deductive form of learning and cannot by itself account for the
creation of new knowledge starting from scratch.
In the case of the medical student watching the expert, we assume that the student’s
prior knowledge is sufﬁcient to infer the patient’s disease D from the symptoms. This is
not, however, enough to explain the fact that the doctor prescribes a particular medicine M.
The student needs to propose another rule, namely, that M generally is effective against D.
Given this rule and the student’s prior knowledge, the student can now explain why the expert
prescribes M in this particular case. We can generalize this example to come up with the
entailment constraint
Background ∧Hypothesis∧Descriptions |= Classiﬁcations .
(20.5)
That is, the background knowledge and the new hypothesis combine to explain the examples.
▶
As with pure inductive learning, the learning algorithm should propose hypotheses that are as
simple as possible, consistent with this constraint. Algorithms that satisfy constraint (20.5)
are called knowledge-based inductive learning, or KBIL, algorithms.
Knowledge-based
inductive learning
KBIL algorithms, which are described in detail in Section 20.5, have been studied mainly
in the ﬁeld of inductive logic programming, or ILP. In ILP systems, prior knowledge plays
Inductive logic
programming
two key roles in reducing the complexity of learning:
1. Because any hypothesis generated must be consistent with the prior knowledge as well
as with the new observations, the effective hypothesis space size is reduced to include
only those theories that are consistent with what is already known.
2. For any given set of observations, the size of the hypothesis required to construct an
explanation for the observations can be much reduced, because the prior knowledge
will be available to help out the new rules in explaining the observations. The smaller
the hypothesis, the easier it is to ﬁnd.
In addition to allowing the use of prior knowledge in induction, ILP systems can formulate
hypotheses in general ﬁrst-order logic, rather than in the restricted attribute-based language
of Chapter 19. This means that they can learn in environments that cannot be understood by
simpler systems.
20.3 Explanation-Based Learning
Explanation-based learning is a method for extracting general rules from individual obser-
vations. As an example, consider the problem of differentiating and simplifying algebraic
expressions (Exercise 9.17). If we differentiate an expression such as X2 with respect to
X, we obtain 2X. (We use a capital letter for the arithmetic unknown X, to distinguish it
from the logical variable x.) In a logical reasoning system, the goal might be expressed as
ASK(Derivative(X2,X)=d, KB), with solution d = 2X.
Anyone who knows differential calculus can see this solution “by inspection” as a result
of practice in solving such problems. A student encountering such problems for the ﬁrst
time, or a program with no experience, will have a much more difﬁcult job. Application
of the standard rules of differentiation eventually yields the expression 1 × (2 × (X(2−1))),
