---
chunk_id: "book-ca4fca8dd8-chunk-1269"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1269
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
769
generalization of the old example to ﬁt the needs of the new problem. This latter form of
analogical reasoning is found most commonly in case-based reasoning (Kolodner, 1993)
and derivational analogy (Veloso and Carbonell, 1993).
Relevance information in the form of functional dependencies was ﬁrst developed in the
database community, where it is used to structure large sets of attributes into manageable sub-
sets. Functional dependencies were used for analogical reasoning by Carbonell and Collins
(1973) and rediscovered and given a full logical analysis by Davies and Russell (Davies,
1985; Davies and Russell, 1987). Their role as prior knowledge in inductive learning was
explored by Russell and Grosof (1987). The equivalence of determinations to a restricted-
vocabulary hypothesis space was proved in Russell (1988). Learning algorithms for determi-
nations and the improved performance obtained by RBDTL were ﬁrst shown in the FOCUS
algorithm, due to Almuallim and Dietterich (1991). Tadepalli (1993) describes a very inge-
nious algorithm for learning with determinations that shows large improvements in learning
speed.
The idea that inductive learning can be performed by inverse deduction can be traced
to W. S. Jevons (1874), who wrote, “The study both of Formal Logic and of the Theory of
Probabilities has led me to adopt the opinion that there is no such thing as a distinct method
of induction as contrasted with deduction, but that induction is simply an inverse employ-
ment of deduction.” Computational investigations began with the remarkable Ph.D. thesis by
Gordon Plotkin (1971) at Edinburgh. Although Plotkin developed many of the theorems and
methods that are in current use in ILP, he was discouraged by some undecidability results for
certain subproblems in induction. MIS (Shapiro, 1981) reintroduced the problem of learning
logic programs, but was seen mainly as a contribution to the theory of automated debug-
ging. Work on rule induction, such as the ID3 (Quinlan, 1986) and CN2 (Clark and Niblett,
1989) systems, led to FOIL (Quinlan, 1990), which for the ﬁrst time allowed practical induc-
tion of relational rules. The ﬁeld of relational learning was reinvigorated by Muggleton and
Buntine (1988), whose CIGOL program incorporated a slightly incomplete version of inverse
resolution and was capable of generating new predicates. The inverse resolution method also
appears in (Russell, 1986), with a simple algorithm given in a footnote. The next major sys-
tem was GOLEM (Muggleton and Feng, 1990), which uses a covering algorithm based on
Plotkin’s concept of relative least general generalization. ITOU (Rouveirol and Puget, 1989)
and CLINT (De Raedt, 1992) were other systems of that era. More recently, PROGOL (Mug-
gleton, 1995) has taken a hybrid (top-down and bottom-up) approach to inverse entailment
and has been applied to a number of practical problems, particularly in biology and natural
language processing. Muggleton (2000) describes an extension of PROGOL to handle uncer-
tainty in the form of stochastic logic programs.
A formal analysis of ILP methods appears in Muggleton (1991), a large collection of
papers in Muggleton (1992), and a collection of techniques and applications in the book
by Lavrauc and Duzeroski (1994). Page and Srinivasan (2002) give a more recent overview of
the ﬁeld’s history and challenges for the future. Early complexity results by Haussler (1989)
suggested that learning ﬁrst-order sentences was intractible. However, with better understand-
ing of the importance of syntactic restrictions on clauses, positive results have been obtained
even for clauses with recursion (Duzeroski et al., 1992). Learnability results for ILP are
surveyed by Kietz and Duzeroski (1994) and Cohen and Page (1995).
Although ILP now seems to be the dominant approach to constructive induction, it has
not been the only approach taken. So-called discovery systems aim to model the process
Discovery system
