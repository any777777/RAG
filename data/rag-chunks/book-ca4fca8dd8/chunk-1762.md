---
chunk_id: "book-ca4fca8dd8-chunk-1762"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1762
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 29.2
AI Architectures
1071
The truly gargantuan power of today’s machines tempts one to think that we could bypass
all the clever devices and rely more on brute force. So let’s try to counteract this tendency.
We begin with what physicists believe to be the speed of the ultimate 1kg computing device:
about 1051 operations per second, or a billion trillion trillion times faster than the fastest su-
percomputer as of 2020 (Lloyd, 2000).1 Then we propose a simple task: enumerating strings
of English words, much as Borges proposed in The Library of Babel. Borges stipulated books
of 410 pages. Would that be feasible? Not quite. In fact, the computer running for a year
could enumerate only the 11-word strings.
Now consider the fact that a detailed plan for a human life consists of (very roughly)
twenty trillion potential muscle actuations (Russell, 2019), and you begin to see the scale
of the problem. A computer that is a billion trillion trillion times more powerful than the
human brain is much further from being rational than a slug is from overtaking the starship
Enterprise traveling at warp nine.
With these considerations in mind, it seems that the goal of building rational agents is
perhaps a little too ambitious. Rather than aiming for something that cannot possibly exist,
we should consider a different normative target—one that necessarily exists. Recall from
Chapter 2 the following simple idea:
agent = architecture+program.
Now ﬁx the agent architecture (the underlying machine capabilities, perhaps with a ﬁxed soft-
ware layer on top) and allow the agent program to vary over all possible programs that the
architecture can support. In any given task environment, one of these programs (or an equiv-
alence class of them) delivers the best possible performance—perhaps not close to perfect
rationality, but still better than any other agent program. We say that this program satisﬁes
the criterion of bounded optimality. Clearly it exists, and clearly it constitutes a desirable
Bounded optimality
goal. The trick is ﬁnding it, or something close to it.
For some elementary classes of agent programs in simple real-time environments, it is
possible to identify bounded-optimal agent programs (Etzioni, 1989; Russell and Subrama-
nian, 1995). The success of Monte Carlo tree search has revived interest in metalevel decision
making, and there is reason to hope that bounded optimality within more complex families of
agent programs can be achieved by techniques such as metalevel reinforcement learning. It
should also be possible to develop a constructive theory of architecture, beginning with theo-
rems on the bounded optimality of suitable methods of combining different bounded-optimal
components such as reﬂex and action–value systems.
General AI
Much of the progress in AI in the 21st century so far has been guided by competition on nar-
row tasks, such as the DARPA Grand Challenge for autonomous cars, the ImageNet object
recognition competition, or playing Go, chess, poker, or Jeopardy! against a world cham-
pion. For each separate task, we build a separate AI system, usually with a separate machine
learning model trained from scratch with data collected speciﬁcally for this task. But a truly
intelligent agent should be able to do more than one thing. Alan Turing (1950) proposed his
list (page 1033) and science ﬁction author Robert Heinlein (1973) countered with:
1
We gloss over the fact that this device consumes the entire energy output of a star and operates at a billion
degrees centigrade.
