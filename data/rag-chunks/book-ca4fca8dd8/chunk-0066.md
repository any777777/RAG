---
chunk_id: "book-ca4fca8dd8-chunk-0066"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 66
confidence: "first-pass"
extraction_method: "structured-local"
---

42
Chapter 1
Introduction
Overall, the AI industry boomed from a few million dollars in 1980 to billions of dollars
in 1988, including hundreds of companies building expert systems, vision systems, robots,
and software and hardware specialized for these purposes.
Soon after that came a period called the “AI winter,” in which many companies fell by the
wayside as they failed to deliver on extravagant promises. It turned out to be difﬁcult to build
and maintain expert systems for complex domains, in part because the reasoning methods
used by the systems broke down in the face of uncertainty and in part because the systems
could not learn from experience.
1.3.5 The return of neural networks (1986–present)
In the mid-1980s at least four different groups reinvented the back-propagation learning
algorithm ﬁrst developed in the early 1960s. The algorithm was applied to many learning
problems in computer science and psychology, and the widespread dissemination of the re-
sults in the collection Parallel Distributed Processing (Rumelhart and McClelland, 1986)
caused great excitement.
These so-called connectionist models were seen by some as direct competitors both to
Connectionist
the symbolic models promoted by Newell and Simon and to the logicist approach of Mc-
Carthy and others. It might seem obvious that at some level humans manipulate symbols—in
fact, the anthropologist Terrence Deacon’s book The Symbolic Species (1997) suggests that
this is the deﬁning characteristic of humans. Against this, Geoff Hinton, a leading ﬁgure
in the resurgence of neural networks in the 1980s and 2010s, has described symbols as the
“luminiferous aether of AI”—a reference to the non-existent medium through which many
19th-century physicists believed that electromagnetic waves propagated. Certainly, many
concepts that we name in language fail, on closer inspection, to have the kind of logically
deﬁned necessary and sufﬁcient conditions that early AI researchers hoped to capture in ax-
iomatic form. It may be that connectionist models form internal concepts in a more ﬂuid
and imprecise way that is better suited to the messiness of the real world. They also have
the capability to learn from examples—they can compare their predicted output value to the
true value on a problem and modify their parameters to decrease the difference, making them
more likely to perform well on future examples.
1.3.6 Probabilistic reasoning and machine learning (1987–present)
The brittleness of expert systems led to a new, more scientiﬁc approach incorporating proba-
bility rather than Boolean logic, machine learning rather than hand-coding, and experimental
results rather than philosophical claims.14 It became more common to build on existing theo-
ries than to propose brand-new ones, to base claims on rigorous theorems or solid experimen-
tal methodology (Cohen, 1995) rather than on intuition, and to show relevance to real-world
applications rather than toy examples.
Shared benchmark problem sets became the norm for demonstrating progress, including
the UC Irvine repository for machine learning data sets, the International Planning Compe-
14 Some have characterized this change as a victory of the neats—those who think that AI theories should be
grounded in mathematical rigor—over the scrufﬁes—those who would rather try out lots of ideas, write some
programs, and then assess what seems to be working. Both approaches are important. A shift toward neatness
implies that the ﬁeld has reached a level of stability and maturity. The present emphasis on deep learning may
represent a resurgence of the scrufﬁes.
