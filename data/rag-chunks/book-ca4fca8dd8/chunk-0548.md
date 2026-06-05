---
chunk_id: "book-ca4fca8dd8-chunk-0548"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 548
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.1
Ontological Engineering
333
Anything
AbstractObjects
Sets
Numbers RepresentationalObjects
Intervals
Places
Processes
PhysicalObjects
Humans
Categories
Sentences Measurements
Moments
Things
Stuff
Times
Weights
Animals Agents
Solid Liquid Gas
GeneralizedEvents
Figure 10.1 The upper ontology of the world, showing the topics to be covered later in
the chapter. Each link indicates that the lower concept is a specialization of the upper one.
Specializations are not necessarily disjoint—a human is both an animal and an agent. We
will see in Section 10.3.2 why physical objects come under generalized events.
Before considering the ontology further, we should state one important caveat. We have
elected to use ﬁrst-order logic to discuss the content and organization of knowledge, although
certain aspects of the real world are hard to capture in FOL. The principal difﬁculty is that
most generalizations have exceptions or hold only to a degree. For example, although “toma-
toes are red” is a useful rule, some tomatoes are green, yellow, or orange. Similar exceptions
can be found to almost all the rules in this chapter. The ability to handle exceptions and un-
certainty is extremely important, but is orthogonal to the task of understanding the general
ontology. For this reason, we delay the discussion of exceptions until Section 10.5 of this
chapter, and the more general topic of reasoning with uncertainty until Chapter 12.
Of what use is an upper ontology? Consider the ontology for circuits in Section 8.4.2. It
makes many simplifying assumptions: time is omitted completely; signals are ﬁxed and do
not propagate; the structure of the circuit remains constant. A more general ontology would
consider signals at particular times, and would include the wire lengths and propagation de-
lays. This would allow us to simulate the timing properties of the circuit, and indeed such
simulations are often carried out by circuit designers.
We could also introduce more interesting classes of gates, for example, by describing
the technology (TTL, CMOS, and so on) as well as the input–output speciﬁcation. If we
wanted to discuss reliability or diagnosis, we would include the possibility that the structure
of the circuit or the properties of the gates might change spontaneously. To account for stray
capacitances, we would need to represent where the wires are on the board.
If we look at the wumpus world, similar considerations apply. Although we do represent
time, it has a simple structure: Nothing happens except when the agent acts, and all changes
are instantaneous. A more general ontology, better suited for the real world, would allow for
simultaneous changes extended over time. We also used a Pit predicate to say which squares
have pits. We could have allowed for different kinds of pits by having several individuals
