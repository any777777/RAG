---
chunk_id: "book-ca4fca8dd8-chunk-0492"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 492
confidence: "first-pass"
extraction_method: "structured-local"
---

300
Chapter 9
Inference in First-Order Logic
Fortunately, there is a famous theorem due to Jacques Herbrand (1930) to the effect that
if a sentence is entailed by the original, ﬁrst-order knowledge base, then there is a proof
involving just a ﬁnite subset of the propositionalized knowledge base. Since any such subset
has a maximum depth of nesting among its ground terms, we can ﬁnd the subset by ﬁrst
generating all the instantiations with constant symbols (Richard and John), then all terms of
depth 1 (Father(Richard) and Father(John)), then all terms of depth 2, and so on, until we
are able to construct a propositional proof of the entailed sentence.
We have sketched an approach to ﬁrst-order inference via propositionalization that is
complete—that is, any entailed sentence can be proved. This is a major achievement, given
that the space of possible models is inﬁnite. On the other hand, we do not know until the
proof is done that the sentence is entailed! What happens when the sentence is not entailed?
Can we tell? Well, for ﬁrst-order logic, it turns out that we cannot. Our proof procedure can
go on and on, generating more and more deeply nested terms, but we will not know whether
it is stuck in a hopeless loop or whether the proof is just about to pop out. This is very much
like the halting problem for Turing machines. Alan Turing (1936) and Alonzo Church (1936)
both proved, in rather different ways, the inevitability of this state of affairs. The question of
▶
entailment for ﬁrst-order logic is semidecidable—that is, algorithms exist that say yes to every
entailed sentence, but no algorithm exists that also says no to every nonentailed sentence.
9.2 Uniﬁcation and First-Order Inference
The sharp-eyed reader will have noticed that the propositionalization approach generates
many unnecessary instantiations of universally quantiﬁed sentences. We’d rather have an
approach that uses just the one rule, reasoning that {x/John} solves the query Evil(x) as fol-
lows: given the rule that greedy kings are evil, ﬁnd some x such that x is a king and x is
greedy, and then infer that this x is evil. More generally, if there is some substitution θ that
makes each of the conjuncts of the premise of the implication identical to sentences already
in the knowledge base, then we can assert the conclusion of the implication, after applying
θ. In this case, the substitution θ={x/John} achieves that aim. Now suppose that instead of
knowing Greedy(John), we know that everyone is greedy:
∀y Greedy(y).
(9.2)
Then we would still like to be able to conclude that Evil(John), because we know that John
is a king (given) and John is greedy (because everyone is greedy). What we need for this to
work is to ﬁnd a substitution for both the variables in the implication sentence and the vari-
ables in the sentences that are in the knowledge base. In this case, applying the substitution
{x/John,y/John} to the implication premises King(x) and Greedy(x) and the knowledge-
base sentences King(John) and Greedy(y) will make them identical. Thus, we can infer the
consequent of the implication.
This inference process can be captured as a single inference rule that we call Generalized
Modus Ponens:2 For atomic sentences pi, pi′, and q, where there is a substitution θ such that
Generalized Modus
Ponens
2
Generalized Modus Ponens is more general than Modus Ponens (page 241) in the sense that the known facts
and the premise of the implication need match only up to a substitution, rather than exactly. On the other hand,
Modus Ponens allows any sentence α as the premise, rather than just a conjunction of atomic sentences.
