---
chunk_id: "book-ca4fca8dd8-chunk-0793"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 793
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
477
Uncertain reasoning in AI has not always been based on probability theory. As noted
in Chapter 12, early probabilistic systems fell out of favor in the early 1970s, leaving a par-
tial vacuum to be ﬁlled by alternative methods. These included rule-based expert systems,
Dempster–Shafer theory, and (to some extent) fuzzy logic.9
Rule-based approaches to uncertainty hoped to build on the success of logical rule-
based systems, but add a sort of “fudge factor”—more politely called a certainty factor—
to each rule to accommodate uncertainty. The ﬁrst such system was MYCIN (Shortliffe,
1976), a medical expert system for bacterial infections. The collection Rule-Based Expert
Systems (Buchanan and Shortliffe, 1984) provides a complete overview of MYCIN and its
descendants (see also Steﬁk, 1995).
David Heckerman (1986) showed that a slightly modiﬁed version of certainty factor cal-
culations gives correct probabilistic results in some cases, but results in serious overcounting
of evidence in other cases. As rule sets became larger, undesirable interactions between rules
became more common, and practitioners found that the certainty factors of many other rules
had to be “tweaked” when new rules were added. The basic mathematical properties that
allow chains of reasoning in logic simply do not hold for probability.
Dempster–Shafer theory originates with a paper by Arthur Dempster (1968) proposing a
generalization of probability to interval values and a combination rule for using them. Such
an approach might alleviate the difﬁculty of specifying probabilities exactly. Later work by
Glenn Shafer (1976) led to the Dempster–Shafer theory’s being viewed as a competing ap-
proach to probability. Pearl (1988) and Ruspini et al. (1992) analyze the relationship between
the Dempster–Shafer theory and standard probability theory. In many cases, probability the-
ory does not require probabilities to be speciﬁed exactly: we can express uncertainty about
probability values as (second-order) probability distributions, as explained in Chapter 21.
Fuzzy sets were developed by LotﬁZadeh (1965) in response to the perceived difﬁculty
of providing exact inputs to intelligent systems. A fuzzy set is one in which membership is a
matter of degree. Fuzzy logic is a method for reasoning with logical expressions describing
membership in fuzzy sets. Fuzzy control is a methodology for constructing control systems
in which the mapping between real-valued input and output parameters is represented by
fuzzy rules. Fuzzy control has been very successful in commercial products such as automatic
transmissions, video cameras, and electric shavers. The text by Zimmermann (2001) provides
a thorough introduction to fuzzy set theory; papers on fuzzy applications are collected in
Zimmermann (1999).
Fuzzy logic has often been perceived incorrectly as a direct competitor to probability the-
ory, whereas in fact it addresses a different set of issues: rather than considering uncertainty
about the truth of well-deﬁned propositions, fuzzy logic handles vagueness in the mapping
from terms in a symbolic theory to an actual world. Vagueness is a real issue in any applica-
tion of logic, probability, or indeed standard mathematical models to reality. Even a variable
as impeccable as the mass of the Earth turns out, on inspection, to vary with time as mete-
orites and molecules come and go. It is also imprecise—does it include the atmosphere? If
so, to what height? In some cases, further elaboration of the model can reduce vagueness, but
fuzzy logic takes vagueness as a given and develops a theory around it.
9
A fourth approach, default reasoning, treats conclusions not as “believed to a certain degree,” but as “believed
until a better reason is found to believe something else.” It is covered in Chapter 10.
