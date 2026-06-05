---
chunk_id: "book-ca4fca8dd8-chunk-1712"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1712
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 28.3
The Ethics of AI
1045
violated his due process rights. Though the Wisconsin Supreme Court found that the sentence
given would be no different without COMPAS in this case, it did issue warnings about the
algorithm’s accuracy and risks to minority defendants. Other researchers have questioned
whether it is appropriate to use algorithms in applications such as sentencing.
We could hope for an algorithm that is both well calibrated and equal opportunity, but,
as Kleinberg et al. (2016) show, that is impossible. If the base classes are different, then
any algorithm that is well calibrated will necessarily not provide equal opportunity, and vice
versa. How can we weigh the two criteria? Equal impact is one possibility. In the case of
COMPAS, this means weighing the negative utility of defendants being falsely classiﬁed as
high risk and losing their freedom, versus the cost to society of an additional crime being
committed, and ﬁnding the point that optimizes the tradeoff. This is complicated because
there are multiple costs to consider. There are individual costs—a defendant who is wrong-
fully held in jail suffers a loss, as does the victim of a defendant who was wrongfully released
and re-offends. But beyond that there are group costs—everyone has a certain fear that they
will be wrongfully jailed, or will be the victim of a crime, and all taxpayers contribute to the
costs of jails and courts. If we give value to those fears and costs in proportion to the size of
a group, then utility for the majority may come at the expense of a minority.
Another problem with the whole idea of recidivism scoring, regardless of the model used,
is that we don’t have unbiased ground truth data. The data does not tell us who has committed
a crime—all we know is who has been convicted of a crime. If the arresting ofﬁcers, judge,
or jury is biased, then the data will be biased. If more ofﬁcers patrol some locations, then
the data will be biased against people in those locations. Only defendants who are released
are candidates to recommit, so if the judges making the release decisions are biased, the data
may be biased. If you assume that behind the biased data set there is an underlying, unknown,
unbiased data set which has been corrupted by an agent with biases, then there are techniques
to recover an approximation to the unbiased data. Jiang and Nachum (2019) describe various
scenarios and the techniques involved.
One more risk is that machine learning can be used to justify bias. If decisions are made
by a biased human after consulting with a machine learning system, the human can say “here
is how my interpretation of the model supports my decision, so you shouldn’t question my
decision.” But other interpretations could lead to an opposite decision.
Sometimes fairness means that we should reconsider the objective function, not the data
or the algorithm. For example, in making job hiring decisions, if the objective is to hire
candidates with the best qualiﬁcations in hand, we risk unfairly rewarding those who have
had advantageous educational opportunities throughout their lives, thereby enforcing class
boundaries. But if the objective is to hire candidates with the best ability to learn on the job,
we have a better chance to cut across class boundaries and choose from a broader pool. Many
companies have programs designed for such applicants, and ﬁnd that after a year of training,
the employees hired this way do as well as the traditional candidates. Similarly, just 18% of
computer science graduates in the U.S. are women, but some schools, such as Harvey Mudd
University, have achieved 50% parity with an approach that is focused on encouraging and
retaining those who start the computer science program, especially those who start with less
programming experience.
A ﬁnal complication is deciding which classes deserve protection. In the U.S., the Fair
Housing Act recognized seven protected classes: race, color, religion, national origin, sex,
