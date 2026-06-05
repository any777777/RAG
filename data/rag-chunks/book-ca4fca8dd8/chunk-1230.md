---
chunk_id: "book-ca4fca8dd8-chunk-1230"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1230
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.1
A Logical Formulation of Learning
741
• An example can be a false positive for the hypothesis, if the hypothesis says it should
False positive
be positive but in fact it is negative.1
If an example is a false positive or false negative for a hypothesis, then the example and the
hypothesis are logically inconsistent with each other. Assuming that the example is a correct
observation of fact, then the hypothesis can be ruled out. Logically, this is exactly analogous
to the resolution rule of inference (see Chapter 9), where the disjunction of hypotheses cor-
responds to a clause and the example corresponds to a literal that resolves against one of the
literals in the clause. An ordinary logical inference system therefore could, in principle, learn
from the example by eliminating one or more hypotheses. Suppose, for example, that the
example is denoted by the sentence I1, and the hypothesis space is h1 ∨h2 ∨h3 ∨h4. Then if
I1 is inconsistent with h2 and h3, the logical inference system can deduce the new hypothesis
space h1 ∨h4.
We therefore can characterize inductive learning in a logical setting as a process of grad-
ually eliminating hypotheses that are inconsistent with the examples, narrowing down the
possibilities. Because the hypothesis space is usually vast (or even inﬁnite in the case of
ﬁrst-order logic), we do not recommend trying to build a learning system using resolution-
based theorem proving and a complete enumeration of the hypothesis space. Instead, we will
describe two approaches that ﬁnd logically consistent hypotheses with much less effort.
20.1.2 Current-best-hypothesis search
The idea behind current-best-hypothesis search is to maintain a single hypothesis, and to
Current-best-
hypothesis
adjust it as new examples arrive in order to maintain consistency. The basic algorithm was
described by John Stuart Mill (1843), and may well have appeared even earlier.
Suppose we have some hypothesis such as hr, of which we have grown quite fond. As
long as each new example is consistent, we need do nothing. Then along comes a false neg-
ative example, X13. What do we do? Figure 20.1(a) shows hr schematically as a region:
everything inside the rectangle is part of the extension of hr. The examples that have actu-
ally been seen so far are shown as “+” or “–”, and we see that hr correctly categorizes all
the examples as positive or negative examples of WillWait. In Figure 20.1(b), a new exam-
ple (circled) is a false negative: the hypothesis says it should be negative but it is actually
positive. The extension of the hypothesis must be increased to include it. This is called gen-
eralization; one possible generalization is shown in Figure 20.1(c). Then in Figure 20.1(d),
Generalization
we see a false positive: the hypothesis says the new example (circled) should be positive,
but it actually is negative. The extension of the hypothesis must be decreased to exclude
the example. This is called specialization; in Figure 20.1(e) we see one possible specializa-
Specialization
tion of the hypothesis. The “more general than” and “more speciﬁc than” relations between
hypotheses provide the logical structure on the hypothesis space that makes efﬁcient search
possible.
We can now specify the CURRENT-BEST-LEARNING algorithm, shown in Figure 20.2.
Notice that each time we consider generalizing or specializing the hypothesis, we must check
for consistency with the other examples, because an arbitrary increase/decrease in the exten-
sion might include/exclude previously seen negative/positive examples.
1
The terms “false positive” and “false negative” are used in medicine to describe erroneous results from lab
tests. A result is a false positive if it indicates that the patient has the disease when in fact no disease is present.
