---
chunk_id: "book-ca4fca8dd8-chunk-0595"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 595
confidence: "first-pass"
extraction_method: "structured-local"
---

360
Chapter 10
Knowledge Representation
circumscription; the underlying theory of stable model semantics was introduced by Gelfond
and Lifschitz (1988), and the leading answer set programming systems are DLV (Eiter et al.,
1998) and SMODELS (Niemel¨a et al., 2000). Brewka et al. (1997) give a good overview of
the various approaches to nonmonotonic logic. Clark (1978) covers the negation-as-failure
approach to logic programming and Clark completion. Lifschitz (2001) discusses the appli-
cation of answer set programming to planning. A variety of nonmonotonic reasoning systems
based on logic programming are documented in the proceedings of the conferences on Logic
Programming and Nonmonotonic Reasoning (LPNMR).
The study of truth maintenance systems began with the TMS (Doyle, 1979) and RUP
(McAllester, 1980) systems, both of which were essentially JTMSs. Forbus and de Kleer
(1993) explain in depth how TMSs can be used in AI applications. Nayak and Williams
(1997) show how an efﬁcient incremental TMS called an ITMS makes it feasible to plan the
operations of a NASA spacecraft in real time.
This chapter could not cover every area of knowledge representation in depth. The three
principal topics omitted are the following:
Qualitative physics: Qualitative physics is a subﬁeld of knowledge representation concerned
Qualitative physics
speciﬁcally with constructing a logical, nonnumeric theory of physical objects and processes.
The term was coined by Johan de Kleer (1975), although the enterprise could be said to
have started in Fahlman’s (1974) BUILD, a sophisticated planner for constructing complex
towers of blocks. Fahlman discovered in the process of designing it that most of the effort
(80%, by his estimate) went into modeling the physics of the blocks world to calculate the
stability of various subassemblies of blocks, rather than into planning per se. He sketches
a hypothetical naive-physics-like process to explain why young children can solve BUILD-
like problems without access to the high-speed ﬂoating-point arithmetic used in BUILD’s
physical modeling. Hayes (1985a) uses “histories”—four-dimensional slices of space-time
similar to Davidson’s events—to construct a fairly complex naive physics of liquids. Davis
(2008) gives an update to the ontology of liquids that describes the pouring of liquids into
containers.
De Kleer and Brown (1985), Ken Forbus (1985), and Benjamin Kuipers (1985) indepen-
dently and almost simultaneously developed systems that can reason about a physical system
based on qualitative abstractions of the underlying equations. Qualitative physics soon devel-
oped to the point where it became possible to analyze an impressive variety of complex phys-
ical systems (Yip, 1991). Qualitative techniques have been used to construct novel designs
for clocks, windshield wipers, and six-legged walkers (Subramanian and Wang, 1994). The
collection Readings in Qualitative Reasoning about Physical Systems (Weld and de Kleer,
1990), an encyclopedia article by Kuipers (2001), and a handbook article by Davis (2007)
provide good introductions to the ﬁeld.
Spatial reasoning: The reasoning necessary to navigate in the wumpus world is trivial in
Spatial reasoning
comparison to the rich spatial structure of the real world. The earliest serious attempt to
capture commonsense reasoning about space appears in the work of Ernest Davis (1986,
1990). The region connection calculus of Cohn et al. (1997) supports a form of qualitative
spatial reasoning and has led to new kinds of geographical information systems; see also
(Davis, 2006). As with qualitative physics, an agent can go a long way, so to speak, without
resorting to a full metric representation.
