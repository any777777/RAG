---
chunk_id: "book-ca4fca8dd8-chunk-0530"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 530
confidence: "first-pass"
extraction_method: "structured-local"
---

324
Chapter 9
Inference in First-Order Logic
This is called a lifting lemma, because it lifts a proof step from ground clauses up to general
Lifting lemma
ﬁrst-order clauses. In order to prove his basic lifting lemma, Robinson had to invent uniﬁ-
cation and derive all of the properties of most general uniﬁers. Rather than repeat the proof
here, we simply illustrate the lemma:
C1 = ¬P(x,F(x,A))∨¬Q(x,A)∨R(x,B)
C2 = ¬N(G(y),z)∨P(H(y),z)
C′
1 = ¬P(H(B),F(H(B),A))∨¬Q(H(B),A)∨R(H(B),B)
C′
2 = ¬N(G(B),F(H(B),A))∨P(H(B),F(H(B),A))
C′ = ¬N(G(B),F(H(B),A))∨¬Q(H(B),A)∨R(H(B),B)
C = ¬N(G(y),F(H(y),A))∨¬Q(H(y),A)∨R(H(y),B).
We see that indeed C′ is a ground instance of C. In general, for C′
1 and C′
2 to have any
resolvents, they must be constructed by ﬁrst applying to C1 and C2 the most general uniﬁer of
a pair of complementary literals in C1 and C2. From the lifting lemma, it is easy to derive a
similar statement about any sequence of applications of the resolution rule:
For any clause C′ in the resolution closure of S′ there is a clause C in the resolution
closure of S such that C′ is a ground instance of C and the derivation of C is the
same length as the derivation of C′.
From this fact, it follows that if the empty clause appears in the resolution closure of S′, it
must also appear in the resolution closure of S. This is because the empty clause cannot be a
ground instance of any other clause. To recap: we have shown that if S is unsatisﬁable, then
there is a ﬁnite derivation of the empty clause using the resolution rule.
The lifting of theorem proving from ground clauses to ﬁrst-order clauses provides a vast
increase in power. This increase comes from the fact that the ﬁrst-order proof need instantiate
variables only as far as necessary for the proof, whereas the ground-clause methods were
required to examine a huge number of arbitrary instantiations.
9.5.5 Equality
None of the inference methods described so far in this chapter can handle an assertion of the
form x = y without some additional work. Three distinct approaches can be taken. The ﬁrst is
to axiomatize equality—to write down sentences about the equality relation in the knowledge
base. We need to say that equality is reﬂexive, symmetric, and transitive, and we also have
to say that we can substitute equals for equals in any predicate or function. So we need three
basic axioms, and then one for each predicate and function:
∀x x=x
∀x,y x=y ⇒y=x
∀x,y,z x=y∧y=z ⇒x=z
∀x,y x=y ⇒(P1(x) ⇔P1(y))
∀x,y x=y ⇒(P2(x) ⇔P2(y))
...
∀w,x,y,z w=y∧x=z ⇒(F1(w,x)=F1(y,z))
∀w,x,y,z w=y∧x=z ⇒(F2(w,x)=F2(y,z))
...
