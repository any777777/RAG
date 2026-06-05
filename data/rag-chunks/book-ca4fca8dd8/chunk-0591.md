---
chunk_id: "book-ca4fca8dd8-chunk-0591"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 591
confidence: "first-pass"
extraction_method: "structured-local"
---

358
Chapter 10
Knowledge Representation
and Davis (1990, 2005). An inspirational discussion of the general project of commonsense
knowledge representation appears in Hayes’s (1978, 1985b) “Naive Physics Manifesto.”
Successful deep ontologies within a speciﬁc ﬁeld include the Gene Ontology project
(Gene Ontology Consortium, 2008) and the Chemical Markup Language (Murray-Rust et al.,
2003). Doubts about the feasibility of a single ontology for all knowledge are expressed by
Doctorow (2001), Gruber (2004), Halevy et al. (2009), and Smith (2004).
The event calculus was introduced by Kowalski and Sergot (1986) to handle continuous
time, and there have been several variations (Sadri and Kowalski, 1995; Shanahan, 1997) and
overviews (Shanahan, 1999; Mueller, 2006). James Allen introduced time intervals for the
same reason (Allen, 1984), arguing that intervals were much more natural than situations for
reasoning about extended and concurrent events. In van Lambalgen and Hamm (2005) we see
how the logic of events maps onto the language we use to talk about events. An alternative to
the event and situation calculi is the ﬂuent calculus (Thielscher, 1999), which reiﬁes the facts
out of which states are composed.
Peter Ladkin (1986a, 1986b) introduced “concave” time intervals (intervals with gaps—
essentially, unions of ordinary “convex” time intervals) and applied the techniques of math-
ematical abstract algebra to time representation. Allen (1991) systematically investigates the
wide variety of techniques available for time representation; van Beek and Manchak (1996)
analyze algorithms for temporal reasoning. There are signiﬁcant commonalities between the
event-based ontology given in this chapter and an analysis of events due to the philosopher
Donald Davidson (1980). The histories in Pat Hayes’s (1985a) ontology of liquids and the
chronicles in McDermott’s (1985) theory of plans were also important inﬂuences on the ﬁeld
and on this chapter.
The question of the ontological status of substances has a long history. Plato proposed
that substances were abstract entities entirely distinct from physical objects; he would say
MadeOf(Butter3,Butter) rather than Butter3 ∈Butter. This leads to a substance hierarchy in
which, for example, UnsaltedButter is a more speciﬁc substance than Butter. The position
adopted in this chapter, in which substances are categories of objects, was championed by
Richard Montague (1973). It has also been adopted in the CYC project. Copeland (1993)
mounts a serious, but not invincible, attack.
The alternative approach mentioned in the chapter, in which butter is one object con-
sisting of all buttery objects in the universe, was proposed originally by the Polish logician
Le´sniewski (1916). His mereology (the name is derived from the Greek word for “part”)
used the part–whole relation as a substitute for mathematical set theory, with the aim of elim-
inating abstract entities such as sets. A more readable exposition of these ideas is given by
Leonard and Goodman (1940), and Goodman’s The Structure of Appearance (1977) applies
the ideas to various problems in knowledge representation.
While some aspects of the mereological approach are awkward—for example, the need
for a separate inheritance mechanism based on part–whole relations—the approach gained
the support of Quine (1960). Harry Bunt (1985) has provided an extensive analysis of its
use in knowledge representation. Casati and Varzi (1999) cover parts, wholes, and a general
theory of spatial locations.
There are three main approaches to the study of mental objects. The one taken in this
chapter, based on modal logic and possible worlds, is the classical approach from philosophy
(Hintikka, 1962; Kripke, 1963; Hughes and Cresswell, 1996). The book Reasoning about
