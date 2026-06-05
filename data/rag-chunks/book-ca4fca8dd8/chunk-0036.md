---
chunk_id: "book-ca4fca8dd8-chunk-0036"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 36
confidence: "first-pass"
extraction_method: "structured-local"
---

26
Chapter 1
Introduction
of an outcome. The modern notion of rational decision making under uncertainty involves
maximizing expected utility, as explained in Chapter 15.
In matters of ethics and public policy, a decision maker must consider the interests of
multiple individuals. Jeremy Bentham (1823) and John Stuart Mill (1863) promoted the idea
of utilitarianism: that rational decision making based on maximizing utility should apply
Utilitarianism
to all spheres of human activity, including public policy decisions made on behalf of many
individuals. Utilitarianism is a speciﬁc kind of consequentialism: the idea that what is right
and wrong is determined by the expected outcomes of an action.
In contrast, Immanuel Kant, in 1785, proposed a theory of rule-based or deontological
ethics, in which “doing the right thing” is determined not by outcomes but by universal social
Deontological ethics
laws that govern allowable actions, such as “don’t lie” or “don’t kill.” Thus, a utilitarian could
tell a white lie if the expected good outweighs the bad, but a Kantian would be bound not to,
because lying is inherently wrong. Mill acknowledged the value of rules, but understood them
as efﬁcient decision procedures compiled from ﬁrst-principles reasoning about consequences.
Many modern AI systems adopt exactly this approach.
1.2.2 Mathematics
• What are the formal rules to draw valid conclusions?
• What can be computed?
• How do we reason with uncertain information?
Philosophers staked out some of the fundamental ideas of AI, but the leap to a formal science
required the mathematization of logic and probability and the introduction of a new branch
of mathematics: computation.
The idea of formal logic can be traced back to the philosophers of ancient Greece, India,
Formal logic
and China, but its mathematical development really began with the work of George Boole
(1815–1864), who worked out the details of propositional, or Boolean, logic (Boole, 1847).
In 1879, Gottlob Frege (1848–1925) extended Boole’s logic to include objects and relations,
creating the ﬁrst-order logic that is used today.5 In addition to its central role in the early pe-
riod of AI research, ﬁrst-order logic motivated the work of G¨odel and Turing that underpinned
computation itself, as we explain below.
The theory of probability can be seen as generalizing logic to situations with uncertain
Probability
information—a consideration of great importance for AI. Gerolamo Cardano (1501–1576)
ﬁrst framed the idea of probability, describing it in terms of the possible outcomes of gam-
bling events. In 1654, Blaise Pascal (1623–1662), in a letter to Pierre Fermat (1601–1665),
showed how to predict the future of an unﬁnished gambling game and assign average pay-
offs to the gamblers. Probability quickly became an invaluable part of the quantitative sci-
ences, helping to deal with uncertain measurements and incomplete theories. Jacob Bernoulli
(1654–1705, uncle of Daniel), Pierre Laplace (1749–1827), and others advanced the theory
and introduced new statistical methods. Thomas Bayes (1702–1761) proposed a rule for up-
dating probabilities in the light of new evidence; Bayes’ rule is a crucial tool for AI systems.
The formalization of probability, combined with the availability of data, led to the emer-
gence of statistics as a ﬁeld.
One of the ﬁrst uses was John Graunt’s analysis of Lon-
Statistics
5
Frege’s proposed notation for ﬁrst-order logic—an arcane combination of textual and geometric features—
never became popular.
