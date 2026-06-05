---
chunk_id: "book-ca4fca8dd8-chunk-0532"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 532
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.5
Resolution
325
Given these sentences, a standard inference procedure such as resolution can perform tasks
requiring equality reasoning, such as solving mathematical equations. However, these axioms
will generate a lot of conclusions, most of them not helpful to a proof. So the second approach
is to add inference rules rather than axioms. The simplest rule, demodulation, takes a unit
clause x=y and some clause α that contains the term x, and yields a new clause formed by
substituting y for x within α. It works if the term within α uniﬁes with x; it need not be exactly
equal to x. Note that demodulation is directional; given x = y, the x always gets replaced with
y, never vice versa. That means that demodulation can be used for simplifying expressions
using demodulators such as z+0=z or z1 =z. As another example, given
Father(Father(x)) = PaternalGrandfather(x)
Birthdate(Father(Father(Bella)),1926)
we can conclude by demodulation
Birthdate(PaternalGrandfather(Bella),1926).
More formally, we have
• Demodulation: For any terms x, y, and z, where z appears somewhere in literal mi and
Demodulation
where UNIFY(x,z) = θ ̸= failure,
x=y,
m1 ∨···∨mn
SUB(SUBST(θ,x),SUBST(θ,y),m1 ∨···∨mn) .
where SUBST is the usual substitution of a binding list, and SUB(x,y,m) means to re-
place x with y somewhere within m.
The rule can also be extended to handle non-unit clauses in which an equal sign appears:
• Paramodulation: For any terms x, y, and z, where z appears somewhere in literal mi,
Paramodulation
and where UNIFY(x,z) = θ,
ℓ1 ∨···∨ℓk ∨x=y,
m1 ∨···∨mn
SUB(SUBST(θ,x),SUBST(θ,y),SUBST(θ,ℓ1 ∨···∨ℓk ∨m1 ∨···∨mn)) .
For example, from
P(F(x,B),x)∨Q(x)
and
F(A,y)=y∨R(y)
we have θ=UNIFY(F(A,y),F(x,B))={x/A,y/B}, and we can conclude by paramodulation
the sentence
P(B,A)∨Q(A)∨R(B).
Paramodulation yields a complete inference procedure for ﬁrst-order logic with equality.
A third approach handles equality reasoning entirely within an extended uniﬁcation algo-
rithm. That is, terms are uniﬁable if they are provably equal under some substitution, where
“provably” allows for equality reasoning. For example, the terms 1+2 and 2+1 normally are
not uniﬁable, but a uniﬁcation algorithm that knows that x+y=y+x could unify them with
the empty substitution. Equational uniﬁcation of this kind can be done with efﬁcient algo-
Equational
uniﬁcation
rithms designed for the particular axioms used (commutativity, associativity, and so on) rather
than through explicit inference with those axioms. Theorem provers using this technique are
closely related to the CLP systems described in Section 9.4.
