---
chunk_id: "book-ca4fca8dd8-chunk-0910"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 910
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
549
late 1970s and early 1980s concentrated on answering questions, rather than on making de-
cisions. Those systems that did recommend actions generally did so using condition–action
rules rather than explicit representations of outcomes and preferences.
Decision networks offer a far more ﬂexible approach, for example by allowing prefer-
ences to change while keeping the transition model constant, or vice versa. They also al-
low a principled calculation of what information to seek next. In the late 1980s, partly due
to Pearl’s work on Bayes nets, decision-theoretic expert systems gained widespread accep-
tance (Horvitz et al., 1988; Cowell et al., 2002). In fact, from 1991 onward, the cover design
of the journal Artiﬁcial Intelligence has depicted a decision network, although some artistic
license appears to have been taken with the direction of the arrows.
Practical attempts to measure human utilities began with post-war decision analysis (see
above). The micromort utility measure is discussed by Howard (1989). Thaler Thaler (1992)
found that for a 1/1000 chance of death, a respondent wouldn’t pay more than $200 to remove
the risk, but wouldn’t accept $50,000 to take on the risk.
The use of QALYs (quality-adjusted life years) to perform cost–beneﬁt analyses of med-
ical interventions and related social policies dates back at least to work by Klarman et al.
(1968), although the term itself was ﬁrst used by Zeckhauser and Shepard (1976). Like
money, QALYs correspond directly to utilities only under fairly strong assumptions, such as
risk neutrality, that are often violated (Beresniak et al., 2015); nonetheless, QALYs are much
widely used in practice, for example in forming National Health Service policies in the UK.
See Russell (1990) for a typical example of an argument for a major change in public health
policy on grounds of increased expected utility measured in QALYs.
Keeney and Raiffa (1976) give an introduction to multiattribute utility theory. They
describe early computer implementations of methods for eliciting the necessary parameters
for a multiattribute utility function and include extensive accounts of real applications of the
theory. Abbas (2018) covers many advances since 1976. The theory was introduced to AI pri-
marily by the work of Wellman (1985), who also investigated the use of stochastic dominance
and qualitative probability models (Wellman, 1988, 1990a). Wellman and Doyle (1992) pro-
vide a preliminary sketch of how a complex set of utility-independence relationships might be
used to provide a structured model of a utility function, in much the same way that Bayesian
networks provide a structured model of joint probability distributions. Bacchus and Grove
(1995, 1996) and La Mura and Shoham (1999) give further results along these lines. Boutilier
et al. (2004) describe CP-nets, a fully worked out graphical model formalism for conditional
ceteribus paribus preference statements.
The optimizer’s curse was brought to the attention of decision analysts in a forceful
way by Smith and Winkler (2006), who pointed out that the ﬁnancial beneﬁts to the client
projected by analysts for their proposed course of action almost never materialized. They
trace this directly to the bias introduced by selecting an optimal action and show that a more
complete Bayesian analysis eliminates the problem.
The same underlying concept has been called post-decision disappointment by Harrison
Post-decision
disappointment
and March (1984) and was noted in the context of analyzing capital investment projects by
Brown (1974). The optimizer’s curse is also closely related to the winner’s curse (Capen
Winner’s curse
et al., 1971; Thaler, 1992), which applies to competitive bidding in auctions: whoever wins
the auction is very likely to have overestimated the value of the object in question. Capen et
al. quote a petroleum engineer on the topic of bidding for oil-drilling rights: “If one wins a
