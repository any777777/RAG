---
chunk_id: "book-ca4fca8dd8-chunk-0550"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 550
confidence: "first-pass"
extraction_method: "structured-local"
---

334
Chapter 10
Knowledge Representation
belonging to the class of pits, each having different properties. Similarly, we might want to
allow for other animals besides wumpuses. It might not be possible to pin down the exact
species from the available percepts, so we would need to build up a biological taxonomy to
help the agent predict the behavior of cave dwellers from scanty clues.
For any special-purpose ontology, it is possible to make changes like these to move to-
ward greater generality. An obvious question then arises: do all these ontologies converge
on a general-purpose ontology? After centuries of philosophical and computational inves-
tigation, the answer is “Maybe.” In this section, we present one general-purpose ontology
that synthesizes ideas from those centuries. Two major characteristics of general-purpose
ontologies distinguish them from collections of special-purpose ontologies:
• A general-purpose ontology should be applicable in more or less any special-purpose
domain (with the addition of domain-speciﬁc axioms). This means that no representa-
tional issue can be ﬁnessed or swept under the carpet.
• In any sufﬁciently demanding domain, different areas of knowledge must be uniﬁed,
because reasoning and problem solving could involve several areas simultaneously. A
robot circuit-repair system, for instance, needs to reason about circuits in terms of elec-
trical connectivity and physical layout, and about time, both for circuit timing analysis
and estimating labor costs. The sentences describing time therefore must be capable
of being combined with those describing spatial layout and must work equally well for
nanoseconds and minutes and for angstroms and meters.
We should say up front that the enterprise of general ontological engineering has so far had
only limited success. None of the top AI applications (as listed in Chapter 1) make use of
a general ontology—they all use special-purpose knowledge engineering and machine learn-
ing. Social/political considerations can make it difﬁcult for competing parties to agree on an
ontology. As Tom Gruber (2004) says, “Every ontology is a treaty—a social agreement—
among people with some common motive in sharing.” When competing concerns outweigh
the motivation for sharing, there can be no common ontology. The smaller the number of
stakeholders, the easier it is to create an ontology, and thus it is harder to create a general-
purpose ontology than a limited-purpose one, such as the Open Biomedical Ontology (Smith
et al., 2007). Those ontologies that do exist have been created along four routes:
1. By a team of trained ontologists or logicians, who architect the ontology and write
axioms. The CYC system was mostly built this way (Lenat and Guha, 1990).
2. By importing categories, attributes, and values from an existing database or databases.
DBPEDIA was built by importing structured facts from Wikipedia (Bizer et al., 2007).
3. By parsing text documents and extracting information from them. TEXTRUNNER was
built by reading a large corpus of Web pages (Banko and Etzioni, 2008).
4. By enticing unskilled amateurs to enter commonsense knowledge. The OPENMIND
system was built by volunteers who proposed facts in English (Singh et al., 2002;
Chklovski and Gil, 2005).
As an example, the Google Knowledge Graph uses semistructured content from Wikipedia,
combining it with other content gathered from across the web under human curation. It
contains over 70 billion facts and provides answers for about a third of Google searches
(Dong et al., 2014).
