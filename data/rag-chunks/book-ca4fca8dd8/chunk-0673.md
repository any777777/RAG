---
chunk_id: "book-ca4fca8dd8-chunk-0673"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 673
confidence: "first-pass"
extraction_method: "structured-local"
---

404
Chapter 12
Quantifying Uncertainty
the likelihood that, and degree to which, they will be achieved. The remainder of this section
hones these ideas, in preparation for the development of the general theories of uncertain
reasoning and rational decisions that we present in this and subsequent chapters.
12.1.1 Summarizing uncertainty
Let’s consider an example of uncertain reasoning: diagnosing a dental patient’s toothache.
Diagnosis—whether for medicine, automobile repair, or whatever—almost always involves
uncertainty. Let us try to write rules for dental diagnosis using propositional logic, so that we
can see how the logical approach breaks down. Consider the following simple rule:
Toothache ⇒Cavity.
The problem is that this rule is wrong. Not all patients with toothaches have cavities; some
of them have gum disease, an abscess, or one of several other problems:
Toothache ⇒Cavity∨GumProblem∨Abscess...
Unfortunately, in order to make the rule true, we have to add an almost unlimited list of
possible problems. We could try turning the rule into a causal rule:
Cavity ⇒Toothache.
But this rule is not right either; not all cavities cause pain. The only way to ﬁx the rule
is to make it logically exhaustive: to augment the left-hand side with all the qualiﬁcations
required for a cavity to cause a toothache. Trying to use logic to cope with a domain like
medical diagnosis thus fails for three main reasons:
• Laziness: It is too much work to list the complete set of antecedents or consequents
Laziness
needed to ensure an exceptionless rule and too hard to use such rules.
• Theoretical ignorance: Medical science has no complete theory for the domain.
Theoretical
ignorance
• Practical ignorance: Even if we know all the rules, we might be uncertain about a
Practical ignorance
particular patient because not all the necessary tests have been or can be run.
The connection between toothaches and cavities is not a strict logical consequence in either
direction. This is typical of the medical domain, as well as most other judgmental domains:
law, business, design, automobile repair, gardening, dating, and so on. The agent’s knowledge
can at best provide only a degree of belief in the relevant sentences. Our main tool for
Degree of belief
dealing with degrees of belief is probability theory. In the terminology of Section 8.1, the
Probability theory
ontological commitments of logic and probability theory are the same—that the world is
composed of facts that do or do not hold in any particular case—but the epistemological
commitments are different: a logical agent believes each sentence to be true or false or has
no opinion, whereas a probabilistic agent may have a numerical degree of belief between 0
(for sentences that are certainly false) and 1 (certainly true).
The theory of probability provides a way of summarizing the uncertainty that comes from
▶
our laziness and ignorance, thereby solving the qualiﬁcation problem. We might not know
for sure what afﬂicts a particular patient, but we believe that there is, say, an 80% chance—
that is, a probability of 0.8—that the patient who has a toothache has a cavity. That is, we
expect that out of all the situations that are indistinguishable from the current situation as far
as our knowledge goes, the patient will have a cavity in 80% of them. This belief could be
derived from statistical data—80% of the toothache patients seen so far have had cavities—or
from some general dental knowledge, or from a combination of evidence sources.
