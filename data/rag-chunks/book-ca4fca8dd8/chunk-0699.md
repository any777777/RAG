---
chunk_id: "book-ca4fca8dd8-chunk-0699"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 699
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.5
Bayes’ Rule and Its Use
419
nasty steel probe catches in the aching tooth of a patient? If we know the full joint distribution
(Figure 12.3), we can read off the answer:
P(Cavity|toothache∧catch) = α⟨0.108,0.016⟩≈⟨0.871,0.129⟩.
We know, however, that such an approach does not scale up to larger numbers of variables.
We can try using Bayes’ rule to reformulate the problem:
P(Cavity|toothache∧catch)
= αP(toothache∧catch|Cavity)P(Cavity).
(12.16)
For this reformulation to work, we need to know the conditional probabilities of the conjunc-
tion toothache∧catch for each value of Cavity. That might be feasible for just two evidence
variables, but again it does not scale up. If there are n possible evidence variables (X rays,
diet, oral hygiene, etc.), then there are O(2n) possible combinations of observed values for
which we would need to know conditional probabilities. This is no better than using the full
joint distribution.
To make progress, we need to ﬁnd some additional assertions about the domain that will
enable us to simplify the expressions. The notion of independence in Section 12.4 provides
a clue, but needs reﬁning. It would be nice if Toothache and Catch were independent, but
they are not: if the probe catches in the tooth, then it is likely that the tooth has a cavity
and that the cavity causes a toothache. These variables are independent, however, given
the presence or the absence of a cavity. Each is directly caused by the cavity, but neither
has a direct effect on the other: toothache depends on the state of the nerves in the tooth,
whereas the probe’s accuracy depends primarily on the dentist’s skill, to which the toothache
is irrelevant.7 Mathematically, this property is written as
P(toothache∧catch|Cavity) = P(toothache|Cavity)P(catch|Cavity).
(12.17)
This equation expresses the conditional independence of toothache and catch given Cavity.
Conditional
independence
We can plug it into Equation (12.16) to obtain the probability of a cavity:
P(Cavity|toothache∧catch)
= αP(toothache|Cavity)P(catch|Cavity)P(Cavity).
(12.18)
Now the information requirements are the same as for inference, using each piece of evi-
dence separately: the prior probability P(Cavity) for the query variable and the conditional
probability of each effect, given its cause.
The general deﬁnition of conditional independence of two variables X and Y, given a
third variable Z, is
P(X,Y |Z) = P(X |Z)P(Y |Z).
In the dentist domain, for example, it seems reasonable to assert conditional independence of
the variables Toothache and Catch, given Cavity:
P(Toothache,Catch|Cavity) = P(Toothache|Cavity)P(Catch|Cavity).
(12.19)
Notice that this assertion is somewhat stronger than Equation (12.17), which asserts indepen-
dence only for speciﬁc values of Toothache and Catch. As with absolute independence in
Equation (12.11), the equivalent forms
P(X |Y,Z)=P(X |Z)
and
P(Y |X,Z)=P(Y |Z)
7
We assume that the patient and dentist are distinct individuals.
