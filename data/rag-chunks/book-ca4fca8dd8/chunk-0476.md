---
chunk_id: "book-ca4fca8dd8-chunk-0476"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 476
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.4
Knowledge Engineering in First-Order Logic
289
reason to distinguish among pits.9 It is simpler to use a unary predicate Pit that is true of
squares containing pits. Finally, since there is exactly one wumpus, a constant Wumpus is
just as good as a unary predicate (and perhaps more digniﬁed from the wumpus’s viewpoint).
The agent’s location changes over time, so we write At(Agent,s,t) to mean that the
agent is at square s at time t. We can ﬁx the wumpus to a speciﬁc location forever with
∀t At(Wumpus,[1,3],t). We can then say that objects can be at only one location at a time:
∀x,s1,s2,t At(x,s1,t)∧At(x,s2,t) ⇒s1 = s2 .
Given its current location, the agent can infer properties of the square from properties of its
current percept. For example, if the agent is at a square and perceives a breeze, then that
square is breezy:
∀s,t At(Agent,s,t)∧Breeze(t) ⇒Breezy(s).
It is useful to know that a square is breezy because we know that the pits cannot move about.
Notice that Breezy has no time argument.
Having discovered which places are breezy (or smelly) and, very importantly, not breezy
(or not smelly), the agent can deduce where the pits are (and where the wumpus is). Whereas
propositional logic necessitates a separate axiom for each square (see R2 and R3 on page 238)
and would need a different set of axioms for each geographical layout of the world, ﬁrst-order
logic just needs one axiom:
∀s Breezy(s) ⇔∃r Adjacent(r,s)∧Pit(r).
(8.4)
Similarly, in ﬁrst-order logic we can quantify over time, so we need just one successor-state
axiom for each predicate, rather than a different copy for each time step. For example, the
axiom for the arrow (Equation (7.2) on page 258) becomes
∀t HaveArrow(t +1) ⇔(HaveArrow(t)∧¬Action(Shoot,t)).
From these two example sentences, we can see that the ﬁrst-order logic formulation is no
less concise than the original English-language description given in Chapter 7. The reader
is invited to construct analogous axioms for the agent’s location and orientation; in these
cases, the axioms quantify over both space and time. As in the case of propositional state
estimation, an agent can use logical inference with axioms of this kind to keep track of aspects
of the world that are not directly observed. Chapter 11 goes into more depth on the subject of
ﬁrst-order successor-state axioms and their uses for constructing plans.
8.4 Knowledge Engineering in First-Order Logic
The preceding section illustrated the use of ﬁrst-order logic to represent knowledge in three
simple domains. This section describes the general process of knowledge-base construction—
a process called knowledge engineering. A knowledge engineer is someone who investigates
Knowledge
engineering
a particular domain, learns what concepts are important in that domain, and creates a for-
mal representation of the objects and relations in the domain. We illustrate the knowledge
engineering process in an electronic circuit domain. The approach we take is suitable for
developing special-purpose knowledge bases whose domain is carefully circumscribed and
9
Similarly, most of us do not name each bird that ﬂies overhead as it migrates to warmer regions in winter. An
ornithologist wishing to study migration patterns, survival rates, and so on does name each bird, by means of a
ring on its leg, because individual birds must be tracked.
