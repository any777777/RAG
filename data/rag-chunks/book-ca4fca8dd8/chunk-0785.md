---
chunk_id: "book-ca4fca8dd8-chunk-0785"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 785
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
473
pugnacious “In Defense of Probability” and his later article “An Inquiry into Computer Un-
derstanding” (Cheeseman, 1988, with commentaries) helped to turn the tables.
The resurgence of probability depended mainly, however, on Pearl’s development of
Bayesian networks and the broad development of a probabilistic approach to AI as outlined
in his book, Probabilistic Reasoning in Intelligent Systems (Pearl, 1988). The book cov-
ered both representational issues, including conditional independence relationships and the
d-separation criterion, and algorithmic approaches. Geiger et al. (1990a) and Tian et al.
(1998) presented key computational results on efﬁcient detection of d-separation.
Eugene Charniak helped present Pearl’s ideas to AI researchers with a popular article,
“Bayesian networks without tears”8 (1991), and book (1993). The book by Dean and Well-
man (1991) also helped introduce Bayesian networks to AI researchers. Shachter (1998)
presented a simpliﬁed way to determine d-separation called the “Bayes-ball” algorithm.
As applications of Bayes nets were developed, researchers found it necessary to go be-
yond the basic model of discrete variables with CPTs. For example, the CPCS system (Prad-
han et al., 1994), a Bayesian network for internal medicine with 448 nodes and 906 links,
made extensive use of the noisy logical operators proposed by Good (1961). Boutilier et al.
(1996) analyzed the algorithmic beneﬁts of context-speciﬁc independence. The inclusion
of continuous random variables in Bayesian networks was considered by Pearl (1988) and
Shachter and Kenley (1989); these papers discussed networks containing only continuous
variables with linear Gaussian distributions.
Hybrid networks with both discrete and continuous variables were investigated by Lau-
ritzen and Wermuth (1989) and implemented in the cHUGIN system (Olesen, 1993). Further
analysis of linear–Gaussian models, with connections to many other models used in statis-
tics, appears in Roweis and Ghahramani (1999); Lerner (2002) provides a very thorough
discussion of their use in hybrid Bayes nets. The probit distribution is usually attributed to
Gaddum (1933) and Bliss (1934), although it had been discovered several times in the 19th
century. Bliss’s work was expanded considerably by Finney (1947). The probit has been used
widely for modeling discrete choice phenomena and can be extended to handle more than two
choices (Daganzo, 1979). The expit (inverse logit) model was introduced by Berkson (1944);
initially much derided, it eventually became more popular than the probit model. Bishop
(1995) gives a simple justiﬁcation for its use.
Early applications of Bayes nets in medicine included the MUNIN system for diagnosing
neuromuscular disorders (Andersen et al., 1989) and the PATHFINDER system for pathology
(Heckerman, 1991). Applications in engineering include the Electric Power Research Insti-
tute’s work on monitoring power generators (Morjaria et al., 1995), NASA’s work on display-
ing time-critical information at Mission Control in Houston (Horvitz and Barry, 1995), and
the general ﬁeld of network tomography, which aims to infer unobserved local properties of
nodes and links in the Internet from observations of end-to-end message performance (Cas-
tro et al., 2004). Perhaps the most widely used Bayesian network systems have been the
diagnosis-and-repair modules (e.g., the Printer Wizard) in Microsoft Windows (Breese and
Heckerman, 1996) and the Ofﬁce Assistant in Microsoft Ofﬁce (Horvitz et al., 1998).
Another important application area is biology: the mathematical models used to analyze
genetic inheritance in family trees (so-called pedigree analysis) are in fact a special form
Pedigree analysis
8
The title of the original version of the article was “Pearl for swine.”
