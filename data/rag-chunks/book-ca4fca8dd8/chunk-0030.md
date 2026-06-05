---
chunk_id: "book-ca4fca8dd8-chunk-0030"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 30
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.2
The Foundations of Artiﬁcial Intelligence
23
correctly. For example, in designing a self-driving car, one might think that the objective is
to reach the destination safely. But driving along any road incurs a risk of injury due to other
errant drivers, equipment failure, and so on; thus, a strict goal of safety requires staying in the
garage. There is a tradeoff between making progress towards the destination and incurring a
risk of injury. How should this tradeoff be made? Furthermore, to what extent can we allow
the car to take actions that would annoy other drivers? How much should the car moderate
its acceleration, steering, and braking to avoid shaking up the passenger? These kinds of
questions are difﬁcult to answer a priori. They are particularly problematic in the general
area of human–robot interaction, of which the self-driving car is one example.
The problem of achieving agreement between our true preferences and the objective we
put into the machine is called the value alignment problem: the values or objectives put into
Value alignment
problem
the machine must be aligned with those of the human. If we are developing an AI system in
the lab or in a simulator—as has been the case for most of the ﬁeld’s history—there is an easy
ﬁx for an incorrectly speciﬁed objective: reset the system, ﬁx the objective, and try again.
As the ﬁeld progresses towards increasingly capable intelligent systems that are deployed
in the real world, this approach is no longer viable. A system deployed with an incorrect
objective will have negative consequences. Moreover, the more intelligent the system, the
more negative the consequences.
Returning to the apparently unproblematic example of chess, consider what happens if
the machine is intelligent enough to reason and act beyond the conﬁnes of the chessboard.
In that case, it might attempt to increase its chances of winning by such ruses as hypnotiz-
ing or blackmailing its opponent or bribing the audience to make rustling noises during its
opponent’s thinking time.3 It might also attempt to hijack additional computing power for
itself. These behaviors are not “unintelligent” or “insane”; they are a logical consequence ◀
of deﬁning winning as the sole objective for the machine.
It is impossible to anticipate all the ways in which a machine pursuing a ﬁxed objective
might misbehave. There is good reason, then, to think that the standard model is inadequate.
We don’t want machines that are intelligent in the sense of pursuing their objectives; we want
them to pursue our objectives. If we cannot transfer those objectives perfectly to the machine,
then we need a new formulation—one in which the machine is pursuing our objectives, but
is necessarily uncertain as to what they are. When a machine knows that it doesn’t know the
complete objective, it has an incentive to act cautiously, to ask permission, to learn more about
our preferences through observation, and to defer to human control. Ultimately, we want
agents that are provably beneﬁcial to humans. We will return to this topic in Section 1.5.
Provably beneﬁcial
1.2 The Foundations of Artiﬁcial Intelligence
In this section, we provide a brief history of the disciplines that contributed ideas, viewpoints,
and techniques to AI. Like any history, this one concentrates on a small number of people,
events, and ideas and ignores others that also were important. We organize the history around
a series of questions. We certainly would not wish to give the impression that these questions
are the only ones the disciplines address or that the disciplines have all been working toward
AI as their ultimate fruition.
3
In one of the ﬁrst books on chess, Ruy Lopez (1561) wrote, “Always place the board so the sun is in your
opponent’s eyes.”
