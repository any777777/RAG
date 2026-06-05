---
chunk_id: "book-ca4fca8dd8-chunk-0709"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 709
confidence: "first-pass"
extraction_method: "structured-local"
---

426
Chapter 12
Quantifying Uncertainty
• Bayes’ rule allows unknown probabilities to be computed from known conditional
probabilities, usually in the causal direction. Applying Bayes’ rule with many pieces of
evidence runs into the same scaling problems as does the full joint distribution.
• Conditional independence brought about by direct causal relationships in the domain
allows the full joint distribution to be factored into smaller, conditional distributions.
The naive Bayes model assumes the conditional independence of all effect variables,
given a single cause variable; its size grows linearly with the number of effects.
• A wumpus-world agent can calculate probabilities for unobserved aspects of the world,
thereby improving on the decisions of a purely logical agent. Conditional independence
makes these calculations tractable.
Bibliographical and Historical Notes
Probability theory was invented as a way of analyzing games of chance. In about 850 CE the
Indian mathematician Mahaviracarya described how to arrange a set of bets that can’t lose
(what we now call a Dutch book). In Europe, the ﬁrst signiﬁcant systematic analyses were
produced by Girolamo Cardano around 1565, although publication was posthumous (1663).
By that time, probability had been established as a mathematical discipline due to a series of
results from a famous correspondence between Blaise Pascal and Pierre de Fermat in 1654.
The ﬁrst published textbook on probability was De Ratiociniis in Ludo Aleae (On Reasoning
in a Game of Chance) by Huygens (1657). The “laziness and ignorance” view of uncertainty
was described by John Arbuthnot in the preface of his translation of Huygens (Arbuthnot,
1692): “It is impossible for a Die, with such determin’d force and direction, not to fall on
such determin’d side, only I don’t know the force and direction which makes it fall on such
determin’d side, and therefore I call it Chance, which is nothing but the want of art.”
The connection between probability and reasoning dates back at least to the nineteenth
century: in 1819, Pierre Laplace said, “Probability theory is nothing but common sense re-
duced to calculation.” In 1850, James Maxwell said, “The true logic for this world is the
calculus of Probabilities, which takes account of the magnitude of the probability which is,
or ought to be, in a reasonable man’s mind.”
There has been endless debate over the source and status of probability numbers. The
frequentist position is that the numbers can come only from experiments: if we test 100
Frequentist
people and ﬁnd that 10 of them have a cavity, then we can say that the probability of a cavity
is approximately 0.1. In this view, the assertion “the probability of a cavity is 0.1” means that
0.1 is the fraction that would be observed in the limit of inﬁnitely many samples. From any
ﬁnite sample, we can estimate the true fraction and also calculate how accurate our estimate
is likely to be.
The objectivist view is that probabilities are real aspects of the universe—propensities
Objectivist
of objects to behave in certain ways—rather than being just descriptions of an observer’s
degree of belief. For example, the fact that a fair coin comes up heads with probability
0.5 is a propensity of the coin itself. In this view, frequentist measurements are attempts to
observe these propensities. Most physicists agree that quantum phenomena are objectively
probabilistic, but uncertainty at the macroscopic scale—e.g., in coin tossing—usually arises
from ignorance of initial conditions and does not seem consistent with the propensity view.
