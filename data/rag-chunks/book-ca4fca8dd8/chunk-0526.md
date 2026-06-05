---
chunk_id: "book-ca4fca8dd8-chunk-0526"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 526
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.5
Resolution
321
¬Loves(y, Jack)
Loves(G(Jack), Jack)
¬Kills(Curiosity, Tuna)
Kills(Jack, Tuna)
Kills(Curiosity, Tuna)
¬Cat(x)
Animal(x)
Cat(Tuna)
¬Animal(F(Jack))
Loves(G(Jack), Jack)
Animal(F(x))
Loves(G(x), x)
¬Loves(y, x)
¬Kills(x, Tuna)
Kills(Jack, Tuna)
¬Loves(y, x)
¬Animal(z)
¬Kills(x, z)
Animal(Tuna)
¬Loves(x,F(x))
Loves(G(x), x)
¬Animal(x)
Loves(Jack, x)
^
^
^
^
^
^
^
^
^
Figure 9.11 A resolution proof that Curiosity killed the cat. Notice the use of factoring in
the derivation of the clause Loves(G(Jack),Jack). Notice also in the upper right, the uniﬁ-
cation of Loves(x,F(x)) and Loves(Jack,x) can only succeed after the variables have been
standardized apart.
9.5.4 Completeness of resolution
This section gives a completeness proof of resolution. It can be safely skipped by those who
are willing to take it on faith.
We show that resolution is refutation-complete, which means that if a set of sentences
Refutation
completeness
is unsatisﬁable, then resolution will always be able to derive a contradiction. Resolution
cannot be used to generate all logical consequences of a set of sentences, but it can be used
to establish that a given sentence is entailed by the set of sentences. Hence, it can be used to
ﬁnd all answers to a given question, Q(x), by proving that KB∧¬Q(x) is unsatisﬁable.
We take it as given that any sentence in ﬁrst-order logic (without equality) can be rewrit-
ten as a set of clauses in CNF. This can be proved by induction on the form of the sentence,
using atomic sentences as the base case (Davis and Putnam, 1960). Our goal therefore is to
prove the following: if S is an unsatisﬁable set of clauses, then the application of a ﬁnite ◀
number of resolution steps to S will yield a contradiction.
Our proof sketch follows Robinson’s original proof with some simpliﬁcations from Gene-
sereth and Nilsson (1987). The basic structure of the proof (Figure 9.12) is as follows:
1. First, we observe that if S is unsatisﬁable, then there exists a particular set of ground
instances of the clauses of S such that this set is also unsatisﬁable (Herbrand’s theorem).
2. We then appeal to the ground resolution theorem given in Chapter 7, which states that
propositional resolution is complete for ground sentences.
3. We then use a lifting lemma to show that, for any propositional resolution proof using
the set of ground sentences, there is a corresponding ﬁrst-order resolution proof using
the ﬁrst-order sentences from which the ground sentences were obtained.
To carry out the ﬁrst step, we need three new concepts:
• Herbrand universe: If S is a set of clauses, then HS, the Herbrand universe of S, is the
Herbrand universe
set of all ground terms constructible from the following:
a. The function symbols in S, if any.
b. The constant symbols in S, if any; if none, then a default constant symbol, S.
