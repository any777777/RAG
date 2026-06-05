---
chunk_id: "book-ca4fca8dd8-chunk-1063"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1063
confidence: "first-pass"
extraction_method: "structured-local"
---

636
Chapter 17
Multiagent Decision Making
Bibliographical and Historical Notes
It is a curiosity of the ﬁeld that researchers in AI did not begin to seriously consider the issues
surrounding interacting agents until the 1980s—and the multiagent systems ﬁeld did not re-
ally become established as a distinctive subdiscipline of AI until a decade later. Nevertheless,
ideas that hint at multiagent systems were present in the 1970s. For example, in his highly
inﬂuential Society of Mind theory, Marvin Minsky (1986, 2007) proposed that human minds
are constructed from an ensemble of agents. Doug Lenat had similar ideas in a framework
he called BEINGS (Lenat, 1975). In the 1970s, building on his PhD work on the PLANNER
system, Carl Hewitt proposed a model of computation as interacting agents called the ac-
tor model, which has become established as one of the fundamental models in concurrent
computation (Hewitt, 1977; Agha, 1986).
The prehistory of the multiagent systems ﬁeld is thoroughly documented in a collection
of papers entitled Readings in Distributed Artiﬁcial Intelligence (Bond and Gasser, 1988).
The collection is prefaced with a detailed statement of the key research challenges in multi-
agent systems, which remains remarkably relevant today, more than thirty years after it was
written. Early research on multiagent systems tended to assume that all agents in a system
were acting with common interest, with a single designer. This is now recognized as a spe-
cial case of the more general multiagent setting—the special case is known as cooperative
distributed problem solving. A key system of this time was the Distributed Vehicle Moni-
Cooperative
distributed problem
solving
toring Testbed (DVMT), developed under the supervision of Victor Lesser at the University
of Massachusetts (Lesser and Corkill, 1988). The DVMT modeled a scenario in which a col-
lection of geographically distributed acoustic sensor agents cooperate to track the movement
of vehicles.
The contemporary era of multiagent systems research began in the late 1980s, when it
was widely realized that agents with differing preferences are the norm in AI and society—
from this point on, game theory began to be established as the main methodology for studying
such agents.
Multiagent planning has leaped in popularity in recent years, although it does have a long
history. Konolige (1982) formalizes multiagent planning in ﬁrst-order logic, while Pednault
(1986) gives a STRIPS-style description. The notion of joint intention, which is essential if
agents are to execute a joint plan, comes from work on communicative acts (Cohen and Per-
rault, 1979; Cohen and Levesque, 1990; Cohen et al., 1990). Boutilier and Brafman (2001)
show how to adapt partial-order planning to a multiactor setting. Brafman and Domshlak
(2008) devise a multiactor planning algorithm whose complexity grows only linearly with
the number of actors, provided that the degree of coupling (measured partly by the tree width
of the graph of interactions among agents) is bounded.
Multiagent planning is hardest when there are adversarial agents. As Jean-Paul Sartre
(1960) said, “In a football match, everything is complicated by the presence of the other
team.” General Dwight D. Eisenhower said, “In preparing for battle I have always found
that plans are useless, but planning is indispensable,” meaning that it is important to have a
conditional plan or policy, and not to expect an unconditional plan to succeed.
The topic of distributed and multiagent reinforcement learning (RL) was not covered in
this chapter but is of great current interest. In distributed RL, the aim is to devise methods by
which multiple, coordinated agents learn to optimize a common utility function. For example,
