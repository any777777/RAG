---
chunk_id: "book-ca4fca8dd8-chunk-1608"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1608
confidence: "first-pass"
extraction_method: "structured-local"
---

976
Chapter 26
Robotics
S1
S2
S4
S3
push backward
lift up
set down
retract, lift higher
move
forward
no
yes
stuck?
(a)
(b)
Figure 26.32 (a) Genghis, a hexapod robot. (Image courtesy of Rodney A. Brooks.) (b) An
augmented ﬁnite state machine (AFSM) that controls one leg. The AFSM reacts to sensor
feedback: if a leg is stuck during the forward swinging phase, it will be lifted increasingly
higher.
models of the terrain for path planning. Moreover, even if we added high-precision cameras
and rangeﬁnders, the 12 degrees of freedom (two for each leg) would render the resulting
path planning problem computationally difﬁcult.
It is possible, nonetheless, to specify a controller directly without an explicit environ-
mental model. (We have already seen this with the PD controller, which was able to keep a
complex robot arm on target without an explicit model of the robot dynamics.)
For the hexapod robot we ﬁrst choose a gait, or pattern of movement of the limbs. One
Gait
statically stable gait is to ﬁrst move the right front, right rear, and left center legs forward
(keeping the other three ﬁxed), and then move the other three. This gait works well on
ﬂat terrain. On rugged terrain, obstacles may prevent a leg from swinging forward. This
problem can be overcome by a remarkably simple control rule: when a leg’s forward motion
is blocked, simply retract it, lift it higher, and try again. The resulting controller is shown in
Figure 26.32(b) as a simple ﬁnite state machine; it constitutes a reﬂex agent with state, where
the internal state is represented by the index of the current machine state (s1 through s4).
26.9.2 Subsumption architectures
The subsumption architecture (Brooks, 1986) is a framework for assembling reactive con-
Subsumption
architecture
trollers out of ﬁnite state machines. Nodes in these machines may contain tests for certain
sensor variables, in which case the execution trace of a ﬁnite state machine is conditioned
on the outcome of such a test. Arcs can be tagged with messages that will be generated
when traversing them, and that are sent to the robot’s motors or to other ﬁnite state machines.
Additionally, ﬁnite state machines possess internal timers (clocks) that control the time it
takes to traverse an arc. The resulting machines are called augmented ﬁnite state machines
(AFSMs), where the augmentation refers to the use of clocks.
Augmented ﬁnite
state machine
(AFSM)
An example of a simple AFSM is the four-state machine we just talked about, shown in
Figure 26.32(b). This AFSM implements a cyclic controller, whose execution mostly does
not rely on environmental feedback. The forward swing phase, however, does rely on sensor
feedback. If the leg is stuck, meaning that it has failed to execute the forward swing, the
