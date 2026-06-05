---
chunk_id: "book-ca4fca8dd8-chunk-0778"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 778
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 469

Section 13.5
Causal Networks
469
Rain
WetGrass
GreenerGrass
Cloudy
Sprinkler
Rain
(a)
GreenerGrass
WetGrass
Cloudy
(b)
Sprinkler
= True
Figure 13.23 (a) A causal Bayesian network representing cause–effect relations among ﬁve
variables. (b) The network after performing the action “turn Sprinkler on.”
13.5.1 Representing actions: The do-operator
Consider again the Sprinkler story of Figure 13.23(a). According to the standard semantics of
Bayes nets, the joint distribution of the ﬁve variables is given by a product of ﬁve conditional
distributions:
P(c,r,s,w,g) = P(c) P(r|c) P(s|c) P(w|r,s) P(g|w)
(13.14)
where we have abbreviated each variable name by its ﬁrst letter. As a system of structural
equations, the model looks like this:
C = fC(UC)
R = fR(C,UR)
S = fS(C,US)
(13.15)
W = fW(R,S,UW)
G = fG(W,UG)
where, without loss of generality, fC can be the identity function. The U-variables in these
equations represent unmodeled variables, also called error terms or disturbances, that per-
Unmodeled variable
turb the functional relationship between each variable and its parents. For example, UW may
represent another potential source of wetness, in addition to Sprinkler and Rain—perhaps
MorningDew or FireﬁghtingHelicopter.
If all the U-variables are mutually independent random variables with suitably chosen
priors, the joint distribution in Equation (13.14) can be represented exactly by the structural
equations in Equation (13.15). Thus, a system of stochastic relationships can be captured
by a system of deterministic relationships, each of which is affected by an exogenous dis-
turbance. However, the system of structural equations gives us more than that: it allows us
to predict how interventions will affect the operation of the system and hence the observable
consequences of those interventions. This is not possible given just the joint distribution.

## Page 470
